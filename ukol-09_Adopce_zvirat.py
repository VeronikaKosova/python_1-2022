from this import d
from tkinter.tix import COLUMN
from numpy import column_stack
import pandas

adopce = pandas.read_csv("adopce-zvirat.csv", sep=";")
print(adopce)

print(adopce.info())
print(adopce.columns)
print(adopce.iloc[35])

# BONUS
# adopce = pandas.read_csv("adopce-zvirat.csv", index_col="nazev_cz")
# print(adopce)
# print(adopce.index.is_unique)
# print(adopce.sort_index())
# print(adopce.loc["Outloň váhavý"])
# print(adopce.loc["Želva Smithova" a "Želva žlutočelá"])



