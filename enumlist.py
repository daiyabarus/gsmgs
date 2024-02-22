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

def externalgerancellrelation_col():
    return {
        "NodeId": 0,
        "BscFunctionId": 1,
        "BscMId": 2,
        "GeranCellMId": 3,
        "GeranCellId": 4,
        "ExternalGeranCellRelationId": 5,
        "awOffset": 6,
        "bqOffset": 7,
        "bqOffsetAfr": 8,
        "bqOffsetAwb": 9,
        "cand": 10,
        "externalGeranCellRelationId": 11,
        "gprsValid": 12,
        "hiHyst": 13,
        "kHyst": 14,
        "kOffset": 15,
        "lHyst": 16,
        "lOffset": 17,
        "loHyst": 18,
        "offset": 19,
        "pROffset": 20,
        "relType": 21,
        "tRHyst": 22,
        "tROffset": 23,
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
