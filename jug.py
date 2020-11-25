class Jug:
    #construtor
    def __init__(self, total_capacity):
        self._total_capacity = total_capacity
        self._current_volume = 0

    def get_total_capacity(self):
        return self._total_capacity

    def get_current_volume(self):
        return self._current_volume

    def set_current_volume(self, value):
        self._current_volume = value

    #operador de esvaziar
    def spill(self):
        if self._current_volume != 0:
            self._current_volume = 0
            return True
        return False

    #operador de encher
    def fill(self):
        if self._current_volume < self._total_capacity:
            self._current_volume = self._total_capacity
            return True
        return False