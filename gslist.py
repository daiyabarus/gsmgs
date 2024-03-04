def gs_cellloadsharing():
    return [
        ("clsAcc", "80"),
        ("clsLevel", "5"),
        ("clsRamp", "10"),
        ("clsState", "ACTIVE"),
        ("hoClsAcc", "ON"),
        ("rHyst", "75"),
    ]


def gs_channelallocandopt():
    return [
        ("chap", "0"),
        ("csPsAlloc", "CSLASTPSFIRST"),
        ("csPsPrio", "PSPRIO"),
        ("fPdch", "0"),
        ("gprsPrio", "0"),
        ("mc", "OFF"),
        ("pdchPreempt", "4"),
        ("primpLim", "8"),
        ("sPdch", "1"),
    ]


def gs_channelgroup():
    return [
        ("band", "null"),
        ("bccd", "YES"),
        ("cbch", "NO"),
        ("hopType", "DEFAULT"),
        ("numReqBpc", "8"),
        ("numReqCs3Cs4Bpc", "0"),
        ("numReqEgprsBpc", "4"),
        ("odpdchLimit", "100"),
        ("sas", "QUALITY"),
        ("scType", "UL"),
        ("sdcch", "1"),
        ("tn", "1#2#7"),
        ("tn7Bcch", "EGPRS"),
        ("tnBcch", "EGPRS"),
    ]


def gs_dtm():
    return [
        ("allocPref", "QUAL"),
        ("dtmState", "NO"),
        ("maxLapdm", "5"),
    ]


def gs_dynamicfrhrmodeadaption():
    return [
        ("dmQb", "ON"),
        ("dmQbAmr", "50"),
        ("dmQbNAmr", "0"),
        ("dmQg", "ON"),
        ("dmQgAmr", "35"),
        ("dmQgNAmr", "0"),
        ("dmSupp", "OFF"),
        ("dmtFAmr", "100"),
        ("dmtFNAmr", "100"),
        ("dmtHAmr", "10"),
        ("dmtHNAmr", "0"),
    ]


def gs_dynamichrallocation():
    return [
        ("dha", "ON"),
        ("dtHAmr", "85"),
        ("dtHNAmr", "0"),
    ]


def gs_gerancell():
    return [
        ("bcchType", "NCOMB"),
        ("cSysType", "GSM800"),
        ("fnOffset", "0"),
        ("irc", "ON"),
        ("state", "ACTIVE"),
        ("xRange", "NO"),
    ]


def gs_gerancellrelation():
    return [
        ("cand", "BOTH"),
        ("awOffset", "3"),
        ("bqOffset", "5"),
        ("bqOffsetAfr", "5"),
        ("cs", "SUFFIX"),
        ("hiHyst", "5"),
        ("kHyst", "3"),
        ("kOffset", "0"),
        ("lHyst", "3"),
        ("lOffset", "0"),
        ("loHyst", "5"),
        ("offset", "0"),
        ("tRHyst", "2"),
        ("tROffset", "0"),
    ]


def gs_externalgerancellrelation():
    return [
        ("cand", "BOTH"),
        ("awOffset", "3"),
        ("bqOffset", "5"),
        ("bqOffsetAfr", "5"),
        ("hiHyst", "5"),
        ("kHyst", "3"),
        ("kOffset", "0"),
        ("lHyst", "3"),
        ("lOffset", "0"),
        ("loHyst", "5"),
        ("offset", "0"),
        ("tRHyst", "2"),
        ("tROffset", "0"),
    ]


def gs_gprs():
    return [
        ("chCsDl", "CS2"),
        ("gprsSupState", "YES"),
        ("pskOnBcch", "YES"),
        ("scAlloc", "UL"),
    ]


def gs_hierarchicalcellstructure():
    return [
        ("fastMsReg", "OFF"),
        ("hcsIn", "0"),
        ("hcsOut", "100"),
        ("layer", "7"),
        ("layerHyst", "2"),
        ("layerThr", "-100"),
        ("pSsTemp", "0"),
        ("pTimTemp", "0"),
    ]


def gs_idlechannelmeasurement():
    return [
        ("icmState", "ACTIVE"),
        ("intAve", "25"),
        ("limit1", "SUFFIX"),
        ("limit2", "SUFFIX"),
        ("limit3", "SUFFIX"),
        ("limit4", "SUFFIX"),
    ]


def gs_idlemodeandpaging():
    return [
        ("acc", "null"),
        ("accMin", "SUFFIX"),
        ("agBlk", "2"),
        ("att", "YES"),
        ("cb", "NO"),
        ("cbq", "HIGH"),
        ("crh", "6"),
        ("cro", "2"),
        ("maxRet", "4"),
        ("mFrms", "5"),
        ("nccPerm", "0#1#2#3#4#5#6#7"),
        ("pt", "0"),
        ("siMsg1", "ON"),
        ("siMsg7", "OFF"),
        ("siMsg8", "OFF"),
        ("t3212", "40"),
        ("to", "0"),
        ("tx", "50"),
    ]


def gs_interranmobility():
    return [
        ("fastRet3g", "ACTIVE"),
        ("fastRetLte", "ACTIVE"),
        ("fddMrr", "1"),
        ("fddQMin", "2"),
        ("fddQMinOff", "0"),
        ("fddQOff", "0"),
        ("fddRepThr2", "10"),
        ("fddRscpMin", "3"),
        ("isHoLev", "99"),
        ("qsc", "7"),
        ("qsci", "QSEARCH_I"),
        ("qsi", "7"),
        ("sPrio", "YES"),
    ]


def gs_lchadaptiveconf():
    return [
        ("acState", "ON"),
        ("sLevel", "2"),
        ("sTime", "180"),
    ]


def gs_locatingfilter():
    return [
        ("ferLen", "3"),
        ("qEvalSd", "6"),
        ("qEvalSi", "6"),
        ("qLenSd", "10"),
        ("qLenSi", "4"),
        ("ssEvalSd", "6"),
        ("ssEvalSi", "6"),
        ("ssLenSd", "10"),
        ("ssLenSi", "4"),
        ("ssRampSd", "5"),
        ("ssRampSi", "1"),
    ]


def gs_locatingintracellhandover():
    return [
        ("iho", "ON"),
        ("maxIHo", "2"),
        ("qOffsetDl", "-2"),
        ("qOffsetDlAfr", "-2"),
        ("qOffsetUl", "-2"),
        ("qOffsetUlAfr", "-2"),
        ("tiHo", "10"),
        ("tMaxiHo", "11"),
    ]


def gs_locatingpenalty():
    return [
        ("pSsBq", "7"),
        ("pSsHf", "63"),
        ("pSsTa", "63"),
        ("pTimBq", "15"),
        ("pTimHf", "5"),
        ("pTimTa", "30"),
    ]


def gs_locatingurgency():
    return [
        ("cellQ", "HIGH"),
        ("qLimDl", "55"),
        ("qLimDlAfr", "65"),
        ("qLimUl", "55"),
        ("qLimUlAfr", "65"),
        ("taLim", "62"),
    ]


def gs_mobility():
    return [
        ("aw", "ON"),
        ("bcchDtcb", "-63"),
        ("hystSep", "-90"),
        ("maxTa", "63"),
        ("mbcr", "TWO"),
        ("missNM", "3"),
        ("ncrpt", "1920MS"),
        ("scho", "OFF"),
    ]


def gs_msqueuing():
    return [
        ("MsQueuingId", "1"),
        ("qLength", "8"),
        ("resLimit", "25"),
    ]


def gs_powercontrol():
    return [
        ("amrPcState", "INACTIVE"),
        ("hpbState", "SUFFIX"),
    ]


def gs_powercontroldownlink():
    return [
        ("bsPwrMin", "-20"),
        ("bsRPwrOffset", "16"),
        ("dBtsPcState", "ACTIVE"),
        ("dtxD", "ON"),
        ("lCompDl", "60"),
        ("qCompDl", "60"),
        ("qDesDl", "30"),
        ("qDesDlAfr", "40"),
        ("qDesDlAhr", "40"),
        ("ssDesDl", "92"),
        ("ssDesDlAfr", "90"),
        ("ssDesDlAhr", "90"),
        ("ssDesDlAwb", "90"),
        ("ssOffsetDl", "5"),
        ("ssOffsetDlAfr", "5"),
    ]


def gs_powercontroluplink():
    return [
        ("bsRxMin", "150"),
        ("bsRxSuff", "150"),
        ("cchPwr", "33"),
        ("dmsPcState", "ACTIVE"),
        ("dtxU", "USE"),
        ("gamma", "32"),
        ("lCompUl", "60"),
        ("msrPwrOffset", "-2"),
        ("msRxMin", "100"),
        ("msRxSuff", "0"),
        ("msTxPwr", "33"),
        ("qCompUl", "60"),
        ("qDesUl", "30"),
        ("qDesUlAfr", "40"),
        ("qDesUlAhr", "40"),
        ("ssDesUl", "94"),
        ("ssDesUlAfr", "92"),
        ("ssDesUlAhr", "92"),
        ("ssOffsetUl", "10"),
        ("ssOffsetUlAfr", "10"),
        ("ssOffsetUlAwb", "0"),
    ]


def gs_powersavings():
    return [
        ("bcchPs", "ACTIVE"),
        ("btsPsHyst", "5"),
        ("preCcch", "YES"),
        ("pro", "4"),
    ]


def gs_radiolinktimeout():
    return [
        ("rLinkT", "48"),
        ("rLinkTaFr", "48"),
        ("rLinkTaHr", "48"),
        ("rLinkTAwb", "16"),
        ("rLinkUp", "48"),
        ("rLinkUpAfr", "48"),
        ("rLinkUpAhr", "48"),
        ("rLinkUpAwb", "16"),
    ]


def gs_subcellloaddistribution():
    return [
        ("scld", "OFF"),
        ("scldLOl", "20"),
        ("scldLUl", "20"),
        ("scldSc", "UL"),
    ]
