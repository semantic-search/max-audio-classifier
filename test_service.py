from classification_service import predict

file_path = 'samples/birds1.wav'

audio_results = predict(file_path)
print("results", audio_results)