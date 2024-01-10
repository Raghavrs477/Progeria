import difflib
import smtplib
from email.mime.text import MIMEText
import tkinter as tk
from tkinter import messagebox

# Dictionary of symptoms for a specific disease
symptoms = {
    "Disease A": ["symptom1", "symptom2", "symptom3"],
    "Disease B": ["symptom4", "symptom5", "symptom6"],
    # Add more diseases and their corresponding symptoms
}

# Function to evaluate symptoms and determine the disease
def evaluate_symptoms(user_symptoms):
    matches = {}

    # Loop through the diseases and symptoms
    for disease, symptom_list in symptoms.items():
        # Compare user symptoms with disease symptoms using sequence matcher
        match_ratio = difflib.SequenceMatcher(None, user_symptoms, symptom_list).ratio()
        matches[disease] = match_ratio

    # Sort the dictionary based on the match ratio
    sorted_matches = sorted(matches.items(), key=lambda x: x[1], reverse=True)
    return sorted_matches

# Function to handle button click and evaluate symptoms
def evaluate_symptoms_click():
    user_input = entry.get().lower().split(",")
    # Clean up user input
    user_symptoms = [symptom.strip() for symptom in user_input]

    # Evaluate symptoms and determine the disease
    disease_matches = evaluate_symptoms(user_symptoms)

    # Prepare result text
    result_text = "Results:\n"
    for disease, match_ratio in disease_matches:
        result_text += f"{disease}: {match_ratio * 100}% match\n"

    # Show result in message box
    messagebox.showinfo("Evaluation Result", result_text)

    # Register and send the report via email
    register_and_send_email(result_text)

# Function to register and send email
def register_and_send_email(report_text):
    # Gmail account credentials
    sender_email = "your-email@gmail.com"
    sender_password = "your-password"

    # Receiver email address
    receiver_email = entry_email.get()

    # Compose the email message
    message = MIMEText(report_text)
    message["Subject"] = "Symptom Evaluation Report"
    message["From"] = sender_email
    message["To"] = receiver_email

    # Connect to the Gmail SMTP server and send the email
    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(sender_email, sender_password)
        server.send_message(message)
        messagebox.showinfo("Email Sent", f"Report sent successfully to {receiver_email}!")

# Create the GUI window
window = tk.Tk()
window.title("Symptom Evaluator")

# Create and pack the symptom entry label and text entry field
label = tk.Label(window, text="Enter your symptoms separated by commas:")
label.pack()

entry = tk.Entry(window, width=50)
entry.pack()

# Create and pack the email entry label and text entry field
label_email = tk.Label(window, text="Enter your email address:")
label_email.pack()

entry_email = tk.Entry(window, width=50)
entry_email.pack()

# Create and pack the Evaluate button
button = tk.Button(window, text="Evaluate Symptoms", command=evaluate_symptoms_click)
button.pack()

# Run the GUI main loop
window.mainloop()
