from transformers import BertTokenizer, BertModel
import torch
from timeit import default_timer as timer

tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
model = BertModel.from_pretrained('bert-base-uncased')

isQuantized = True
if (isQuantized):
        torch.backends.quantized.engine = 'qnnpack'
        quantized_model = torch.quantization.quantize_dynamic(model, {torch.nn.Linear}, dtype=torch.qint8)
        model = quantized_model
        torch.save(quantized_model, "./quantized_bert.pth")


# inputs of diff sizes
input5 = tokenizer("Hello, my dog is cute", return_tensors="pt")
input10 = tokenizer("Hello, my dog is cute Hello, my dog is cute", return_tensors="pt")
input25 = tokenizer("Hello, my dog is cute Hello, my dog is cute Hello, my dog is cute Hello, my dog is cute Hello, my dog is cute", return_tensors="pt")
input75 = tokenizer("Hello, my dog is cute Hello, my dog is cute Hello, my dog is cute Hello, my dog is cute Hello, my dog is cute Hello, my dog is cute Hello, my dog is cute Hello, my dog is cute Hello, my dog is cute Hello, my dog is cute Hello, my dog is cute Hello, my dog is cute Hello, my dog is cute Hello, my dog is cute Hello, my dog is cute", return_tensors="pt")
input150 = tokenizer("Hello, my dog is cute Hello, my dog is cute Hello, my dog is cute Hello, my dog is cute Hello, my dog is cute Hello, my dog is cute Hello, my dog is cute Hello, my dog is cute Hello, my dog is cute Hello, my dog is cute Hello, my dog is cute Hello, my dog is cute Hello, my dog is cute Hello, my dog is cute Hello, my dog is cute Hello, my dog is cute Hello, my dog is cute Hello, my dog is cute Hello, my dog is cute Hello, my dog is cute Hello, my dog is cute Hello, my dog is cute Hello, my dog is cute Hello, my dog is cute Hello, my dog is cute Hello, my dog is cute Hello, my dog is cute Hello, my dog is cute Hello, my dog is cute Hello, my dog is cute", return_tensors="pt")

input_list = [input5, input10, input25, input75, input150]

# timing
outputs = model(**input_list[0]) # run once to make sure model loading, etc. is not included in timing
for i in range(len(input_list)):
		inputs = input_list[i]
		start = timer()
		for j in range(10):
			print(j)
			outputs = model(**inputs)
		end = timer()
		print("AVG TIME: " + str((end - start)/(j+1)) + " s") # Time in seconds, e.g. 5.38091952400282



last_hidden_states = outputs.last_hidden_state

print("DONE")