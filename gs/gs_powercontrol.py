def gs_powercontrol_process(
    txt_data: list,
    newreference_gsmcells: list,
    newreference_sites: list,
    gslist_data: list,
    dt_col: dict,
    moc: str,
):
    gs_result = []

    geran_to_loc = {
        cell["cell"]: cell["locCode"] for cell in newreference_gsmcells
    }
    loc_to_er = {site["locCode"]: site["er"] for site in newreference_sites}

    for raw_data in txt_data:
        if str(raw_data).strip() == "" or "NodeId" in str(raw_data):
            continue

        g_data = str(raw_data).split()
        NodeId = g_data[dt_col.get("NodeId", 0)]
        GeranCellId = g_data[dt_col.get("GeranCellId", 4)]
        locCode = geran_to_loc.get(GeranCellId, None)
        er = loc_to_er.get(locCode, "")

        for gs_data in gslist_data:
            param = gs_data[0]
            baseline_value = gs_data[1]

            if baseline_value == "SUFFIX":
                if param == "hpbState":
                    if any(
                        substring in er
                        for substring in [
                            "er_ON_DURHAM",
                            "er_ON_PEEL",
                            "er_ON_HALTON",
                            "er_ON_TORONTO",
                            "er_ON_YORK",
                        ]
                    ):
                        baseline_value = "ACTIVE"
                    else:
                        baseline_value = "INACTIVE"

            index_param = dt_col.get(param, -1)
            if index_param == -1:
                oss_value = "OSS_VALUE_NOT_FOUND"
            else:
                oss_value = g_data[index_param]

            compliance = (
                "MATCH"
                if str(oss_value) == str(baseline_value)
                else "MISMATCH"
            )

            prefix = (
                "SubNetwork=ONRM_ROOT_MO,SubNetwork="
                if "CA1BSC1" in NodeId or "VA1BSC1" in NodeId
                else "SubNetwork=ONRM_ROOT_MO_R,SubNetwork="
            )
            gs_data = [
                NodeId,
                GeranCellId,
                moc,
                param,
                oss_value,
                baseline_value,
                compliance,
                f"cmedit set {prefix}{NodeId},MeContext={NodeId},"
                f"ManagedElement={NodeId},BscFunction=1,BscM=1,"
                f"GeranCellM=1,GeranCell={GeranCellId},"
                f"PowerControl=1 "
                f"{param}={baseline_value}"
                f" --force",
            ]

            gs_result.append(gs_data)

    return gs_result
