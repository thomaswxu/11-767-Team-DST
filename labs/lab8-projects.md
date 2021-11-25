Lab 8: Group work on projects
===
The goal of this lab is for you to make progess on your project, together as a group. You'll set goals and work towards them, and report what you got done, chaellenges you faced, and subsequent plans.

Group name: DST
---
Group members present in lab today: Saloni Mittal, Dhruv Naik, Thomas Xu

1: Plan
----
1. What is your plan for today, and this week? 
> 1. Set up HiTUT repo on Jetson, measure latency/power/etc., apply early-exit techniques to speed-up inference, similar to this paper [BERT Loses Patience: Fast and Robust Inference with Early Exit](https://proceedings.neurips.cc//paper/2020/file/d4dd111a4fd973394238aca5c05bebe3-Paper.pdf)
> 2. Quantize ALFRED Seq2Seq model on Jetson, and compare vs. unquantized version (latency, size, power consumption, etc.)
> 3. Benchmark accuracy and efficiency metrics with decreasing vocabulary size, re-trained models with lower hidden dimensions and compare performance.


2. How will each group member contribute towards this plan?
> - Saloni: Focus on 1 
> - Dhruv: Focus on 3, 2
> - Thomas: Focus on 2, 3

2: Execution
----
1. What have you achieved today / this week? Was this more than you had planned to get done? If so, what do you think worked well?  

> - While running HiTUT on CPU, it uses around 2.2 GB of RAM with batch size of 1. As a preliminary experiment to compress the model size, we performed int8 quantization of the linear layers of the model. Although, the model size reduces from 477 MB to 232 MB, there's a drastic loss in performance. The following table compares the original model's performance with the quantized model.
> - In the previous lab report, we missed mentioning and reporting the action argument accuracy.  Each action has two parts (type, arg) where type is the type (e.g., Goto) and arg is the argument/subject it is interacting with (e.g., Knife).

Model| Actions | action type accuracy | argument accuracy | mask accuracy |
---| --- | --- | --- | --- | 
| | sub-goals | 0.982 | 0.934 | NA |
Original | Navi. Actions | 0.889 | NA |  NA |
|| Mani. actions | 0.996 | 0.991 | 0.969 |
--- | --- | --- | --- | --- |
| | sub-goals | 0.314 | 0.200 | NA |
Quantized | Navi. Actions | 0.394 | NA | NA |
| | Mani. actions | 0.150| 0.270 | 0.189

> - This table shows that quantizing the linear layers in the HiTUT model has a drastic negative impact on the performance, which is understandable as the linear layers are essentially what the BERT architecture is composed of. Clearly, this model is highly sensitive to 8 bit quantization.
> -  We also wanted to perform only Embedding layer quantization on the model to measure how important it is to navigation task. But pytorch 1.6 does not support quantization of nn.Embedding layer.
> - The embedding matrix for this particular model is particuarly very large, Embedding(50265, 768) with more than 50k vocab size. Next, we want to try out some embedding matrix compression techniques.
> - For implementing early-exit methods on the HiTUT model, we require to do some training of additonal classification layers inserted at each layer of the transformer. We will do this after distilling this model into a 6-layer smaller model.

> - Quantized ALFRED Seq2Seq model on Jetson. Results below:
> - Fixed QConfig issues faced with Dynamic Quantization on-device.

| Set | loss_action_low | loss_action_low_mask | loss_subgoal_aux | loss_progress_aux | action_low_f1 | action_low_em | total_loss |
| ---   | --- | --- | --- | --- | --- | --- | --- |
| valid_seen | 0.625  | 0.393  | 0.0013|0.0056 | 0.776 | 0.0 | 1.026 | 
| valid_unseen | 1.283 | 1.998 | 0.001 | 0.0054 | 0.721 | 0.0 | 3.288 |

> - The quantized model's loss and F1 scores are the same as the normal model's scores reported in the last lab. This is consistent with the observations from experiments run by Tutorials in PyTorch (https://pytorch.org/tutorials/intermediate/dynamic_quantization_bert_tutorial.html, https://pytorch.org/tutorials/advanced/dynamic_quantization_tutorial.html) and experiments discussed in the paper: [Q8BERT: Quantized 8Bit BERT](https://arxiv.org/pdf/1910.06188.pdf). 

Inference RAM Consumption (Batch Size=8):
| Model | RAM |
| - | - |
| Normal | 1074 MB |
| Quantized | 894 MB |

Model Size:
| Model | Size |
| - | - |
| Normal | 176 MB |
| Quantized | 47.3 MB |


> - UNKed many words from vocabulary of ALFRED Seq2Seq and retrained. Number of words in each vocab section is given in the table below.
>   - UNK: Removing words from vocabulary and replacing them with a special "UNK" token to use for unknown words

| | words | action_low | action_high |
| --- | --- | --- | --- |
| Original | 2360 | 15 | 93 |
| Prune <6 occurrences | 1211 | 14 | 91 |

### **Challenges**
> - HiTUT repo includes MKL packages (e.g. mkl-fft) as requirements, which are not supported on the Jetson's architecture. Will try removing these from the requirements and, if necessary, replacing them with a supported similar package.
> - Quantized benchmark results from ALFRED Seq2Seq were very similar to the unquantized/original results. This result is very unintuitive and we are not certain why this is observed.


3. What were the contributions of each group member towards all of the above?
> - Saloni: Quantization and comparison for HiTUT, Looking into code implementation of early exit methods on BERT
> - Dhruv: Quantization and comparison for ALFRED Seq2Seq
> - Thomas: UNKing the input vocab for ALFRED Seq2Seq

3: Next steps
----
1. Are you making sufficient progress towards completing your final project? Explain why or why not. If not, please report how you plan to change the scope and/or focus of your project accordingly.

> Yes

2. Based on your work today / this week, and your answer to (1), what are your group's planned next steps?
> Next Steps:
> 1. Retrain ALFRED Seq2Seq with shrunken input vocab size and benchmark against original for accuracy/latency/etc.
> 2. Embedding Matrix Compression for HiTUT ( the vocab size is more than 50k tokens)
> 3. Distilling the HiTUT teacher model's knowledge into a smaller model.
> 4. Train the HiTUT model to dynamically learn to early exit during inference.


3. How will each group member contribute towards those steps? 
> - Saloni: 4, 3
> - Dhruv: 2, 3
> - Thomas: 1, 4