
import vertexai
from vertexai.generative_models import GenerativeModel, Part


def video_to_text(video):
    vertexai.init(project="headstarterweek4", location="us-central1")

    model = GenerativeModel("gemini-1.5-flash-001")

    prompt = """
    You are a customer support agent that watches videos and detects any complaints in it and categorizes the complaints.
    Analyzes video content, detecting and categorizing complaints
    """

    # video_file = Part.from_uri(video, mime_type="video/mp4")

    contents = [video, prompt]

    response = model.generate_content(contents)
    print(response.text)

    return response