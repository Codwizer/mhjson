"""
Example of group_by()
"""
from mhjson import MHjson

e1 = MHjson("./data.json").at("products").group_by("price").get()

print("result", e1)
