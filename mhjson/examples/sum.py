"""
Example of sum()
"""
from mhjson import MHjson

e1 = MHjson("./data.json").at("users.5.visits").sum("year")

print("result", e1)
