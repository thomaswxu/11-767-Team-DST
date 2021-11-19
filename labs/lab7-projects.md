Lab 7: Group work on projects
===
The goal of this lab is for you to make progess on your project, together as a group. You'll set goals and work towards them, and report what you got done, chaellenges you faced, and subsequent plans.

Group name: DST
---
Group members present in lab today: Saloni Mittal, Dhruv Naik, Thomas Xu

1: Plan
----
1. What is your plan for today, and this week? 
> - Set up the GitHub repo for HiTUT BERT
> - Check in with Ankit and CMU IT regarding GCP VM issues
> - Split of loss from ALFRED Seq2Seq into individual components
> - Set up new SD card on Jetson to have enough storage for multiple repos/models
> - Shrinking ALFRED Seq2Seq vocabulary

2. How will each group member contribute towards this plan?
> - Saloni: Set up HiTUT on GCP
> - Dhruv: Split ALFRED Seq2Seq loss into separate components
> - Thomas: Set up new SD card on Jetson and install required dependencies

2: Execution
----
1. What have you achieved today / this week? Was this more than you had planned to get done? If so, what do you think worked well?  
> - Resolved the GCP admin issue with the CMU computing help. Successfully, set up a VM and the runtime python environment for HiTUT repo.
> - Tested the HiTUT RoBERTa trained checkpoint on valid_seen of the ALFRED without the simulator.
> - The total number of parameters in HiTUT is: **124.76 M** ;  while number of parameters in the seq2seq lstm model is : **45.93M**.
> - The HiTUT model breaks the ALFRED naviagtion tasks into three sub-problems: sub-goal planning, scene navigation, and object manipulation.
> - Here are the statistics of the data distribution of the validation seen dataset in ALFRED.

| Actions | # data instances |
| --- | --- |
| sub-goals | 6.4k |
| Navi. Actions | 39k |
| Mani. actions | 8.3k|

> - The following numbers are per action accuracy for all the sub-goals, navigation actions and the manipulation actions present in the validation seen dataset.

| Actions | action accuracy | mask accuracy |
| --- | --- | --- |
| sub-goals | 0.982 | NA |
| Navi. Actions | 0.889 | NA |
| Mani. actions | 0.996 | 0.969 |

> - For the manipulation action sub-task, the model generates a segmentation mask on the current visual observation to indicate which object to interact with. The mask prediction is crucial because the action will not be successfully executed with an incorrect grounding even if is correctly predicted.

> - Ran ALFRED Seq2Seq with split up loss components:

| Set | loss_action_low | loss_action_low_mask | loss_subgoal_aux | loss_progress_aux | action_low_f1 | action_low_em | total_loss |
| ---   | --- | --- | --- | --- | --- | --- | --- |
| valid_seen | 0.626  | 0.393  | 0.0013|0.0056 | 0.776 | 0.0 | 1.026 | 
| valid_unseen | 1.284 | 1.998 | 0.001 | 0.005 | 0.720 | 0.0 | 3.288 |

> - Set up new SD card on Jetson to increase storage space from 32 GB to 256 GB
>   - Now can fit additional repos/models in addition to the ALFRED repo (was taking up almost entire storage space previously)

> - Ground work on running tests for different vocabulary size, layer dimensions in Seq2seq LSTM model
>   - Current codebase does not make use of <UNK>, thus after "UNK"-ing last N tokens or less frequent tokens, we need to retrain the model to learn a good embedding representation for <UNK> token.

3. What were the contributions of each group member towards all of the above?
> - Saloni: Fixed GCP set up issues with CMU IT/GCP support, set up HiTUT and got initial results on GCP
> - Dhruv: Ran ALFRED Seq2Seq on unseen and seen validation splits, generating sub goal metrics and losses
> - Thomas: Set up new SD card on Jetson, installed torch/np/etc. with ALFRED dependencies

3: Next steps
----
1. Are you making sufficient progress towards completing your final project? Explain why or why not. If not, please report how you plan to change the scope and/or focus of your project accordingly.

> Yes

2. Based on your work today / this week, and your answer to (1), what are your group's planned next steps?
> Next Steps:
> 1. Set up HiTUT repo on Jetson, measure latency/power/etc., apply early-exit techniques to speed-up inference, similar to this paper [BERT Loses Patience: Fast and Robust Inference with Early Exit](https://proceedings.neurips.cc//paper/2020/file/d4dd111a4fd973394238aca5c05bebe3-Paper.pdf)
> 2. Quantize ALFRED Seq2Seq model on Jetson, and compare vs. unquantized version (latency, size, power consumption, etc.)
> 3. Benchmark accuracy and efficiency metrics with decreasing vocabulary size, re-trained models with lower hidden dimensions and compare performance.

3. How will each group member contribute towards those steps? 
> - Saloni: Focus on 1 
> - Dhruv: Focus on 3, 2
> - Thomas: Focus on 2, 3
