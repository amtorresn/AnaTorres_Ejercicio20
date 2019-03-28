import numpy as np
import math

class Complejo():
    def __init__(x, y):
        self.real = x
        self.imaginario = y
        self.norma = np.sqrt(x**2 + y**2)
        
    def conjugado(self):
        conjugado = self.x - 1j*self.y
        return conjugado
        
    def calcula_norma(self):
        return self.norma
    
    def pow(self, n):
      
        real = np.power(self.x**2 - self.y**2, n).real
        imag = np.power(self.x**2 - self.y**2, n).imag
        return Complejo(real, imag) 