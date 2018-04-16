import random
  
  class Perceptron:
  
    def __init__(self, learn_speed, num_weights):
    
      self.speed = learn_speed
    
      self.weights = []
      for x in range(0, num_weights):
        self.weights.append(random.random()*2-1)

    def feed_forward(self, inputs):
      sum = 0
      # multiply inputs by weights and sum them
      for x in range(0, len(self.weights)):
        sum += self.weights[x] * inputs[x]
      # return the 'activated' sum
      return self.activate(sum)
      
    def activate(self, num):
      # turn a sum over 0 into 1, and below 0 into -1
      if num > 0:
        return 1
      return -1

    def train(self, inputs, desired_output):
      guess = self.feed_forward(inputs)
      error = desired_output - guess
      
      for x in range(0, len(self.weights)):
        self.weights[x] += error*inputs[x]*self.speed