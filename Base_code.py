#dummy, dummy

import numpy as np


class LagrangeInterpolation:
    '''
    Vorraussetzung: nodes, function_values sind arrays gleicher Länge; Elemente von nodes paarweise disjunkt
    Effekt: speichert Listen als numpy arrays in self.nodes, self.function_values
    Ergebnis: Erstellt Polynom
    '''
    def __init__(self, nodes, function_values):
        self.nodes = np.array(nodes)
        self.function_values = np.array(function_values)
        
        if len(self.nodes) != len(self.function_values):
            raise ValueError("Anzahl der Stützstellen und Funktionswerte muss gleich sein!")
        
        if not self._check_distinctness(self.nodes):
            raise ValueError("Stützstellen nicht paarweise disjunkt!")

    '''
    Vorraussetzung: x ist (array von) float
    Effekt: keiner
    Ergebnis: return y-wert(e) des Interpolationspolynoms an Stelle(n) x
    '''
    def __call__(self, x):
        #ohne numpy wäre die laufzeit katastrophal 
        #bereitet arrays vor
        x = np.asarray(x)
        res = np.zeros_like(x, dtype=float)

        for k in range(len(self.function_values)):
            res += self.function_values[k] * self.__lagrange(x, self.nodes, k)

        return res

    '''
    Vorraussetzung: nodes ist numpy array / liste
    Effekt: keiner
    Ergebnis: return True wenn nodes paarweise disjunkt
    '''
    @staticmethod
    def _check_distinctness(nodes):
        return len(set(nodes)) == len(nodes)

    '''
    Vorraussetzung: x ist  Wert/Array; nodes ist array; k ist int
    Effekt: keiner
    Ergebnis: return wert(e) des k-ten Lagrangepolynoms an stelle(n) x
    '''
    #eigentlich self.nodes, aber aus aufgabenstellung so
    def __lagrange(self, x, nodes, k):
        #startwert 1; form wie x array
        res = np.ones_like(x, dtype=float)
        for j in range(len(nodes)):
            if j != k:
                res *= (x - nodes[j]) / (nodes[k] - nodes[j])

        return res
            
if __name__ == '__main__':
    p = LagrangeInterpolation([0, 1], [2, 5])
    
    print(f"p(0) = {p(0)}")
    print(f"p(1) = {p(1)}")