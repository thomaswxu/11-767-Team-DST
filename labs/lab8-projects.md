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

> - While running HiTUT on CPU, it uses around 2.2 GB of RAM with batch size of 1. As a preliminary experiment to compress model size, we performed int8 quantization of the linear layers of the model. Although, the model size reduces from 477 MB to 232 MB, there's a drastic loss in performance. The following table compares the original model's performance with the quantized model.

Model| Actions | action type accuracy | argument accuracy | mask accuracy |
---| --- | --- | --- | --- | 
| | sub-goals | 0.982 | 0.934 | NA |
Original | Navi. Actions | 0.889 | NA |  NA |
|| Mani. actions | 0.996 | 0.991 | 0.969 |
--- | --- | --- | --- | --- |
| | sub-goals | 0.314 | 0.200 | NA |
Quantized | Navi. Actions | 0.394 | NA | NA |
| | Mani. actions | 0.150| 0.189 | 0.

> - Quantized ALFRED Seq2Seq model on Jetson. Results below:
(TODO)

> - UNKed many words from vocabulary of ALFRED Seq2Seq and retrained.
>   - UNK: Removing words from vocabulary and replacing them with a special "UNK" token to use for unknown words

| | words | action_low | action_high |
| --- | --- | --- | --- |
| Original | 2360 | 15 | 93 |
| Prune <4 occurrences | . | . | . |


3. What were the contributions of each group member towards all of the above?
> - Saloni: 
> - Dhruv: 
> - Thomas: 

3: Next steps
----
1. Are you making sufficient progress towards completing your final project? Explain why or why not. If not, please report how you plan to change the scope and/or focus of your project accordingly.

> Yes

2. Based on your work today / this week, and your answer to (1), what are your group's planned next steps?
> Next Steps:
> 1. ...

3. How will each group member contribute towards those steps? 
> - Saloni: 
> - Dhruv: 
> - Thomas: 
