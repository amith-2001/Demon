import os
import matplotlib.pyplot as plt

#for loading and visualizing audio files
import librosa
import librosa.display

#to play audio
# import IPython.display as ipd

path1 = "C:/Users/harsh/OneDrive/Desktop/forest  monitoring dataset/wav files/background/birds"
path2 = "C:/Users/harsh/OneDrive/Desktop/forest  monitoring dataset/wav files/background/animals"
path3 = "C:/Users/harsh/OneDrive/Desktop/forest  monitoring dataset/wav files/background/chainsaw"
path4 = "C:/Users/harsh/OneDrive/Desktop/forest  monitoring dataset/wav files/background/forest"
path5 = "C:/Users/harsh/OneDrive/Desktop/forest  monitoring dataset/wav files/background/insects"
path6 = "C:/Users/harsh/OneDrive/Desktop/forest  monitoring dataset/wav files/background/rain"
path7 = "C:/Users/harsh/OneDrive/Desktop/forest  monitoring dataset/wav files/background/river"
path8 = "C:/Users/harsh/OneDrive/Desktop/forest  monitoring dataset/wav files/background/wind"
# output_path = "C:/Users/harsh/OneDrive/Desktop/forest  monitoring dataset/wav files"

path = [path1,path2,path3,path4,path5,path6,path7,path8]



for i in path:
    os.chdir(i)
    files = os.listdir()

    for input_file in files:
        x, sr = librosa.load(input_file, sr=44100)

        print(type(x), type(sr))
        print(x.shape, sr)


        X = librosa.stft(x)
        Xdb = librosa.amplitude_to_db(abs(X))
        plt.figure(figsize=(14, 5))
        librosa.display.specshow(Xdb, sr=sr, x_axis='time', y_axis='hz')
        plt.colorbar()
        # plt.show()
        plt.savefig(i+'/spectrogram/'+input_file[:-4]+'.png')