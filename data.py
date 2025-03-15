import json
import matplotlib.pyplot as plt
import numpy as np

#code for displaying the fruits data visually

with open('fruits.json', 'r', encoding='utf-8') as file:
    data = json.load(file)
    fruits = data["fruits"]


indices = np.arange(len(fruits))


fig, ax = plt.subplots(figsize=(10, 8))
ax.barh(indices, np.ones(len(fruits)), color='skyblue')
ax.set_yticks(indices)
ax.set_yticklabels(fruits)
ax.invert_yaxis() 
ax.set_xlabel("Count")
ax.set_title("Fruit List Visualization")

plt.show()
