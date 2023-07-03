import matplotlib.pyplot as plt
import pandas as pd

file_path = "./archive.ics.uci.edu_ml_machine-learning-databases_00616_Tetuan City power consumption.csv"
df = pd.read_csv(file_path)

def latihan4(x):
    if x == "a":
        df.plot(
        kind="line",
        x="DateTime",
        y="Temperature",
        figsize=(10, 5)
        )
    elif x == "b":
        df.head(20).plot(
        kind="line",
        x="DateTime",
        y="Temperature",
        figsize=(10, 4)
        )
        plt.xticks(range(0,20), df["DateTime"].head(20),rotation=90)
    elif x == "c":
        df.tail(20).plot(
        kind="line",
        x="DateTime",
        y="Temperature",
        figsize=(10, 4)
        )
        plt.xticks(range(0,20), df["DateTime"].tail(20),rotation=90)

latihan4(input("Masukkan poin a, b, atau c: "))
plt.title("Temperature")
plt.ylabel("Temperature")
plt.xlabel("DateTime")
plt.show()