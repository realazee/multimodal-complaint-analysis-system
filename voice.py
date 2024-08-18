# Import the Speech-to-Text client library
from google.cloud import speech


def audio_to_speech(audio):
    # Instantiates a client
    client = speech.SpeechClient()

    # The content of the audio file to transcribe
    audio_content = audio

    # transcribe speech
    audio = speech.RecognitionAudio(content=audio_content)

    config = speech.RecognitionConfig(
        encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
        sample_rate_hertz=24000,
        language_code="en-US",
        model="default",
        audio_channel_count=1,
        enable_word_confidence=True,
        enable_word_time_offsets=True,
    )

    # Detects speech in the audio file
    operation = client.long_running_recognize(config=config, audio=audio)

    print("Waiting for operation to complete...")
    response = operation.result(timeout=90)

    for result in response.results:
        print("Transcript: {}".format(result.alternatives[0].transcript))
    return response