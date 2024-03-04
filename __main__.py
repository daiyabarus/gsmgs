import sys
import os
import gslist
import enumlist
import time
from datetime import datetime

from gs import (
    gs_channelallocandopt_process,
    gs_cellloadsharing_process,
    gs_channelgroup_process,
    gs_dtm_process,
    gs_dynamicfrhrmodeadaption_process,
    gs_dynamichrallocation_process,
    gs_gerancell_process,
    gs_gerancellrelation_process,
    gs_gprs_process,
    gs_hierarchicalcellstructure_process,
    gs_idlechannelmeasurement_process,
    gs_idlemodeandpaging_process,
    gs_interranmobility_process,
    gs_lchadaptiveconf_process,
    gs_locatingfilter_process,
    gs_locatingintracellhandover_process,
    gs_locatingpenalty_process,
    gs_locatingurgency_process,
    gs_mobility_process,
    gs_msqueuing_process,
    gs_powercontrol_process,
    gs_powercontroldownlink_process,
    gs_powercontroluplink_process,
    gs_powersavings_process,
    gs_radiolinktimeout_process,
    gs_subcellloaddistribution_process,
    gs_externalgerancellrelation_process,
)

from printtofile import PrintToFile
from gsheaderslist import Headers
from toget import ToGet
from gscheck_result import gs_process_result

startTime = time.time()
print("StartTime: ", datetime.fromtimestamp(startTime))


def main():
    source_folder = sys.argv[1]
    # source_netstats = sys.argv[2]
    # source_newreference = sys.argv[3]
    # source_masterlist = sys.argv[4]
    source_data = sys.argv[2]
    source_netstats = os.path.join(source_data, "netstatRemedy.csv")
    source_masterlist = os.path.join(source_data, "MasterSiteList.xlsx")
    source_newreference = os.path.join(source_data, "newReference.xlsx")

    gs_result_final = []

    gerancell_csv = os.path.join(source_folder, "GeranCell.csv")
    gerancell_data = ToGet.txtfile_to_list(txtpath=gerancell_csv)
    gs_result_gerancell = gs_gerancell_process(
        txt_data=gerancell_data,
        gslist_data=gslist.gs_gerancell(),
        dt_col=enumlist.gerancell_col(),
        moc="GeranCell",
    )
    gs_result_final.extend(gs_result_gerancell)

    cellloadsharing_csv = os.path.join(source_folder, "CellLoadSharing.csv")
    cellloadsharing_data = ToGet.txtfile_to_list(txtpath=cellloadsharing_csv)
    gs_result_cellloadsharing = gs_cellloadsharing_process(
        txt_data=cellloadsharing_data,
        gslist_data=gslist.gs_cellloadsharing(),
        dt_col=enumlist.cellloadsharing_col(),
        moc="CellLoadSharing",
    )
    gs_result_final.extend(gs_result_cellloadsharing)

    channelallocandopt_csv = os.path.join(
        source_folder, "ChannelAllocAndOpt.csv"
    )
    channelallocandopt_data = ToGet.txtfile_to_list(
        txtpath=channelallocandopt_csv
    )
    gs_result_channelallocandopt = gs_channelallocandopt_process(
        txt_data=channelallocandopt_data,
        gslist_data=gslist.gs_channelallocandopt(),
        dt_col=enumlist.channelallocandopt_col(),
        moc="ChannelAllocAndOpt",
    )
    gs_result_final.extend(gs_result_channelallocandopt)

    # ChannelGroup.csv
    channelgroup_csv = os.path.join(source_folder, "ChannelGroup.csv")
    channelgroup_data = ToGet.txtfile_to_list(txtpath=channelgroup_csv)
    gs_result_channelgroup = gs_channelgroup_process(
        txt_data=channelgroup_data,
        gslist_data=gslist.gs_channelgroup(),
        dt_col=enumlist.channelgroup_col(),
        moc="ChannelGroup",
    )
    gs_result_final.extend(gs_result_channelgroup)

    # Dtm.csv
    dtm_csv = os.path.join(source_folder, "Dtm.csv")
    dtm_data = ToGet.txtfile_to_list(txtpath=dtm_csv)
    gs_result_dtm = gs_dtm_process(
        txt_data=dtm_data,
        gslist_data=gslist.gs_dtm(),
        dt_col=enumlist.dtm_col(),
        moc="Dtm",
    )
    gs_result_final.extend(gs_result_dtm)

    # DynamicFrHrModeAdaption.csv
    dynamicfrhrmodeadaption_csv = os.path.join(
        source_folder, "DynamicFrHrModeAdaption.csv"
    )
    dynamicfrhrmodeadaption_data = ToGet.txtfile_to_list(
        txtpath=dynamicfrhrmodeadaption_csv
    )
    gs_result_dynamicfrhrmodeadaption = gs_dynamicfrhrmodeadaption_process(
        txt_data=dynamicfrhrmodeadaption_data,
        gslist_data=gslist.gs_dynamicfrhrmodeadaption(),
        dt_col=enumlist.dynamicfrhrmodeadaption_col(),
        moc="DynamicFrHrModeAdaption",
    )
    gs_result_final.extend(gs_result_dynamicfrhrmodeadaption)

    # DynamicHrAllocation.csv
    dynamichrallocation_csv = os.path.join(
        source_folder, "DynamicHrAllocation.csv"
    )
    dynamichrallocation_data = ToGet.txtfile_to_list(
        txtpath=dynamichrallocation_csv
    )
    gs_result_dynamichrallocation = gs_dynamichrallocation_process(
        txt_data=dynamichrallocation_data,
        gslist_data=gslist.gs_dynamichrallocation(),
        dt_col=enumlist.dynamichrallocation_col(),
        moc="DynamicHrAllocation",
    )
    gs_result_final.extend(gs_result_dynamichrallocation)

    # GeranCellRelation.csv
    gerancellrelation_csv = os.path.join(
        source_folder, "GeranCellRelation.csv"
    )
    gerancellrelation_data = ToGet.txtfile_to_list(
        txtpath=gerancellrelation_csv
    )
    gs_result_gerancellrelation = gs_gerancellrelation_process(
        txt_data=gerancellrelation_data,
        gslist_data=gslist.gs_gerancellrelation(),
        dt_col=enumlist.gerancellrelation_col(),
        moc="GeranCellRelation",
    )
    gs_result_final.extend(gs_result_gerancellrelation)

    # ExternalGeranCellRelation.csv
    externalgerancellrelation_csv = os.path.join(
        source_folder, "ExternalGeranCellRelation.csv"
    )
    externalgerancellrelation_data = ToGet.txtfile_to_list(
        txtpath=externalgerancellrelation_csv
    )
    gs_result_externalgerancellrelation = gs_externalgerancellrelation_process(
        txt_data=externalgerancellrelation_data,
        gslist_data=gslist.gs_externalgerancellrelation(),
        dt_col=enumlist.externalgerancellrelation_col(),
        moc="ExternalGeranCellRelation",
    )
    gs_result_final.extend(gs_result_externalgerancellrelation)

    # Gprs.csv
    gprs_csv = os.path.join(source_folder, "Gprs.csv")
    gprs_data = ToGet.txtfile_to_list(txtpath=gprs_csv)
    gs_result_gprs = gs_gprs_process(
        txt_data=gprs_data,
        gslist_data=gslist.gs_gprs(),
        dt_col=enumlist.gprs_col(),
        moc="Gprs",
    )
    gs_result_final.extend(gs_result_gprs)

    # HierarchicalCellStructure.csv
    hierarchicalcellstructure_csv = os.path.join(
        source_folder, "HierarchicalCellStructure.csv"
    )
    hierarchicalcellstructure_data = ToGet.txtfile_to_list(
        txtpath=hierarchicalcellstructure_csv
    )
    gs_result_hierarchicalcellstructure = gs_hierarchicalcellstructure_process(
        txt_data=hierarchicalcellstructure_data,
        gslist_data=gslist.gs_hierarchicalcellstructure(),
        dt_col=enumlist.hierarchicalcellstructure_col(),
        moc="HierarchicalCellStructure",
    )
    gs_result_final.extend(gs_result_hierarchicalcellstructure)

    # IdleChannelMeasurement.csv
    netstatremedy_data = ToGet.csv_to_list(csv_file=source_netstats)
    idlechannelmeasurement_csv = os.path.join(
        source_folder, "IdleChannelMeasurement.csv"
    )
    idlechannelmeasurement_data = ToGet.txtfile_to_list(
        txtpath=idlechannelmeasurement_csv
    )
    gs_result_idlechannelmeasurement = gs_idlechannelmeasurement_process(
        txt_data=idlechannelmeasurement_data,
        netstatremedy_data=netstatremedy_data,
        gslist_data=gslist.gs_idlechannelmeasurement(),
        dt_col=enumlist.idlechannelmeasurement_col(),
        moc="IdleChannelMeasurement",
    )
    gs_result_final.extend(gs_result_idlechannelmeasurement)

    # IdleModeAndPaging.csv
    mastersite_sheets = ToGet.open_sheet_by_name(
        source_masterlist, "MasterSiteList"
    )
    mastersite_list = ToGet.sheet_to_dict_list(mastersite_sheets)
    netstatremedy_data = ToGet.csv_to_list(csv_file=source_netstats)

    idlemodeandpaging_csv = os.path.join(
        source_folder, "IdleModeAndPaging.csv"
    )
    idlemodeandpaging_data = ToGet.txtfile_to_list(
        txtpath=idlemodeandpaging_csv
    )
    gs_result_idlemodeandpaging = gs_idlemodeandpaging_process(
        txt_data=idlemodeandpaging_data,
        netlist_data=netstatremedy_data,
        mastersite_data=mastersite_list,
        gslist_data=gslist.gs_idlemodeandpaging(),
        dt_col=enumlist.idlemodeandpaging_col(),
        moc="IdleModeAndPaging",
    )
    gs_result_final.extend(gs_result_idlemodeandpaging)

    # InterRanMobility.csv
    interranmobility_csv = os.path.join(source_folder, "InterRanMobility.csv")
    interranmobility_data = ToGet.txtfile_to_list(txtpath=interranmobility_csv)
    gs_result_interranmobility = gs_interranmobility_process(
        txt_data=interranmobility_data,
        gslist_data=gslist.gs_interranmobility(),
        dt_col=enumlist.interranmobility_col(),
        moc="InterRanMobility",
    )
    gs_result_final.extend(gs_result_interranmobility)

    # LchAdaptiveConf.csv
    lchadaptiveconf_csv = os.path.join(source_folder, "LchAdaptiveConf.csv")
    lchadaptiveconf_data = ToGet.txtfile_to_list(txtpath=lchadaptiveconf_csv)
    gs_result_lchadaptiveconf = gs_lchadaptiveconf_process(
        txt_data=lchadaptiveconf_data,
        gslist_data=gslist.gs_lchadaptiveconf(),
        dt_col=enumlist.lchadaptiveconf_col(),
        moc="LchAdaptiveConf",
    )
    gs_result_final.extend(gs_result_lchadaptiveconf)

    # LocatingFilter.csv
    LocatingFilter_csv = os.path.join(source_folder, "LocatingFilter.csv")
    locatingfilter_data = ToGet.txtfile_to_list(txtpath=LocatingFilter_csv)
    gs_result_locatingfilter = gs_locatingfilter_process(
        txt_data=locatingfilter_data,
        gslist_data=gslist.gs_locatingfilter(),
        dt_col=enumlist.locatingfilter_col(),
        moc="LocatingFilter",
    )
    gs_result_final.extend(gs_result_locatingfilter)

    # LocatingIntraCellHandover.csv
    locatingintracellhandover_csv = os.path.join(
        source_folder, "LocatingIntraCellHandover.csv"
    )
    locatingintracellhandover_data = ToGet.txtfile_to_list(
        txtpath=locatingintracellhandover_csv
    )
    gs_result_locatingintracellhandover = gs_locatingintracellhandover_process(
        txt_data=locatingintracellhandover_data,
        gslist_data=gslist.gs_locatingintracellhandover(),
        dt_col=enumlist.locatingintracellhandover_col(),
        moc="LocatingIntraCellHandover",
    )
    gs_result_final.extend(gs_result_locatingintracellhandover)

    # LocatingPenalty.csv
    locatingpenalty_csv = os.path.join(source_folder, "LocatingPenalty.csv")
    locatingpenalty_data = ToGet.txtfile_to_list(txtpath=locatingpenalty_csv)
    gs_result_locatingpenalty = gs_locatingpenalty_process(
        txt_data=locatingpenalty_data,
        gslist_data=gslist.gs_locatingpenalty(),
        dt_col=enumlist.locatingpenalty_col(),
        moc="LocatingPenalty",
    )
    gs_result_final.extend(gs_result_locatingpenalty)

    # LocatingUrgency.csv
    locatingurgency_csv = os.path.join(source_folder, "LocatingUrgency.csv")
    locatingurgency_data = ToGet.txtfile_to_list(txtpath=locatingurgency_csv)
    gs_result_locatingurgency = gs_locatingurgency_process(
        txt_data=locatingurgency_data,
        gslist_data=gslist.gs_locatingurgency(),
        dt_col=enumlist.locatingurgency_col(),
        moc="LocatingUrgency",
    )
    gs_result_final.extend(gs_result_locatingurgency)

    # Mobility.csv
    mobility_csv = os.path.join(source_folder, "Mobility.csv")
    mobility_data = ToGet.txtfile_to_list(txtpath=mobility_csv)
    gs_result_mobility = gs_mobility_process(
        txt_data=mobility_data,
        gslist_data=gslist.gs_mobility(),
        dt_col=enumlist.mobility_col(),
        moc="Mobility",
    )
    gs_result_final.extend(gs_result_mobility)

    # MsQueuing.csv
    msqueuing_csv = os.path.join(source_folder, "MsQueuing.csv")
    msqueuing_data = ToGet.txtfile_to_list(txtpath=msqueuing_csv)
    gs_result_msqueuing = gs_msqueuing_process(
        txt_data=msqueuing_data,
        gslist_data=gslist.gs_msqueuing(),
        dt_col=enumlist.msqueuing_col(),
        moc="MsQueuing",
    )
    gs_result_final.extend(gs_result_msqueuing)

    new_gsmcells_sheet = ToGet.open_sheet_by_name(
        source_newreference, "gsmCells"
    )
    new_sites_sheet = ToGet.open_sheet_by_name(source_newreference, "sites")
    new_gsmcells = ToGet.sheet_to_dict_list(new_gsmcells_sheet)
    new_sites = ToGet.sheet_to_dict_list(new_sites_sheet)
    powercontrol_csv = os.path.join(source_folder, "PowerControl.csv")
    powercontrol_data = ToGet.txtfile_to_list(txtpath=powercontrol_csv)
    gs_result_powercontrol = gs_powercontrol_process(
        txt_data=powercontrol_data,
        newreference_gsmcells=new_gsmcells,
        newreference_sites=new_sites,
        gslist_data=gslist.gs_powercontrol(),
        dt_col=enumlist.powercontrol_col(),
        moc="PowerControl",
    )
    gs_result_final.extend(gs_result_powercontrol)

    # PowerControlDownlink.csv
    powercontroldownlink_csv = os.path.join(
        source_folder, "PowerControlDownlink.csv"
    )
    powercontroldownlink_data = ToGet.txtfile_to_list(
        txtpath=powercontroldownlink_csv
    )
    gs_result_powercontroldownlink = gs_powercontroldownlink_process(
        txt_data=powercontroldownlink_data,
        gslist_data=gslist.gs_powercontroldownlink(),
        dt_col=enumlist.powercontroldownlink_col(),
        moc="PowerControlDownlink",
    )
    gs_result_final.extend(gs_result_powercontroldownlink)

    # PowerControlUplink.csv
    powercontroluplink_csv = os.path.join(
        source_folder, "PowerControlUplink.csv"
    )
    powercontroluplink_data = ToGet.txtfile_to_list(
        txtpath=powercontroluplink_csv
    )
    gs_result_powercontroluplink = gs_powercontroluplink_process(
        txt_data=powercontroluplink_data,
        gslist_data=gslist.gs_powercontroluplink(),
        dt_col=enumlist.powercontroluplink_col(),
        moc="PowerControlUplink",
    )
    gs_result_final.extend(gs_result_powercontroluplink)

    # PowerSavings.csv
    powersavings_csv = os.path.join(source_folder, "PowerSavings.csv")
    powersavings_data = ToGet.txtfile_to_list(txtpath=powersavings_csv)
    gs_result_powersavings = gs_powersavings_process(
        txt_data=powersavings_data,
        gslist_data=gslist.gs_powersavings(),
        dt_col=enumlist.powersavings_col(),
        moc="PowerSavings",
    )
    gs_result_final.extend(gs_result_powersavings)

    # RadioLinkTimeout.csv
    radiolinktimeout_csv = os.path.join(source_folder, "RadioLinkTimeout.csv")
    radiolinktimeout_data = ToGet.txtfile_to_list(txtpath=radiolinktimeout_csv)
    gs_result_radiolinktimeout = gs_radiolinktimeout_process(
        txt_data=radiolinktimeout_data,
        gslist_data=gslist.gs_radiolinktimeout(),
        dt_col=enumlist.radiolinktimeout_col(),
        moc="RadioLinkTimeout",
    )
    gs_result_final.extend(gs_result_radiolinktimeout)

    # SubcellLoadDistribution.csv
    subcellloaddistribution_csv = os.path.join(
        source_folder, "SubcellLoadDistribution.csv"
    )
    subcellloaddistribution_data = ToGet.txtfile_to_list(
        txtpath=subcellloaddistribution_csv
    )
    gs_result_subcellloaddistribution = gs_subcellloaddistribution_process(
        txt_data=subcellloaddistribution_data,
        gslist_data=gslist.gs_subcellloaddistribution(),
        dt_col=enumlist.subcellloaddistribution_col(),
        moc="SubcellLoadDistribution",
    )
    gs_result_final.extend(gs_result_subcellloaddistribution)

    # GS Result Process
    gsresult_summary = gs_process_result(
        netpath=source_netstats,
        gs_result_gerancell=gs_result_gerancell,
        gs_result_channelallocandopt=gs_result_channelallocandopt,
        gs_result_cellloadsharing=gs_result_cellloadsharing,
        gs_result_channelgroup=gs_result_channelgroup,
        gs_result_dtm=gs_result_dtm,
        gs_result_dynamicfrhrmodeadaption=gs_result_dynamicfrhrmodeadaption,
        gs_result_dynamichrallocation=gs_result_dynamichrallocation,
        gs_result_gerancellrelation=gs_result_gerancellrelation,
        gs_result_externalgerancellrelation=gs_result_externalgerancellrelation,
        gs_result_gprs=gs_result_gprs,
        gs_result_hierarchicalcellstructure=gs_result_hierarchicalcellstructure,
        gs_result_idlechannelmeasurement=gs_result_idlechannelmeasurement,
        gs_result_idlemodeandpaging=gs_result_idlemodeandpaging,
        gs_result_interranmobility=gs_result_interranmobility,
        gs_result_lchadaptiveconf=gs_result_lchadaptiveconf,
        gs_result_locatingfilter=gs_result_locatingfilter,
        gs_result_locatingintracellhandover=gs_result_locatingintracellhandover,
        gs_result_locatingpenalty=gs_result_locatingpenalty,
        gs_result_locatingurgency=gs_result_locatingurgency,
        gs_result_mobility=gs_result_mobility,
        gs_result_msqueuing=gs_result_msqueuing,
        gs_result_powercontrol=gs_result_powercontrol,
        gs_result_powercontroldownlink=gs_result_powercontroldownlink,
        gs_result_powercontroluplink=gs_result_powercontroluplink,
        gs_result_powersavings=gs_result_powersavings,
        gs_result_radiolinktimeout=gs_result_radiolinktimeout,
        gs_result_subcellloaddistribution=gs_result_subcellloaddistribution,
    )

    enm = source_folder[:3]
    result_file = os.path.join(
        source_folder,
        str(enm) + "_GS_GSM_RESULT_" + ToGet.get_current_datetime() + ".xlsx",
    )

    is_ok_gsresult = PrintToFile.to_xlsx_undefined_filled(
        file_to_save=result_file,
        ws_name="Summary",
        list_of_header=Headers.header_result(),
        list_of_contents=gsresult_summary,
        list_of_red=["MISMATCH", "UNDEFINED", "FAIL"],
        list_of_green=["PASS", "MATCH"],
    )

    is_ok_gerancell = PrintToFile.to_xlsx_undefined_filled(
        file_to_save=result_file,
        ws_name="GS_Audit",
        list_of_header=Headers.header_baseline(),
        list_of_contents=gs_result_final,
        list_of_red=["MISMATCH"],
        list_of_green=["MATCH"],
    )

    print("GS Result save as:", result_file)
    print("Summary", is_ok_gsresult)
    print("GeranCell", is_ok_gerancell)


if __name__ == "__main__":
    main()

endTime = time.time()
print("endTime: ", datetime.fromtimestamp(endTime))
elapsedTimeInMins = (endTime - startTime) / 60
print("Total Run Time (mins): ", elapsedTimeInMins)
