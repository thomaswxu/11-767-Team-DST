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
| Seq2Seq Inference | 1 | 8.06 | 6.3 &pm; 0.6 |
| Seq2Seq Inference | 2 | 10.22 | 6.3 &pm; 0.6 |
| Seq2Seq Inference | 4 | 22.31 | 6.4 &pm; 0.5 |
| Seq2Seq Inference | 8 | 46.63 | 6.6 &pm; 0.5 |
| HiTUT Inference | 1 | 1.24 | 7.6 &pm; 0.4 |
| HiTUT Inference | 2 | 1.88 | 8.0 &pm; 0.5 |
| HiTUT Inference | 4 | 3.83 | 8.0 &pm; 0.5 |
| HiTUT Inference | 8 | 7.50 | 8.2 &pm; 0.5 |
| HiTUT Inference | 32 | 28.10 | 8.7 &pm; 1.0 |

**Note**: Seq2Seq refers to our quantized Seq2Seq, and HiTUT refers to our pruned HiTUT.

2. Multiply energy draw by inference time to get an estimate of energy required per inference (you can average over input size).
> Seq2Seq (Averaged over input size):
> - Inference energy draw: 6.4 W
> - Inference time: 21.50 s
> - Energy required per inference: 6.4 * 21.50 = **137.60 J**

> HiTUT (Averaged over input size):
> - Inference energy draw: 8.1 W
> - Inference time: 8.6 s
> - Energy required per inference: 8.1 * 8.6 = **69.66 J**

3. Multiply this by the carbon intensity of the location of your device. You can use [this resource](https://www.epa.gov/egrid/power-profiler#/).
> - Device location: **CMU Campus** (NSH Basement), Pittsburgh PA
> - EPA eGRID region: [RFCW](https://www.epa.gov/egrid/power-profiler#/RFCW)
> - Carbon intensity at this location: **1067.7 lbs CO2/MWh**
> - Estimated carbon usage per inference:
>     - Seq2Seq: **4.08 * 10<sup>-5</sup> lbs** (0.0276 g)
>     - HiTUT: **2.07 * 10<sup>-5</sup> lbs** (0.0094 g)

4. Please include at least this estimate in your final project report.

2: Training
----
1. Did your project require training a model? If so, compute that estimate as well. If you used cloud resources, you can use [this tool](https://mlco2.github.io/impact/#compute) to help estimate. Otherwise, try to use the methods discussed last class for estmating carbon footprint due to training. Show your work and explain.
> - We did some training of the HiTUT model using cloud resources. In particular, we used Google Cloud Platform (GCP) in the region us-central1, which has a carbon efficiency of **0.57 kg CO2/kWh** (1.26 lbs CO2/kWh). A cumulative of **36 hours** of computation was performed on hardware of type Tesla K80 (TDP of 300W).
> - Total emissions are estimated to be **6.16 kg CO2** (13.58 lbs CO2) of which 100 percent was directly offset by the cloud provider.  
> - Estimations were conducted using the [MachineLearning Impact calculator](https://mlco2.github.io/impact#compute).


3: Extra
----
1. Everything else: Do you have logs you can use to estimate the amount of energy + carbon that went in to all project development? Other ways of estimating? Was your device plugged in and running for the entire semester?
2. Supply chain / lifecycle analysis: Can you estimate the additional footprint due to manufacturing hardware? Lifetime energy use of your project if it was deployed in the real world?
3. If you have a Pi or Jetson 4GB: Compare Kill-a-watt measurements to command line energy measurements, and discuuss.
