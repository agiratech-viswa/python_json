import json

#loads
with open('abc.json', 'r') as f:
    fc = f.read()

data = json.loads(fc)
print(data)

#dumps
d_dum=json.dumps(data,indent=2)
print(d_dum)

for emp in data['emp']:
    print(emp['id'],emp['name'])
    
