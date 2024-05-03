from math import inf

class BatPop(object):

    def __init__(self, function):
        self.bat_pop = []
        self.function = function
        self.average_volume = 0
        self.best_bat_score = inf
        self.best_bat_coordinates = []
        self.bat_pop_size = 0

    def append_bat(self, bat):
        if bat.score < self.best_bat_score:
            self.best_bat_score = bat.score
            self.best_bat_coordinates = bat.coordinates
        self.bat_pop.append(bat)
        self.bat_pop_size += 1

    def get_average(self):
        result = 0
        for bat in self.bat_pop:
            result += bat.volume

        self.average_volume = result / self.bat_pop_size
