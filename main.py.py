import numpy as np
import matplotlib.pyplot as plt
import scipy.signal as signal


numerator = [193*25.64, 193,0,1,0] # 193*25.64*s^4 + 193*s^3
denominator = [1, 30+320*np.pi, 300+9600*np.pi, 1000+96000*np.pi, 320000*np.pi] # (s+10)^3 * (s+320*pi)

sys = signal.TransferFunction(numerator, denominator)
freqAng, magDB, phase = signal.bode(sys) # freqAng: Frecuencia angular, magDB: Magnitud de ganancia en dB, phase: Fase en grados

# Grafico

plt.figure()
plt.subplot(2,1,1)
plt.semilogx(freqAng, magDB) # Av dB
plt.grid(True)
plt.ylabel('Magnitud (dB)')

plt.subplot(2, 1, 2)
plt.semilogx(freqAng, phase)  # Phase
plt.grid(True)
plt.xlabel('Frecuencia (rad/s)')
plt.ylabel('Fase (grados)')

plt.show()