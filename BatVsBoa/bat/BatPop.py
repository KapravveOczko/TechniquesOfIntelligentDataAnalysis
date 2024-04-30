class BatPop(object):

    def __init__(self, function):
        self.bat_pop = []
        self.function = function
        self.average_volume = 0
        self.best_bat_x = 0

    def set_best_bat_x(self):
        best_x = self.best_bat_x

        for x in self.bat_pop:
            if self.function(x) > self.function(best_x):
                best_x = x

        self.best_bat_x = best_x

    def append_bat(self, Bat):
        self.bat_pop.append(Bat)

    def get_average(self):
        result = 0
        for bat in self.bat_pop:
            result += bat.volume
        return result / len(self.bat_pop)