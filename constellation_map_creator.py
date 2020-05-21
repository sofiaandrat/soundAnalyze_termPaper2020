from scipy.signal import find_peaks
import pandas as pd

class ConstellationMap:
    def __init__(self, data_frame):
        self.data_frame = data_frame
        self.stars_dict = {}

    def find_stars(self):
        for column in self.data_frame.columns:
            a = self.data_frame.[1][1]
            peaks, _ = find_peaks(self.data_frame.loc[:, [column]][1])
            print(self.data_frame.loc[:, [column]])
            print(peaks)
