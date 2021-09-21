Lab 2: Project Workshopping / Peer Feedback
===
The goal of this lab is for you to give and receive peer feedback on project outlines before writing up your proposal. 

- **You can find your team's reviewing assignments in the first sheet [here](https://docs.google.com/spreadsheets/d/1_pw_lYkFutMjuL1_j6RdxNyQlj7LvF_f5eEKr1Qm-w0/edit?usp=sharing).**
- **The second sheet contains links to all teams' outlines to review.**
- **Once you have reviewed an outline, please enter a link to your review (e.g. a Google Doc, public github repo, etc.) replacing your team name in the corresponding other team's row in the third sheet.**


Here's a reminder of what your completed project proposal should include:
- Motivation
- Hypotheses (key ideas)
- How you will test those hypotheses: datasets, ablations, and other experiments or analyses.
- Related work and baselines
- I/O: What are the inputs and output modalities? What existing tools will you use to convert device inputs (that are not a core part of your project) to a format readable by the model, and vice versa?
- Hardware, including any peripherals required, and reasoning for why that hardware is needed for this project. (This is where you will request additional hardware and/or peripherals for your project!)
- Will you need to perform training off-device? If so, do you need cloud compute credits (GCP or AWS), and how much?
- Potential challenges, and how you might adjust the project to adapt to those challenges.
- Potential extensions to the project.
- Potential ethical implications of the project.
- Timeline and milestones. (Tip: align with Thursday in-class labs!)

Group name:
---
Group members present in lab today:

1: Review 1
----
Name of team being reviewed: 
1. How does your team's background align with that of the proposed project (e.g. if the proposed project is in CV but your team's backgorund is mostly NLP, state that here. Similarly, if your team also has someone who specializes in the area of the proposed project, state that here.)
2. Are the motivation, hypotheses, and plan to test those hypotheses clear? If not, where could the team provide more clarification or explanation? 
3. Does the project seem properly scoped for a semester-long project? Why or why not? How might the team be able to adjust the project to be appropriately scoped?
4. Are there any potential ethical concerns that arise from the proposed project? 
5. Any additional comments or concerns? Any related work you know of that might be relevant and/or helpful?

2: Review 2
----
Name of team being reviewed: How do you turn this on
1. How does your team's background align with that of the proposed project (e.g. if the proposed project is in CV but your team's backgorund is mostly NLP, state that here. Similarly, if your team also has someone who specializes in the area of the proposed project, state that here.)  
>This project is in the area of automatic speech recognition. Our team has two members with NLP backgrounds. No experts in ASR on our team  
2. Are the motivation, hypotheses, and plan to test those hypotheses clear? If not, where could the team provide more clarification or explanation?  
>The motivation and hypotheses are very clear (implementing existing ASR end-to-end models on edge devices). The plans to test the hypotheses make sense (dataset, baselines, metrics given), but more clarifying information could be given regarding each of the given items: e.g. a brief explanation of what is in the Librespeech dataset, what metrics the baselines use, etc.  
3. Does the project seem properly scoped for a semester-long project? Why or why not? How might the team be able to adjust the project to be appropriately scoped?  
>The project scope seems appropriate for a semester-long project: it mainly focuses on taking existing ASR end-to-end models and pruning/distilling/etc. until it can run well on an edge device. If this is completed early, the project can be extended by improving the on-edge performance so that each of the listed metrics improve.  
4. Are there any potential ethical concerns that arise from the proposed project?  
>No ethical concerns.  
5. Any additional comments or concerns? Any related work you know of that might be relevant and/or helpful?  
>No additional comments or concerns.  

3: Review 3
----
YU: 
1. How does your team's background align with that of the proposed project (e.g. if the proposed project is in CV but your team's backgorund is mostly NLP, state that here. Similarly, if your team also has someone who specializes in the area of the proposed project, state that here.)
> Our team's background is primarily in NLP and Robotics, but all the team members have some exposure to vision based machine learning tasks.


2. Are the motivation, hypotheses, and plan to test those hypotheses clear? If not, where could the team provide more clarification or explanation? 

> ### Motivation
>Usecases, where on-device inference using SuperPoint network is helpful, can be given to explain the motivation for fitting the model on a Jetson Nano.
> ### Hypotheses
> The current model size and the proposed percentage reduction using mentioned model could be mentioned. It would be helpful to have the current benchmark numbers as well, as well as what you think should be the distilled/quantized model's approximate accuracy/other metrics, so that it makes sense to run it on-device.

3. Does the project seem properly scoped for a semester-long project? Why or why not? How might the team be able to adjust the project to be appropriately scoped?
> The project is very open ended at the moment, as there are no concrete benchmark/size reduction/speed goals mentioned. But it can definitely be scoped as a semester-long project

4. Are there any potential ethical concerns that arise from the proposed project? 
> No obvious ethical concerns that arise from the given task.

6. Any additional comments or concerns? Any related work you know of that might be relevant and/or helpful?


4: Receiving feedback
----
Read the feedback that the other groups gave on your proposal, and discuss as a group how you will integrate that into your proposal. List 3-5 useful pieces of feedback from your reviews that you will integrate into your proposal:
1. ...
2. ...
3. ...
4. ...
5. ...

You may also use this time to get additional feedback from instructors and/or start working on your proposal.


