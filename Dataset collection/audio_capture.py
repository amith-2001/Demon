import sounddevice
from scipy.io.wavfile import write

fs = 44100
seconds = 10

aud = sounddevice.rec(int(seconds*fs),samplerate=fs,channels=1)
sounddevice.wait()
write('audio_out.wav',fs,aud)