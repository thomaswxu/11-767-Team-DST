Lab 5: Group work on projects
===
The goal of this lab is for you to make progess on your project, together as a group. You'll set goals and work towards them, and report what you got done, chaellenges you faced, and subsequent plans.

Group name:
---
Group members present in lab today:

1: Plan
----
1. What is your plan for today, and this week? 

> We had benchmarked our model in the previous lab. Now, we want to assess at what input batch sizes or other factors like memory mapped disk space do we max out the RAM on the device. Also, how does the latency and power consumption scale on doing so. 
We also want to benchmark the model's performance after quantization.

2. How will each group member contribute towards this plan?

2: Execution
----
1. What have you achieved today / this week? Was this more than you had planned to get done? If so, what do you think worked well?
2. Was there anything you had hoped to achieve, but did not? What happened? How did you work to resolve these challenges?
3. What were the contributions of each group member towards all of the above?

3: Next steps
----
1. Are you making sufficient progress towards completing your final project? Explain why or why not. If not, please report how you plan to change the scope and/or focus of your project accordingly.

> The team

2. Based on your work today / this week, and your answer to (1), what are your group's planned next steps?
> Next Steps:
> - Build a shallow transformer-based Seq2Seq model similar to the benchmarked model. Compare LSTM-based Seq2Seq against a transformer-based model. We hypothesise that the latency should improve with the latter as it allows data parallelism. We would also like to perform comparisons on power consumption profiles.
> - Explore other compression techniques that can be applied to our two Seq2Seq model.
> - Explore what advanced concepts/techniques introduced in the class can be utilized for our architectures. 

3. How will each group member contribute towards those steps? 
