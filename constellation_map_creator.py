from scipy.signal import find_peaks
import pandas as pd
import numpy as np


class ConstellationMap:
    def __init__(self, data_frame):
        self.data_frame = data_frame
        self.stars_dict = {}
        self.extremums = None
        self.map = None
        self.data_for_map_drawing = []
        self.figsize = (0, 0)

    def __str__(self):
        string = ''
        for raw in self.map.values:
            string += " ".join(map(str, raw))
            string += '\n'
        return string

    def find_stars(self):
        self.extremums = self.__find_extrema__(self.data_frame)
        self.__create_map__()

    def __find_extrema__(self, tolerance=0.5):
        diff = self.data_frame.diff()
        extrema = diff[np.abs(diff) < tolerance]
        return extrema

    def __create_map__(self, tolerance=2):
        self.map = self.extremums
        self.map = self.map.fillna(0)
        self.map = self.map.mask(abs(self.map) < tolerance, 0)
        self.map = self.map.mask(abs(self.map) > tolerance, 1)
        for time, row in self.map.iterrows():
            for freq, element in np.ndenumerate(row):
                if element > 0:
                    self.data_for_map_drawing.append([freq[0], time])
        self.data_for_map_drawing = np.array(self.data_for_map_drawing)
        self.figsize = (self.map.values.shape[0] // 5, self.map.values.shape[1] // 10)