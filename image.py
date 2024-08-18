from google.cloud import vision
import io

#gets image and detects text in image
def text_in_image(image):
    client = vision.ImageAnnotatorClient()

    image_path = image

    with open(image_path, "rb") as image_file:
        content = image_file.read()
        
    image = vision.Image(content=content)

    response = client.text_detection(image=image)
    texts = response.text_annotations

    print('Detected text:')
    for text in texts:
        print(text.description)

    if response.error.message:
        raise Exception(f'{response.error.message}')
    
    return