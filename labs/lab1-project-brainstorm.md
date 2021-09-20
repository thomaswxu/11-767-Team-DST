Lab 1: Project Brainstorming
===
The goal of this lab is for you to work as a group to brainstorm project ideas. At the end of this exercise you should have an outline for your project proposal that you can share with others to get feedback. We will share these outlines for peer feedback in the next lab.

Group name: DST
---
Group members present in lab today: Thomas Xu, Dhruv Naik, Saloni Mittal

1: Ideas
----
Write down 3-5 project ideas your group considered (a few sentences each). Depending on your group and process, the ideas may be very different, or they may be variations on one central idea.
 1. AirBERT is a pretrained model for VLN which can be finetuned for downstream VLN tasks. We propose to compress/distill this model and deploy it on the Jetson Nano, and finally use it for navigating in an environment given a natural language instruction.

 2. VilBERT is a task-agnostic pretrained model for Vision and Language tasks. We plan to make a visual chatbot on the device which can use both visual and language modalities using the compressed/distilled VilBERT.
    
 3. Automatic speech recognition in noisy environments. We will focus on robustness in spoken language understanding, wherein a robot has to understand and execute speech commands in a typical noisy environment.


2: Narrowing
----

**Idea: Vision-and-language Navigation**  

**1. How would this project leverage the expertise of each member of your group?**  
Saloni and Dhruv have experience working with NLP and vision models. Tom has experience using vision and robotic navigation.  

**2. In completing this project, what new things would you learn about:**  
(a) Hardware: stretch goals would be making a mobile base to physically navigate in a 3D environment (lab room); would use: simple chassis, motor driver board, motors + wheels, camera.    
(b) Efficiency in machine learning: knowledge distillation, power budgeting, and other compression techniques. (The original model is already 2.3 GB)   
(c) I/O modalities  
Camera/image sequences, natural language instruction.  
(d) Other: RL techniques for navigation, learning robust joint representations with vision and language.

**3. What potential road blocks or challenges do you foresee in this project? How might you adjust the project scope in case these aspects present unsurmountable challenges?**  
Main challenge is compressing the model until it can be run on the 2GB Jetson Nano. We also want the model to be able to run in near real-time. If these are insurmountable, an option would be to use the 4GB Jetson instead. Another chalenge can be working with the Matterport 3D simulator. From online blogs and forums, looks like setting up the simulator on local machine and running it smoothly can be a task.

**4. How could you potentially extend the scope of this project if you had e.g. one more month?**  
On-device active learning, improving model generalization to out-of-domain data, adding more complex hardware (mobile base).  


  
  
**Idea: Automatic Speech Recognition (ASR) in noisy environment.**  
**1. How would this project leverage the expertise of each member of your group?**  
Saloni and Dhruv have experience working with NLP and vision models. Tom has experience using vision and robotic navigation.  

**2. In completing this project, what new things would you learn about:**  
(a) Hardware: Microphone   
(b) Efficiency in machine learning: Power budgeting, general compression techniques.   
(c) I/O modalities: Audio/Mic, language  

**3. What potential road blocks or challenges do you foresee in this project? How might you adjust the project scope in case these aspects present unsurmountable challenges?**  
Will need a dataset with many different types of noisy audio/speech data in it (mimics real-life distribution of noisy audio data). Scope could be adjusted to only focus on a few types of noise.

**4. How could you potentially extend the scope of this project if you had e.g. one more month?**  
Could try using adversarial training on the small model to test robustness.

3: Outline
----
Choose one of the ideas you've considered, and outline a project proposal for that idea. This outline will be shared with other groups next class (Tuesday) to get feedback.

Your outline should include:
**Motivation**
To enable robots to smoothly navigate through realistic 3D visual environemnts using natural language has been a long-standing challenge. In vision-and-language navigation (VLN) tasks an embodied agent should first interpret the instructions and then determine if the visual inputs along a path matches the descriptions provided in the instructions. Given the extremely diverse nature of image and language inputs, the generalization of VLN agents to unseen environments remains challenging. There have been recent works in developing large visiolinguistic transformer-based models that are pretrained on large image-text pairs from the web. They show that pretraining helps in generalization and fine-tuning on embodied path-instruction data significantly improves performance on the downstream VLN task. One such pretrained model released in 2021 is AirBert which is trained on millions of VLN path-instruction (PI) pairs. They use Bnb (a large scacle VLN dataset created from AirBnb data) for pretraining and show that the AirBert model outperforms the state-of-the-art for for Room-to-Room (R2R) navigation and Remote Referring Expression (REVERIE) benchmarks.
For our project we propose to use this huge model for a VLN task.Our main focus will be on applying different compression/distillation techniques to AirBert, in order to deploy it on a 2gb Jetson Nano.
- Hypotheses (key ideas)
- How you will test those hypotheses: datasets, baselines, ablations, and other experiments or analyses.
- I/O: What are the inputs and output modalities? What existing tools will you use to convert device inputs (that are not a core part of your project) to a format readable by the model, and vice versa?
- Hardware, including any peripherals required, and reasoning for why that hardware was chosen for this project. (This is where you will request additional hardware and/or peripherals for your project!)
- Potential challenges, and how you might adjust the project to adapt to those challenges.
- Potential extensions to the project.

