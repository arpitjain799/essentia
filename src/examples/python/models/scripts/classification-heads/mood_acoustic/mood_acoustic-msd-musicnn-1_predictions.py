from essentia.standard import MonoLoader, TensorflowPredictMusiCNN, TensorflowPredict2D

audio = MonoLoader(filename="audio.wav", sampleRate=16000)()
embedding_model = TensorflowPredictMusiCNN(graphFilename="msd-musicnn-1.pb", output="model/dense/BiasAdd")
embeddings = embedding_model(audio)

model = TensorflowPredict2D(graphFilename="mood_acoustic-msd-musicnn-1.pb", output="model/Softmax")
predictions = model(embeddings)
