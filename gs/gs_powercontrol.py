# TODO: need Update SUFFIX

from enumlist import POWERCONTROL_COL


def check_compliance(oss_value: str, baseline_value: str):
    if str(oss_value) == str(baseline_value):
        return "MATCH"

    return "MISMATCH"


def gs_powercontrol_process(txt_data: list, gslist_data: list, dt_col: dict, moc: str):
    gs_result = []

    for raw_data in txt_data:

        if str(raw_data).strip() == "" or "NodeId" in str(raw_data):
            continue

        g_data = str(raw_data).split()
        NodeId = g_data[dt_col.get("NodeId", 0)]
        GeranCellId = g_data[dt_col.get("GeranCellId", 4)]

        pre_data = [NodeId, GeranCellId, "", "", "", "", "", ""]

        for gs_data in gslist_data:
            param = gs_data[0]
            baseline_value = gs_data[1]

            index_param = dt_col.get(param, -1)
            if index_param == -1:
                oss_value = "OSS_VALUE_NOT_FOUND"
            else:
                oss_value = g_data[index_param]

            compliance = check_compliance(
                oss_value=oss_value, baseline_value=baseline_value
            )

            if baseline_value == "SUFFIX":

                if param == "hpbState":
                    if "TO3BSC1" in NodeId:
                        baseline_value = "ACTIVE"
                        compliance = check_compliance(
                            oss_value=oss_value, baseline_value=baseline_value
                        )
                        pre_data[POWERCONTROL_COL.hpbState_OSS.value] = oss_value
                        pre_data[POWERCONTROL_COL.hpbState_BASELINE.value] = (
                            baseline_value
                        )
                        pre_data[POWERCONTROL_COL.hpbState_COMPLIANCE.value] = (
                            compliance
                        )

                    elif "TO5BSC1" in NodeId:
                        baseline_value = "ACTIVE"
                        compliance = check_compliance(
                            oss_value=oss_value, baseline_value=baseline_value
                        )
                        pre_data[POWERCONTROL_COL.hpbState_OSS.value] = oss_value
                        pre_data[POWERCONTROL_COL.hpbState_BASELINE.value] = (
                            baseline_value
                        )
                        pre_data[POWERCONTROL_COL.hpbState_COMPLIANCE.value] = (
                            compliance
                        )

                    elif "VA1BSC1" in NodeId:
                        baseline_value = "INACTIVE"
                        compliance = check_compliance(
                            oss_value=oss_value, baseline_value=baseline_value
                        )
                        pre_data[POWERCONTROL_COL.hpbState_OSS.value] = oss_value
                        pre_data[POWERCONTROL_COL.hpbState_BASELINE.value] = (
                            baseline_value
                        )
                        pre_data[POWERCONTROL_COL.hpbState_COMPLIANCE.value] = (
                            compliance
                        )

                    elif "CA1BSC1" in NodeId:
                        baseline_value = "INACTIVE"
                        compliance = check_compliance(
                            oss_value=oss_value, baseline_value=baseline_value
                        )
                        pre_data[POWERCONTROL_COL.hpbState_OSS.value] = oss_value
                        pre_data[POWERCONTROL_COL.hpbState_BASELINE.value] = (
                            baseline_value
                        )
                        pre_data[POWERCONTROL_COL.hpbState_COMPLIANCE.value] = (
                            compliance
                        )

                    elif "ML2BSC1" in NodeId:
                        baseline_value = "INACTIVE"
                        compliance = check_compliance(
                            oss_value=oss_value, baseline_value=baseline_value
                        )
                        pre_data[POWERCONTROL_COL.hpbState_OSS.value] = oss_value
                        pre_data[POWERCONTROL_COL.hpbState_BASELINE.value] = (
                            baseline_value
                        )
                        pre_data[POWERCONTROL_COL.hpbState_COMPLIANCE.value] = (
                            compliance
                        )

                    elif "HA1BSC1" in NodeId:
                        baseline_value = "INACTIVE"
                        compliance = check_compliance(
                            oss_value=oss_value, baseline_value=baseline_value
                        )
                        pre_data[POWERCONTROL_COL.hpbState_OSS.value] = oss_value
                        pre_data[POWERCONTROL_COL.hpbState_BASELINE.value] = (
                            baseline_value
                        )
                        pre_data[POWERCONTROL_COL.hpbState_COMPLIANCE.value] = (
                            compliance
                        )

            else:
                if param == "amrPcState":
                    pre_data[POWERCONTROL_COL.amrPcState_OSS.value] = oss_value
                    pre_data[POWERCONTROL_COL.amrPcState_BASELINE.value] = (
                        baseline_value
                    )
                    pre_data[POWERCONTROL_COL.amrPcState_COMPLIANCE.value] = compliance

        gs_result.append(pre_data)
    return gs_result
