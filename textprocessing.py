import os
import google.generativeai as genai
import json

def process_text(text):
    genai.configure(api_key=os.environ["GEMINI_API_KEY"])

    systemPrompt = """ You will be Processing text complaints, categorizing and summarizing them before sending to the aggregator 
        If complaint is a no, both category and details should be 'null'.
        You should return in the following JSON format:
        {
        "returnText":[
            {
            "complaint": "whether it is a complaint or not (yes or no)",
            "category": "category of complaint",
            "details": "details of complaint"
            }
            ]
        } 
        """

    # Create the model
    generation_config = {
    "temperature": 1,
    "top_p": 0.95,
    "top_k": 64,
    "max_output_tokens": 8192,
    "response_mime_type": "application/json",
    }

    model = genai.GenerativeModel(
    model_name="gemini-1.5-flash",
    generation_config=generation_config,
    system_instruction=systemPrompt,
    )

    response = model.generate_content(text)
    print(response.text)
    responseJSON = json.loads(response.text)["returnText"]
    print(type(response.text))
    print(type(responseJSON))
    print(responseJSON)

    return response