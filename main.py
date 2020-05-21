import os
import wget
import matplotlib.pyplot as plt
from converter import fromMp3ToWav
from matrix_creator import VolumeMatrix
from constellation_map_creator import ConstellationMap
if not os.path.exists('thinkdsp.py'):
    wget.download('https://github.com/AllenDowney/ThinkDSP/raw/master/code/thinkdsp.py')
from thinkdsp import read_wave, decorate  # no pep8

if __name__ == "__main__":

    src = 'D:/курсач/songs data/Моё сердце остановилось/after/DaryaLoban.mp3'
    if 'mp3' in src:
        src = fromMp3ToWav(src)
    wave = read_wave(src)
    wave.normalize()
    #wave = wave.segment(start=0, duration=0.5)
    # pyplot.show()
    spectrum = wave.make_spectrum()
    #plt = spectrum.plot()
    #decorate(xlabel='Frequency (Hz)', ylabel='Amplitude')
    #pyplot.show()
    spectro = wave.make_spectrogram(seg_length=1024)
    #spectro.plot(high=4200)
    #decorate(xlabel='Time (s)',
    #         ylabel='Frequency (Hz)')
    # pyplot.show()
    matrix = VolumeMatrix(wave, (200, 2000), 0.01)
    matrix.decorator()
    const = ConstellationMap(matrix.table)
    const.find_stars()
    const_map = const
    stars = const_map.data_for_map_drawing
    f = open("output.txt", "w+")
    f.write(str(const_map))
    f.close()
    labels = range(1, len(stars) + 1)
    plt.figure(figsize=const_map.figsize)
    plt.subplots_adjust(bottom=0.1)
    plt.scatter(stars[:, 0], stars[:, 1], label='True Position', marker="x")
    plt.show()


