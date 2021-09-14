import sounddevice as sd
from scipy.io.wavfile import write

fs = 44100  # Sample rate
seconds = 5  # Duration of recording

sd.default.device = 11,18

myrecording = sd.rec(int(seconds * fs), samplerate=fs, channels=1)
sd.wait()  # Wait until recording is finished
write('output.wav', fs, myrecording)  # Save as WAV file 