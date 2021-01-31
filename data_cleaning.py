import chompjs
import json


""" this part is to clean the file(data_inmo.json) exported after running the spider  """
with open("data_inmo.json", "r") as a:
    b = json.load(a)

lst_ann = []
for i in b:
    c = i["data"]
    try:
        lst_ann.append(((chompjs.parse_js_object(c))[0])["classified"])
    except:
        pass

with open("data_clean.json", "w") as h:
    for i in lst_ann:
        json.dump(i, h)
        h.write("\n")


# """ this part is to cosntruct the csv file with the desired data -> see image -> colums_to_pick.png"""

# # keys = ["zip", "type", "price", "transactionType"]
# # for key in keys:
# #     print(data_clean[key])
