Lab 6: Group work on projects
===
The goal of this lab is for you to make progess on your project, together as a group. You'll set goals and work towards them, and report what you got done, chaellenges you faced, and subsequent plans.

Group name: DST
---
Group members present in lab today: Saloni Mittal, Dhruv Naik, Thomas Xu

1: Plan
----
1. What is your plan for today, and this week? 

> ...

2. How will each group member contribute towards this plan?
> ...

2: Execution
----
1. What have you achieved today / this week? Was this more than you had planned to get done? If so, what do you think worked well?
> ...

2. Was there anything you had hoped to achieve, but did not? What happened? How did you work to resolve these challenges?

> Challenges:
> - We continued to have issues running on the Jetson's GPU. When trying to add the "--gpu" flag, the Jetson memory usage maxed out almost immediately. We suspect that perhaps it was trying to make a copy of the model, which used up the memory. For now, we run without the "--gpu" flag.
> - We continued to have issues when trying to quantize the ALFRED pretrained seq2seq model (i.e. ran into errors such as "NoneType has no attribute 'weight'). We tried various different quantization functions from the PyTorch documentation (quantize_dynamic, quantize, quantization.prepare, etc.) without success.

3. What were the contributions of each group member towards all of the above?
> - Saloni: 
> - Dhruv:
> - Thomas: 

3: Next steps
----
1. Are you making sufficient progress towards completing your final project? Explain why or why not. If not, please report how you plan to change the scope and/or focus of your project accordingly.

> As before, we are making progress but have consistently been slowed down by numerous errors and issues running the baseline models (running training scripts, applying torch quantization, etc.). This is an ongoing issue; if this is still the case one week from now then we plan to discuss adjusting the project scope again with the Professors.

2. Based on your work today / this week, and your answer to (1), what are your group's planned next steps?
> Next Steps:
> - ...

3. How will each group member contribute towards those steps? 
> - Saloni: 
> - Dhruv:
> - Thomas: 
