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

    src = 'D:/курсач/songs data/три белых коня/after/DaryaLoban.mp3'
    if 'mp3' in src:
        src = fromMp3ToWav(src)
    wave = read_wave(src)
    wave.normalize()
    matrix = VolumeMatrix(wave, (200, 2000), 0.01)
    matrix.decorator()
    const_map = ConstellationMap(matrix)
    const_map.find_stars()
    stars = const_map.data_for_map_drawing
    plt.figure(figsize=(10, 7))
    plt.subplots_adjust(bottom=0.1)
    plt.scatter(stars[:, 0], stars[:, 1], marker="x")
    decorate(xlabel='Time, s', ylabel='Frequency, Hz')
    plt.show()


