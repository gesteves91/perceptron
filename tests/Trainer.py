import random

from Perceptron import Perceptron

class Trainer:
    
    def __init__(self):
      self.perceptron = Perceptron(0.01, 3)
      
    def f(self, x):
      return 0.5*x + 10 # line: f(x) = 0.5x + 10
      
    def train(self):
      for x in range(0, 1000000):
        x_coord = random.random()*500-250
        y_coord = random.random()*500-250
        line_y = self.f(x_coord)
        
        if y_coord > line_y: # above the line
          answer = 1
          self.perceptron.train([x_coord, y_coord,1], answer)
        else: # below the line
          answer = -1
          self.perceptron.train([x_coord, y_coord,1], answer)
      return self.perceptron # return our trained perceptron