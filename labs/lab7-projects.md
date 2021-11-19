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
> - The HiTUT model breaks the ALFRED naviagtion tasks into three sub-problems:


> - Ran ALFRED Seq2Seq with split up loss components:
>   - valid_seen:
>   - 'loss_action_low': 0.6260462720756945
>   - 'loss_action_low_mask': 0.3933338560163975
>   - 'loss_subgoal_aux': 0.0013221983890221252
>   - 'loss_progress_aux': 0.005602777450922472
>   - 'action_low_f1': 0.7763294361960337
>   - 'action_low_em': 0.0
>   - 'total_loss': 1.0263051034315773
> - valid_unseen:
>   - 'loss_action_low': 1.2837616373663363
>   - 'loss_action_low_mask': 1.9977664131185282
>   - 'loss_subgoal_aux': 0.0013499829390481034
>   - 'loss_progress_aux': 0.005384720583527308
>   - 'action_low_f1': 0.7204101302493144
>   - 'action_low_em': 0.0
>   - 'total_loss': 3.2882627663405044

> - Set up new SD card on Jetson to increase storage space from 32 GB to 256 GB
>   - Now can fit additional repos/models in addition to the ALFRED repo (was taking up almost entire storage space previously)

3. What were the contributions of each group member towards all of the above?
> - Saloni: Fixed GCP set up issues with CMU IT/GCP support, set up HiTUT and got initial results on GCP
> - Dhruv: Ran ALFRED Seq2Seq on unseen and seen validation splits, generating sub goal metrics and losses
> - Thomas: Set up new SD card on Jetson, installed torch/np/etc. with ALFRED dependencies

3: Next steps
----
1. Are you making sufficient progress towards completing your final project? Explain why or why not. If not, please report how you plan to change the scope and/or focus of your project accordingly.

> ...

2. Based on your work today / this week, and your answer to (1), what are your group's planned next steps?
> Next Steps:
> - ...

3. How will each group member contribute towards those steps? 
> - Saloni: 
> - Dhruv:
> - Thomas:
