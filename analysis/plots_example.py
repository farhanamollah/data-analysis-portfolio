import matplotlib
matplotlib.use("Agg")  # comment this out if running locally with a GUI
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os

df = pd.read_csv("data/example_data.csv")
sns.boxplot(x="condition", y="response", data=df)
plt.title("Response by Condition")

os.makedirs("figures", exist_ok=True)
plt.savefig("figures/response_by_condition.png", dpi=300, bbox_inches="tight")
print("Saved: figures/response_by_condition.png")
