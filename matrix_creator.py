import os
import wget
import pandas as pd
if not os.path.exists('thinkdsp.py'):
    wget.download('https://github.com/AllenDowney/ThinkDSP/raw/master/code/thinkdsp.py')


class VolumeMatrix:
    def __init__(self, wave, range, tstep):
        self.wave = wave
        self.range = range
        self.tstep = tstep
        self.spectrum = None
        self.peaks = []
        self.matrix = []
        self.dict = {}
        self.table = None

    def __str__(self):
        string = ''
        for raw in self.matrix:
            string += " ".join(map(str, raw))
            string += '\n'
        return string

    def __create_spectrum__(self):
        self.spectrum = self.wave.make_spectrum()
        self.peaks = self.spectrum.peaks()

    def __create_empty_matrix__(self):
        counter = (self.range[1] - self.range[0]) // 100 + 1
        self.matrix = []
        for i in range(counter):
            self.matrix.append([])
        # self.matrix = numpy.array(self.matrix)

    def __fill_matrix__(self):
        counter = int((self.wave.ts[-1] - self.wave.ts[0]) // self.tstep)
        for i in range(counter):
            self.miniWave = VolumeMatrix(self.wave.segment(start=self.wave.ts[0] + i * self.tstep, duration=self.tstep),
                                         self.range, self.tstep)
            self.miniWave.__create_spectrum__()
            for element in self.miniWave.peaks:
                if self.range[0] <= element[1] <= self.range[1]:
                    self.matrix[int((element[1] - self.range[0]) // 100)].append(round(element[0], 3))
                    self.__empty_checker__(i)
        self.__create_dict__()
        self.__draw_picture__()

    def __empty_checker__(self, count):
        for raw in self.matrix:
            if len(raw) < count + 1:
                raw.append(0)

    def decorator(self):
        self.__create_empty_matrix__()
        self.__fill_matrix__()

    def __create_dict__(self):
        counter = (self.range[1] - self.range[0]) // 100 + 1
        for i in range(counter):
            self.dict.update({self.range[0] + i * 100: self.matrix[i]})

    def __draw_picture__(self):
        self.__create_dict__()
        self.table = pd.DataFrame(self.dict)


