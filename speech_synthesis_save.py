import os
# import io
# from pydub import AudioSegment
# from pydub.playback import play
import azure.cognitiveservices.speech as speechsdk

# def play_audio_from_bytes(audio_data, format='wave'):
#     audio_data_io=io.BytesIO(audio_data)
#     audio_segment=AudioSegment.from_file(audio_data_io,format=format)
#     play(audio_segment)

# This example requires environment variables named "SPEECH_KEY" and "SPEECH_REGION"
speech_config = speechsdk.SpeechConfig(subscription=os.environ.get('SPEECH_KEY'), region=os.environ.get('SPEECH_REGION'))
audio_config = speechsdk.audio.AudioOutputConfig(filename="Test.wav")

# audio_config = speechsdk.audio.AudioOutputConfig(use_default_speaker=True)
# audio_config = speechsdk.audio.AudioOutputConfig(filename="path/to/write/file.wav")
# speech_synthesizer = speechsdk.SpeechSynthesizer(speech_config=speech_config, audio_config=audio_config)
# speech_synthesis_result = speech_synthesizer.speak_text_async("I'm excited to try text to speech").get()


# The neural multilingual voice can speak different languages based on the input text.
speech_config.speech_synthesis_voice_name='zh-TW-HsiaoChenNeural'

speech_synthesizer = speechsdk.SpeechSynthesizer(speech_config=speech_config, audio_config=audio_config)

# Get text from the console and synthesize to the default speaker.
print("Enter some text that you want to speak >")
text = input()

speech_synthesis_result = speech_synthesizer.speak_text_async(text).get()

if speech_synthesis_result.reason == speechsdk.ResultReason.SynthesizingAudioCompleted:
    # audio_data=speech_synthesis_result.audio_data
    # play_audio_from_bytes(audio_data)
    # with open('output.wav','wb') as file:
    #     file.write(audio_data)
    print("Speech synthesized for text [{}]".format(text))
elif speech_synthesis_result.reason == speechsdk.ResultReason.Canceled:
    cancellation_details = speech_synthesis_result.cancellation_details
    print("Speech synthesis canceled: {}".format(cancellation_details.reason))
    if cancellation_details.reason == speechsdk.CancellationReason.Error:
        if cancellation_details.error_details:
            print("Error details: {}".format(cancellation_details.error_details))
            print("Did you set the speech resource key and region values?")