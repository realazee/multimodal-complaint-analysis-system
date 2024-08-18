
import vertexai
from vertexai.generative_models import GenerativeModel, Part

# TODO(developer): Update and un-comment below lines
# project_id = "PROJECT_ID"

vertexai.init(project=project_id, location="us-central1")

model = GenerativeModel("gemini-1.5-flash-001")

prompt = """
You are a customer support agent that watches videos and detects any complaints in it and categorizes the complaints.
Analyzes video content, detecting and categorizing complaints
"""

video_file_uri = "gs://cloud-samples-data/generative-ai/video/pixel8.mp4"
video_file = Part.from_uri(video_file_uri, mime_type="video/mp4")

contents = [video_file, prompt]

response = model.generate_content(contents)
print(response.text)