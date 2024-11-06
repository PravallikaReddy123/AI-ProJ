from deepgram import DeepgramClient, SpeakOptions
import asyncio

async def text_to_speech(api_key, text, output_file_path, m="aura-arcas-en"):
    """
    Convert text to speech asynchronously using Deepgram TTS.
    
    Args:
        api_key (str): The API key for Deepgram.
        text (str): The text to convert to speech.
        output_file_path (str): The path to save the generated speech audio file.
        m (str): The model to use for TTS (default: aura-arcas-en).
    """
    try:
        print('Working... on tts ...')
        
        # Initialize Deepgram client
        client = DeepgramClient(api_key=api_key)
        
        # Define TTS options
        options = SpeakOptions(
            model=m,  # Choose the model you prefer
            encoding="linear16",
            container="wav",
        )
        
        # Make the TTS request asynchronously
        response = await client.speak.v("1").save(output_file_path, {"text": text}, options)
        
        # Confirm the file was saved
        return f"Audio saved to {output_file_path}"

    except Exception as e:
        return f"Failed to convert text to speech: {e}"


# text_to_speech('fa514b70902b8a222eadfacf4920d2e0252be990', "Hello... ", output_file)