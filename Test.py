import sys
import random
import time
import numpy as np
sys.path.insert(0, 'M:/Save/ZSublimesSaves/Python/NeuroEvolution')
from NeuralNetwork import NeuralNetwork
from Blip import Blip







# selectionPool = []
# for blip in self.deadBlips:
#     # print(blip.fitness)
#     blipPoolCount = math.ceil(blip.fitness * 100)
#     for i in range(blipPoolCount):
#         selectionPool.append(blip)
# for i in range(len(selectionPool) - 100):
#     del selectionPool[-1]
# for i in range(self.blipStartCount):
#     rand = random.randint(0,99) #was (1,100) - 1. Not sure what the difference is
#     selection = selectionPool[rand]
#     # print (selection.fitness)
#     child = selection.mutate(self.mutationRate)
#     child.xPos = random.randint(100, screenSize - 100)
#     self.activeBlips.append(child)








# #old functions
# #used when a single blip accepted user-input for movment
# def checkKeyPress(self): #belongs in Game.py
#     keys = pg.key.get_pressed()
#     if keys[pg.K_LEFT]:
#          self.activeBlips[0].move('left')
#     elif keys[pg.K_RIGHT]:
#          self.activeBlips[0].move('right')
#     else:
#         for blip in self.activeBlips:
#             blip.move('null') #keeps the move function in the game loop so all blips continue thinking
# #same as checkKeyPress()
# def move(self, decision): #belongs in Blip.py
#     self.fittness += 1 #fittness increases by 1 each frame
#     self.xPos += self.xVelocity #update position
#     if decision == 0: #left
#         self.xVelocity -= self.xAcceleration
#     elif decision == 1: #right
#         self.xVelocity += self.xAcceleration
#     if decision == 'left': #left
#         self.xVelocity -= self.xAcceleration
#     elif decision == 'right': #right
#         self.xVelocity += self.xAcceleration

# #used when there was a copy function in NeuralNetwork
# def __init__(self, inputnodesORnet, hiddennodes, outputnodes): #belongs in NeuralNetwork.py
#     if isinstance(inputnodesORnet, NeuralNetwork): #if inputnodesORnet is an instance of a neural network:
#         self.inodes = inputnodesORnet.inodes
#         self.hnodes = inputnodesORnet.hnodes
#         self.onodes = inputnodesORnet.onodes
#         self.wih = inputnodesORnet.wih
#         self.who = inputnodesORnet.who
#         self.sigmoidSquish = lambda x: scipy.special.expit(x) #declare activiation function (sigmoid squish) squishes every element in a n array
#     else: #if inputnodesORnet is an integer:
#         self.inodes = inputnodesORnet #in this case, it's inputnodes
#         self.hnodes = hiddennodes
#         self.onodes = outputnodes
#         self.wih = numpy.random.normal(0.0, pow(self.inodes, -0.5), (self.hnodes, self.inodes)) #create random weight matrix (hidden layer)
#         self.who = numpy.random.normal(0.0, pow(self.hnodes, -0.5), (self.onodes, self.hnodes)) #create random weight matrix (output layer)
#         self.sigmoidSquish = lambda x: scipy.special.expit(x) #declare activiation function (sigmoid squish) squishes every element in a n array
