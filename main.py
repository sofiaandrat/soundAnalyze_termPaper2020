import os
import wget
import matplotlib.pyplot as plt
from converter import fromMp3ToWav
from matrix_creator import VolumeMatrix
from constellation_map_creator import ConstellationMap
if not os.path.exists('thinkdsp.py'):
    wget.download('https://github.com/AllenDowney/ThinkDSP/raw/master/code/thinkdsp.py')
from thinkdsp import read_wave  # no pep8

if __name__ == "__main__":

    src = '~/PATH_TO_SOUND_SOURCE/[file_name.mp3 or file_name.wav]'
    if 'mp3' in src:
        src = fromMp3ToWav(src)
    wave = read_wave(src)
    wave.normalize()
    matrix = VolumeMatrix(wave, (200, 2000), 0.01)
    matrix.decorator()
    const_map = ConstellationMap(matrix)
    const_map.find_stars()
    stars = const_map.data_for_map_drawing
    labels = range(1, len(stars) + 1)
    plt.figure(figsize=const_map.figsize)
    plt.subplots_adjust(bottom=0.1)
    plt.scatter(stars[:, 0], stars[:, 1], label='True Position', marker="x")
    plt.show()


