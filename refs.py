import numpy as np


class Ref:
    def __init__(self, valueMatrix):
        self.valueMatrix = np.array(valueMatrix)

    def GetValue(self, coefficient):
        coefficient.lower()
        positions = {
            "a11": self.valueMatrix[0, 1],
            "a12": self.valueMatrix[0, 2],
            "a13": self.valueMatrix[0, 3],
            "a14": self.valueMatrix[0, 4],
            "a15": self.valueMatrix[0, 5],

            "a21": self.valueMatrix[1, 1],
            "a22": self.valueMatrix[1, 2],
            "a23": self.valueMatrix[1, 3],
            "a24": self.valueMatrix[1, 4],
            "a25": self.valueMatrix[1, 5],

            "a31": self.valueMatrix[2, 1],
            "a32": self.valueMatrix[2, 2],
            "a33": self.valueMatrix[2, 3],
            "a34": self.valueMatrix[2, 4],
            "a35": self.valueMatrix[2, 5],

            "a41": self.valueMatrix[3, 1],
            "a42": self.valueMatrix[3, 2],
            "a43": self.valueMatrix[3, 3],
            "a44": self.valueMatrix[3, 4],
            "a45": self.valueMatrix[3, 5],

            "a51": self.valueMatrix[4, 1],
            "a52": self.valueMatrix[4, 2],
            "a53": self.valueMatrix[4, 3],
            "a54": self.valueMatrix[4, 4],
            "a55": self.valueMatrix[4, 5],

            "b1": self.valueMatrix[5, 1],
            "b2": self.valueMatrix[5, 2],
            "b3": self.valueMatrix[5, 3],
            "b4": self.valueMatrix[5, 4],
            "b5": self.valueMatrix[5, 5],

            "c1": self.valueMatrix[0, 0],
            "c2": self.valueMatrix[1, 0],
            "c3": self.valueMatrix[2, 0],
            "c4": self.valueMatrix[3, 0],
            "c5": self.valueMatrix[4, 0]
        }
        return positions.get(coefficient)


ETSHM6_Mentor = Ref([
    [-1, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0.75, 0.0546875, 0.6015625, 0, 0, 0],
    [-0.75, -0.041294642857143, -0.0703125, 0.017857142857143, 0, 0],
    [1, 0.087912087912088, 1.11396011396011, -
        0.042328042328042, -0.15954415954416, 0],
    [np.nan, -0.030952380952381, 0.655555555555556,
        0.203174603174603, 0.203174603174603, -0.030952380952381]
])

ETSHM6 = Ref([
    [-1, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [-0.2, -0.032, -0.048, 0, 0, 0],
    [-0.4, -0.044333333333333, -0.017333333333333, -0.058333333333333, 0, 0],
    [0.666666666666667, -0.0212429507697, 0.954503886602652, -
        1.17026748971193, 0.792562109434537, 0],
    [np.nan, 0.016666666666667, 0.958333333333333, -
        0.801282051282051, 0.651041666666667, 0.175240384615385]
])

ETSHM6_8_7 = Ref([
    [-1, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0.75, 0.0546875, 0.6015625, 0, 0, 0],
    [-0.595238095238095, -0.050827816819418, -
        0.087275556481096, 0.017638520692804, 0, 0],
    [0.538461538461538, 0.053686099661206, 0.328358447809124,
        0.006767348800901, 0.025389287160721, 0],
    [np.nan, 0.005644257703081, 0.544952380952381,
        0.060898591873537, 0.219815561193811, 0.168782528725986]
])

ETSHM6_6_inf = Ref([
    [-1, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0.2, 0.032, 0.088, 0, 0, 0],
    [0.7, 0.0595, 0.5355, 0, 0, 0],
    [-0.5, -0.053921568627451, -0.048611111111111, -
        0.048611111111111, 0.026143790849673, 0],
    [np.nan, 0.014705882352941, 0.261904761904762,
        0.297619047619048, 0.140056022408964, 0.285714285714286],
])
# TODO: Convert to fractions
