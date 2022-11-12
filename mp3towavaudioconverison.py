import os
from pydub import AudioSegment

path1 = "C:/Users/harsh/OneDrive/Desktop/forest  monitoring dataset/mp3 files/Background/Animals"
path2 = "C:/Users/harsh/OneDrive/Desktop/forest  monitoring dataset/mp3 files/Background/Animals"
path3 = "C:/Users/harsh/OneDrive/Desktop/forest  monitoring dataset/mp3 files/Background/Animals"
path4 = "C:/Users/harsh/OneDrive/Desktop/forest  monitoring dataset/mp3 files/Background/Animals"
path5 = "C:/Users/harsh/OneDrive/Desktop/forest  monitoring dataset/mp3 files/Background/Animals"
path6 = "C:/Users/harsh/OneDrive/Desktop/forest  monitoring dataset/mp3 files/Background/Animals"
path7 = "C:/Users/harsh/OneDrive/Desktop/forest  monitoring dataset/mp3 files/Background/Animals"
path8 = "C:/Users/harsh/OneDrive/Desktop/forest  monitoring dataset/mp3 files/Background/Animals"
output_path = "output"

path = [path2,path3,path4,path5,path6,path7,path8]
for i in path:
    os.chdir(i)
    files = os.listdir()
    for input_file in files:
        try:
            print(input_file)
            sound = AudioSegment.from_mp3(input_file)
            sound.export(i+'/wav/'+input_file[:-4]+'.wav', format="wav")
        except:
            pass

