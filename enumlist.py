from enum import Enum


class CELLLOADSHARING_COL(Enum):
    clsAcc_OSS = 2
    clsAcc_BASELINE = 3
    clsAcc_COMPLIANCE = 4
    clsLevel_OSS = 5
    clsLevel_BASELINE = 6
    clsLevel_COMPLIANCE = 7
    clsRamp_OSS = 8
    clsRamp_BASELINE = 9
    clsRamp_COMPLIANCE = 10
    clsState_OSS = 11
    clsState_BASELINE = 12
    clsState_COMPLIANCE = 13
    hoClsAcc_OSS = 14
    hoClsAcc_BASELINE = 15
    hoClsAcc_COMPLIANCE = 16
    rHyst_OSS = 17
    rHyst_BASELINE = 18
    rHyst_COMPLIANCE = 19


class LOCATINGPENALTY_COL(Enum):
    pSsBq_OSS = 2
    pSsBq_BASELINE = 3
    pSsBq_COMPLIANCE = 4
    pSsHf_OSS = 5
    pSsHf_BASELINE = 6
    pSsHf_COMPLIANCE = 7
    pSsTa_OSS = 8
    pSsTa_BASELINE = 9
    pSsTa_COMPLIANCE = 10
    pTimBq_OSS = 11
    pTimBq_BASELINE = 12
    pTimBq_COMPLIANCE = 13
    pTimHf_OSS = 14
    pTimHf_BASELINE = 15
    pTimHf_COMPLIANCE = 16
    pTimTa_OSS = 17
    pTimTa_BASELINE = 18
    pTimTa_COMPLIANCE = 19


class LOCATINGINTRACELLHANDOVER_COL(Enum):
    iho_OSS = 2
    iho_BASELINE = 3
    iho_COMPLIANCE = 4
    maxIHo_OSS = 5
    maxIHo_BASELINE = 6
    maxIHo_COMPLIANCE = 7
    qOffsetDl_OSS = 8
    qOffsetDl_BASELINE = 9
    qOffsetDl_COMPLIANCE = 10
    qOffsetDlAfr_OSS = 11
    qOffsetDlAfr_BASELINE = 12
    qOffsetDlAfr_COMPLIANCE = 13
    qOffsetUl_OSS = 14
    qOffsetUl_BASELINE = 15
    qOffsetUl_COMPLIANCE = 16
    qOffsetUlAfr_OSS = 17
    qOffsetUlAfr_BASELINE = 18
    qOffsetUlAfr_COMPLIANCE = 19
    tiHo_OSS = 20
    tiHo_BASELINE = 21
    tiHo_COMPLIANCE = 22
    tMaxiHo_OSS = 23
    tMaxiHo_BASELINE = 24
    tMaxiHo_COMPLIANCE = 25


class LOCATINGFILTER_COL(Enum):
    ferLen_OSS = 2
    ferLen_BASELINE = 3
    ferLen_COMPLIANCE = 4
    qEvalSd_OSS = 5
    qEvalSd_BASELINE = 6
    qEvalSd_COMPLIANCE = 7
    qEvalSi_OSS = 8
    qEvalSi_BASELINE = 9
    qEvalSi_COMPLIANCE = 10
    qLenSd_OSS = 11
    qLenSd_BASELINE = 12
    qLenSd_COMPLIANCE = 13
    qLenSi_OSS = 14
    qLenSi_BASELINE = 15
    qLenSi_COMPLIANCE = 16
    ssEvalSd_OSS = 17
    ssEvalSd_BASELINE = 18
    ssEvalSd_COMPLIANCE = 19
    ssEvalSi_OSS = 20
    ssEvalSi_BASELINE = 21
    ssEvalSi_COMPLIANCE = 22
    ssLenSd_OSS = 23
    ssLenSd_BASELINE = 24
    ssLenSd_COMPLIANCE = 25
    ssLenSi_OSS = 26
    ssLenSi_BASELINE = 27
    ssLenSi_COMPLIANCE = 28
    ssRampSd_OSS = 29
    ssRampSd_BASELINE = 30
    ssRampSd_COMPLIANCE = 31
    ssRampSi_OSS = 32
    ssRampSi_BASELINE = 33
    ssRampSi_COMPLIANCE = 34


class INTERRANMOBILITY_COL(Enum):
    fastRet3g_OSS = 2
    fastRet3g_BASELINE = 3
    fastRet3g_COMPLIANCE = 4
    fastRetLte_OSS = 5
    fastRetLte_BASELINE = 6
    fastRetLte_COMPLIANCE = 7
    fddMrr_OSS = 8
    fddMrr_BASELINE = 9
    fddMrr_COMPLIANCE = 10
    fddQMin_OSS = 11
    fddQMin_BASELINE = 12
    fddQMin_COMPLIANCE = 13
    fddQMinOff_OSS = 14
    fddQMinOff_BASELINE = 15
    fddQMinOff_COMPLIANCE = 16
    fddQOff_OSS = 17
    fddQOff_BASELINE = 18
    fddQOff_COMPLIANCE = 19
    fddRepThr2_OSS = 20
    fddRepThr2_BASELINE = 21
    fddRepThr2_COMPLIANCE = 22
    fddRscpMin_OSS = 23
    fddRscpMin_BASELINE = 24
    fddRscpMin_COMPLIANCE = 25
    isHoLev_OSS = 26
    isHoLev_BASELINE = 27
    isHoLev_COMPLIANCE = 28
    qsc_OSS = 29
    qsc_BASELINE = 30
    qsc_COMPLIANCE = 31
    qsci_OSS = 32
    qsci_BASELINE = 33
    qsci_COMPLIANCE = 34
    qsi_OSS = 35
    qsi_BASELINE = 36
    qsi_COMPLIANCE = 37
    sPrio_OSS = 38
    sPrio_BASELINE = 39
    sPrio_COMPLIANCE = 40


class IDLEMODEANDPAGING_COL(Enum):
    acc_OSS = 2
    acc_BASELINE = 3
    acc_COMPLIANCE = 4
    accMin_OSS = 5
    accMin_BASELINE = 6
    accMin_COMPLIANCE = 7
    agBlk_OSS = 8
    agBlk_BASELINE = 9
    agBlk_COMPLIANCE = 10
    att_OSS = 11
    att_BASELINE = 12
    att_COMPLIANCE = 13
    cb_OSS = 14
    cb_BASELINE = 15
    cb_COMPLIANCE = 16
    cbq_OSS = 17
    cbq_BASELINE = 18
    cbq_COMPLIANCE = 19
    crh_OSS = 20
    crh_BASELINE = 21
    crh_COMPLIANCE = 22
    cro_OSS = 23
    cro_BASELINE = 24
    cro_COMPLIANCE = 25
    maxRet_OSS = 26
    maxRet_BASELINE = 27
    maxRet_COMPLIANCE = 28
    mFrms_OSS = 29
    mFrms_BASELINE = 30
    mFrms_COMPLIANCE = 31
    nccPerm_OSS = 32
    nccPerm_BASELINE = 33
    nccPerm_COMPLIANCE = 34
    pt_OSS = 35
    pt_BASELINE = 36
    pt_COMPLIANCE = 37
    siMsg1_OSS = 38
    siMsg1_BASELINE = 39
    siMsg1_COMPLIANCE = 40
    siMsg7_OSS = 41
    siMsg7_BASELINE = 42
    siMsg7_COMPLIANCE = 43
    siMsg8_OSS = 44
    siMsg8_BASELINE = 45
    siMsg8_COMPLIANCE = 46
    t3212_OSS = 47
    t3212_BASELINE = 48
    t3212_COMPLIANCE = 49
    to_OSS = 50
    to_BASELINE = 51
    to_COMPLIANCE = 52
    tx_OSS = 53
    tx_BASELINE = 54
    tx_COMPLIANCE = 55


class IDLECHANNELMEASUREMENT_COL(Enum):
    icmState_OSS = 2
    icmState_BASELINE = 3
    icmState_COMPLIANCE = 4
    intAve_OSS = 5
    intAve_BASELINE = 6
    intAve_COMPLIANCE = 7
    limit1_OSS = 8
    limit1_BASELINE = 9
    limit1_COMPLIANCE = 10
    limit2_OSS = 11
    limit2_BASELINE = 12
    limit2_COMPLIANCE = 13
    limit3_OSS = 14
    limit3_BASELINE = 15
    limit3_COMPLIANCE = 16
    limit4_OSS = 17
    limit4_BASELINE = 18
    limit4_COMPLIANCE = 19


class HIERARCHICALCELLSTRUCTURE_COL(Enum):
    fastMsReg_OSS = 2
    fastMsReg_BASELINE = 3
    fastMsReg_COMPLIANCE = 4
    hcsIn_OSS = 5
    hcsIn_BASELINE = 6
    hcsIn_COMPLIANCE = 7
    hcsOut_OSS = 8
    hcsOut_BASELINE = 9
    hcsOut_COMPLIANCE = 10
    layer_OSS = 11
    layer_BASELINE = 12
    layer_COMPLIANCE = 13
    layerHyst_OSS = 14
    layerHyst_BASELINE = 15
    layerHyst_COMPLIANCE = 16
    layerThr_OSS = 17
    layerThr_BASELINE = 18
    layerThr_COMPLIANCE = 19
    pSsTemp_OSS = 20
    pSsTemp_BASELINE = 21
    pSsTemp_COMPLIANCE = 22
    pTimTemp_OSS = 23
    pTimTemp_BASELINE = 24
    pTimTemp_COMPLIANCE = 25


class GPRS_COL(Enum):
    chCsDl_OSS = 2
    chCsDl_BASELINE = 3
    chCsDl_COMPLIANCE = 4
    gprsSupState_OSS = 5
    gprsSupState_BASELINE = 6
    gprsSupState_COMPLIANCE = 7
    pskOnBcch_OSS = 8
    pskOnBcch_BASELINE = 9
    pskOnBcch_COMPLIANCE = 10
    scAlloc_OSS = 11
    scAlloc_BASELINE = 12
    scAlloc_COMPLIANCE = 13


class GERANCELLRELATION_COL(Enum):
    awOffset_OSS = 3
    awOffset_BASELINE = 4
    awOffset_COMPLIANCE = 5
    bqOffset_OSS = 6
    bqOffset_BASELINE = 7
    bqOffset_COMPLIANCE = 8
    bqOffsetAfr_OSS = 9
    bqOffsetAfr_BASELINE = 10
    bqOffsetAfr_COMPLIANCE = 11
    cand_OSS = 12
    cand_BASELINE = 13
    cand_COMPLIANCE = 14
    cs_OSS = 15
    cs_BASELINE = 16
    cs_COMPLIANCE = 17
    hiHyst_OSS = 18
    hiHyst_BASELINE = 19
    hiHyst_COMPLIANCE = 20
    kHyst_OSS = 21
    kHyst_BASELINE = 22
    kHyst_COMPLIANCE = 23
    kOffset_OSS = 24
    kOffset_BASELINE = 25
    kOffset_COMPLIANCE = 26
    lHyst_OSS = 27
    lHyst_BASELINE = 28
    lHyst_COMPLIANCE = 29
    lOffset_OSS = 30
    lOffset_BASELINE = 31
    lOffset_COMPLIANCE = 32
    loHyst_OSS = 33
    loHyst_BASELINE = 34
    loHyst_COMPLIANCE = 35
    offset_OSS = 36
    offset_BASELINE = 37
    offset_COMPLIANCE = 38
    tRHyst_OSS = 39
    tRHyst_BASELINE = 40
    tRHyst_COMPLIANCE = 41
    tROffset_OSS = 42
    tROffset_BASELINE = 43
    tROffset_COMPLIANCE = 44


class GERANCELL_COL(Enum):
    bcchType_OSS = 2
    bcchType_BASELINE = 3
    bcchType_COMPLIANCE = 4
    cSysType_OSS = 5
    cSysType_BASELINE = 6
    cSysType_COMPLIANCE = 7
    fnOffset_OSS = 8
    fnOffset_BASELINE = 9
    fnOffset_COMPLIANCE = 10
    irc_OSS = 11
    irc_BASELINE = 12
    irc_COMPLIANCE = 13
    state_OSS = 14
    state_BASELINE = 15
    state_COMPLIANCE = 16
    xRange_OSS = 17
    xRange_BASELINE = 18
    xRange_COMPLIANCE = 19


class DYNAMICHRALLOCATION_COL(Enum):
    dha_OSS = 2
    dha_BASELINE = 3
    dha_COMPLIANCE = 4
    dtHAmr_OSS = 5
    dtHAmr_BASELINE = 6
    dtHAmr_COMPLIANCE = 7
    dtHNAmr_OSS = 8
    dtHNAmr_BASELINE = 9
    dtHNAmr_COMPLIANCE = 10


class DYNAMICFRHRMODEADAPTION_COL(Enum):
    dmQb_OSS = 2
    dmQb_BASELINE = 3
    dmQb_COMPLIANCE = 4
    dmQbAmr_OSS = 5
    dmQbAmr_BASELINE = 6
    dmQbAmr_COMPLIANCE = 7
    dmQbNAmr_OSS = 8
    dmQbNAmr_BASELINE = 9
    dmQbNAmr_COMPLIANCE = 10
    dmQg_OSS = 11
    dmQg_BASELINE = 12
    dmQg_COMPLIANCE = 13
    dmQgAmr_OSS = 14
    dmQgAmr_BASELINE = 15
    dmQgAmr_COMPLIANCE = 16
    dmQgNAmr_OSS = 17
    dmQgNAmr_BASELINE = 18
    dmQgNAmr_COMPLIANCE = 19
    dmSupp_OSS = 20
    dmSupp_BASELINE = 21
    dmSupp_COMPLIANCE = 22
    dmtFAmr_OSS = 23
    dmtFAmr_BASELINE = 24
    dmtFAmr_COMPLIANCE = 25
    dmtFNAmr_OSS = 26
    dmtFNAmr_BASELINE = 27
    dmtFNAmr_COMPLIANCE = 28
    dmtHAmr_OSS = 29
    dmtHAmr_BASELINE = 30
    dmtHAmr_COMPLIANCE = 31
    dmtHNAmr_OSS = 32
    dmtHNAmr_BASELINE = 33
    dmtHNAmr_COMPLIANCE = 34


class DTM_COL(Enum):
    allocPref_OSS = 2
    allocPref_BASELINE = 3
    allocPref_COMPLIANCE = 4
    dtmState_OSS = 5
    dtmState_BASELINE = 6
    dtmState_COMPLIANCE = 7
    maxLapdm_OSS = 8
    maxLapdm_BASELINE = 9
    maxLapdm_COMPLIANCE = 10


class CHANNELGROUP_COL(Enum):
    band_OSS = 2
    band_BASELINE = 3
    band_COMPLIANCE = 4
    bccd_OSS = 5
    bccd_BASELINE = 6
    bccd_COMPLIANCE = 7
    cbch_OSS = 8
    cbch_BASELINE = 9
    cbch_COMPLIANCE = 10
    hopType_OSS = 11
    hopType_BASELINE = 12
    hopType_COMPLIANCE = 13
    numReqBpc_OSS = 14
    numReqBpc_BASELINE = 15
    numReqBpc_COMPLIANCE = 16
    numReqCs3Cs4_OSS = 17
    numReqCs3Cs4_BASELINE = 18
    numReqCs3Cs4_COMPLIANCE = 19
    numReqEgprsB_OSS = 20
    numReqEgprsB_BASELINE = 21
    numReqEgprsB_COMPLIANCE = 22
    odpdchLimit_OSS = 23
    odpdchLimit_BASELINE = 24
    odpdchLimit_COMPLIANCE = 25
    sas_OSS = 26
    sas_BASELINE = 27
    sas_COMPLIANCE = 28
    scType_OSS = 29
    scType_BASELINE = 30
    scType_COMPLIANCE = 31
    sdcch_OSS = 32
    sdcch_BASELINE = 33
    sdcch_COMPLIANCE = 34
    tn_OSS = 35
    tn_BASELINE = 36
    tn_COMPLIANCE = 37
    tn7Bcch_OSS = 38
    tn7Bcch_BASELINE = 39
    tn7Bcch_COMPLIANCE = 40
    tnBcch_OSS = 41
    tnBcch_BASELINE = 42
    tnBcch_COMPLIANCE = 43


class CHANNELALLOCANDOPT_COL(Enum):
    chap_OSS = 2
    chap_BASELINE = 3
    chap_COMPLIANCE = 4
    csPsAlloc_OSS = 5
    csPsAlloc_BASELINE = 6
    csPsAlloc_COMPLIANCE = 7
    csPsPrio_OSS = 8
    csPsPrio_BASELINE = 9
    csPsPrio_COMPLIANCE = 10
    fPdch_OSS = 11
    fPdch_BASELINE = 12
    fPdch_COMPLIANCE = 13
    gprsPrio_OSS = 14
    gprsPrio_BASELINE = 15
    gprsPrio_COMPLIANCE = 16
    mc_OSS = 17
    mc_BASELINE = 18
    mc_COMPLIANCE = 19
    pdchPreempt_OSS = 20
    pdchPreempt_BASELINE = 21
    pdchPreempt_COMPLIANCE = 22
    primpLim_OSS = 23
    primpLim_BASELINE = 24
    primpLim_COMPLIANCE = 25
    sPdch_OSS = 26
    sPdch_BASELINE = 27
    sPdch_COMPLIANCE = 28


class POWERCONTROLUPLINK_COL(Enum):
    bsRxMin_OSS = 2
    bsRxMin_BASELINE = 3
    bsRxMin_COMPLIANCE = 4
    bsRxSuff_OSS = 5
    bsRxSuff_BASELINE = 6
    bsRxSuff_COMPLIANCE = 7
    cchPwr_OSS = 8
    cchPwr_BASELINE = 9
    cchPwr_COMPLIANCE = 10
    dmsPcState_OSS = 11
    dmsPcState_BASELINE = 12
    dmsPcState_COMPLIANCE = 13
    dtxU_OSS = 14
    dtxU_BASELINE = 15
    dtxU_COMPLIANCE = 16
    gamma_OSS = 17
    gamma_BASELINE = 18
    gamma_COMPLIANCE = 19
    lCompUl_OSS = 20
    lCompUl_BASELINE = 21
    lCompUl_COMPLIANCE = 22
    msrPwrOffset_OSS = 23
    msrPwrOffset_BASELINE = 24
    msrPwrOffset_COMPLIANCE = 25
    msRxMin_OSS = 26
    msRxMin_BASELINE = 27
    msRxMin_COMPLIANCE = 28
    msRxSuff_OSS = 29
    msRxSuff_BASELINE = 30
    msRxSuff_COMPLIANCE = 31
    msTxPwr_OSS = 32
    msTxPwr_BASELINE = 33
    msTxPwr_COMPLIANCE = 34
    qCompUl_OSS = 35
    qCompUl_BASELINE = 36
    qCompUl_COMPLIANCE = 37
    qDesUl_OSS = 38
    qDesUl_BASELINE = 39
    qDesUl_COMPLIANCE = 40
    qDesUlAfr_OSS = 41
    qDesUlAfr_BASELINE = 42
    qDesUlAfr_COMPLIANCE = 43
    qDesUlAhr_OSS = 44
    qDesUlAhr_BASELINE = 45
    qDesUlAhr_COMPLIANCE = 46
    ssDesUl_OSS = 47
    ssDesUl_BASELINE = 48
    ssDesUl_COMPLIANCE = 49
    ssDesUlAfr_OSS = 50
    ssDesUlAfr_BASELINE = 51
    ssDesUlAfr_COMPLIANCE = 52
    ssDesUlAhr_OSS = 53
    ssDesUlAhr_BASELINE = 54
    ssDesUlAhr_COMPLIANCE = 55
    ssOffsetUl_OSS = 56
    ssOffsetUl_BASELINE = 57
    ssOffsetUl_COMPLIANCE = 58
    ssOffsetUlAfr_OSS = 59
    ssOffsetUlAfr_BASELINE = 60
    ssOffsetUlAfr_COMPLIANCE = 61
    ssOffsetUlAwb_OSS = 62
    ssOffsetUlAwb_BASELINE = 63
    ssOffsetUlAwb_COMPLIANCE = 64


class POWERCONTROLDOWNLINK_COL(Enum):
    bsPwrMin_OSS = 2
    bsPwrMin_BASELINE = 3
    bsPwrMin_COMPLIANCE = 4
    bsRPwrOffset_OSS = 5
    bsRPwrOffset_BASELINE = 6
    bsRPwrOffset_COMPLIANCE = 7
    dBtsPcState_OSS = 8
    dBtsPcState_BASELINE = 9
    dBtsPcState_COMPLIANCE = 10
    dtxD_OSS = 11
    dtxD_BASELINE = 12
    dtxD_COMPLIANCE = 13
    lCompDl_OSS = 14
    lCompDl_BASELINE = 15
    lCompDl_COMPLIANCE = 16
    qCompDl_OSS = 17
    qCompDl_BASELINE = 18
    qCompDl_COMPLIANCE = 19
    qDesDl_OSS = 20
    qDesDl_BASELINE = 21
    qDesDl_COMPLIANCE = 22
    qDesDlAfr_OSS = 23
    qDesDlAfr_BASELINE = 24
    qDesDlAfr_COMPLIANCE = 25
    qDesDlAhr_OSS = 26
    qDesDlAhr_BASELINE = 27
    qDesDlAhr_COMPLIANCE = 28
    ssDesDl_OSS = 29
    ssDesDl_BASELINE = 30
    ssDesDl_COMPLIANCE = 31
    ssDesDlAfr_OSS = 32
    ssDesDlAfr_BASELINE = 33
    ssDesDlAfr_COMPLIANCE = 34
    ssDesDlAhr_OSS = 35
    ssDesDlAhr_BASELINE = 36
    ssDesDlAhr_COMPLIANCE = 37
    ssDesDlAwb_OSS = 38
    ssDesDlAwb_BASELINE = 39
    ssDesDlAwb_COMPLIANCE = 40
    ssOffsetDl_OSS = 41
    ssOffsetDl_BASELINE = 42
    ssOffsetDl_COMPLIANCE = 43
    ssOffsetDlAfr_OSS = 44
    ssOffsetDlAfr_BASELINE = 45
    ssOffsetDlAfr_COMPLIANCE = 46


class POWERCONTROL_COL(Enum):
    amrPcState_OSS = 2
    amrPcState_BASELINE = 3
    amrPcState_COMPLIANCE = 4
    hpbState_OSS = 5
    hpbState_BASELINE = 6
    hpbState_COMPLIANCE = 7


class MSQUEUING_COL(Enum):
    qLength_OSS = 2
    qLength_BASELINE = 3
    qLength_COMPLIANCE = 4
    resLimit_OSS = 5
    resLimit_BASELINE = 6
    resLimit_COMPLIANCE = 7


class MOBILITY_COL(Enum):
    aw_OSS = 2
    aw_BASELINE = 3
    aw_COMPLIANCE = 4
    bcchDtcb_OSS = 5
    bcchDtcb_BASELINE = 6
    bcchDtcb_COMPLIANCE = 7
    hystSep_OSS = 8
    hystSep_BASELINE = 9
    hystSep_COMPLIANCE = 10
    maxTa_OSS = 11
    maxTa_BASELINE = 12
    maxTa_COMPLIANCE = 13
    mbcr_OSS = 14
    mbcr_BASELINE = 15
    mbcr_COMPLIANCE = 16
    missNM_OSS = 17
    missNM_BASELINE = 18
    missNM_COMPLIANCE = 19
    ncrpt_OSS = 20
    ncrpt_BASELINE = 21
    ncrpt_COMPLIANCE = 22
    scho_OSS = 23
    scho_BASELINE = 24
    scho_COMPLIANCE = 25


class LOCATINGURGENCY_COL(Enum):
    cellQ_OSS = 2
    cellQ_BASELINE = 3
    cellQ_COMPLIANCE = 4
    qLimDl_OSS = 5
    qLimDl_BASELINE = 6
    qLimDl_COMPLIANCE = 7
    qLimDlAfr_OSS = 8
    qLimDlAfr_BASELINE = 9
    qLimDlAfr_COMPLIANCE = 10
    qLimUl_OSS = 11
    qLimUl_BASELINE = 12
    qLimUl_COMPLIANCE = 13
    qLimUlAfr_OSS = 14
    qLimUlAfr_BASELINE = 15
    qLimUlAfr_COMPLIANCE = 16
    taLim_OSS = 17
    taLim_BASELINE = 18
    taLim_COMPLIANCE = 19


class SUBCELLLOADDISTRIBUTION_COL(Enum):
    scld_OSS = 2
    scld_BASELINE = 3
    scld_COMPLIANCE = 4
    scldLOl_OSS = 5
    scldLOl_BASELINE = 6
    scldLOl_COMPLIANCE = 7
    scldLUl_OSS = 8
    scldLUl_BASELINE = 9
    scldLUl_COMPLIANCE = 10
    scldSc_OSS = 11
    scldSc_BASELINE = 12
    scldSc_COMPLIANCE = 13


class POWERSAVINGS_COL(Enum):
    bcchPs_OSS = 2
    bcchPs_BASELINE = 3
    bcchPs_COMPLIANCE = 4
    btsPsHyst_OSS = 5
    btsPsHyst_BASELINE = 6
    btsPsHyst_COMPLIANCE = 7
    preCcch_OSS = 8
    preCcch_BASELINE = 9
    preCcch_COMPLIANCE = 10
    pro_OSS = 11
    pro_BASELINE = 12
    pro_COMPLIANCE = 13


class LCHADAPTIVECONF_COL(Enum):
    acState_OSS = 2
    acState_BASELINE = 3
    acState_COMPLIANCE = 4
    sLevel_OSS = 5
    sLevel_BASELINE = 6
    sLevel_COMPLIANCE = 7
    sTime_OSS = 8
    sTime_BASELINE = 9
    sTime_COMPLIANCE = 10


class RADIOLINKTIMEOUT_COL(Enum):
    rLinkT_OSS = 2
    rLinkT_BASELINE = 3
    rLinkT_COMPLIANCE = 4
    rLinkTaFr_OSS = 5
    rLinkTaFr_BASELINE = 6
    rLinkTaFr_COMPLIANCE = 7
    rLinkTaHr_OSS = 8
    rLinkTaHr_BASELINE = 9
    rLinkTaHr_COMPLIANCE = 10
    rLinkTAwb_OSS = 11
    rLinkTAwb_BASELINE = 12
    rLinkTAwb_COMPLIANCE = 13
    rLinkUp_OSS = 14
    rLinkUp_BASELINE = 15
    rLinkUp_COMPLIANCE = 16
    rLinkUpAfr_OSS = 17
    rLinkUpAfr_BASELINE = 18
    rLinkUpAfr_COMPLIANCE = 19
    rLinkUpAhr_OSS = 20
    rLinkUpAhr_BASELINE = 21
    rLinkUpAhr_COMPLIANCE = 22
    rLinkUpAwb_OSS = 23
    rLinkUpAwb_BASELINE = 24
    rLinkUpAwb_COMPLIANCE = 25


def cellloadsharing_col():
    return {
        "NodeId": 0,
        "BscFunctionId": 1,
        "BscMId": 2,
        "GeranCellMId": 3,
        "GeranCellId": 4,
        "ChannelAllocAndOptId": 5,
        "CellLoadSharingId": 6,
        "clsAcc": 7,
        "clsLevel": 8,
        "clsRamp": 9,
        "clsState": 10,
        "hoClsAcc": 11,
        "rHyst": 12,
    }


def dtm_col():
    return {
        "NodeId": 0,
        "BscFunctionId": 1,
        "BscMId": 2,
        "GeranCellMId": 3,
        "GeranCellId": 4,
        "DtmId": 5,
        "allocPref": 6,
        "dtmState": 7,
        "maxLapdm": 8,
    }


def dynamichrallocation_col():
    return {
        "NodeId": 0,
        "BscFunctionId": 1,
        "BscMId": 2,
        "GeranCellMId": 3,
        "GeranCellId": 4,
        "ChannelAllocAndOptId": 5,
        "DynamicHrAllocationId": 6,
        "dha": 7,
        "dtHAmr": 8,
        "dtHNAmr": 9,
    }


def gerancellrelation_col():
    return {
        "NodeId": 0,
        "BscFunctionId": 1,
        "BscMId": 2,
        "GeranCellMId": 3,
        "GeranCellId": 4,
        "GeranCellRelationId": 5,
        "awOffset": 6,
        "bqOffset": 7,
        "bqOffsetAfr": 8,
        "cand": 9,
        "cs": 10,
        "hiHyst": 11,
        "kHyst": 12,
        "kOffset": 13,
        "lHyst": 14,
        "lOffset": 15,
        "loHyst": 16,
        "offset": 17,
        "tRHyst": 18,
        "tROffset": 19,
    }


def gprs_col():
    return {
        "NodeId": 0,
        "BscFunctionId": 1,
        "BscMId": 2,
        "GeranCellMId": 3,
        "GeranCellId": 4,
        "GprsId": 5,
        "chCsDl": 6,
        "gprsSupState": 7,
        "pskOnBcch": 8,
        "scAlloc": 9,
    }


def hierarchicalcellstructure_col():
    return {
        "NodeId": 0,
        "BscFunctionId": 1,
        "BscMId": 2,
        "GeranCellMId": 3,
        "GeranCellId": 4,
        "HierarchicalCellStructureId": 5,
        "fastMsReg": 6,
        "hcsIn": 7,
        "hcsOut": 8,
        "layer": 9,
        "layerHyst": 10,
        "layerThr": 11,
        "pSsTemp": 12,
        "pTimTemp": 13,
    }


def idlechannelmeasurement_col():
    return {
        "NodeId": 0,
        "BscFunctionId": 1,
        "BscMId": 2,
        "GeranCellMId": 3,
        "GeranCellId": 4,
        "ChannelAllocAndOptId": 5,
        "IdleChannelMeasurementId": 6,
        "icmState": 7,
        "intAve": 8,
        "limit1": 9,
        "limit2": 10,
        "limit3": 11,
        "limit4": 12,
    }


def interranmobility_col():
    return {
        "NodeId": 0,
        "BscFunctionId": 1,
        "BscMId": 2,
        "GeranCellMId": 3,
        "GeranCellId": 4,
        "MobilityId": 5,
        "InterRanMobilityId": 6,
        "fastRet3g": 7,
        "fastRetLte": 8,
        "fddMrr": 9,
        "fddQMin": 10,
        "fddQMinOff": 11,
        "fddQOff": 12,
        "fddRepThr2": 13,
        "fddRscpMin": 14,
        "isHoLev": 15,
        "qsc": 16,
        "qsci": 17,
        "qsi": 18,
        "sPrio": 19,
    }


def lchadaptiveconf_col():
    return {
        "NodeId": 0,
        "BscFunctionId": 1,
        "BscMId": 2,
        "GeranCellMId": 3,
        "GeranCellId": 4,
        "ChannelAllocAndOptId": 5,
        "LchAdaptiveConfId": 6,
        "acState": 7,
        "sLevel": 8,
        "sTime": 9,
    }


def locatingfilter_col():
    return {
        "NodeId": 0,
        "BscFunctionId": 1,
        "BscMId": 2,
        "GeranCellMId": 3,
        "GeranCellId": 4,
        "MobilityId": 5,
        "LocatingFilterId": 6,
        "ferLen": 7,
        "qEvalSd": 8,
        "qEvalSi": 9,
        "qLenSd": 10,
        "qLenSi": 11,
        "ssEvalSd": 12,
        "ssEvalSi": 13,
        "ssLenSd": 14,
        "ssLenSi": 15,
        "ssRampSd": 16,
        "ssRampSi": 17,
    }


def locatingintracellhandover_col():
    return {
        "NodeId": 0,
        "BscFunctionId": 1,
        "BscMId": 2,
        "GeranCellMId": 3,
        "GeranCellId": 4,
        "MobilityId": 5,
        "LocatingIntraCellHandoverId": 6,
        "iho": 7,
        "maxIHo": 8,
        "qOffsetDl": 9,
        "qOffsetDlAfr": 10,
        "qOffsetUl": 11,
        "qOffsetUlAfr": 12,
        "tiHo": 13,
        "tMaxiHo": 14,
    }


def locatingpenalty_col():
    return {
        "NodeId": 0,
        "BscFunctionId": 1,
        "BscMId": 2,
        "GeranCellMId": 3,
        "GeranCellId": 4,
        "MobilityId": 5,
        "LocatingPenaltyId": 6,
        "pSsBq": 7,
        "pSsHf": 8,
        "pSsTa": 9,
        "pTimBq": 10,
        "pTimHf": 11,
        "pTimTa": 12,
    }


def locatingurgency_col():
    return {
        "NodeId": 0,
        "BscFunctionId": 1,
        "BscMId": 2,
        "GeranCellMId": 3,
        "GeranCellId": 4,
        "MobilityId": 5,
        "LocatingUrgencyId": 6,
        "cellQ": 7,
        "qLimDl": 8,
        "qLimDlAfr": 9,
        "qLimUl": 10,
        "qLimUlAfr": 11,
        "taLim": 12,
    }


def mobility_col():
    return {
        "NodeId": 0,
        "BscFunctionId": 1,
        "BscMId": 2,
        "GeranCellMId": 3,
        "GeranCellId": 4,
        "MobilityId": 5,
        "aw": 6,
        "bcchDtcb": 7,
        "hystSep": 8,
        "maxTa": 9,
        "mbcr": 10,
        "missNM": 11,
        "ncrpt": 12,
        "scho": 13,
    }


def msqueuing_col():
    return {
        "NodeId": 0,
        "BscFunctionId": 1,
        "BscMId": 2,
        "GeranCellMId": 3,
        "GeranCellId": 4,
        "MsQueuingId": 5,
        "qLength": 6,
        "resLimit": 7,
    }


def powercontrol_col():
    return {
        "NodeId": 0,
        "BscFunctionId": 1,
        "BscMId": 2,
        "GeranCellMId": 3,
        "GeranCellId": 4,
        "PowerControlId": 5,
        "amrPcState": 6,
        "hpbState": 7,
    }


def powercontroldownlink_col():
    return {
        "NodeId": 0,
        "BscFunctionId": 1,
        "BscMId": 2,
        "GeranCellMId": 3,
        "GeranCellId": 4,
        "PowerControlId": 5,
        "PowerControlDownlinkId": 6,
        "bsPwrMin": 7,
        "bsRPwrOffset": 8,
        "dBtsPcState": 9,
        "dtxD": 10,
        "lCompDl": 11,
        "qCompDl": 12,
        "qDesDl": 13,
        "qDesDlAfr": 14,
        "qDesDlAhr": 15,
        "ssDesDl": 16,
        "ssDesDlAfr": 17,
        "ssDesDlAhr": 18,
        "ssDesDlAwb": 19,
        "ssOffsetDl": 20,
        "ssOffsetDlAfr": 21,
    }


def powersavings_col():
    return {
        "NodeId": 0,
        "BscFunctionId": 1,
        "BscMId": 2,
        "GeranCellMId": 3,
        "GeranCellId": 4,
        "PowerSavingsId": 5,
        "bcchPs": 6,
        "btsPsHyst": 7,
        "preCcch": 8,
        "pro": 9,
    }


def radiolinktimeout_col():
    return {
        "NodeId": 0,
        "BscFunctionId": 1,
        "BscMId": 2,
        "GeranCellMId": 3,
        "GeranCellId": 4,
        "MobilityId": 5,
        "RadioLinkTimeoutId": 6,
        "rLinkT": 7,
        "rLinkTaFr": 8,
        "rLinkTaHr": 9,
        "rLinkTAwb": 10,
        "rLinkUp": 11,
        "rLinkUpAfr": 12,
        "rLinkUpAhr": 13,
        "rLinkUpAwb": 14,
    }


def subcellloaddistribution_col():
    return {
        "NodeId": 0,
        "BscFunctionId": 1,
        "BscMId": 2,
        "GeranCellMId": 3,
        "GeranCellId": 4,
        "ChannelAllocAndOptId": 5,
        "SubcellLoadDistributionId": 6,
        "scld": 7,
        "scldLOl": 8,
        "scldLUl": 9,
        "scldSc": 10,
    }


def gerancell_col():
    return {
        "NodeId": 0,
        "BscFunctionId": 1,
        "BscMId": 2,
        "GeranCellMId": 3,
        "GeranCellId": 4,
        "bcchType": 5,
        "cSysType": 6,
        "fnOffset": 7,
        "irc": 8,
        "state": 9,
        "xRange": 10,
    }


def remedy_col():
    return {
        "ERP Sector Name": 0,
        "ERP Site Name": 1,
        "ERP Sector Elect Downtilt": 2,
        "ERP Sector Mechanical Downtilt": 3,
        "ERP Sector Part Of MOCN": 4,
        "ERP Site MOCN Rain": 5,
        "ERP Site MOCN Partner": 6,
        "ERP Sector Status Desc": 7,
        "ERP Sector Status": 8,
        "ERP Site Type Desc": 9,
        "ERP Site Elevation": 10,
        "ERP Site Tower Height": 11,
        "ERP Site Latitude Real nad83": 12,
        "ERP Site Longitude Real nad83": 13,
        "ERP Site Status": 14,
        "ERP Site Status Desc": 15,
        "ERP Site EMG": 16,
        "ERP Site Location Code": 17,
        "ERP Antenna Electrical Downtilt": 18,
        "ERP Antenna MET": 19,
        "ERP Antenna Vertical Beamwidth": 20,
        "ERP Antenna Horizontal Beamwidth": 21,
        "ERP Antenna Gain": 22,
        "ERP Sector Frequency Description": 23,
        "ERP Sector Frequency": 24,
        "ERP Sector Technology Description": 25,
        "ERP Sector Azimuth": 26,
        "ERP Sector Antenna Type": 27,
        "ERP Sector Antenna Omnidirectional": 28,
        "ERP Sector Antenna Gain": 29,
        "ERP Sector Antenna Length": 30,
        "ERP Sector Antenna Height AGL": 31,
        "ERP Site Tower Type": 32,
        "ERP Sector Company Owner": 33,
        "ERP Site Site Owner": 34,
        "ERP Site IC Service Area": 35,
    }


def idlemodeandpaging_col():
    return {
        "NodeId": 0,
        "BscFunctionId": 1,
        "BscMId": 2,
        "GeranCellMId": 3,
        "GeranCellId": 4,
        "IdleModeAndPagingId": 5,
        "acc": 6,
        "accMin": 7,
        "agBlk": 8,
        "att": 9,
        "cb": 10,
        "cbq": 11,
        "crh": 12,
        "cro": 13,
        "maxRet": 14,
        "mFrms": 15,
        "nccPerm": 16,
        "pt": 17,
        "siMsg1": 18,
        "siMsg7": 19,
        "siMsg8": 20,
        "t3212": 21,
        "to": 22,
        "tx": 23,
    }


def powercontroluplink_col():
    return {
        "NodeId": 0,
        "BscFunctionId": 1,
        "BscMId": 2,
        "GeranCellMId": 3,
        "GeranCellId": 4,
        "PowerControlId": 5,
        "PowerControlUplinkId": 6,
        "bsRxMin": 7,
        "bsRxSuff": 8,
        "cchPwr": 9,
        "dmsPcState": 10,
        "dtxU": 11,
        "gamma": 12,
        "lCompUl": 13,
        "msrPwrOffset": 14,
        "msRxMin": 15,
        "msRxSuff": 16,
        "msTxPwr": 17,
        "qCompUl": 18,
        "qDesUl": 19,
        "qDesUlAfr": 20,
        "qDesUlAhr": 21,
        "ssDesUl": 22,
        "ssDesUlAfr": 23,
        "ssDesUlAhr": 24,
        "ssOffsetUl": 25,
        "ssOffsetUlAfr": 26,
        "ssOffsetUlAwb": 27,
    }


def dynamicfrhrmodeadaption_col():
    return {
        "NodeId": 0,
        "BscFunctionId": 1,
        "BscMId": 2,
        "GeranCellMId": 3,
        "GeranCellId": 4,
        "ChannelAllocAndOptId": 5,
        "DynamicFrHrModeAdaptionId": 6,
        "dmQb": 7,
        "dmQbAmr": 8,
        "dmQbNAmr": 9,
        "dmQg": 10,
        "dmQgAmr": 11,
        "dmQgNAmr": 12,
        "dmSupp": 13,
        "dmtFAmr": 14,
        "dmtFNAmr": 15,
        "dmtHAmr": 16,
        "dmtHNAmr": 17,
    }


def channelgroup_col():
    return {
        "NodeId": 0,
        "BscFunctionId": 1,
        "BscMId": 2,
        "GeranCellMId": 3,
        "GeranCellId": 4,
        "ChannelGroupId": 5,
        "band": 6,
        "bccd": 7,
        "cbch": 8,
        "hopType": 9,
        "numReqBpc": 10,
        "numReqCs3Cs4Bpc": 11,
        "numReqEgprsBpc": 12,
        "odpdchLimit": 13,
        "sas": 14,
        "scType": 15,
        "sdcch": 16,
        "tn": 17,
        "tn7Bcch": 18,
        "tnBcch": 19,
    }


def channelallocandopt_col():
    return {
        "NodeId": 0,
        "BscFunctionId": 1,
        "BscMId": 2,
        "GeranCellMId": 3,
        "GeranCellId": 4,
        "ChannelAllocAndOptId": 5,
        "chap": 6,
        "csPsAlloc": 7,
        "csPsPrio": 8,
        "fPdch": 9,
        "gprsPrio": 10,
        "mc": 11,
        "pdchPreempt": 12,
        "primpLim": 13,
        "sPdch": 14,
    }
