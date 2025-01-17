Lab 3: Quantization
===
The goal of this lab is for you to benchmark and compare model size and inference efficiency **between quantized and original models** on your devices. You should benchmark the same models as you benchmarked last lab, so ideally **2*N* models or model variants, where *N* is the size of your group (so, two models per person.)** For now, if you don't have appropriate evaluation data in place that's fine; you can provide pretend data to the model for now and just evaluate efficiency.

Ideally, the models you benchmark will be the same as last class, but if you find that you're unable to run out-of-the-box quantization on your models, feel free to try quantizing other models, or a subset. Just be sure to explain what you tried, and why.

Include any code you write to perform this benchmarking in your Canvas submission (either as a link to a folder on github, in a shared drive, zip, etc).

Group name: DST
---
Group members present in lab today: Thomas Xu, Dhruv Naik, Saloni Mittal

1: Models
----
1. Which models and/or model variants will your group be studying in this lab? What is the original bit width of the models, and what precision will you be quantizing to? What parts of the model will be quantized (e.g. parameters, activations, ...)? Please be specific.

>We  used dynamic quantization provided within Pytorch for each of the following models. All weights corresponding to the linear layers and the activations are quantized to 'int8'. The original bit width of the models is 'FP32'.
> - LXMERT
> - VisualBERT
> - CLIP
> - DistilBERT
> - ALBERT
> - BERT

2. Why did you choose these models?

> - LXMERT consists of three encoders: an object relationship encoder, a language encoder, and a cross-modality encoder.
 VisualBERT is another visually-grounded language model, capable of performing tasks such as captioning, question answering.
> Since VLN task is also a multimodal (image+text) task, these state-of-the-art models are of great relevance.

> - We benchmarked CLIP because it provided contrast by being a model that is still used with Natural Language Processing, but in a different application area (image labelling) vs our project (navigation).

>    - We benchmarked DistilBERT and ALBERT as they contain much less parameters than original BERT-large and perform almost competitively on may benchmarks. We want to see how their quantized version fare against quantized original BERT model (especially in accuracy, experiment to be conducted soon.) We benchmarked BERT to act as a comparison for these.

3. For each model, you will measure model size (in (mega,giga,...)bytes), and inference latency. You will also be varying a parameter such as input size or batch size. What are your hypotheses for how the quantized models will compare to non-quantized models according to these metrics? Do you think latency will track with model size? Explain.
> Quantization converts FP32 weights to INT8, which should translate to approximately a 4x reduction in size.
> The latency should decrease with the model size.


2: Quantization in PyTorch
----
1. [Here is the official documentation for Torch quantization](https://pytorch.org/docs/stable/quantization.html) and an [official blog post](https://pytorch.org/blog/introduction-to-quantization-on-pytorch/) about the functionality. Today we'll be focusing on what the PyTorch documentation refers to as  **dynamic** quantization (experimenting with **static** quantization and **quantization-aware training (QAT)** is an option for extra credit if you wish). 
2. In **dynamic** PyTorch quantization, weights are converted to `int8`, and activations are converted as well before performing computations, so that those computations can be performed using faster `int8` operations. Accumulators are not quantized, and the scaling factors are computed on-the-fly (in **static** quantization, scaling factors are computed using a representative dataset, and remain quantized in accumulators). You can acitvate dynamic quantization to `int8` for a model in PyTorch as follows: 
   ```
   import torch.quantization
   quantized_model = torch.quantization.quantize_dynamic(model, {torch.nn.Linear}, dtype=torch.qint8)
   ```
3. Make sure you can use basic quantized models. Dynamic quantization using torchvision is quite straightforward. e.g. you should be able to run the basic [`classify_image.py`](https://github.com/strubell/11-767/blob/main/labs/lab3-quantization/classify_image.py) script included in this directory, which uses a quantized model (`mobilenet_v2`). If you are having trouble, make sure your version of torch has quantization enabled. This whl should work:
    ```
    wget herron.lti.cs.cmu.edu/~strubell/11-767/torch-1.8.0-cp36-cp36m-linux_aarch64.whl
    pip3 install torch-1.8.0-cp36-cp36m-linux_aarch64.whl
    ```
4. Try changing the model to `mobilenet_v3_large` and set `quantize=False`. (Note that `quantize=True` may fail due to unsupported operations.) What happens?
> Instead of finding "Great Dane" it finds "Blue Tick" after changing to mobilenet_v3_large with no quantization.
5. Try to use this to quantize your models. If you're feeling lost and/or you're unable to get this to work on your model [here is a tutorial on using dynamic quantization on a fine-tuned BERT](https://pytorch.org/tutorials/intermediate/dynamic_quantization_bert_tutorial.html) and [here is one quantizing an LSTM language model](https://pytorch.org/tutorials/advanced/dynamic_quantization_tutorial.html). 
6. Any difficulties you encountered here? Why or why not?
> Some models that we were originally going to quantize did not work with the torch quantization command because the model "had no attribute eval()"

3: Model size
----
1. Compute the size of each model. Given the path to your model on disk, you can compute its size at the command line, e.g.:
   ```
   du -h <path-to-serialized-model>
   ```
   | Model | Original Size (MB)| Quantized Size (MB) |
   | ---   | ---  | --- |
   | LXMERT| 816 | 273 |
   | VisualBert| 434 | 178 |
   | CLIP | 591 | 255 |
   | DistilBERT | 254 | 132 |
   | BERT| 420 | 174 |
   | ALBERT| 45 | 23 |

2. Any difficulties you encountered here? Why or why not?
> N/A

4: Latency
----
1. Compute the inference latency of each model. You can use the same procedure here as you used in the last lab. Here's a reminder of what we did last time: 
   You should measure latency by timing the forward pass only. For example, using `timeit`:
    ```
    from timeit import default_timer as timer

    start = timer()
    # ...
    end = timer()
    print(end - start) # Time in seconds, e.g. 5.38091952400282
    ```
    Best practice is to not include the first pass in timing, since it may include data loading, caching, etc.* and to report the mean and standard deviation of *k* repetitions. For the purposes of this lab, *k*=10 is reasonable. (If standard deviation is high, you may want to run more repetitions. If it is low, you might be able to get away with fewer repetitions.)
    
    For more information on `timeit` and measuring elapsed time in Python, you may want to refer to [this Stack Overflow post](https://stackoverflow.com/questions/7370801/how-to-measure-elapsed-time-in-python).
    
    In the following table we've reported the average latency of batch size 1 per model.

     | Model | Original Model latency (in seconds)| Quantized Model latency (in seconds) |
   | ---   | ---  | --- |
   | LXMERT| 1.193 | 0.472 |
   | VisualBert| 0.652 | 0.234 |
   | CLIP | 1.010 | 0.962 |
   | DistilBERT | 0.173 | 0.063 |
   | BERT| 0.390 | 0.157 |
   | ALBERT | 0.362 | 0.127 |

2. Repeat this, varying one of: batch size, input size, other. Plot the results (sorry this isn't a notebook):
   ```
   import matplotlib.pyplot as plt
   
   plot_fname = "plot.png"
   x = ... # e.g. batch sizes
   y = ... # mean timings
   
   plt.plot(x, y, 'o')
   plt.xlabel('e.g. batch size')
   plt.ylabel('efficiency metric')
   plt.savefig(plot_fname)
   # or plot.show() if you e.g. copy results to laptop
   ```
   
   ---
   ### LXMERT
   ![lxmert1](plot_quant_lxm.png)
   
   ### VisualBert
   ![visualbert](plot_quant_vis.png)

   ### DistilBERT
   ![distilBERT](distilBERT.png)

   ### ALBERT
   ![albert](ALBERT.png)
   
   ### CLIP
   ![clip](plot_clip_quantize.png)

   ### BERT
   ![bert-base-uncased](plot_bert_quantize.png)
   ---
4. Any difficulties you encountered here? Why or why not?
> Had to reinstall torch on device with the above wheel, since the existing torch build did not have QNNPack compiled.
> For ALBERT, when the input token count is 416 words, the computation time for one forward pass increases dramatically to ~650 seconds (Not shown in the plot for scale issues). This behavior is not see in its quantized version. Unable to explain this.

5: Discussion
----
1. Analyze the results. Do they support your hypotheses? Why or why not? Did you notice any strange or unexpected behavior? What might be the underlying reasons for that behavior?
> There is an approximate 4-5x reduction in model size after quantization, which supports the hypotheses. This is because of a straighforward reduction in parameter size from FP32 to INT8.
> Both the quantized models for ALBERT and DistilBERT behave unexpectedly when the input token length increases above 100 tokens. The latency of one forward pass in more than the respective unquantized models after 100 tokens. This is very difficult to explain, and since this happens consistenly for both the models around the same input length, we wonder if this happens for a reason. We also notice similar behavior for CLIP and BERT, further suggesting that this trend is not a coincidence. Perhaps this is due to some strange behavior with the Jetson Nano's compute hardware; e.g. for small input sizes the quantized version with ints may be better optimized, but for large input sizes they are less optimized on the hardware.

5: Extra
----
A few options:
1. Try to run static quantization, or quantization aware training (QAT). Benchmark and report your results. Here is a nice blog post on [using static quantization on Torchvision models](https://leimao.github.io/blog/PyTorch-Static-Quantization/) in PyTorch.
2. Compute FLOPs and/or energy use (if your device has the necessary power monitoring hardware) for your models. 
3. Evaluate on different hardware (for example, you might run the same benchmarking on your laptop.) Compare the results to benchmarking on your device(s).
4. Use real evaluation data and compare accuracy vs. efficiency. Describe your experimental setup in detail (e.g. did you control for input size? Batch size? Are you reporting average efficiency across all examples in the dev set?) Which model(s) appear to have the best trade-off? Do these results differ from benchmarking with synthetic data? Why or why not?

----
\* There are exceptions to this rule, where it may be important to include data loading in benchmarking, depending on the specific application and expected use cases. For the purposes of this lab, we want to isolate any data loading from the inference time due to model computation.
