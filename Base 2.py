import difflib
import smtplib
from email.mime.text import MIMEText

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

# User interface to input symptoms
def user_interface():
    print("Welcome to the Symptom Evaluator!")
    print("Please enter your symptoms separated by commas:")
    user_input = input("> ").lower().split(",")
    # Clean up user input
    user_symptoms = [symptom.strip() for symptom in user_input]
    
    # Evaluate symptoms and determine the disease
    disease_matches = evaluate_symptoms(user_symptoms)
    
    # Display the results
    print("\nResults:")
    result_text = "Results:\n"
    for disease, match_ratio in disease_matches:
        result_text += f"{disease}: {match_ratio * 100}% match\n"

    # Register and send the report via email
    register_and_send_email(result_text)

def register_and_send_email(report_text):
    # Gmail account credentials
    sender_email = "your-email@gmail.com"
    sender_password = "your-password"

    # Receiver email address
    receiver_email = input("Please enter your Gmail address to receive the report: ")
    
    # Compose the email message
    message = MIMEText(report_text)
    message["Subject"] = "Symptom Evaluation Report"
    message["From"] = sender_email
    message["To"] = receiver_email
    
    # Connect to the Gmail SMTP server and send the email
    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(sender_email, sender_password)
        server.send_message(message)
        print(f"Report sent successfully to {receiver_email}!")

# Run the user interface
user_interface()
