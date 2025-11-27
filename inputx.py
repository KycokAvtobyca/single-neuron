from random import uniform, gauss
import math

class InputX:
    def __init__(self, objectNeuron, n_inputs: int = 10):
        from neuron import Neuron
        if not isinstance(objectNeuron, Neuron):
            raise ValueError("objectNeuron должен быть объектом класса Neuron")

        self._objectNeuron = objectNeuron
        self._xs = tuple(max(0, min(1, gauss(0.3, 0.2))) for _ in range(n_inputs))
        self._limit = math.sqrt(6 / (n_inputs + 1))
        self._ws = tuple(uniform(-self.limit, self.limit) for _ in range(n_inputs))
    
    @property
    def xs(self):
        return self._xs
    
    @property
    def ws(self):
        return self._ws
    
    @property
    def limit(self):
        return self._limit
    
    @property
    def objectNeuron(self):
        return self._objectNeuron
