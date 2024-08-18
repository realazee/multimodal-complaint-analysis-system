from google.cloud import vision
import io
import os

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "./googleserviceaccount.json"

#gets image and detects text in image
def text_in_image(image):
    client = vision.ImageAnnotatorClient()

    content = image.read()
        
    image = vision.Image(content=content)
    response = client.text_detection(image=image)
    texts = response.text_annotations
    print(type(texts.textAnnotations))
    print(texts.textAnnotations)

    
    # full_text = " ".join([text.description for text in texts])

    # # Handle errors
    # if response.error.message:
    #     raise Exception(f'{response.error.message}')
    
    return texts.textAnnotations
