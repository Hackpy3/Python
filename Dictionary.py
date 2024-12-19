# Access dictionary
# studentinfo = {
    
#     "Kishan": {
#         "name": "kshan",
#         "location": "khulna",
#         "study": "12",
#         "subject": "commerce",
#         "roll": 6,
#         "number": 125456
#     },
#      "Abul": {
#         "name": "kabil",
#         "location": "dhaka",
#         "study": "11",
#         "subject": "commerce",
#         "roll": 7,
#         "number": 126984
#     }
#}
# print(studentinfo["Abul"])
# x = studentinfo.get("Abul")
# print(x)
# x = studentinfo.keys()
# print(x)

# print all the values/items
studentinfo = {
    
    "Kishan": {
        "name": "kshan",
        "location": "khulna",
        "study": "12",
        "subject": "commerce",
        "roll": 6,
        "number": 125456
    },
     "Abul": {
        "name": "kabil",
        "location": "dhaka",
        "study": "11",
        "subject": "commerce",
        "roll": 7,
        "number": 126984
    }
}
#for a in studentinfo.values():
    #print(a)
for a in studentinfo.items():
    print(a)