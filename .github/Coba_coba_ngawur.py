#memanggil modul numpy sebagai np
import numpy as np
#memanggil modul matplotlib sebagai plt
import matplotlib.pyplot as plt

#Membangun fungsi def untuk Discrete Fourier Transform dengan parameter x
def naive_DFT(x):
    N = np.size(x)
    X = np.zeros((N,),dtype=np.complex128)
    for m in range(0,N):
        for n in range(0,N):
            X[m] += x[n]*np.exp(-np.pi*2j*m*n/N)
    return X

#Membangun fungsi def untuk Inverse Discrete Fourier Transform dengan parameter x
def naive_IDFT(x):
    N = np.size(x)
    X= np.zeros((N,),dtype=np.complex128)
    for m in range(0,N):
        for n in range(0,N):
            X[m] += x[n]*np.exp(np.pi*2j*m*n/N)
    return X/N

#Jumlah sampel yang diambil
N = 600;
#Time sampling
dt = 1.0/200.0
#interval waktu
t = np.linspace(0.0, N*dt, N)
#mendefinisikan fungsi yang akan dilakukan DFT
jenis = input("Masukkan jenis sinyalnya (sinusoidal, eksponensial kompleks, heaviside): ")
A = float(input("Masukkan amplitudo sinyal: "))
w = float(input("Masukkan angular frequencynya dalam pi: "))
teta = float(input("Masukkan sudut fasenya: "))

if jenis == "sinusoidal":
    o = A*np.sin(w*np.pi*t+teta)
elif jenis == "eksponensial kompleks":
    o = np.exp(A*(cos(w*np.pi*t+teta)+1j*sin(w*np.pi+teta)))
elif jenis == "heaviside":
    o = [1 if t[i]>-2 else 0 for i in range(len(t))]
    
yf = naive_DFT(o)
xf = np.linspace(0.0, 1.0/(2.0*dt), N//2)
yi = naive_IDFT(yf)

#mengatur ukuran panjang dan lebar grafik
plt.figure(figsize=(5,15))
#plot grafik data mentah
plt.subplot(3, 1, 1)
plt.plot(t, o, '-')
#untuk memberikan judul pada grafik data mentah
plt.title('Data Mentah')
#untuk memberikan subjudul pada sumbu-y
plt.ylabel('Amp')

#plot grafik Discrete Fourier Transform
plt.subplot(3, 1, 2)
plt.plot(xf, 2.0/N*np.abs(yf[0:N//2]),'r-')
#untuk memberikan judul pada grafik data DFT
plt.title('Power Spectral')
#untuk memberikan subjudul pada masing-masing sumbu
plt.xlabel('frek (Hz)')
plt.ylabel('Spectral')

#plot grafik hasil Inverse DFT
plt.subplot(3, 1, 3)
plt.plot(t, yi, 'y-')
#untuk memberikan judul pada grafik hasil inverse DFT
plt.title('Data Hasil IDFT')
#untuk memberikan subjudul pada masing-masing sumbu
plt.ylabel('Amp')
#untuk memberikan grid pada kanvas
plt.grid()
#untuk menampilkan grafik
plt.show()