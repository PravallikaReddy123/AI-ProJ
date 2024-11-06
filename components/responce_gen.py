import logging
import re  # Importing regex for name removal
from groq import Groq  # Assuming you have a Groq client available

def generate_response(api_key, chat_history):
    """
    Generate a group discussion response using Groq.

    Args:
    api_key (str): The API key for the Groq service.
    chat_history (list): The chat history as a list of messages.

    Returns:
    dict: A dictionary containing generated responses for each participant (Ben, Tony, Steeve).
    """
    print('Working on response generation...')
    
    try:
        # Initialize the Groq client
        client = Groq(api_key=api_key)

        # Generate response using Groq's completion API
        response = client.chat.completions.create(
            model="llama3-8b-8192",  # Replace with your Groq model identifier if needed
            messages=chat_history
        )

        # Extract responses
        raw_response = response.choices[0].message.content
        # print("Raw response:", raw_response)  # Print the raw response for debugging

        # Split the response into lines
        responses = [line.strip() for line in raw_response.split('\n') if line.strip()]

        # Remove names and structure responses into a dictionary
        response_dict = {}
        
        for line in responses:
            if line.startswith("Ben:"):
                response_dict["ben"] = line.replace("Ben: ", "").strip()
            elif line.startswith("Tony:"):
                response_dict["tony"] = line.replace("Tony: ", "").strip()
            elif line.startswith("Steeve:"):
                response_dict["steeve"] = line.replace("Steeve: ", "").strip()
        
        # If any participant's response is missing, assign an empty string
        response_dict.setdefault("ben", "")
        response_dict.setdefault("tony", "")
        response_dict.setdefault("steeve", "")

        # Commenting out the print statements for clean output
        # print("Ben's response:", response_dict["ben"])
        # print("Tony's response:", response_dict["tony"])
        # print("Steeve's response:", response_dict["steeve"])

        return response_dict

    except Exception as e:
        logging.error(f"Failed to generate response: {e}")
        return {"error": "Error in generating response"}
