from essentia.standard import MonoLoader, TempoCNN

audio = MonoLoader(filename="audio.wav", sampleRate=11025)()
model = TempoCNN(graphFilename="deepsquare-k16-3.pb")
global_tempo, local_tempo, local_tempo_probabilities = model(audio)
