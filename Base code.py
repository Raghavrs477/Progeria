# Import required libraries
import difflib

# Dictionary of symptoms for a specific disease
symptoms = {
    "Disease A": ["Hairfall", "Feeling Sick", "Illness","Headache","Skin Probelm","skin",
                  "tiredness","Memory Loss"]
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
    for disease, match_ratio in disease_matches:
            print(f"{disease}: {match_ratio * 100}% match")
            print("please consult a doctor")
      

# Run the user interface
user_interface()

