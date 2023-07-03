import matplotlib.pyplot as plt
import pandas as pd

file_path = "./archive.ics.uci.edu_ml_machine-learning-databases_00616_Tetuan City power consumption.csv"
df = pd.read_csv(file_path)


def get_humidity_class(humidity):
    if humidity < 69:
        return "Low"
    if humidity < 80:
        return "Medium"
    return "High"
df["Humidity class"] = df["Humidity"].map(get_humidity_class)
print(df["Humidity class"].value_counts())
df["Humidity class"].value_counts().plot(
 kind="pie",
 autopct="%1.2f%%",
 colors=("#18AEE2", "#DA5455", "#FF8E00")
)
plt.title("Humidity Class")
plt.ylabel("")
plt.show()


