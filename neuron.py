from inputx import InputX

class Neuron:
    def __init__(self):
        self._inputX = InputX(self)
        self.xs = self._inputX.xs
        self.ws = self._inputX.ws
        self.z = Neuron.summator(self.xs, self.ws)

    @staticmethod
    def summator(xs, ws):
        return sum(x*w for x,w in zip(xs,ws))

    def activate(self):
        return 1 if self.z >= 0.5 else 0