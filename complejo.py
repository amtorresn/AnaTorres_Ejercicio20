import numpy as np
import cmath

class Complejo:
    def __init__(self, x, y):
        self.real = x
        self.imaginario = y
        self.norma = np.sqrt(x**2 + y**2)
        
    def conjugado(self):
        real = self.real
        imag = -self.imaginario
        return Complejo(real, imag)
        
    def calcula_norma(self):
        return self.norma
    
    def pow(self, n):
      
        real = np.power(self.real**2 - self.imaginario**2, n).real
        imag = np.power(self.real**2 - self.imaginario**2, n).imag
        return Complejo(real, imag) 