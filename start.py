import json
import random

with open("names.txt", "r") as names_file:
    names = names_file.read().splitlines()

used_names = names.copy()

file_path = "PathTo/build/json/_metadata.json"

# open the input file
with open(file_path, "r") as input_file:
    # read the json file
    data = json.load(input_file)

# loop through the data list and update each element's "name" key
for element in data:
    if len(used_names) == 0:
        used_names = names.copy()
    random_name = random.choice(used_names)
    element["name"] = random_name
    used_names.remove(random_name)

output_file_path = "new.json"

# open the output file
with open(output_file_path, "w") as output_file:
    # write the updated json to the output file
    json.dump(data, output_file, indent=4)

print("File Successfully updated")
