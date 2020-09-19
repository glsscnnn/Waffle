def synthesize_text(text, file_name):

    from google.cloud import texttospeech

    client = texttospeech.TextToSpeechClient()

    input_text = texttospeech.SynthesisInput(text=text)

    voice = texttospeech.VoiceSelectionParams(
        language_code="en-US",
        name="en-US-Wavenet-D",
    )

    audio_config = texttospeech.AudioConfig(
        audio_encoding=texttospeech.AudioEncoding.MP3
    )

    response = client.synthesize_speech(
        request={"input": input_text, "voice": voice, "audio_config": audio_config}
    )

    with open(file_name, "wb") as out:
        out.write(response.audio_content)
        print('Audio content written to file "{0}"'.format(file_name))

def main():
    import sys

    with open(sys.argv[1], "r") as f:
        text = f.read()
        synthesize_text(text, sys.argv[2])

if __name__ == "__main__":
    main()


