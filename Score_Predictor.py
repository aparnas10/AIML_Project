from sklearn.linear_model import LinearRegression

import numpy as np
# Sample data set
x = np.array([
    [1, 40, 50],
    [2, 50, 60],
    [3, 55, 65],
    [4, 60, 70],
    [5, 65, 75],
    [6, 70, 80],
    [7, 75, 85],
    [8, 80, 90],
    [9, 85, 95],
    [10, 90, 100]
])
# Target Score
y =np.array([50, 55, 60, 70, 75, 80, 85, 45, 90, 95])

# Creating model
model = LinearRegression()
# Fitting model
model.fit(x, y)

try:
    # Taking user input
    hours = float(input("Enter hours studied (0 to 10): "))
    prev_score = float(input("Enter previous score (0 to 100): "))
    attendance = float(input("Enter attendance percentage (0 to 100): "))
    prediction = model.predict([[hours,prev_score,attendance]])
    # Printing result i.e. predicted score
    print("Predicted score: ",prediction)
except ValueError:
    print('Please enter valid numbers.')