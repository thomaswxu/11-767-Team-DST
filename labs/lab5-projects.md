Lab 5: Group work on projects
===
The goal of this lab is for you to make progess on your project, together as a group. You'll set goals and work towards them, and report what you got done, chaellenges you faced, and subsequent plans.

Group name:
---
Group members present in lab today: Saloni Mittal, Dhruv Naik, Thomas Xu

1: Plan
----
1. What is your plan for today, and this week? 

> We benchmarked the model on a laptop in previous class due to issues with installation of requirements on device (CUDA version mismatch, h5py installation etc). This week we plan to debug the installation issues on device, run the seq2seq model on device, benchmark the latency and memory consumed, using a small validation subset, since the entire dataset is too large to fit on device. We also plan to quantize the model and compare the results with our existing benchmarking results.
Lastly, we will plan our experiments and work for the coming weeks, and decide on particular areas such as memory consumption, model size or latency to improve on.

2. How will each group member contribute towards this plan?
> Each member will help transfer necessary data and model files to Jetson, and will work together to debug any issues encountered running the model on device.

2: Execution
----
1. What have you achieved today / this week? Was this more than you had planned to get done? If so, what do you think worked well?
> We compared performance across different batch sizes on the baseline model (ALFRED, Seq2Seq) on the Jetson Nano. We compared batch size to latency and RAM usage (see figures below).

| Batch Size | Avg Latency (s) | Max RAM used (GB) |
| ---   | --- | --- |
| 1 | 8.015 | 1.02
| 2 | 10.275 | 1.20 |
| 4 | 22.250 | 1.42 |
| 8 | 46.571 | 1.85 |

![batch_latency](lab5_batch_latency.png)
![batch_ram](lab5_batch_ram.png)


2. Was there anything you had hoped to achieve, but did not? What happened? How did you work to resolve these challenges?

> Challenges:
> - We were not able to run this on the Jetson's GPU. When trying to add the "--gpu" flag, the Jetson memory usage maxed out almost immediately. We suspect that perhaps it was trying to make a copy of the model, which used up the memory. For now, we run without the "--gpu" flag.
> - The batch size used was not being set correctly from the command line argument for some reason; we had to fix this via hard coding.
> - The Jetson was out of storage space so we had to delete many other files and environments to make space for ALFRED
> - We observed memory usage increases with time for part of the execution. There was potentially a  memory leak (even after using torch.nograd() for the relevant functions). 
> - We wanted to quantize the ALFRED pretrained seq2seq model to compare performance for this lab, but ran into errors: e.g. "NoneType has no attribute 'weight'. We are still trying to debug these errors.

3. What were the contributions of each group member towards all of the above?
> - Saloni: Run different batch sizes on Jetson, debug GPU vs CPU usage, help debug quantization on Jetson, reduce input data sizes to fit on memory
> - Dhruv: Debug GPU vs CPU usage, run different batch sizes on Jetson, transfer json features to Jetson, install Jtop, clear space on Jetson, debugging errors with parsing arguments and issue preprocessing a small subset transferred to device
> - Thomas: Compare Jetson results to results from laptop, debug FileNotFoundErrors, record performance data, move valid_seen/valid_unseen data to Jetson, help debug quantization on Jetson

3: Next steps
----
1. Are you making sufficient progress towards completing your final project? Explain why or why not. If not, please report how you plan to change the scope and/or focus of your project accordingly.

> The team is making progress, but we have been consistently been slowed down by numerous errors and issues running the baseline models. Things that we accomplished quickly on different models in previous labs (e.g. quantization) resulted in very many bugs with the ALFRED repo that take us a long time to solve. This is an ongoing issue; if this is still the case one week from now then we plan to discuss adjusting the project scope again with the Professors.

2. Based on your work today / this week, and your answer to (1), what are your group's planned next steps?
> Next Steps:
> - Fix the bug stopping us from quantizing the pretrained Seq2Seq model, then re-run the above tests to compare performance.
> - Build a shallow transformer-based Seq2Seq model similar to the benchmarked model. Compare LSTM-based Seq2Seq against a transformer-based model. We hypothesise that the latency should improve with the latter as it allows data parallelism. We would also like to perform comparisons on power consumption profiles.
> - Explore other compression techniques that can be applied to our two Seq2Seq model.
> - Explore what advanced concepts/techniques introduced in the class can be utilized for our architectures. 

3. How will each group member contribute towards those steps? 
> - Saloni: Look into what work is required for the shallow transformer-based Seq2Seq model,
> - Dhruv: Explore other compression techniques from class to apply, debug Torch quantization bug
> - Thomas: Explore other compression techniques to apply, look into architecture specific compression techniques to use for project.
