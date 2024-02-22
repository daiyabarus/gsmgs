from toget import ToGet

def gs_idlechannelmeasurement_process(
    txt_data: list,
    netstatremedy_data: list,
    gslist_data: list,
    dt_col: dict,
    moc: str
):
    gs_result = []

    netstatremedy_dict = {str(row[0]).strip(): row[9] for row in netstatremedy_data}

    for raw_data in txt_data:
        if str(raw_data).strip() == "" or "NodeId" in str(raw_data):
            continue

        g_data = str(raw_data).split()
        NodeId = g_data[dt_col.get("NodeId", 0)]
        GeranCellId = g_data[dt_col.get("GeranCellId", 4)]
        sector_type = netstatremedy_dict.get(GeranCellId, "")

        for gs_data in gslist_data:
            param = gs_data[0]
            baseline_value = gs_data[1]

            if baseline_value == "SUFFIX":
                if param == "limit1":
                    if "MICRO" in sector_type:
                        baseline_value = "4"
                    else:
                        baseline_value = "0"

                elif param == "limit2":
                    if "MICRO" in sector_type:
                        baseline_value = "8"
                    else:
                        baseline_value = "3"

                elif param == "limit3":
                    if "MICRO" in sector_type:
                        baseline_value = "12"
                    else:
                        baseline_value = "6"

                elif param == "limit4":
                    if "MICRO" in sector_type:
                        baseline_value = "18"
                    else:
                        baseline_value = "12"

            index_param = dt_col.get(param, -1)
            if index_param == -1:
                oss_value = "OSS_VALUE_NOT_FOUND"
            else:
                oss_value = g_data[index_param]

            if ToGet.is_compare(oss_value, baseline_value):
                compliance = "MATCH"
            else:
                compliance = "MISMATCH"

            prefix = (
                "SubNetwork=ONRM_ROOT_MO,SubNetwork="
                if "CA1BSC1" in NodeId or "VA1BSC1" in NodeId
                else "SubNetwork=ONRM_ROOT_MO_R,SubNetwork="
            )
            gs_data = [NodeId,
                       GeranCellId,
                       moc,
                       param,
                       oss_value,
                       baseline_value,
                       compliance,
                       f"cmedit set {prefix}{NodeId},MeContext={NodeId},"
                       f"ManagedElement={NodeId},BscFunction=1,BscM=1,"
                       f"GeranCellM=1,GeranCell={GeranCellId},"
                       f"ChannelAllocAndOpt=1,IdleChannelMeasurement=1 "
                       f"{param}={baseline_value}"
                       f" --force"]

            gs_result.append(gs_data)

    return gs_result
