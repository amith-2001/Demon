from os import path
from pydub import AudioSegment
import os
# assign files

input_file = "C:/Harshith/python projects/pythonProject/new/chainsaw/audio2.4.mp3"
os.chdir('C:/Harshith/python projects/pythonProject/converted_chainsaw')
output_file = "Chainsaw_5"

# convert mp3 file to wav file
sound = AudioSegment.from_mp3(input_file)
sound.export(output_file, format="wav")