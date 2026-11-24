import numpy as np 
import pandas as pd
import os
import requests

numbers = np.array([1, 2, 3, 4, 5])
print("Numpy Array:", numbers)
print("Mean:", numbers.mean())

data ={
    "name" :["John", "Jane", "Doe"],
    "age" :[28, 34, 29],
}
df = pd.DataFrame(data)
print("Pandas DataFrame:")
print(df)