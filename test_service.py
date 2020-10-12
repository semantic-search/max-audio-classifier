from classification_service import predict
import requests
import os

# NOTE : works with only wav file

audio_url = "https://www2.cs.uic.edu/~i101/SoundFiles/BabyElephantWalk60.wav"
r = requests.get(audio_url, allow_redirects=True)

print("file download done")

file_name = '/workspace/audio_test.wav'
open(file_name, 'wb').write(r.content)

audio_results = predict(file_name)
print("results", audio_results)
