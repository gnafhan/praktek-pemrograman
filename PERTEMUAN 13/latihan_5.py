import matplotlib.pyplot as plt
import pandas as pd

file_path = "./archive.ics.uci.edu_ml_machine-learning-databases_00616_Tetuan City power consumption.csv"
df = pd.read_csv(file_path)


def latihan5(x):
    if x == "a":
        df.plot(
            kind="scatter",
            x="Temperature",
            y="Zone 1 Power Consumption",
        )
    elif x == "b":
        df.head(100).plot(
            kind="scatter",
            x="Temperature",
            y="Zone 1 Power Consumption",
        )
    elif x == "c":
        df.tail(100).plot(
            kind="scatter",
            x="Temperature",
            y="Zone 1 Power Consumption",
        )
latihan5(input("Masukkan poin a, b, atau c: "))
plt.title("Temperature vs Zone 1 Power consumption")
plt.show()
