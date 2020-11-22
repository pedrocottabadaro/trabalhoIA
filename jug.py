import copy as Copy


class Jug:
    """
    Liquid recipient.
    It has a total capacity of liquid, a current volume.
    It can spill its content, be filled to its capacity, receive liquid and transfer its amount to another jug

    Args:
        none

    Returns:
        A Jug instance   
    """

    def __init__(self, total_capacity):
        self._total_capacity = total_capacity
        self._current_volume = 0

    def get_total_capacity(self):
        return self._total_capacity

    def get_current_volume(self):
        return self._current_volume

    def set_current_volume(self, value):
        self._current_volume = value

    def spill(self):
        if self._current_volume != 0:
            self._current_volume = 0
            return True
        return False

    def fill(self):
        if self._current_volume < self._total_capacity:
            self._current_volume = self._total_capacity
            return True
        return False

    def transfer_to(self, target_jug):
        if not self._current_volume == 0:
            if (target_jug.get_current_volume() + self._current_volume) >= target_jug.get_total_capacity():
                target_jug.set_current_volume(self._total_capacity)
            else:
                target_jug.set_current_volume(self._current_volume)
            
            self.spill()
            return True
        return False