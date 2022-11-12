from pydub import AudioSegment 
from pydub.utils import make_chunks 
import os
myaudio = AudioSegment.from_file("C:/Harshith/python projects/pythonProject/converted/Forest_13.wav")
chunk_length_ms = 180000 # pydub calculates in millisec
chunks = make_chunks(myaudio,chunk_length_ms) #Make chunks of one sec 
for i, chunk in enumerate(chunks): 
    os.chdir('C:/Harshith/python projects/pythonProject/background_split')
    chunk_name = "{0}.wav".format(i+469)
    print ("exporting", chunk_name) 
    chunk.export(chunk_name, format="wav") 
