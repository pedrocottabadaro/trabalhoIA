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
        self.spill()

    def get_total_capacity(self):
        return _total_capacity
    
    def get_current_volume(self):
        return _current_volume
    
    def spill(self):
        self._current_volume = 0

    def fill(self):
        self._current_volume = self._total_capacity
    
    def put(self, quantity):
        if ((self._current_volume + quantity) < self._total_capacity):
            self._current_volume = self._total_capacity
        else:
            self._current_volume += quantity

    def transfer_to(self, node):
        if not self._current_volume == 0:
            node.pour_in(self._current_volume)
            self.spill()