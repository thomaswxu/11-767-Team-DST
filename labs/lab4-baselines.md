Lab 4: Baselines and Related Work
===
The goal of this lab is for you to survey work related to your project, decide on the most relevant baselines, and start to implement them.

Ideally, the outcome of this lab would be: (1) the related work section of your project report is written and (2) baselines have been benchmarked.

Group name: DST
---
Group members present in lab today: Thomas Xu, Druhv Naik, Saloni Mittal

1: Related Work
----
1. Choose at least 2 pieces of related work per group member. For each piece of related work, write a paragraph that includes:
    - Summary of the main contributions of that work.
    - How your proposed project builds upon or otherwise relates to that work.

**Room-Across-Room: Multilingual Vision-and-Language
Navigation with Dense Spatiotemporal Grounding**
> - Summary of main contributions:
>   - The authors introduce "Room-Across-Room" (RxR), which is a new Vision-and-Language Navigation (VLN) dataset. This new dataset expands upon previous datasets by addressing previous biases in paths and providing additional information for visible entities. It also supports three typologically diverse languages (English, Hindi, Telegu) to prevent overfitting to particular languages. They also provide baseline scores for monolingual, multilingual, and multitask VLN learning settings.
> - How we build upon or relate to the work:
>   - Our project examines how existing VLN models can be run on edge devices. Most of the existing research we have found makes use of datasets and simulators (e.g. R2R, Matterport) that are similar to the one in this work. 

**Are We There Yet? Learning to Localize in Embodied Instruction Following**
> - Summary of main contributions:
>   - The authors address the challenge of the agent localizing itself and target key locations in the simulated environment during VLN tasks. To do so, they add additional viewing angles to the agent's field of view (FOV), so that they may better train the agent to predict its localized location with relation to the target location each timestep. The authors also add their own object detection module to the pipelines of existing work to improve upon baseline performance.
> - How we built upon or relate to the work:
>   - Our project and this work both examine VLN performance for embodied agents in simulated environments. This work focuses more closely on one aspect of that, namely the challenges of learning the ability to localize, whereas we focus on reducing model size so that it may be run on the edge.

**(Related Work)**
> ...  

**(Related Work)**
> ...  

...

2: Baselines
----
1. What are the baselines that you will be running for your approach? Please be specific: data, splits, models and model variants, any other relevant information.  

**(Baseline/Model Name)**
> - Data: 
> - Splits:
> - ...

2. These baselines should be able to run on your device within a reasonable amount of time. If you haven't yet tried to run them, please include a back-of-the-envelope calculation of why you think they will fit in memory. If the baselines will not fit in memory, return to (1) and adjust accordingly.  
> ...
3. How will you be evaluating your baselines?
> ...
4. Implement and run the baselines. Document any challenges you run into here, and how you solve them or plan to solve them.
> ...
5. If you finish running and evaluating your baselines, did the results align with your hypotheses? Are there any changes or focusing that you can do for your project based on insights from these results?
> ...

3: Extra
----
More related work, more baselines, more implementation, more analysis. Work on your project.


FAQ
----
1. Our baseline is the SotA model from XXX 2021 which doesn't fit on device.  

Yikes! I think you meant to say -- "We used some very minimal off the shelf components from torchvision/huggingface/... to ensure our basic pipeline can run"

2. We're evaluating our baseline on accuracy only

I think you meant to say -- "We plan to plot accuracy against XXXX to see how compute and performance trade-off. Specifically, we can shrink our baseline by doing YYYY"
