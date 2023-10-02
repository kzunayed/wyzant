import pandas as pd
import matplotlib.pyplot as plt
from ipywidgets import widgets, interact


data = pd.read_csv('nyc_fare.csv')
data.head()
print(len(data))

# Scatterplot of Fare Amount vs Tip Amount
plt.scatter(data['fare_amount'], data['tip_amount'], alpha=0.5)
plt.xlabel('Fare Amount')
plt.xlim(0, 300)
plt.ylabel('Tip Amount')
plt.title('Scatter Plot of Fare Amount vs. Tip Amount')
plt.grid(True)
plt.show()


# histogram for fare_amount
plt.hist(data['fare_amount'], bins=30, range=(0, 300), edgecolor='black')
plt.xlabel('Fare Amount')
plt.ylabel('Frequency')
plt.title('Histogram of Fare Amounts')
plt.grid(True)
plt.show()


# Function to filter data based on the threshold and print the length
def filter_and_print(threshold=100.00):
    high_tip_data = data[data['tip_amount'] > threshold]
    print(f"Number of trips with tip amount > ${threshold:.2f}: {len(high_tip_data)}")

# Create an interactive slider for the threshold
interact(filter_and_print, threshold=(0.00, 300.00, 10.00))
