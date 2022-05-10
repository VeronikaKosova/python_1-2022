from gettext import install
import pandas

teplota = pandas.read_csv("temperature.csv")
teplota = teplota.set_index("City")
print(teplota.head())
print(teplota.loc["Prague"])
print(teplota[teplota["AvgTemperature"] > 80])
print(teplota[(teplota["AvgTemperature"] > 60) & (teplota["Region"] == "Europe")])
print(teplota[(teplota["AvgTemperature"] > 80) | (teplota["AvgTemperature"] < -20)])



