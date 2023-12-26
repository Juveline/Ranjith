import json
import csv

with open ("file.json", "r") as f:
    data =json.load(f)
    names = data["look"]

with open ("file.json", "w") as f:
    fieldnames = names[0].keys()
    writer = csv.DictWriter(f,fieldnames=fieldnames)
    writer.writeheader()
    for name in names:
        writer.writerow(name)