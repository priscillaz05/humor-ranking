import re
import json


### Read in captions and description

raw_captions = []

with open("captions.txt", "r") as file:
    lines = file.readlines()
    for line in lines:
        raw_captions.append(line)

print(raw_captions)

captions = [re.sub(r'^\d+\.\s*', '', caption).rstrip() for caption in raw_captions]

print(captions)

with open("celebrity.txt", "r") as file:
    celebrity = file.read()

with open("description.txt", "r") as file:
    description = file.read()

print(celebrity, '\n')
print(description)


### Format for training data

data = [{"celebrity": celebrity, "description": description, "caption": caption} for caption in captions]

with open("raw_data.json", "w") as f:
    json.dump(data, f, indent=2)


### Simulate scored data
# The output of this step is what we use to fine-tune llama

# I let GPT score these jokes
scores = [78, 70, 82, 65, 88, 72, 85, 74, 68, 80]

for object, score in zip(data, scores):
    object["score"] = score

with open("scored_data.json", "w") as f:
    json.dump(data, f, indent=2)



### Simulated model output
# Hopefully, this is what our ranker model outputs for each caption

for object in data:
    del object["celebrity"]
    del object["description"]

with open("output.json", "w") as f:
    json.dump(data, f, indent=2) 


### Rank captions based on scores

sorted_captions = [item["caption"] for item in sorted(data, key=lambda x: x["score"], reverse=True)]

with open("ranked_captions.txt", "w") as f:
    for caption in sorted_captions:
        f.write(caption + "\n")