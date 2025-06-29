import numpy as np
import matplotlib.pyplot as plt

# Parámetros comunes
Fs = 1000                # Frecuencia de muestreo (Hz)
T = 1                    # Duración de la señal (s)
N = int(T * Fs)          # Número de muestras
t = np.linspace(0, T, N, endpoint=False)  # Vector de tiempo
frecuencia_seno = 5      # Frecuencia para la señal senoidal

# Función para graficar dominio del tiempo y espectro de frecuencia
def analizar_senal(signal, nombre):
    fft_result = np.fft.fft(signal)
    freq = np.fft.fftfreq(N, 1/Fs)
    
    # Magnitud y fase
    magnitud = np.abs(fft_result)
    fase = np.angle(fft_result)

    # Gráficas
    plt.figure(figsize=(14, 8))

    # Señal en el dominio del tiempo
    plt.subplot(3, 1, 1)
    plt.plot(t, signal, label='Señal en el tiempo')
    plt.title(f'{nombre} - Dominio del Tiempo')
    plt.xlabel('Tiempo [s]')
    plt.ylabel('Amplitud')
    plt.grid()

    # Magnitud del espectro
    plt.subplot(3, 1, 2)
    plt.plot(freq[:N//2], magnitud[:N//2])
    plt.title(f'{nombre} - Magnitud del Espectro de Frecuencia')
    plt.xlabel('Frecuencia [Hz]')
    plt.ylabel('|X(f)|')
    plt.grid()

    # Fase del espectro
    plt.subplot(3, 1, 3)
    plt.plot(freq[:N//2], fase[:N//2])
    plt.title(f'{nombre} - Fase del Espectro de Frecuencia')
    plt.xlabel('Frecuencia [Hz]')
    plt.ylabel('Fase [rad]')
    plt.grid()

    plt.tight_layout()
    plt.show()

# -----------------------------
# Señales elementales
# -----------------------------

# 1. Pulso rectangular (duración 0.2s entre 0.4 y 0.6)
pulso_rect = np.where((t >= 0.4) & (t < 0.6), 1, 0)
analizar_senal(pulso_rect, "Pulso Rectangular")

# 2. Función escalón (desde 0.5s en adelante)
escalon = np.where(t >= 0.5, 1, 0)
analizar_senal(escalon, "Función Escalón")

# 3. Señal senoidal (5 Hz)
seno = np.sin(2 * np.pi * frecuencia_seno * t)
analizar_senal(seno, "Señal Senoidal")

# -----------------------------
# Propiedades de la FFT
# -----------------------------

# A. Propiedad de Linealidad: combinación de pulso y seno
combinacion = 0.5 * pulso_rect + 0.5 * seno
analizar_senal(combinacion, "Linealidad: Pulso + Senoidal")

# B. Desplazamiento en el tiempo: seno desplazado 0.2s
seno_desplazado = np.sin(2 * np.pi * frecuencia_seno * (t - 0.2))
analizar_senal(seno_desplazado, "Senoidal Desplazada (0.2s)")

# C. Escalamiento en frecuencia: seno con el doble de frecuencia
seno_escalado = np.sin(2 * np.pi * 2 * frecuencia_seno * t)
analizar_senal(seno_escalado, "Senoidal con Frecuencia Escalada (2x)")

