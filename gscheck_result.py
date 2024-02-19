from utils import UtilFunc
from enumlist import remedy_col


def cr_dt_from_netstats(netpath: str):
    netlist = UtilFunc.csv_to_list(csv_file=netpath)
    dt_col = remedy_col()

    dt_sector_name__site_name = dict()
    dt_sector_name__loc_code = dict()

    for data in netlist:
        sector_name = data[dt_col.get("ERP Sector Name", 0)]
        site_name = data[dt_col.get("ERP Site Name", 1)]
        loc_code = data[dt_col.get("ERP Site Location Code", 17)]

        if sector_name != "" and sector_name not in dt_sector_name__site_name:
            dt_sector_name__site_name[sector_name] = site_name

        if sector_name != "" and sector_name not in dt_sector_name__loc_code:
            dt_sector_name__loc_code[sector_name] = loc_code

    return dt_sector_name__site_name, dt_sector_name__loc_code


def get_mismatches(gslist: list) -> dict:
    dt_mismatch = dict()
    for data_1 in gslist:
        # mismatch_tmp = [item for item in data_1 if item == "MISMATCH"]
        gerancellid = data_1[1]
        mismatch_tmp = []
        for data_2 in data_1:
            if str(data_2).lower() == "mismatch":
                mismatch_tmp.append("MISMATCH")

        if gerancellid not in dt_mismatch:
            dt_mismatch[gerancellid] = len(mismatch_tmp)
        else:
            mismatch_count = dt_mismatch[gerancellid]
            mismatch_count = mismatch_count + len(mismatch_tmp)
            dt_mismatch[gerancellid] = mismatch_count

    return dt_mismatch


def gs_process_result(
    netpath: str,
    gs_result_gerancell: list,
    gs_result_subcellloaddistribution: list,
    gs_result_radiolinktimeout: list,
    gs_result_powersavings: list,
    gs_result_powercontroluplink: list,
    gs_result_powercontroldownlink: list,
    gs_result_powercontrol: list,
    gs_result_msqueuing: list,
    gs_result_mobility: list,
    gs_result_locatingurgency: list,
    gs_result_locatingpenalty: list,
    gs_result_locatingintracellhandover: list,
    gs_result_locatingfilter: list,
    gs_result_lchadaptiveconf: list,
    gs_result_interranmobility: list,
    gs_result_idlemodeandpaging: list,
    gs_result_idlechannelmeasurement: list,
    gs_result_hierarchicalcellstructure: list,
    gs_result_gprs: list,
    gs_result_gerancellrelation: list,
    gs_result_dynamichrallocation: list,
    gs_result_dynamicfrhrmodeadaption: list,
    gs_result_dtm: list,
    gs_result_channelgroup: list,
    gs_result_channelallocandopt: list,
    gs_result_cellloadsharing: list,
):
    gs_result = []

    dt_mismatch_gerancell = get_mismatches(gs_result_gerancell)
    dt_mismatch_subcellloaddistribution = get_mismatches(
        gs_result_subcellloaddistribution
    )
    dt_mismatch_radiolinktimeout = get_mismatches(gs_result_radiolinktimeout)
    dt_mismatch_powersavings = get_mismatches(gs_result_powersavings)
    dt_mismatch_powercontroluplink = get_mismatches(gs_result_powercontroluplink)
    dt_mismatch_powercontroldownlink = get_mismatches(gs_result_powercontroldownlink)
    dt_mismatch_powercontrol = get_mismatches(gs_result_powercontrol)
    dt_mismatch_msqueuing = get_mismatches(gs_result_msqueuing)
    dt_mismatch_mobility = get_mismatches(gs_result_mobility)
    dt_mismatch_locatingurgency = get_mismatches(gs_result_locatingurgency)
    dt_mismatch_locatingpenalty = get_mismatches(gs_result_locatingpenalty)
    dt_mismatch_locatingintracellhandover = get_mismatches(
        gs_result_locatingintracellhandover
    )
    dt_mismatch_locatingfilter = get_mismatches(gs_result_locatingfilter)
    dt_mismatch_lchadaptiveconf = get_mismatches(gs_result_lchadaptiveconf)
    dt_mismatch_interranmobility = get_mismatches(gs_result_interranmobility)
    dt_mismatch_idlemodeandpaging = get_mismatches(gs_result_idlemodeandpaging)
    dt_mismatch_idlechannelmeasurement = get_mismatches(
        gs_result_idlechannelmeasurement
    )
    dt_mismatch_hierarchicalcellstructure = get_mismatches(
        gs_result_hierarchicalcellstructure
    )
    dt_mismatch_gprs = get_mismatches(gs_result_gprs)
    dt_mismatch_gerancellrelation = get_mismatches(gs_result_gerancellrelation)
    dt_mismatch_dynamichrallocation = get_mismatches(gs_result_dynamichrallocation)
    dt_mismatch_dynamicfrhrmodeadaption = get_mismatches(
        gs_result_dynamicfrhrmodeadaption
    )
    dt_mismatch_dtm = get_mismatches(gs_result_dtm)
    dt_mismatch_channelgroup = get_mismatches(gs_result_channelgroup)
    dt_mismatch_channelallocandopt = get_mismatches(gs_result_channelallocandopt)
    dt_mismatch_cellloadsharing = get_mismatches(gs_result_cellloadsharing)

    dt_sector_name__site_name, dt_sector_name__loc_code = cr_dt_from_netstats(
        netpath=netpath
    )

    for gerancell_data in gs_result_gerancell:
        NodeId = gerancell_data[0]
        GeranCellId = gerancell_data[1]
        loc_code = dt_sector_name__loc_code.get(GeranCellId, "UNDEFINED")
        site_name = dt_sector_name__site_name.get(GeranCellId, "UNDEFINED")
        audit_date = UtilFunc.get_current_datetime_MMDDYYYY()
        audit_by = "YUPANA"
        gerancell_pass: int = get_moc_pass(dt_mismatch_gerancell, GeranCellId)
        subcellloaddistribution_pass: int = get_moc_pass(
            dt_mismatch_subcellloaddistribution, GeranCellId
        )
        radiolinktimeout_pass: int = get_moc_pass(
            dt_mismatch_radiolinktimeout, GeranCellId
        )
        powersavings_pass: int = get_moc_pass(dt_mismatch_powersavings, GeranCellId)
        powercontroluplink_pass: int = get_moc_pass(
            dt_mismatch_powercontroluplink, GeranCellId
        )
        powercontroldownlink_pass: int = get_moc_pass(
            dt_mismatch_powercontroldownlink, GeranCellId
        )
        powercontrol_pass: int = get_moc_pass(dt_mismatch_powercontrol, GeranCellId)
        msqueuing_pass: int = get_moc_pass(dt_mismatch_msqueuing, GeranCellId)
        mobility_pass: int = get_moc_pass(dt_mismatch_mobility, GeranCellId)
        locatingurgency_pass: int = get_moc_pass(
            dt_mismatch_locatingurgency, GeranCellId
        )
        locatingpenalty_pass: int = get_moc_pass(
            dt_mismatch_locatingpenalty, GeranCellId
        )
        locatingintracellhandover_pass: int = get_moc_pass(
            dt_mismatch_locatingintracellhandover, GeranCellId
        )
        locatingfilter_pass: int = get_moc_pass(dt_mismatch_locatingfilter, GeranCellId)
        lchadaptiveconf_pass: int = get_moc_pass(
            dt_mismatch_lchadaptiveconf, GeranCellId
        )
        interranmobility_pass: int = get_moc_pass(
            dt_mismatch_interranmobility, GeranCellId
        )
        idlemodeandpaging_pass: int = get_moc_pass(
            dt_mismatch_idlemodeandpaging, GeranCellId
        )
        idlechannelmeasurement_pass: int = get_moc_pass(
            dt_mismatch_idlechannelmeasurement, GeranCellId
        )
        hierarchicalcellstructure_pass: int = get_moc_pass(
            dt_mismatch_hierarchicalcellstructure, GeranCellId
        )
        gprs_pass: int = get_moc_pass(dt_mismatch_gprs, GeranCellId)
        gerancellrelation_pass: int = get_moc_pass(
            dt_mismatch_gerancellrelation, GeranCellId
        )
        dynamichrallocation_pass: int = get_moc_pass(
            dt_mismatch_dynamichrallocation, GeranCellId
        )
        dynamicfrhrmodeadaption_pass: int = get_moc_pass(
            dt_mismatch_dynamicfrhrmodeadaption, GeranCellId
        )
        dtm_pass: int = get_moc_pass(dt_mismatch_dtm, GeranCellId)
        channelgroup_pass: int = get_moc_pass(dt_mismatch_channelgroup, GeranCellId)
        channelallocandopt_pass: int = get_moc_pass(
            dt_mismatch_channelallocandopt, GeranCellId
        )
        cellloadsharing_pass: int = get_moc_pass(
            dt_mismatch_cellloadsharing, GeranCellId
        )
        remark = ""
        approved_by_rogers = ""

        data1 = [
            NodeId,
            GeranCellId,
            loc_code,
            site_name,
            audit_date,
            audit_by,
            gerancell_pass,
            subcellloaddistribution_pass,
            radiolinktimeout_pass,
            powersavings_pass,
            powercontroluplink_pass,
            powercontroldownlink_pass,
            powercontrol_pass,
            msqueuing_pass,
            mobility_pass,
            locatingurgency_pass,
            locatingpenalty_pass,
            locatingintracellhandover_pass,
            locatingfilter_pass,
            lchadaptiveconf_pass,
            interranmobility_pass,
            idlemodeandpaging_pass,
            idlechannelmeasurement_pass,
            hierarchicalcellstructure_pass,
            gprs_pass,
            gerancellrelation_pass,
            dynamichrallocation_pass,
            dynamicfrhrmodeadaption_pass,
            dtm_pass,
            channelgroup_pass,
            channelallocandopt_pass,
            cellloadsharing_pass,
            remark,
            approved_by_rogers,
        ]

        gs_result.append(data1)

    return gs_result


def get_moc_pass(dt_pass: dict, GeranCellId: str) -> str:
    moc_miss: int = dt_pass.get(GeranCellId, 999)
    moc_pass = "FAIL"
    if moc_miss == 999:
        moc_pass = "UNDEFINED"
    elif moc_miss == 0:
        moc_pass = "PASS"
    elif moc_miss > 0:
        # moc_pass = f"FAIL/{moc_miss}"
        moc_pass = "FAIL"

    return moc_pass
