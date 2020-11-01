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
    
    def spill(self):
        self._current_volume = 0

    def fill(self):
        self._current_volume = self._total_capacity
    
    def transfer_from(self, node):
        if ((self._current_volume + node.get_current_volume) < self._total_capacity):
            self._current_volume = self._total_capacity
        else:
            self._current_volume += node.get_current_volume

    def transfer_to(self, node):
        if not self._current_volume == 0:
            node.transfer_from(self)
            self.spill()