import pandas as pd
import matplotlib.pyplot as plt

# Read JSON data
with open('data.json', 'r') as file:
    data = pd.read_json(file)

# Pie Chart
plt.figure(figsize=(8, 6))
plt.pie(data['counts'], labels=data['fruits'], autopct='%1.1f%%', startangle=90)
plt.title("Fruits Distribution")
plt.axis('equal')
plt.show()

# Bar Chart 
plt.figure(figsize=(8, 6))
plt.bar(data['fruits'], data['counts'], color='skyblue')
plt.title('Fruits Counts')
plt.xlabel('Fruits')
plt.ylabel('Counts')
plt.show()

# Histogram

plt.figure(figsize=(8, 6))
plt.hist(data['sales'], bins=5, color='green', edgecolor='black')
plt.title('Sales Distribution')
plt.xlabel('Sales')
plt.ylabel('Frequency')
plt.show()
