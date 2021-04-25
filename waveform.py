import matplotlib.pyplot as plt
from wave import open
import numpy as np

song_name = "test.wav"
raw = open (song_name, "r")
raw = raw.readframes(-1)
wav = np.frombuffer(raw, dtype=int)

plt.figure(figsize=(15, 3))
plt.title("Waveform")
plt.plot(wav, color="red")
plt.ylabel("Amplitude")
plt.show()
