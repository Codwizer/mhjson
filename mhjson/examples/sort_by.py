"""
Example of sort_by()
"""
from mhjson import MHjson

e1 = MHjson("./data.json").at("products").sort_by("id", "desc").get()

print("result", e1)
