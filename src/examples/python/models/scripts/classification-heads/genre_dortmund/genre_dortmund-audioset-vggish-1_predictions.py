from essentia.standard import MonoLoader, TensorflowPredictVGGish, TensorflowPredict2D

audio = MonoLoader(filename="audio.wav", sampleRate=16000)()
embedding_model = TensorflowPredictVGGish(graphFilename="audioset-vggish-3.pb", output="model/vggish/embeddings")
embeddings = embedding_model(audio)

model = TensorflowPredict2D(graphFilename="genre_dortmund-audioset-vggish-1.pb", output="model/Softmax")
predictions = model(embeddings)
