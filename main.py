import os
import wget
from matplotlib import pyplot
from converter import fromMp3ToWav
if not os.path.exists('thinkdsp.py'):
    wget.download('https://github.com/AllenDowney/ThinkDSP/raw/master/code/thinkdsp.py')
from thinkdsp import read_wave, decorate  # no pep8

if __name__ == "__main__":

    src = 'D:/курсач/songs data/буквы/ё.mp3'
    if 'mp3' in src:
        src = fromMp3ToWav(src)
    wave = read_wave(src)
    wave.normalize()
    wave = wave.segment(start=0.7, duration=0.01)
    pyplot.show()
    spectrum = wave.make_spectrum()
    spectrum.plot()
    d = spectrum.peaks()
    decorate(xlabel='Frequency (Hz)', ylabel='Amplitude')
    pyplot.show()
    spectro = wave.make_spectrogram(seg_length=1024)
    spectro.plot(high=4200)
    decorate(xlabel='Time (s)',
             ylabel='Frequency (Hz)')
    pyplot.show()