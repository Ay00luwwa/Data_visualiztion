import pandas as pd
import matplotlib.pyplot as plt
import json

# Load data
with open('jsondata.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

# Extract topics
pestles = [item['pestle'] for item in data]

# Convert to pandas series to easily count occurrences
pestle_series = pd.Series(pestles)

# Count occurrences of each topic
pestle_counts = pestle_series.value_counts()

# Plotting
pestle_counts.plot(kind='bar')
plt.xlabel('Topic')
plt.ylabel('Count')
plt.title('Count of Each Pestle')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
