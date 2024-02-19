# TODO: Update suffix gerancellrelation
from enumlist import GERANCELLRELATION_COL


def check_compliance(oss_value: str, baseline_value: str):
    if str(oss_value) == str(baseline_value):
        return "MATCH"

    return "MISMATCH"


def gs_gerancellrelation_process(
    txt_data: list, gslist_data: list, dt_col: dict, moc: str
):
    gs_result = []

    for raw_data in txt_data:

        if str(raw_data).strip() == "" or "NodeId" in str(raw_data):
            continue

        g_data = str(raw_data).split()
        NodeId = g_data[dt_col.get("NodeId", 0)]
        GeranCellId = g_data[dt_col.get("GeranCellId", 4)]
        GeranCellRelationId = g_data[dt_col.get("GeranCellRelationId", 6)]

        pre_data = [
            NodeId,
            GeranCellId,
            GeranCellRelationId,
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
        ]

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

                if param == "cs":
                    if str(GeranCellId[:-1]) == str(GeranCellRelationId[:-1]):
                        baseline_value = "YES"
                        compliance = check_compliance(
                            oss_value=oss_value, baseline_value=baseline_value
                        )
                        pre_data[GERANCELLRELATION_COL.cs_OSS.value] = oss_value
                        pre_data[GERANCELLRELATION_COL.cs_BASELINE.value] = (
                            baseline_value
                        )
                        pre_data[GERANCELLRELATION_COL.cs_COMPLIANCE.value] = compliance

                    elif str(GeranCellId[:-1]) != str(GeranCellRelationId[:-1]):
                        baseline_value = "NO"
                        compliance = check_compliance(
                            oss_value=oss_value, baseline_value=baseline_value
                        )
                        pre_data[GERANCELLRELATION_COL.cs_OSS.value] = oss_value
                        pre_data[GERANCELLRELATION_COL.cs_BASELINE.value] = (
                            baseline_value
                        )
                        pre_data[GERANCELLRELATION_COL.cs_COMPLIANCE.value] = compliance
            else:
                if param == "awOffset":
                    pre_data[GERANCELLRELATION_COL.awOffset_OSS.value] = oss_value
                    pre_data[GERANCELLRELATION_COL.awOffset_BASELINE.value] = (
                        baseline_value
                    )
                    pre_data[GERANCELLRELATION_COL.awOffset_COMPLIANCE.value] = (
                        compliance
                    )
                elif param == "bqOffset":
                    pre_data[GERANCELLRELATION_COL.bqOffset_OSS.value] = oss_value
                    pre_data[GERANCELLRELATION_COL.bqOffset_BASELINE.value] = (
                        baseline_value
                    )
                    pre_data[GERANCELLRELATION_COL.bqOffset_COMPLIANCE.value] = (
                        compliance
                    )
                elif param == "bqOffsetAfr":
                    pre_data[GERANCELLRELATION_COL.bqOffsetAfr_OSS.value] = oss_value
                    pre_data[GERANCELLRELATION_COL.bqOffsetAfr_BASELINE.value] = (
                        baseline_value
                    )
                    pre_data[GERANCELLRELATION_COL.bqOffsetAfr_COMPLIANCE.value] = (
                        compliance
                    )
                elif param == "cand":
                    pre_data[GERANCELLRELATION_COL.cand_OSS.value] = oss_value
                    pre_data[GERANCELLRELATION_COL.cand_BASELINE.value] = baseline_value
                    pre_data[GERANCELLRELATION_COL.cand_COMPLIANCE.value] = compliance

                elif param == "hiHyst":
                    pre_data[GERANCELLRELATION_COL.hiHyst_OSS.value] = oss_value
                    pre_data[GERANCELLRELATION_COL.hiHyst_BASELINE.value] = (
                        baseline_value
                    )
                    pre_data[GERANCELLRELATION_COL.hiHyst_COMPLIANCE.value] = compliance
                elif param == "kHyst":
                    pre_data[GERANCELLRELATION_COL.kHyst_OSS.value] = oss_value
                    pre_data[GERANCELLRELATION_COL.kHyst_BASELINE.value] = (
                        baseline_value
                    )
                    pre_data[GERANCELLRELATION_COL.kHyst_COMPLIANCE.value] = compliance
                elif param == "kOffset":
                    pre_data[GERANCELLRELATION_COL.kOffset_OSS.value] = oss_value
                    pre_data[GERANCELLRELATION_COL.kOffset_BASELINE.value] = (
                        baseline_value
                    )
                    pre_data[GERANCELLRELATION_COL.kOffset_COMPLIANCE.value] = (
                        compliance
                    )
                elif param == "lHyst":
                    pre_data[GERANCELLRELATION_COL.lHyst_OSS.value] = oss_value
                    pre_data[GERANCELLRELATION_COL.lHyst_BASELINE.value] = (
                        baseline_value
                    )
                    pre_data[GERANCELLRELATION_COL.lHyst_COMPLIANCE.value] = compliance
                elif param == "lOffset":
                    pre_data[GERANCELLRELATION_COL.lOffset_OSS.value] = oss_value
                    pre_data[GERANCELLRELATION_COL.lOffset_BASELINE.value] = (
                        baseline_value
                    )
                    pre_data[GERANCELLRELATION_COL.lOffset_COMPLIANCE.value] = (
                        compliance
                    )
                elif param == "loHyst":
                    pre_data[GERANCELLRELATION_COL.loHyst_OSS.value] = oss_value
                    pre_data[GERANCELLRELATION_COL.loHyst_BASELINE.value] = (
                        baseline_value
                    )
                    pre_data[GERANCELLRELATION_COL.loHyst_COMPLIANCE.value] = compliance
                elif param == "offset":
                    pre_data[GERANCELLRELATION_COL.offset_OSS.value] = oss_value
                    pre_data[GERANCELLRELATION_COL.offset_BASELINE.value] = (
                        baseline_value
                    )
                    pre_data[GERANCELLRELATION_COL.offset_COMPLIANCE.value] = compliance
                elif param == "tRHyst":
                    pre_data[GERANCELLRELATION_COL.tRHyst_OSS.value] = oss_value
                    pre_data[GERANCELLRELATION_COL.tRHyst_BASELINE.value] = (
                        baseline_value
                    )
                    pre_data[GERANCELLRELATION_COL.tRHyst_COMPLIANCE.value] = compliance
                elif param == "tROffset":
                    pre_data[GERANCELLRELATION_COL.tROffset_OSS.value] = oss_value
                    pre_data[GERANCELLRELATION_COL.tROffset_BASELINE.value] = (
                        baseline_value
                    )
                    pre_data[GERANCELLRELATION_COL.tROffset_COMPLIANCE.value] = (
                        compliance
                    )

        gs_result.append(pre_data)
    return gs_result
