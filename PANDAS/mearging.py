import pandas as pd

df_1 = pd.DataFrame({
    "Customerid":[1,2,3,4,5],
    "Customername":["Anil","Bhuro","Chinkal","Dalpat","Emam"]
})

df_2 = pd.DataFrame({
    "Customerid":[1,2,3,4,9],
    "paying":[230,540,650,345,353]
})

df_joining = pd.merge(df_1,df_2,on="Customerid",how="inner")
print("Inner join : \n",df_joining)

df_outjoin = pd.merge(df_1,df_2,on="Customerid",how="outer")
print("Outer join : \n",df_outjoin)

df_leftjoin = pd.merge(df_1,df_2,on="Customerid",how="left")
print("Left join : \n",df_leftjoin)

df_rightjoin = pd.merge(df_1,df_2,on="Customerid",how="right")
print("Right join : \n",df_rightjoin)

