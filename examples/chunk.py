"""
Example of chunk()
"""
from mhjson import MHjson

e1 = MHjson("./data.json").at("users").where("location", "=", "Barisal").chunk(2)

print("result", e1)
