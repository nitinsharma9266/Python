import numpy as np
import pandas as pd
dict1={
    "name":["Nitin","Harshit","naitik","Ansh"],
    "Marks":[95,67,78,34],
    "City":["hardoi","kauraha","bariely","shahjahanpur"]
}
df=pd.DataFrame(dict1)

df.to_csv("friends.csv")
df.to_csv("friends False .csv",index=False)
df.head(2)

df.tail(2)
df.describe()
nitin=pd.read_csv("nitin.csv")

print("\n")
# print(nitin['speed'])
print("\n")
# nitin["speed"][0]=90
nitin.loc[0, "speed"] = 90

nitin.to_csv("nitin.csv",index=False)

df.index=["First","Second","Third","Fourth"]

df

ser=pd.Series(np.random.rand(34))

print(ser)

type(ser)

newdf=pd.DataFrame(np.random.rand(334,5), index=np.arange(334))

newdf.head(5)

newdf.tail(10)

type(newdf)

newdf.describe()

newdf.dtypes


