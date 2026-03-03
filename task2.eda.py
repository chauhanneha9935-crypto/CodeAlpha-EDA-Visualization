import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("quotes_dataset.csv")

print("First 5 Rows:")
print(df.head())

print("\nDataset Info:")
print(df.info())

print("\nMissing Values:")
print(df.isnull().sum())

author_counts = df["Author"].value_counts()

plt.figure()
author_counts.head(5).plot(kind='bar')
plt.title("Top 5 Authors by Number of Quotes")
plt.xlabel("Author")
plt.ylabel("Number of Quotes")

plt.tight_layout()
plt.show(block=True)