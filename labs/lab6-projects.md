Lab 6: Group work on projects
===
The goal of this lab is for you to make progess on your project, together as a group. You'll set goals and work towards them, and report what you got done, chaellenges you faced, and subsequent plans.

Group name: DST
---
Group members present in lab today: Saloni Mittal, Dhruv Naik, Thomas Xu

1: Plan
----
1. What is your plan for today, and this week? 

> Our current baseline is LSTM-based. We want to explore transformer-based models and compare their performance against our baseline; mainly power consumption and inference speed metrics. We will also perform some preliminary research on other compression techniques for the project. We also want to fix the quantization error that we faced in last lab.

2. How will each group member contribute towards this plan?
> This is our initial tentative plan for this coming week.
> - Preliminary research on other compression techniques for the project  - Thomas/Dhruv
> - Preliminary work/research on transformer Seq2Seq - Saloni
> - Fix quantization for ALFRED + benchmark - Dhruv

2: Execution
----
1. What have you achieved today / this week? Was this more than you had planned to get done? If so, what do you think worked well?  

**Knowledge Distillation Research**
> - We plan to apply knowledge distillation on the baseline models for the project, so this week we conducted research on existing work in knowledge for LSTM-based models. Part of our rationale for choosing knowledge distillation were the discussions in lecture, which mentioned that knowledge distillation can work for any kind of underlying architecture. We opted not to do pruning because in lecture it was mentioned that pruning is worse than quantization, which we plan to do, and we opted not to try adaptive compute because it may not work well with different batch sizes. So for knowledge distillation on LSTM/similar models, we looked into:
>   - [Knowledge Distillation for Sequence Model](https://www.researchgate.net/profile/Zhehuai-Chen/publication/327389374_Knowledge_Distillation_for_Sequence_Model/links/5c4a6923458515a4c73e94c5/Knowledge-Distillation-for-Sequence-Model.pdf): This paper proposes "sequence-level" knowledge distillation, with the purpose of improving distillation performance for sequence models like Connectionist Temporal Classification (CTC). The authors show that using this sequence-level knowledge distillation gives significant improvements over frame-level distillation on a Switchboard and Chinese corpus.
>   - [Sequence-Level Knowledge Distillation](https://arxiv.org/abs/1606.07947): Like the above paper, in this work the authors proposed sequence-level knowledge distillation methods that show improvementes over word-level distillation, in the area of machine translation. 
> - Sadly neither this nor the above work provided code or GitHub repos that we could find, so it will be difficult to implement their findings for our project. Thus we will most likely apply the BERT-based models and knowledge distillation we found (below).  

**Transformer-based version of Baseline**
> - Our current baseline Seq2Seq model uses LSTMs as encoders and decoders. We want to evaluate the power and efficiency perfomance of a transformer-based model and compare it against our LSTM-based model. 
>> - We came across a github repo, https://github.com/594zyc/HiTUT that implements a BERT-based model for the ALFRED benchmark. The code is easy to understand and can be easily tweaked. Currently, thier trained checkpoint is a RoBERTa fine-tuned on ALFRED in a multi-task learning setup. The model size is 476 MB with 12 transformer layers, embedding dimension 768, inner dimension 2048 and 4 muti-attention heads. Please find the model architecture of HiTUT in the image below.
<p align="center">
<img src="HiTuT.png " width="256" height="256">
</p>

>> - We plan to use this model as the teacher model and perform knowledge distillation on a smaller 6-layer RoBERTa student model just as done in DistillBERT. We chose this model as it performs significantly better than our current baseline and therefore, is more suited to become the teacher model. The below image compares HiTUT vs Seq2Seq results on ALFRED.
<p align="center">
<img src="Seq2SeqVsHiTUT.png " width="300" height="200">
</p>

>> - One appealing factor of this particular github repo is that its environment is very similar to the ALFRED environment that already exists on jetson. Hence, we will not need to create a completely different python environment that takes up space.

>>- We also spent some time exploring the existing Seq2Seq baseline code and see if it can be tweaked to replace the LSTM model with transformer blocks. The code is very complex and we've made some progress here. This week one of us will continue work on this if we run into any blockers with our first idea of HiTUT.

> - We also tried setting up a VM on GCP for training purposes for our coming experiments. As we have signed up with our andrew accounts, GCP throws an admin access error and doesn't allow us to create a VM. We have raised a ticket with CMU IT about this as suggested by our TA, Ankit.


2. Was there anything you had hoped to achieve, but did not? What happened? How did you work to resolve these challenges?

> Challenges:
> - We continued to have issues when trying to quantize the ALFRED pretrained seq2seq model (i.e. ran into errors such as "NoneType has no attribute 'weight'). We tried various different quantization functions from the PyTorch documentation (quantize_dynamic, quantize, quantization.prepare, etc.) without success.

3. What were the contributions of each group member towards all of the above?
> - Saloni: Preliminary exploration of Seq2Seq transformer-based model creation/GCP VM error follow-up/ finding HiTUT model and creating action plan for knowledge distillation on this model.
> - Dhruv:
> - Thomas: 

3: Next steps
----
1. Are you making sufficient progress towards completing your final project? Explain why or why not. If not, please report how you plan to change the scope and/or focus of your project accordingly.

> As before, we are making progress but have consistently been slowed down by numerous errors and issues running the baseline models (running training scripts, applying torch quantization, etc.). This is an ongoing issue; if this is still the case one week from now then we plan to discuss adjusting the project scope again with the Professors.

2. Based on your work today / this week, and your answer to (1), what are your group's planned next steps?
> Next Steps:
> - Set up the GitHub repo for BERT/Distilbert
> - Deep-dive into the quantization issues (looking into the actual torch.py files) for the baseline

3. How will each group member contribute towards those steps? 
> - Saloni: Train a 6-layer HiTUT model via knowledge distillation using the larger HiTUT teacher model/Follow-up with CMU IT on the GCP VM creation issue.
> - Dhruv:
> - Thomas: 
