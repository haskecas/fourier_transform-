import math
import matplotlib.pyplot as plt
from ft import *

class sinwave:
    def __init__(self, wavef, waver): #waver syands for wave range tuple with 2 miliseconds where first one is ms wave starts at and last one ms it end at
        self.wavef = wavef
        self.waver = waver

sample_rate = 44100
dur = 2
waves = [sinwave(440, (0, 1000)),
         sinwave(220, (200, 500)),
         sinwave(2000, (400, 1800)),
         sinwave(10, (1, 1000))]
wave = []


for i in range(int(dur*sample_rate)):
    piecetoadd=0
    t = i/sample_rate
    curr_int_time = int(t * 1000)
    for w in waves:
        if w.waver[0] <= curr_int_time and w.waver[1] >= curr_int_time:
            piecetoadd+=math.sin(2*math.pi*w.wavef*t)
    #wave.append(math.cos(2*math.pi*440*t))
    wave.append(piecetoadd)
res = fourier_transform(wave, sample_rate)
for i in res.keys():
    if res[i][0]:
        print(f"{i} Hz Is present: {res[i][0]} (sin value: {res[i][1]} cos value: {res[i][2]})")
#print(wave)
#plt.plot(wave, color='green')
#plt.show()
