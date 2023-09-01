import numpy as np


class Clock:
    def __init__(self):
        self.numBalls = 0
        self.line_1 = []
        self.line_5 = []
        self.line_60 = []
        self.balls = np.arange(self.numBalls).tolist()
        self.fullCycles = 0
