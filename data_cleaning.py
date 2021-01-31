import chompjs

"""Im sure this could be more "elegant" and make the info prettier"""


with open("data_inmo.json", "r") as file:
    a = file.read()
    b = chompjs.parse_js_object(a)
lst = []
for i in b:
    c = i["data"]
    d = chompjs.parse_js_object(c)
    lst.append(d[0])

data_clean1 = []
for i in lst:
    e = i["classified"]
    data_clean1.append(e)


# keys = ["zip", "type", "price", "transactionType"]
# for key in keys:
#     print(data_clean[key])
