import numpy as np 
import librosa
import matplotlib.pyplot as plt



def printer(text):
    print(text)
    return


def voice2spectrogram(path):
    y, sr = librosa.load(path)
    S = np.abs(librosa.stft(y))
    fig, ax = plt.subplots()
    img = librosa.display.specshow(librosa.amplitude_to_db(S,ref=np.max),y_axis='log', x_axis='time', ax=ax)
    ax.set_title('Power spectrogram')
    fig.colorbar(img, ax=ax, format="%+2.0f dB")
    plt.imshow()
    return