import numpy as np


class ConstellationMap:
    def __init__(self, voluem_matrix):
        self.data_frame = voluem_matrix.table
        self.tstep = voluem_matrix.tstep
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

    def __create_map__(self, tolerance=8):
        self.map = self.extremums
        self.map = self.map.fillna(0)
        self.map = self.map.mask(abs(self.map) < tolerance, 0)
        self.map = self.map.mask(abs(self.map) > tolerance, 1)
        for freq, row in self.map.T.iterrows():
            for time, element in np.ndenumerate(row):
                if element > 0:
                    self.data_for_map_drawing.append([time[0] * self.tstep, freq])
        self.data_for_map_drawing = np.array(self.data_for_map_drawing)
        self.figsize = (self.map.values.shape[0] // 15, self.map.values.shape[1] // 4)