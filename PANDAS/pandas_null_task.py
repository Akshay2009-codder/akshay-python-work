import numpy as np
import pandas as pd
from numpy.ma.core import where

data = {
    "student":["Akshay","Sahal","Yash"],
    "subject":["Python","Java","C++"],
    "score":[90,95,80],
    "city":["Tharad","Chadotar", None]
}

info = pd.DataFrame(data)
print("\n printing dataframe")
print(info)

print("\n colomn that have only none value")
print(info[info.isnull()])

print("\n filling missing values")
info.fillna(value="Unknown",inplace=True)

print("\n creating new pass column")
info["pass"] = "fail"
info.loc[info["score"]>=85,"pass"] = "pass"

print("\n printing fainal dataframe")
print(info)
