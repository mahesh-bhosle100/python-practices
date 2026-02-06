import json
# javascripts oriantaion notation
"""
JSON ek lightweight data format hai jo data ko store aur exchange karne ke liye use hota hai.
Ye human-readable hota hai aur machines ke liye parse karna easy hota hai.

"""

data = {"name": "Mahesh", "age": 22}
# json_data = json.dumps(data) # dump python to json 

# print(json_data)
# print(data) 



# json_data = json.loads(json_data) # load json to pyhton 

# print(json_data)


with open ("data.json" ,"w")as f :
    json.dump(data,f)