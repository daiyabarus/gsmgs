#!/usr/bin/python
# Python Script to get data from ENM
# usage python gsm-gs-oss.py list_cell.txt

# from operator import itemgetter
import os
import time
import sys
import enmscripting

session = enmscripting.open()
myOSS = os.popen(
    "cat /etc/hosts | grep rogers | tail -1 | sed -e 's/\s/\./g' | awk -F'.' '{print $8}'"
).read()

basePath = sys.path[0]
homedir = os.path.expanduser("~")
OutputDir = (
    homedir
    + "/gsmgs/"
    + myOSS.upper().rstrip().replace("DNS", "")
    + "_GSM_AUDIT_"
    + time.strftime("%d%m%y")
    + "/"
)
cell_list = []

print(sys.argv[1])
f = open(sys.argv[1])
for line in f:
    cell_list.append(line.strip())
f.close()

if not os.path.exists(OutputDir):
    os.mkdir(OutputDir)
else:
    os.system("rm " + OutputDir + "*.csv")


os.chdir(OutputDir)

command1 = "cmedit get *BSC* CellLoadSharing.(hoClsAcc,rHyst,clsRamp,clsLevel,clsState,clsAcc) -t"
command2 = "cmedit get *BSC* ChannelAllocAndOpt.(sPdch,fPdch,csPsAlloc,chap,mc,pdchPreempt,primpLim,csPsPrio,gprsPrio) -t"
command3 = "cmedit get *BSC* ChannelGroup.(band,bccd,hopType,tnBcch,sas,odpdchLimit,scType,sdcch,tn,cbch,numReqBpc,numReqCs3Cs4Bpc,numReqEgprsBpc,tn7Bcch,numReqCs3Cs4Bpc,numReqEgprsBpc,numReqCs3Cs4Bpc,numReqEgprsBpc) -t"
command4 = "cmedit get *BSC* Dtm.(dtmState,maxLapdm,allocPref) -t"
command5 = "cmedit get *BSC* DynamicFrHrModeAdaption.(dmtFAmr,dmSupp,dmQg,dmtFNAmr,dmtHNAmr,dmQb,dmtHAmr,dmQbAmr,dmQbNAmr,dmQgAmr,dmQgNAmr) -t"
command6 = "cmedit get *BSC* DynamicHrAllocation.(dha,dtHAmr,dtHNAmr) -t"
command7 = "cmedit get *BSC* GeranCell.(cSysType,irc,state,bcchType,fnOffset,xRange) -t"
command8 = "cmedit get *BSC* GeranCellRelation.(cs,cand,lHyst,tRHyst,awOffset,bqOffset,hiHyst,loHyst,bqOffsetAfr,kHyst,kOffset,lOffset,tROffset,offset) -t"
command9 = "cmedit get *BSC* Gprs.(chCsDl,pskOnBcch,scAlloc,gprsSupState) -t"
command10 = "cmedit get *BSC* HierarchicalCellStructure.(layerThr,layer,pTimTemp,layerHyst,pSsTemp,fastMsReg,hcsIn,hcsOut) -t"
command11 = "cmedit get *BSC* IdleChannelMeasurement.(icmState,intAve,limit1,limit2,limit3,limit4) -t"
command12 = "cmedit get *BSC* IdleModeAndPaging.(nccPerm,tx,accMin,mFrms,agBlk,crh,cb,cbq,acc,maxRet,att,t3212,cro,to,pt,siMsg1,siMsg7,siMsg8) -t"
command13 = "cmedit get *BSC* InterRanMobility.(fddMrr,fastRet3g,fastRetLte,fddQMinOff,fddQMin,isHoLev,fddRscpMin,qsi,sPrio,qsc,qsci,fddQOff,fddRepThr2) -t"
command14 = "cmedit get *BSC* LchAdaptiveConf.(sLevel,sTime,acState) -t"
command15 = "cmedit get *BSC* LocatingFilter.(ssEvalSd,qEvalSd,ssEvalSi,qEvalSi,ssLenSd,qLenSd,ssLenSi,qLenSi,ssRampSd,ssRampSi,ferLen) -t"
command16 = "cmedit get *BSC* LocatingIntraCellHandover.(qOffsetUlAfr,iho,maxIHo,tMaxiHo,tiHo,qOffsetDl,qOffsetUl,qOffsetDlAfr) -t"
command17 = "cmedit get *BSC* LocatingPenalty.(pTimHf,pTimBq,pTimTa,pSsBq,pSsHf,pSsTa) -t"
command18 = "cmedit get *BSC* LocatingUrgency.(taLim,cellQ,qLimUl,qLimDl,qLimUlAfr,qLimDlAfr) -t"
command19 = "cmedit get *BSC* Mobility.(ncrpt,mbcr,maxTa,aw,scho,hystSep,missNM,bcchDtcb) -t"
command20 = "cmedit get *BSC* MsQueuing.(resLimit,qLength) -t"
command21 = "cmedit get *BSC* PowerControl.(amrPcState,hpbState) -t"
command22 = "cmedit get *BSC* PowerControlDownlink.(ssDesDlAwb,bsRPwrOffset,dtxD,ssDesDl,qDesDl,lCompDl,qCompDl,ssDesDlAfr,qDesDlAfr,ssDesDlAhr,qDesDlAhr,ssOffsetDl,ssOffsetDlAfr,dBtsPcState,bsPwrMin) -t"
command23 = "cmedit get *BSC* PowerControlUplink.(gamma,ssOffsetUlAfr,ssOffsetUl,ssOffsetUlAwb,msrPwrOffset,cchPwr,msRxMin,msRxSuff,bsRxMin,msTxPwr,bsRxSuff,dtxU,ssDesUl,qDesUl,lCompUl,qCompUl,ssDesUlAfr,qDesUlAfr,ssDesUlAhr,qDesUlAhr,dmsPcState) -t"
command24 = "cmedit get *BSC* PowerSavings.(preCcch,bcchPs,btsPsHyst,pro) -t"
command25 = "cmedit get *BSC* RadioLinkTimeout.(rLinkTaFr,rLinkTAwb,rLinkUp,rLinkUpAfr,rLinkT,rLinkUpAwb,rLinkTaHr,rLinkUpAhr) -t"
command26 = (
    "cmedit get *BSC* SubcellLoadDistribution.(scld,scldLUl,scldLOl,scldSc) -t"
)
command27 = "cmedit get *BSC* ExternalGeranCellRelation.(*) -t "

output1 = OutputDir + "CellLoadSharing.csv"
output2 = OutputDir + "ChannelAllocAndOpt.csv"
output3 = OutputDir + "ChannelGroup.csv"
output4 = OutputDir + "Dtm.csv"
output5 = OutputDir + "DynamicFrHrModeAdaption.csv"
output6 = OutputDir + "DynamicHrAllocation.csv"
output7 = OutputDir + "GeranCell.csv"
output8 = OutputDir + "GeranCellRelation.csv"
output9 = OutputDir + "Gprs.csv"
output10 = OutputDir + "HierarchicalCellStructure.csv"
output11 = OutputDir + "IdleChannelMeasurement.csv"
output12 = OutputDir + "IdleModeAndPaging.csv"
output13 = OutputDir + "InterRanMobility.csv"
output14 = OutputDir + "LchAdaptiveConf.csv"
output15 = OutputDir + "LocatingFilter.csv"
output16 = OutputDir + "LocatingIntraCellHandover.csv"
output17 = OutputDir + "LocatingPenalty.csv"
output18 = OutputDir + "LocatingUrgency.csv"
output19 = OutputDir + "Mobility.csv"
output20 = OutputDir + "MsQueuing.csv"
output21 = OutputDir + "PowerControl.csv"
output22 = OutputDir + "PowerControlDownlink.csv"
output23 = OutputDir + "PowerControlUplink.csv"
output24 = OutputDir + "PowerSavings.csv"
output25 = OutputDir + "RadioLinkTimeout.csv"
output26 = OutputDir + "SubcellLoadDistribution.csv"
output27 = OutputDir + "ExternalGeranCellRelation.csv"

terminal = session.terminal()
result1 = terminal.execute(command1)
result2 = terminal.execute(command2)
result3 = terminal.execute(command3)
result4 = terminal.execute(command4)
result5 = terminal.execute(command5)
result6 = terminal.execute(command6)
result7 = terminal.execute(command7)
result8 = terminal.execute(command8)
result9 = terminal.execute(command9)
result10 = terminal.execute(command10)
result11 = terminal.execute(command11)
result12 = terminal.execute(command12)
result13 = terminal.execute(command13)
result14 = terminal.execute(command14)
result15 = terminal.execute(command15)
result16 = terminal.execute(command16)
result17 = terminal.execute(command17)
result18 = terminal.execute(command18)
result19 = terminal.execute(command19)
result20 = terminal.execute(command20)
result21 = terminal.execute(command21)
result22 = terminal.execute(command22)
result23 = terminal.execute(command23)
result24 = terminal.execute(command24)
result25 = terminal.execute(command25)
result26 = terminal.execute(command26)
result27 = terminal.execute(command27)


def contains(list_of_strings_to_check, line):
    for string in list_of_strings_to_check:
        if string in line:
            return False
    return True


list_of_strings = ["SubNetwork,SubNetwork", "instance(s)"]


def contains_cell(cell_list, line):
    for string in cell_list:
        if string in line:
            return True
    return False


if result2.is_command_result_available():
    filename = open(output2, "w")
    for line in result2.get_output():
        if "NodeId" in line:
            filename.write(line + "\n")
        elif contains(list_of_strings, line):
            if contains_cell(cell_list, line):
                filename.write(
                    line.replace("[", "")
                    .replace("]", "")
                    .replace("{", "")
                    .replace("}", "")
                    .replace(", ", ",")
                    + "\n"
                )
    filename.close()
else:
    print(result2._result_lines)


if result1.is_command_result_available():
    filename = open(output1, "w")
    for line in result1.get_output():
        if "NodeId" in line:
            filename.write(line + "\n")
        elif contains(list_of_strings, line):
            if contains_cell(cell_list, line):
                filename.write(
                    line.replace("[", "")
                    .replace("]", "")
                    .replace("{", "")
                    .replace("}", "")
                    .replace(", ", ",")
                    + "\n"
                )
    filename.close()
else:
    print(result1._result_lines)

if result3.is_command_result_available():
    filename = open(output3, "w")
    for line in result3.get_output():
        if "NodeId" in line:
            filename.write(line + "\n")
        elif contains(list_of_strings, line):
            if contains_cell(cell_list, line):
                filename.write(
                    line.replace("[", "")
                    .replace("]", "")
                    .replace("{", "")
                    .replace("}", "")
                    .replace(", ", ",")
                    + "\n"
                )
    filename.close()
else:
    print(result3._result_lines)

if result4.is_command_result_available():
    filename = open(output4, "w")
    for line in result4.get_output():
        if "NodeId" in line:
            filename.write(line + "\n")
        elif contains(list_of_strings, line):
            if contains_cell(cell_list, line):
                filename.write(
                    line.replace("[", "")
                    .replace("]", "")
                    .replace("{", "")
                    .replace("}", "")
                    .replace(", ", ",")
                    + "\n"
                )
    filename.close()
else:
    print(result4._result_lines)

if result5.is_command_result_available():
    filename = open(output5, "w")
    for line in result5.get_output():
        if "NodeId" in line:
            filename.write(line + "\n")
        elif contains(list_of_strings, line):
            if contains_cell(cell_list, line):
                filename.write(
                    line.replace("[", "")
                    .replace("]", "")
                    .replace("{", "")
                    .replace("}", "")
                    .replace(", ", ",")
                    + "\n"
                )
    filename.close()
else:
    print(result5._result_lines)

if result6.is_command_result_available():
    filename = open(output6, "w")
    for line in result6.get_output():
        if "NodeId" in line:
            filename.write(line + "\n")
        elif contains(list_of_strings, line):
            if contains_cell(cell_list, line):
                filename.write(
                    line.replace("[", "")
                    .replace("]", "")
                    .replace("{", "")
                    .replace("}", "")
                    .replace(", ", ",")
                    + "\n"
                )
    filename.close()
else:
    print(result6._result_lines)

if result7.is_command_result_available():
    filename = open(output7, "w")
    for line in result7.get_output():
        if "NodeId" in line:
            filename.write(line + "\n")
        elif contains(list_of_strings, line):
            if contains_cell(cell_list, line):
                filename.write(
                    line.replace("[", "")
                    .replace("]", "")
                    .replace("{", "")
                    .replace("}", "")
                    .replace(", ", ",")
                    + "\n"
                )
    filename.close()
else:
    print(result7._result_lines)

if result8.is_command_result_available():
    filename = open(output8, "w")
    for line in result8.get_output():
        if "NodeId" in line:
            filename.write(line + "\n")
        elif contains(list_of_strings, line):
            if contains_cell(cell_list, line):
                filename.write(
                    line.replace("[", "")
                    .replace("]", "")
                    .replace("{", "")
                    .replace("}", "")
                    .replace(", ", ",")
                    + "\n"
                )
    filename.close()
else:
    print(result8._result_lines)

if result9.is_command_result_available():
    filename = open(output9, "w")
    for line in result9.get_output():
        if "NodeId" in line:
            filename.write(line + "\n")
        elif contains(list_of_strings, line):
            if contains_cell(cell_list, line):
                filename.write(
                    line.replace("[", "")
                    .replace("]", "")
                    .replace("{", "")
                    .replace("}", "")
                    .replace(", ", ",")
                    + "\n"
                )
    filename.close()
else:
    print(result9._result_lines)

if result10.is_command_result_available():
    filename = open(output10, "w")
    for line in result10.get_output():
        if "NodeId" in line:
            filename.write(line + "\n")
        elif contains(list_of_strings, line):
            if contains_cell(cell_list, line):
                filename.write(
                    line.replace("[", "")
                    .replace("]", "")
                    .replace("{", "")
                    .replace("}", "")
                    .replace(", ", ",")
                    + "\n"
                )
    filename.close()
else:
    print(result10._result_lines)

if result11.is_command_result_available():
    filename = open(output11, "w")
    for line in result11.get_output():
        if "NodeId" in line:
            filename.write(line + "\n")
        elif contains(list_of_strings, line):
            if contains_cell(cell_list, line):
                filename.write(
                    line.replace("[", "")
                    .replace("]", "")
                    .replace("{", "")
                    .replace("}", "")
                    .replace(", ", ",")
                    + "\n"
                )
    filename.close()
else:
    print(result11._result_lines)

if result12.is_command_result_available():
    filename = open(output12, "w")
    for line in result12.get_output():
        if "NodeId" in line:
            filename.write(line + "\n")
        elif contains(list_of_strings, line):
            if contains_cell(cell_list, line):
                filename.write(
                    line.replace("[", "")
                    .replace("]", "")
                    .replace("{", "")
                    .replace("}", "")
                    .replace(", ", ",")
                    + "\n"
                )
    filename.close()
else:
    print(result12._result_lines)

if result13.is_command_result_available():
    filename = open(output13, "w")
    for line in result13.get_output():
        if "NodeId" in line:
            filename.write(line + "\n")
        elif contains(list_of_strings, line):
            if contains_cell(cell_list, line):
                filename.write(
                    line.replace("[", "")
                    .replace("]", "")
                    .replace("{", "")
                    .replace("}", "")
                    .replace(", ", ",")
                    + "\n"
                )
    filename.close()
else:
    print(result13._result_lines)

if result14.is_command_result_available():
    filename = open(output14, "w")
    for line in result14.get_output():
        if "NodeId" in line:
            filename.write(line + "\n")
        elif contains(list_of_strings, line):
            if contains_cell(cell_list, line):
                filename.write(
                    line.replace("[", "")
                    .replace("]", "")
                    .replace("{", "")
                    .replace("}", "")
                    .replace(", ", ",")
                    + "\n"
                )
    filename.close()
else:
    print(result14._result_lines)

if result15.is_command_result_available():
    filename = open(output15, "w")
    for line in result15.get_output():
        if "NodeId" in line:
            filename.write(line + "\n")
        elif contains(list_of_strings, line):
            if contains_cell(cell_list, line):
                filename.write(
                    line.replace("[", "")
                    .replace("]", "")
                    .replace("{", "")
                    .replace("}", "")
                    .replace(", ", ",")
                    + "\n"
                )
    filename.close()
else:
    print(result15._result_lines)

if result16.is_command_result_available():
    filename = open(output16, "w")
    for line in result16.get_output():
        if "NodeId" in line:
            filename.write(line + "\n")
        elif contains(list_of_strings, line):
            if contains_cell(cell_list, line):
                filename.write(
                    line.replace("[", "")
                    .replace("]", "")
                    .replace("{", "")
                    .replace("}", "")
                    .replace(", ", ",")
                    + "\n"
                )
    filename.close()
else:
    print(result16._result_lines)

if result17.is_command_result_available():
    filename = open(output17, "w")
    for line in result17.get_output():
        if "NodeId" in line:
            filename.write(line + "\n")
        elif contains(list_of_strings, line):
            if contains_cell(cell_list, line):
                filename.write(
                    line.replace("[", "")
                    .replace("]", "")
                    .replace("{", "")
                    .replace("}", "")
                    .replace(", ", ",")
                    + "\n"
                )
    filename.close()
else:
    print(result17._result_lines)

if result18.is_command_result_available():
    filename = open(output18, "w")
    for line in result18.get_output():
        if "NodeId" in line:
            filename.write(line + "\n")
        elif contains(list_of_strings, line):
            if contains_cell(cell_list, line):
                filename.write(
                    line.replace("[", "")
                    .replace("]", "")
                    .replace("{", "")
                    .replace("}", "")
                    .replace(", ", ",")
                    + "\n"
                )
    filename.close()
else:
    print(result18._result_lines)

if result19.is_command_result_available():
    filename = open(output19, "w")
    for line in result19.get_output():
        if "NodeId" in line:
            filename.write(line + "\n")
        elif contains(list_of_strings, line):
            if contains_cell(cell_list, line):
                filename.write(
                    line.replace("[", "")
                    .replace("]", "")
                    .replace("{", "")
                    .replace("}", "")
                    .replace(", ", ",")
                    + "\n"
                )
    filename.close()
else:
    print(result19._result_lines)

if result20.is_command_result_available():
    filename = open(output20, "w")
    for line in result20.get_output():
        if "NodeId" in line:
            filename.write(line + "\n")
        elif contains(list_of_strings, line):
            if contains_cell(cell_list, line):
                filename.write(
                    line.replace("[", "")
                    .replace("]", "")
                    .replace("{", "")
                    .replace("}", "")
                    .replace(", ", ",")
                    + "\n"
                )
    filename.close()
else:
    print(result20._result_lines)

if result21.is_command_result_available():
    filename = open(output21, "w")
    for line in result21.get_output():
        if "NodeId" in line:
            filename.write(line + "\n")
        elif contains(list_of_strings, line):
            if contains_cell(cell_list, line):
                filename.write(
                    line.replace("[", "")
                    .replace("]", "")
                    .replace("{", "")
                    .replace("}", "")
                    .replace(", ", ",")
                    + "\n"
                )
    filename.close()
else:
    print(result21._result_lines)

if result22.is_command_result_available():
    filename = open(output22, "w")
    for line in result22.get_output():
        if "NodeId" in line:
            filename.write(line + "\n")
        elif contains(list_of_strings, line):
            if contains_cell(cell_list, line):
                filename.write(
                    line.replace("[", "")
                    .replace("]", "")
                    .replace("{", "")
                    .replace("}", "")
                    .replace(", ", ",")
                    + "\n"
                )
    filename.close()
else:
    print(result22._result_lines)

if result23.is_command_result_available():
    filename = open(output23, "w")
    for line in result23.get_output():
        if "NodeId" in line:
            filename.write(line + "\n")
        elif contains(list_of_strings, line):
            if contains_cell(cell_list, line):
                filename.write(
                    line.replace("[", "")
                    .replace("]", "")
                    .replace("{", "")
                    .replace("}", "")
                    .replace(", ", ",")
                    + "\n"
                )
    filename.close()
else:
    print(result23._result_lines)

if result24.is_command_result_available():
    filename = open(output24, "w")
    for line in result24.get_output():
        if "NodeId" in line:
            filename.write(line + "\n")
        elif contains(list_of_strings, line):
            if contains_cell(cell_list, line):
                filename.write(
                    line.replace("[", "")
                    .replace("]", "")
                    .replace("{", "")
                    .replace("}", "")
                    .replace(", ", ",")
                    + "\n"
                )
    filename.close()
else:
    print(result24._result_lines)

if result25.is_command_result_available():
    filename = open(output25, "w")
    for line in result25.get_output():
        if "NodeId" in line:
            filename.write(line + "\n")
        elif contains(list_of_strings, line):
            if contains_cell(cell_list, line):
                filename.write(
                    line.replace("[", "")
                    .replace("]", "")
                    .replace("{", "")
                    .replace("}", "")
                    .replace(", ", ",")
                    + "\n"
                )
    filename.close()
else:
    print(result25._result_lines)

if result26.is_command_result_available():
    filename = open(output26, "w")
    for line in result26.get_output():
        if "NodeId" in line:
            filename.write(line + "\n")
        elif contains(list_of_strings, line):
            if contains_cell(cell_list, line):
                filename.write(
                    line.replace("[", "")
                    .replace("]", "")
                    .replace("{", "")
                    .replace("}", "")
                    .replace(", ", ",")
                    + "\n"
                )
    filename.close()
else:
    print(result26._result_lines)

if result27.is_command_result_available():
    filename = open(output27, "w")
    for line in result27.get_output():
        if "NodeId" in line:
            filename.write(line + "\n")
        elif contains(list_of_strings, line):
            if contains_cell(cell_list, line):
                filename.write(
                    line.replace("[", "")
                    .replace("]", "")
                    .replace("{", "")
                    .replace("}", "")
                    .replace(", ", ",")
                    + "\n"
                )
    filename.close()
else:
    print(result27._result_lines)

enmscripting.close(session)
