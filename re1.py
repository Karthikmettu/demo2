import pandas as pd

temp = [30, 32, 35, 32, 31, 32, 34]

df = pd.DataFrame(temp, columns=["Temperature"])

print(df)

print("Mean:", df["Temperature"].mean())
print("Median:", df["Temperature"].median())
print("Mode:")
print(df["Temperature"].mode())