
import pandas as pd
import matplotlib.pyplot as plt

names = ["  ali", "SARA  ", "aHMED", "  Fatima ", "USMAN", "ayesha ", "HASSAN", " zain "]
marks = ["75", "88", "absent", "90", "65", "80", "70", "85"]

df = pd.DataFrame({
    "Name": names,
    "Marks": marks
})

df["Name"] = df["Name"].str.strip().str.title()

df["Marks"] = pd.to_numeric(df["Marks"], errors="coerce")

mean_marks = df["Marks"].mean()
df["Marks"] = df["Marks"].fillna(mean_marks)

print("Cleaned Student Marks:")
print(df)

df.plot(x="Name", y="Marks", kind="bar")

plt.title("Student Marks")
plt.xlabel("Student Name")
plt.ylabel("Marks")
plt.tight_layout()
plt.savefig("marks_bar.png")
plt.show()
print("marks_bar.png has been saved successfully.")