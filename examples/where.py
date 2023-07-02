"""
Example of where()
"""
from  mhjson import MHjson

e1 = MHjson("./data.json").at("users")\
                        .where("id", ">", 3)\
                        .where("location", "=", "Barisal")\
                        .get()


e2 = MHjson("./data.json").at("users")\
                        .where("id", ">", 3)\
                        .where("location", "=", "Barisal")\
                        .get()


e3 = MHjson("./data.json").at("users")\
                        .where("id", ">", 3)\
                        .where("location", "=", "barisal", True)\
                        .get()

print("result", e1)
print("result", e2)
print("result", e3)
