info={
    "name":"Arsaln",
    "subjects":["python", "java","c++"],
    "topics":("dict", "set"),
    "grade":9.6,
    "roll_number":23,
    "adult":True,
    "stat":{
        "one":"A",
        "two":"B",
    }
}
info["name"]="Arsalan Qadir"
print(type(info))
print(info["name"])
# Type casting of keys in list
print(list(info.keys()))