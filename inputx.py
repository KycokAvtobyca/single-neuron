from random import uniform
import math

class InputX:
    def __init__(self, objectNeuron, n_inputs: int = 10):
        from neuron import Neuron
        if not isinstance(objectNeuron, Neuron):
            raise ValueError("objectNeuron должен быть объектом класса Neuron")

        self._objectNeuron = objectNeuron
        self._xs = tuple(uniform(0, 1) for _ in range(n_inputs))
        self._ws = tuple(uniform(-1, 1) for _ in range(n_inputs))
    
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
