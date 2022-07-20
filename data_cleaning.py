from turtle import pd
import csv
import pandas as pd

df = pd.read_csv("total_stars.csv")

del df["Star Name (SC)"]
del df["Distance (ly)"]
del df["Mass(MJ)"]
del df["Radius (RJ)"]

df.to_csv("main.csv")