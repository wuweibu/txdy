import json

#反序列化   sample.json -> python
with open('sample.json') as f:
    sample=json.load(f)

print(sample.keys())

new_sample= {}
new_sample[] = sample[]

#序列化 python-> json

with open('new_sample','w')as f:
    json.dump(new_sample,f,indent=4)     



