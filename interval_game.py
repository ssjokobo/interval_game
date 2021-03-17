from random import random
import math

pitches = ['C', 'D', 'E', 'F', 'G', 'A', 'B']
chord_tones = {'C': 0, 'E': 4, 'G': 7, 'B': 11, 'D': 2, 'F': 5, 'A': 9}
accidentals = ['b', '', '#']

def random_pitch(): 
    return math.floor((random() * 7))

def random_acci():
    return math.floor((random() * 3))

def compare(p1, p2):
    if p1.val == p2.val:
        return 'root'
    elif p1.val < p2.val:
        p2.num - p1.num + 1
        return
    else:

class PitchClass():
    def __init__(self):
        self.num = random_pitch()
        self.acc = random_acci()
        self.name = pitches[self.num] + accidentals[self.acc]
        self.val = chord_tones[pitches[self.num]] + self.acc - 1

class MajorScale(pitch):
    def __init__(self, pitch):
        self.list = 

root = PitchClass()
tension = PitchClass()

print('If {0} is the root, what is the tension number for {1}?'.format(root.name, tension.name))
print(root.val)
print(tension.val)
