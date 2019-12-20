import matplotlib.pyplot as plt
import numpy as np
from scipy.signal import find_peaks
archivo = open("ecg.csv")
raw_data=archivo.readlines()
for i in range(len(raw_data)):
    raw_data[i]=raw_data[i].strip().split(",")
for i in range (len (raw_data[0])):
    raw_data[0][i]=int(raw_data[0][i])
peaks=find_peaks(raw_data[0],threshold=2,distance=250)[0]
frecuencia_muestreo=500
segundos=len(raw_data[0])/frecuencia_muestreo
frecuencia=60*len(peaks)/segundos
print("el paciente tiene una frecuencia cardiaca de {} por lo tanto esta bien".
format (round(frecuencia,0)))
x=list(range(len(raw_data[0])))
plt.plot(x,raw_data[0])                     # Plot the sine of each x point
plt.title("Grafico de electrocardiograma")
plt.xlabel("tiempo")
plt.ylabel("uVolts")
for peak in peaks:
    plt.plot(x[peak],raw_data[0][peak],'x')
plt.savefig("Grafico_ecg.png")    # Plot the sine of each x point
plt.show()                                          # Display the plot
