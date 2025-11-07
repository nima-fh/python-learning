import json
import csv

with open("data.json","r+") as df:
    s=json.load(df)

print(s)
    
print(s["data"]["name"])

with open("data.csv","r+") as dc:
   data=list(csv.DictReader(dc))
   for i in data:
       print(i)