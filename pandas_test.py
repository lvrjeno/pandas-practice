import pandas as pd
import matplotlib.pyplot as plt

# Step 1: Read CSV
df = pd.read_csv("data.csv")

# Step 2: Preview Data
print("\n--- First 5 Rows ---")
print(df.head())

# Step 3: Data Info
print("\n--- Info ---")
print(df.info())

# Step 4: Descriptive Statistics
print("\n--- Summary Statistics ---")
print(df.describe())

# Step 5: Sorting
sorted_df = df.sort_values(by="Duration", ascending=False)
print("\n--- Sorted by Duration ---")
print(sorted_df.head())

# Step 6: Filtering
high_pulse = df[df["Pulse"] > 100]
print("\n--- Pulse > 100 ---")
print(high_pulse)

# Step 7: Grouping
avg_by_maxpulse = df.groupby("Maxpulse")["Calories"].mean()
print("\n--- Average Calories by Maxpulse ---")
print(avg_by_maxpulse)

# Step 8: Plotting
plt.figure(figsize=(8,5))
plt.plot(df["Duration"], df["Calories"], marker="o")
plt.title("Duration vs Calories Burned")
plt.xlabel("Duration")
plt.ylabel("Calories")
plt.grid(True)
plt.show()
