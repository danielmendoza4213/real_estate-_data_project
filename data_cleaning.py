import chompjs
import json
import pandas as pd


""" this part is to clean the file(data_inmo.json) exported after running the spider  """
with open("data_inmo.json", "r") as a:
    b = json.load(a)

lst_ann = []

""" We used the try and except so if we encouter a link without the desired information, the procces will continue"""
for i in b:

    try:
        c = i["data"]
        """ this is basicaly taking the porstion inside "classified, it is inside this key that most of the 
        information is"""
        lst_ann.append(((chompjs.parse_js_object(c))[0])["classified"])
    except:
        pass

""" we saved the information as a json file and csv"""
with open("data_clean.json", "w") as h:
    for i in lst_ann:
        json.dump(i, h)
        h.write("\n")

df = pd.read_json("data_clean.json", lines=True)
df.to_csv("data_clean.csv", index=None)

""" this part is to cosntruct the csv file with the desired data -> see image -> colums_to_pick.png
    we did not manage to build a file with the columns names a"""

# # keys = ["zip", "type", "price", "transactionType"]
# # for key in keys:
# #     print(data_clean[key])
