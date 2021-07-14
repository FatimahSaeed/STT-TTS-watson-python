from ibm_watson import TextToSpeechV1
from ibm_watson.websocket import RecognizeCallback, AudioSource
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

# Insert API Key in place of 
# 'YOUR UNIQUE API KEY'
authenticator = IAMAuthenticator('XqzbDvKtATALn-aCP4JsFSqmK90yhid-Yp45KQUWR3Il')
tts = TextToSpeechV1(
    authenticator=authenticator
)

#Insert URL in place of 'API_URL' 
tts.set_service_url('https://api.us-south.text-to-speech.watson.cloud.ibm.com/instances/3c98b92e-eed0-4e5c-9f7b-1e13bd38e592')

with open('./speech.mp3', 'wb') as audio_file:
     res = tts.synthesize('Testing text to speech service', accept='audio/mp3', voice='en-US_AllisonV3Voice').get_result()
     audio_file.write(res.content) #write the content to the audio file 

print("Exporting process completed!")