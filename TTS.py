
from ibm_watson import TextToSpeechV1
from ibm_watson.websocket import RecognizeCallback, AudioSource
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

# Insert API Key in place of 
# 'YOUR UNIQUE API KEY'
authenticator = IAMAuthenticator('YOUR UNIQUE API KEY')
tts = TextToSpeechV1(
    authenticator=authenticator
)

#Insert URL in place of 'API_URL' 
tts.set_service_url('API_URL')

# recognize text using IBM Text to Speech
# save TTS as mp3 file
with open('./speech.mp3', 'wb') as audio_file:
     res = tts.synthesize('Testing text to speech service', accept='audio/mp3', voice='en-US_AllisonV3Voice').get_result()
     audio_file.write(res.content) #write the content to the audio file 

print("Exporting process completed!")
