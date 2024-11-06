from flask import Flask, render_template, request, jsonify
# from pipeline import run_pipeline
from flask_cors import CORS
import os
import asyncio

from components.transcription import transcribe_audio
from components.respo_gen import generate_response___
from components.tts import text_to_speech

chat_history_ = [
    {"role": "system", "content": """ You are an English Communication voice chatbot called Peter. 
        You have to reply very short(just in two or three sentences) and sweet. """},
    {"role":"assistant", "content":"Hello, I am Peter. I'll help you learn English. What shall we start with? Is there any topic you'd like to talk or learn about?"}
]

app = Flask(__name__)
CORS(app)

UPLOAD_FOLDER = 'uploads'
OUTPUT_FILE = 'static/output.wav'

if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

@app.route('/chat')
def index():
    return render_template('index.html')

@app.route('/chat/upload', methods=['POST'])
async def upload_file():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400

    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400

    filepath = os.path.join(UPLOAD_FOLDER, 'recording.wav')
    file.save(filepath)

    # Transcribe the audio asynchronously
    user_input = await asyncio.to_thread(transcribe_audio, 'ddbf32fde2fa328ab0f486c251de09ce1492be6d', filepath)

    if not user_input.strip():  # Check if transcription is empty
        return jsonify({'error': 'No voice detected'}), 400

    print(user_input)
    chat_history_.append({"role": "user", "content": user_input})


    response_text = await asyncio.to_thread(generate_response___, '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', chat_history_)
    print(response_text)


    output_file = os.path.join('static', 'output.wav')
    await text_to_speech('fa514b70902b8a222eadfacf4920d2e0252be990', response_text, output_file)

    chat_history_.append({"role": "assistant", "content": response_text})

    # Return the transcription and the audio URL
    return jsonify({
        'message': user_input,
        'response': response_text,
        'audio_url': f'/static/output.wav'
    }), 200

if __name__ == '__main__':
    app.run(debug=True)
