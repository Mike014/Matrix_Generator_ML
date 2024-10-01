# -*- coding: utf-8 -*-
import tkinter as tk
from tkinter import messagebox
from sklearn.linear_model import LinearRegression
import numpy as np

def generate_matrix():
    try:
        n = int(entry.get())
        if n < 1:
            raise ValueError("n must be greater than 0")
        matrix = [[(i + j) % n + 1 for i in range(n)] for j in range(n)]
        display_matrix(matrix)
        apply_ml(matrix)
    except ValueError as e:
        messagebox.showerror("Invalid input", str(e))

def display_matrix(matrix):
    result_text.delete(1.0, tk.END)
    for row in matrix:
        result_text.insert(tk.END, ' '.join(map(str, row)) + '\n')

def apply_ml(matrix):
    # Convert the matrix to a numpy array
    X = np.array(matrix)
    y = np.sum(X, axis=1)  

    # Apply Linear Regression
    model = LinearRegression()
    model.fit(X, y)
    predictions = model.predict(X)

    # Display the results
    result_text.insert(tk.END, "\nML Predictions:\n")
    result_text.insert(tk.END, ' '.join(map(str, predictions)) + '\n')

# Create the main window
root = tk.Tk()
root.title("Matrix Generator with ML")

# Create and position the widgets
tk.Label(root, text="Enter the value of n:").pack(pady=5)
entry = tk.Entry(root)
entry.pack(pady=5)

tk.Button(root, text="Generate Matrix", command=generate_matrix).pack(pady=5)

result_text = tk.Text(root, height=20, width=50)
result_text.pack(pady=5)

# Start the main Tkinter loop
root.mainloop()












































# n = 5

# expression1 = [[(i + j) % n + 1 for i in range(n)] for j in range(n)]

# print(expression1)





