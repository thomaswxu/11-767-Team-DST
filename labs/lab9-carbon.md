Lab 9: Carbon footprint
===
The goal of this lab is for you estimate the carbon footprint of your class project.

Group name: DST
---
Group members present in lab today: Saloni Mittal, Dhruv Naik, Thomas Xu

1: Inference
----
1. Plug your device in to the Kill-a-watt and run inference using your model to get a measurement of the energy draw. What is its baseline energy draw, and how does that compare to running inference?

| State | Batch Size | Avg. Latency (s) | Energy Usage (W) |
| --- | --- | --- | --- |
| Idle | N/A | N/A | 2.3 &pm; 0.1 |
| Seq2Seq Inference | 1 | 28.15 | 6.3 &pm; 0.6 |
| Seq2Seq Inference | 2 | 29.34 | 6.3 &pm; 0.6 |
| Seq2Seq Inference | 4 | 35.18 | 6.4 &pm; 0.5 |
| Seq2Seq Inference | 8 | 45.47 | 6.6 &pm; 0.5 |

2. Multiply energy draw by inference time to get an estimate of energy required per inference (you can average over input size).
> Seq2Seq (Averaged over input size):
> - Inference energy draw: 
> - Average inference time: 
> - Energy required per inference: **__**

3. Multiply this by the carbon intensity of the location of your device. You can use [this resource](https://www.epa.gov/egrid/power-profiler#/).
> - Device location: **CMU Campus** (NSH Basement), Pittsburgh PA
> - EPA eGRID region: [RFCW](https://www.epa.gov/egrid/power-profiler#/RFCW)
> - Carbon intensity at this location: **1067.7 lbs CO2/MWh**
> - Estimated carbon usage per inference: **__**
4. Please include at least this estimate in your final project report.

2: Training
----
1. Did your project require training a model? If so, compute that estimate as well. If you used cloud resources, you can use [this tool](https://mlco2.github.io/impact/#compute) to help estimate. Otherwise, try to use the methods discussed last class for estmating carbon footprint due to training. Show your work and explain.
> - ...

3: Extra
----
1. Everything else: Do you have logs you can use to estimate the amount of energy + carbon that went in to all project development? Other ways of estimating? Was your device plugged in and running for the entire semester?
2. Supply chain / lifecycle analysis: Can you estimate the additional footprint due to manufacturing hardware? Lifetime energy use of your project if it was deployed in the real world?
3. If you have a Pi or Jetson 4GB: Compare Kill-a-watt measurements to command line energy measurements, and discuuss.
