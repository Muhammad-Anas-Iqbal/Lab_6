
import pandas as pd
import matplotlib.pyplot as plt

# Create a messy weather dataset
data = {
    "Date": [
        "2026-09-01", "2026-09-02", "2026-09-03", "2026-09-04",
        "2026-09-05", "2026-09-06", "2026-09-07", "2026-09-08",
        "2026-09-09", "2026-09-10", "2026-09-11", "2026-09-12",
        "2026-09-13", "2026-09-14", "2026-09-15"
    ],
    "City": [
        " Islamabad ", "ISLAMABAD", " lahore", "LAHORE ",
        "Karachi", " karachi ", "ISLAMABAD ", " Lahore",
        "KARACHI", "Islamabad", " lahore ", "KARACHI ",
        "Islamabad", " Lahore ", "Karachi"
    ],
    "Temperature": [
        "32C", "34C", "30C", "29C", "35C",
        "33C", "31C", "28C", "36C", "33C",
        "27C", "34C", "30C", "29C", "35C"
    ],
    "Humidity": [
        45, 40, None, 65, 55, None, 50, 70,
        60, None, 75, 48, 52, 68, 57
    ],
    "Condition": [
        "sunny", " SUNNY ", " Rainy", "CLOUDY ",
        "Sunny", "rainy ", " cloudy", "SUNNY",
        " Rainy ", "cloudy", "RAINY", " sunny",
        "Cloudy ", "rainy", " SUNNY"
    ]
}

df = pd.DataFrame(data)

# Add one duplicated row
df = pd.concat([df, df.iloc[[0]]], ignore_index=True)

# (a) Clean the dataset
df["Date"] = pd.to_datetime(df["Date"])

df["City"] = df["City"].str.strip().str.title()
df["Condition"] = df["Condition"].str.strip().str.title()

df["Temperature"] = df["Temperature"].str.replace(
    "C", "", regex=False
)
df["Temperature"] = pd.to_numeric(df["Temperature"])

df = df.drop_duplicates()

df["Humidity"] = df["Humidity"].fillna(df["Humidity"].median())

print("Cleaned Weather Dataset:")
print(df)

# (b) One-hot encode Condition
df_encoded = pd.get_dummies(df, columns=["Condition"])

print("\nEncoded Columns:")
print(df_encoded.columns)

print("\nOne-Hot Encoded Dataset:")
print(df_encoded)

# (c), (d), (e), (f) Create four plots
fig, ax = plt.subplots(2, 2, figsize=(12, 9))

# Line plot: Temperature over Date
ax[0, 0].plot(df["Date"], df["Temperature"], marker="o")
ax[0, 0].set_title("Temperature Over Date")
ax[0, 0].set_xlabel("Date")
ax[0, 0].set_ylabel("Temperature (C)")
ax[0, 0].tick_params(axis="x", rotation=45)

# Scatter plot: Temperature vs Humidity
ax[0, 1].scatter(df["Temperature"], df["Humidity"])
ax[0, 1].set_title("Temperature vs Humidity")
ax[0, 1].set_xlabel("Temperature (C)")
ax[0, 1].set_ylabel("Humidity")

correlation = df["Temperature"].corr(df["Humidity"])
print("\nTemperature-Humidity Correlation:", correlation)

# Pie chart: Number of days per Condition
condition_counts = df["Condition"].value_counts()
ax[1, 0].pie(
    condition_counts,
    labels=condition_counts.index,
    autopct="%1.1f%%"
)
ax[1, 0].set_title("Weather Condition Distribution")

# Histogram: Temperature
ax[1, 1].hist(df["Temperature"], bins=5, edgecolor="black")
ax[1, 1].set_title("Temperature Distribution")
ax[1, 1].set_xlabel("Temperature (C)")
ax[1, 1].set_ylabel("Frequency")

# Overall dashboard title
fig.suptitle("Weather Overview", fontsize=16)
plt.tight_layout()
plt.savefig("weather_dashboard.png")
plt.show()
print("weather_dashboard.png has been saved successfully.")