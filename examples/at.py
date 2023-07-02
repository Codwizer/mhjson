"""
Example of at()
"""
from mhjson import MHjson

qe = MHjson("./data.json").at("users").where("id", "<", 3).get()

print("result", qe)
