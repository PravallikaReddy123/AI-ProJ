

from deepgram import DeepgramClient, PrerecordedOptions, FileSource
import json
import logging

def transcribe_audio(api_key, audio_file_path):
    """
    Transcribe an audio file using Deepgram.
    
    Args:
    api_key (str): The API key for the Deepgram service.
    audio_file_path (str): The path to the audio file to transcribe.

    Returns:
    str: The transcribed text.
    """
    print('working... on stt')
    try:
        # Initialize the Deepgram client
        deepgram = DeepgramClient(api_key)

        # Read the audio file
        with open(audio_file_path, "rb") as file:
            buffer_data = file.read()

        # Prepare payload and options
        payload: FileSource = {
            "buffer": buffer_data,
        }
        options = PrerecordedOptions(
            model="nova-2",
            smart_format=True,
        )

        # Make the request to Deepgram
        response = deepgram.listen.rest.v("1").transcribe_file(payload, options)
        response_json = response.to_json()
        data = json.loads(response_json)

        # Extract the transcript from the response
        transcript = data['results']['channels'][0]['alternatives'][0]['transcript']

        return transcript

    except Exception as e:
        logging.error(f"Failed to transcribe audio: {e}")
        raise Exception("Error in transcribing audio")
# print(transcribe_audio('ddbf32fde2fa328ab0f486c251de09ce1492be6d',r'C:\Users\Sridhar\_EMPTY FOLDERS\ProJ_B3.O\uploads\recording.wav'))