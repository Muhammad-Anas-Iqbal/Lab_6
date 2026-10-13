
import pandas as pd
import matplotlib.pyplot as plt

data = {
    "Product": ["Laptop", "Mouse", "Keyboard", "Phone", "Charger",
                "Monitor", "Headphones", "Tablet", "USB Cable", "Speaker"],
    "Category": [" electronics ", "ACCESSORIES", " electronics", "Electronics ",
                 " accessories ", "ELECTRONICS", "Accessories", " electronics ",
                 " ACCESSORIES", "Electronics"],
    "Price": ["Rs. 85,000", "Rs. 1,250", "Rs. 3,500", "Rs. 65,000",
              "Rs. 1,800", "Rs. 32,000", "Rs. 4,500", "Rs. 28,000",
              "Rs. 500", "Rs. 6,000"],
    "Stock": [10, 50, 25, 15, 40, 12, 30, 18, 100, 20]
}

df = pd.DataFrame(data)

df["Category"] = df["Category"].str.strip().str.title()

df["Price"] = df["Price"].str.replace("Rs. ", "", regex=False)
df["Price"] = df["Price"].str.replace(",", "", regex=False)
df["Price"] = pd.to_numeric(df["Price"])

df["Category_Code"] = df["Category"].astype("category").cat.codes

print("Cleaned Inventory DataFrame:")
print(df)

avg_price = df.groupby("Category")["Price"].mean()
total_stock = df.groupby("Category")["Stock"].sum()

fig, ax = plt.subplots(1, 2, figsize=(12, 5))

avg_price.plot(kind="bar", ax=ax[0], title="Average Price per Category")
ax[0].set_xlabel("Category")
ax[0].set_ylabel("Average Price (Rs.)")

total_stock.plot(kind="pie", ax=ax[1], autopct="%1.1f%%",
                 title="Share of Total Stock")
ax[1].set_ylabel("")

plt.tight_layout()
plt.savefig("inventory_plots.png")
plt.show()
print("inventory_plots.png has been saved successfully.")