import difflib
import tkinter as tk
from tkinter import messagebox

# Define the symptoms
symptoms = [
    "Fever",
    "Cough",
    "Headache",
    "Fatigue",
    "Sore throat",
    "Shortness of breath",
    "Muscle or body aches",
    "Loss of taste or smell",
    "Nausea or vomiting",
    "Diarrhea"
]

# Function to evaluate symptoms and determine the condition
def evaluate_symptoms():
    selected_symptoms = [symptom.get() for symptom in symptom_vars.values()]
    selected_symptoms = [s for s in selected_symptoms if s != '']
    
    match_ratio = difflib.SequenceMatcher(None, selected_symptoms, symptoms).ratio()
    
    if match_ratio > 0.5:
        messagebox.showinfo("Evaluation Result", "You may have a condition related to the symptoms.")
    else:
        messagebox.showinfo("Evaluation Result", "You are fine.")

# Create the GUI window
window = tk.Tk()
window.title("Symptom Evaluator")

# Create and pack the symptom selection label
label_symptoms = tk.Label(window, text="Select your symptoms:")
label_symptoms.pack()

# Create a frame to hold the symptom selection checkboxes
symptoms_frame = tk.Frame(window)
symptoms_frame.pack()

# Create variables for symptom selection checkboxes
symptom_vars = {}
for symptom in symptoms:
    var = tk.StringVar()
    symptom_vars[symptom] = var
    checkbox = tk.Checkbutton(symptoms_frame, text=symptom, variable=var, onvalue=symptom, offvalue='')
    checkbox.pack(anchor='w')

# Create and pack the Evaluate button
button = tk.Button(window, text="Evaluate Symptoms", command=evaluate_symptoms)
button.pack()

# Run the GUI main loop
window.mainloop()
