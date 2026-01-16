import json
data = '{"name" : "yash", "roll" : 5}'
parsed = json.loads(data) # ye json filr ko dictinory me convert karta hai
print(parsed["roll"])

data2 = {
    "students" : ["yash","rudra","sahal","anas"],
    "roll": [5,4,12,33],
    "frige" : ("Dahi",30),
    "are_boy" : True
}

json_str = json.dumps(data2)   # ye python co json me convert karta hai
print(json_str)