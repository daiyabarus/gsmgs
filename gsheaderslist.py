class Headers:
    @staticmethod
    def header_baseline():
        return [
            "BSC",
            "GeranCell",
            "ManagedObjectClass",
            "Parameter",
            "OssValue",
            "BaselineValue",
            "Compliance",
            "Command",
        ]

    @staticmethod
    def header_result():
        return [
            "BSC",
            "GeranCell",
            "Location Code",
            "Site Name",
            "Audit Date",
            "Audit By:",
            "GeranCellId",
            "SubcellLoadDistribution",
            "RadioLinkTimeout",
            "PowerSavings",
            "PowerControlUplink",
            "PowerControlDownlink",
            "PowerControl",
            "MsQueuing",
            "Mobility",
            "LocatingUrgency",
            "LocatingPenalty",
            "LocatingIntraCellHandover",
            "LocatingFilter",
            "LchAdaptiveConf",
            "InterRanMobility",
            "IdleModeAndPaging",
            "IdleChannelMeasurement",
            "HierarchicalCellStructure",
            "Gprs",
            "GeranCellRelation",
            "DynamicHrAllocation",
            "DynamicFrHrModeAdaption",
            "Dtm",
            "ChannelGroup",
            "ChannelAllocAndOpt",
            "CellLoadSharing",
            "Remaks",
            "Approved by Rogers (Y/N)",
        ]
