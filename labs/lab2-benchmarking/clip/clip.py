from PIL import Image
import requests

from transformers import CLIPProcessor, CLIPModel

import numpy as np

from timeit import default_timer as timer
import matplotlib.pyplot as plt


model = CLIPModel.from_pretrained("openai/clip-vit-base-patch32")
processor = CLIPProcessor.from_pretrained("openai/clip-vit-base-patch32")

default_url = "http://images.cocodataset.org/val2017/000000039769.jpg"
default_image = Image.open(requests.get(default_url, stream=True).raw)

big_url = "https://blog.mystart.com/wp-content/uploads/shutterstock_352176329-e1527775515405.jpg"
big_image = Image.open(requests.get(big_url, stream=True).raw)

small_url = "https://is2-ssl.mzstatic.com/image/thumb/Purple125/v4/9e/0f/d7/9e0fd7e0-c936-f33f-7ef6-d78fe5764ff1/source/256x256bb.jpg"
small_image = Image.open(requests.get(small_url, stream=True).raw)


image = big_image

#inputs = processor(text=["cat", "dog"], images=image, return_tensors="pt", padding=True)
#inputs = processor(text=["a photo of a cat", "a photo of a dog"], images=image, return_tensors="pt", padding=True)
inputs = processor(text=["of a caa photo of a caa photo of a caa photo of a caa photo of a caa photo of a caa photo of a cattttttttt photo of a cata photo of a caa photo of a caa photo of a caa photo of a caa photo of a caa photo of a caa photo of a cattttttt ", "a photo of a doa photo of a doa photo of a doa photo of doggggggggggga photo photo of a doa photo of a doa photo of a doa photo of a doa photo of a doa photo of a doa photo of a doggggggggggga photo of a dog"], images=image, return_tensors="pt", padding=True)




start = timer()
for i in range(10):
    print(i)
    outputs = model(**inputs)
end = timer()
print(i)
print("AVG TIME: " + str((end - start)/(i+1)) + " s") # Time in seconds, e.g. 5.38091952400282

logits_per_image = outputs.logits_per_image # this is the image-text similarity score
probs = logits_per_image.softmax(dim=1) # we can take the softmax to get the label probabilities

# PARAMS
num_params = sum([np.prod(p.size()) for p in model.parameters()])
print("PARAMS: " + str(num_params))


print("DONE")

