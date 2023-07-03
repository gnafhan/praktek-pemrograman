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
df["Humidity class"].value_counts().plot(
 kind="bar",
# warna class low adalah red, warna kelas medium adalah yellow, warna kelas hijau adalah green
 color=["#18AEE2", "#DA5455", "#FF8E00"]
)

plt.title("Humidity Class")
plt.ylabel("")
plt.show()