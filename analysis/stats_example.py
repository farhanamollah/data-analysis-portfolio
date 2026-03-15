import pandas as pd
from scipy import stats

df = pd.read_csv("data/example_data.csv")
group_a = df[df["condition"] == "A"]["response"]
group_b = df[df["condition"] == "B"]["response"]

t, p = stats.ttest_ind(group_a, group_b, equal_var=False)
print(f"t = {t:.3f}, p = {p:.3g}")
