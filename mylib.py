import numpy as np 
import librosa
import matplotlib.pyplot as plt
from scipy import signal
import audiofile
import librosa


def printer(path):
    y, sr = librosa.load(path)
    print(path)
    return y


def voice2spectrogram(path):
    y, sr = librosa.load(path)
    S = np.abs(librosa.stft(y))
    fig, ax = plt.subplots()
    img = librosa.display.specshow(librosa.amplitude_to_db(S,ref=np.max),y_axis='log', x_axis='time', ax=ax)
    ax.set_title('Power spectrogram')
    fig.colorbar(img, ax=ax, format="%+2.0f dB")
    plt.show()
    return img


path = '/speech/db/mul/audio/music/tency2/part1/maneskin_i-wanna-be-your-slave_65162/multi/bass.wav'
img = voice2spectrogram(path)

plt.savefig('test.png')
