#!/bin/bash

#for eta in 21; do for pT in 30; 
#do python submitProdStep.py --nRuns=10 -n 5 -s ${pT}${eta}${run} -d CloseByPhotonsFromVtx -w rtmWorkflowPU -o EdTest \
#--pT=${pT} --Eta=${eta} --minz=0 --PtEta=pt${pT}_eta${eta} \
#--skip-step1 --config2=step2_DIGI_L1TrackTrigger_L1_DIGI2RAW_HLT_PU.py --config3=../step3_EMiterOnly_PU.py \
#-e /eos/cms/store/group/dpg_hgcal/comm_hgcal/escott/TICLstudies/Pass0/ -E /eos/cms/store/user/amagnan/HGCAL/TiCL/EMonlyNew/CloseByPhotonsFromVtx/;
#done; done

#for eta in 21; do for pT in 30; 
#do python submitProdStep.py --nRuns=10 -n 5 -s ${pT}${eta}${run} -d CloseByPhotonsFromVtx -w rtmWorkflowPU -o EdTestStepThree \
#--pT=${pT} --Eta=${eta} --minz=0 --PtEta=pt${pT}_eta${eta} \
#--skip-step1 --skip-step2 --config2=step2_DIGI_L1TrackTrigger_L1_DIGI2RAW_HLT_PU.py --config3=../step3_EMiterOnly_PU.py \
#-e /eos/cms/store/group/dpg_hgcal/comm_hgcal/escott/TICLstudies/Pass0/ -E /eos/cms/store/group/dpg_hgcal/comm_hgcal/escott/TICLstudies/Pass0/CloseByPhotonsFromVtx/;
#done; done

#for eta in 21; do for pT in 30; 
#do python submitProdStep.py --nRuns=10 -n 5 -s ${pT}${eta}${run} -d CloseByPhotonsFromVtx -w rtmWorkflowPU -o EdTestStepThreeTicl \
#--pT=${pT} --Eta=${eta} --minz=0 --PtEta=pt${pT}_eta${eta} \
#--skip-step1 --skip-step2 --skip-step3 --config2=step2_DIGI_L1TrackTrigger_L1_DIGI2RAW_HLT_PU.py --config3=../step3ticl_PU.py \
#-e /eos/cms/store/group/dpg_hgcal/comm_hgcal/escott/TICLstudies/Pass0/ -E /eos/cms/store/group/dpg_hgcal/comm_hgcal/escott/TICLstudies/Pass0/CloseByPhotonsFromVtx/;
#done; done


#for eta in 21; do for pT in 3 5 10 15 20 40 50 75 100 150 200; 
#do python submitProdStep.py --nRuns=10 -n 5 -s ${pT}${eta}${run} -d CloseByPhotonsFromVtx -w rtmWorkflowPU -o EdFullProd \
#--pT=${pT} --Eta=${eta} --minz=0 --PtEta=pt${pT}_eta${eta} \
#--skip-step1 --config2=step2_DIGI_L1TrackTrigger_L1_DIGI2RAW_HLT_PU.py --config3=../step3_EMiterOnly_PU.py \
#-e /eos/cms/store/group/dpg_hgcal/comm_hgcal/escott/TICLstudies/Pass0/ -E /eos/cms/store/user/amagnan/HGCAL/TiCL/EMonlyNew/CloseByPhotonsFromVtx/;
#done; done

for eta in 21; do for pT in 3 5 10 15 20 40 50 75 100 150 200; 
do python submitProdStep.py --nRuns=10 -n 5 -s ${pT}${eta}${run} -d CloseByPhotonsFromVtx -w rtmWorkflowPU -o EdFullProd \
--pT=${pT} --Eta=${eta} --minz=0 --PtEta=pt${pT}_eta${eta} \
--skip-step1 --skip-step2 --skip-step3 --config3=../step3ticl_PU.py \
-e /eos/cms/store/group/dpg_hgcal/comm_hgcal/escott/TICLstudies/Pass0/ -E /eos/cms/store/group/dpg_hgcal/comm_hgcal/escott/TICLstudies/Pass0/CloseByPhotonsFromVtx/;
done; done
