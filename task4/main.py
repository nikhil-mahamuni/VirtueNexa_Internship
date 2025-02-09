import json
import os
import matplotlib.pyplot as plt
import pandas as pd
import tkinter as tk
from tkinter import messagebox, ttk
from datetime import datetime

# File to store workout data
DATA_FILE = "workout_data.json"

# Load existing data
def load_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as file:
            return json.load(file)
    return []

# Save workout data
def save_data(data):
    with open(DATA_FILE, "w") as file:
        json.dump(data, file, indent=4)

# Add workout entry
def add_workout():
    exercise = exercise_var.get()
    sets = sets_var.get()
    reps = reps_var.get()
    weight = weight_var.get()

    if not exercise or not sets or not reps or not weight:
        messagebox.showerror("Error", "All fields are required!")
        return

    new_entry = {
        "date": datetime.now().strftime("%Y-%m-%d"),
        "exercise": exercise,
        "sets": int(sets),
        "reps": int(reps),
        "weight": float(weight)
    }

    data = load_data()
    data.append(new_entry)
    save_data(data)
    messagebox.showinfo("Success", "Workout added successfully!")
    clear_fields()

# Clear input fields
def clear_fields():
    exercise_var.set("")
    sets_var.set("")
    reps_var.set("")
    weight_var.set("")

# Show progress graph
def show_progress():
    data = load_data()
    if not data:
        messagebox.showinfo("Info", "No workout data available!")
        return
    
    df = pd.DataFrame(data)
    
    plt.figure(figsize=(10, 5))
    for exercise in df["exercise"].unique():
        ex_data = df[df["exercise"] == exercise]
        plt.plot(ex_data["date"], ex_data["weight"], marker='o', label=exercise)

    plt.xlabel("Date")
    plt.ylabel("Weight Lifted (kg)")
    plt.title("Workout Progress Over Time")
    plt.xticks(rotation=45)
    plt.legend()
    plt.grid()
    plt.show()

# Generate suggestions
def generate_suggestions():
    data = load_data()
    if not data:
        messagebox.showinfo("Info", "No workout data available!")
        return

    df = pd.DataFrame(data)
    suggestions = ""

    for exercise in df["exercise"].unique():
        ex_data = df[df["exercise"] == exercise]
        if len(ex_data) > 1:
            latest = ex_data.iloc[-1]
            previous = ex_data.iloc[-2]
            
            if latest["weight"] > previous["weight"]:
                suggestions += f"{exercise}: Keep increasing weight!\n"
            else:
                suggestions += f"{exercise}: Try increasing weight gradually.\n"
        else:
            suggestions += f"{exercise}: Keep up the good work!\n"

    messagebox.showinfo("Workout Suggestions", suggestions if suggestions else "No suggestions yet!")

# Create UI
root = tk.Tk()
root.title("Workout Tracker")

# Labels and Inputs
tk.Label(root, text="Exercise:").grid(row=0, column=0, padx=10, pady=5)
exercise_var = tk.StringVar()
tk.Entry(root, textvariable=exercise_var).grid(row=0, column=1, padx=10, pady=5)

tk.Label(root, text="Sets:").grid(row=1, column=0, padx=10, pady=5)
sets_var = tk.StringVar()
tk.Entry(root, textvariable=sets_var).grid(row=1, column=1, padx=10, pady=5)

tk.Label(root, text="Reps:").grid(row=2, column=0, padx=10, pady=5)
reps_var = tk.StringVar()
tk.Entry(root, textvariable=reps_var).grid(row=2, column=1, padx=10, pady=5)

tk.Label(root, text="Weight (kg):").grid(row=3, column=0, padx=10, pady=5)
weight_var = tk.StringVar()
tk.Entry(root, textvariable=weight_var).grid(row=3, column=1, padx=10, pady=5)

# Buttons
tk.Button(root, text="Add Workout", command=add_workout).grid(row=4, column=0, columnspan=2, pady=10)
tk.Button(root, text="Show Progress", command=show_progress).grid(row=5, column=0, columnspan=2, pady=5)
tk.Button(root, text="Get Suggestions", command=generate_suggestions).grid(row=6, column=0, columnspan=2, pady=5)

# Run the application
root.mainloop()
