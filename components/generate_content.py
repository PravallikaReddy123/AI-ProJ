import os
import google.generativeai as genai
from PIL import Image

def process_images(api_key, model_name, images_folder, prompt):
    genai.configure(api_key=api_key)


    multimodal_model = genai.GenerativeModel(model_name)


    image_files = images_folder
    images = [Image.open(image_file) for image_file in image_files]
    contents = images + [prompt]

    responses = multimodal_model.generate_content(contents, stream=False)


    response_texts = [response.text for response in responses]
    return response_texts
