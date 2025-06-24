# pie_chart.py

# Import required libraries
import matplotlib.pyplot as plt
import numpy as np

# Data for the pie chart
y = np.array([35, 25, 20, 10])
datas = ["Mobile", "TV", "Dress", "Doll"]
mexplode = [0.2, 0, 0, 0.6]  # Emphasize Mobile and Doll

# Create the pie chart
plt.pie(y, labels=datas, explode=mexplode, shadow=True)

# Display the chart
plt.show()
