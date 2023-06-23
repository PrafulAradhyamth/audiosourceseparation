import numpy as np 
import librosa
import matplotlib.pyplot as plt

def audio_2_stft(path):
    y, sr = librosa.load(path)
    S = np.abs(librosa.stft(y))


    import matplotlib.pyplot as plt
    fig, ax = plt.subplots()
    img = librosa.display.specshow(librosa.amplitude_to_db(S,ref=np.max),y_axis='log', x_axis='time', ax=ax)
    ax.set_title('Power spectrogram')
    fig.colorbar(img, ax=ax, format="%+2.0f dB")
    
    return S

path = '/speech/db/mul/audio/music/tency2/part1/maneskin_i-wanna-be-your-slave_65162/multi/bass.wav'

S = audio_2_stft(path)