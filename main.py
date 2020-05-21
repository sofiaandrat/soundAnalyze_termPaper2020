import os
import wget
from matplotlib import pyplot
from converter import fromMp3ToWav
from matrix_creator import VolumeMatrix
from constellation_map_creator import ConstellationMap
if not os.path.exists('thinkdsp.py'):
    wget.download('https://github.com/AllenDowney/ThinkDSP/raw/master/code/thinkdsp.py')
from thinkdsp import read_wave, decorate  # no pep8

if __name__ == "__main__":

    src = 'D:/курсач/songs data/буквы/ё.mp3'
    if 'mp3' in src:
        src = fromMp3ToWav(src)
    wave = read_wave(src)
    wave.normalize()
    wave = wave.segment(start=0.5, duration=0.5)
    # pyplot.show()
    spectrum = wave.make_spectrum()
    spectrum.plot()
    decorate(xlabel='Frequency (Hz)', ylabel='Amplitude')
    # pyplot.show()
    spectro = wave.make_spectrogram(seg_length=1024)
    spectro.plot(high=4200)
    decorate(xlabel='Time (s)',
             ylabel='Frequency (Hz)')
    # pyplot.show()
    matrix = VolumeMatrix(wave, (200, 2000), 0.01)
    matrix.decorator()
    f = open("output.txt", "w+")
    f.write(str(matrix))
    f.close()
    const = ConstellationMap(matrix.table)
    const.find_stars()