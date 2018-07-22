import numpy as np


class Method:
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

# Self
NewMethod1 = Method([
[-1, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0],
[0.584, 10702/166861, 9061/22744, 0, 0, 0],
[1/5 * np.sqrt(10), 367039/5646021, 2003748/4470649, 26126/8654901, 0, 0],
[-1/5 * np.sqrt(10), -352996/6728411, -544325/8527947, -1522/1020353, 3543/281930, 0],
[np.nan, 0, 7/12, 0, 5/24, 5/24]
])

NewMethod2 = Method([
[-1, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0],
[0.7731, 3127/60322, 20638/32575, 0, 0, 0],
[-0.7731, -14418/368831, -4274/65647, 20383/1236182, 0, 0],
[1, 14059/217182, 1387/1286, -5195/174507, -4520/39823, 0],
[np.nan, -6787/165751, 21653/32511, 7425/35708, 7425/35708, -6787/165751]
])

# Mentor's
ETSHM6_Mentor = Method([
[-1, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0],
[3/4, 7/128, 77/128, 0, 0, 0],
[3/4, -37/896, -9/128,  1/56, 0, 0],
[18/91, 391/351, -8/189, -56/351, 0],
[np.nan, -13/420, 59/90, 64/315, 64/315, -13/420]
])

# Franco's
ETSHM6 = Method([
    [-1, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [-1/5, -4/125, -6/125, 0, 0, 0],
    [-2/5, -133/3000, -13/750, -7/120, 0, 0],
    [2/3, -1115/52488, 4175/4374, -2275/1944, 5200/6561, 0],
    [np.nan, 1/60, 23/24, -125/156, 125/192, 729/4160]
])

ETSHM6_8_7 = Method([
    [-1, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [3/4, 7/128, 77/128, 0, 0, 0],
    [-25/42, -273042/5371901, -30175/345744, 48025/2722734, 0, 0],
    [7/13, 3829/71322, 3159816/9623069, 62626/9254141, 217096/8550693, 0],
    [np.nan, 403/71400, 2861/5250, 7936/130315, 334159/1520179,  982063/5818511]
])

ETSHM6_6_inf = Method([
    [-1, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [1/5, 4/125, 11/125, 0, 0, 0],
    [7/10, 119/2000, 1071/2000, 0, 0, 0],
    [-1/2, -11/204, -7/144, -7/144, 4/153, 0],
    [np.nan, 1/68, 11/42, 25/84, 50/357, 2/7],
])
# TODO: Convert to fractions