from random import random
import math

pitches = ['C', 'D', 'E', 'F', 'G', 'A', 'B']
chord_tones = {'C': 0, 'D': 2, 'E': 4, 'F': 5, 'G': 7, 'A': 9, 'B': 11}
accidentals = ['b', '', '#']
tension_names = {
    '0': ['root', 'Root'],
    '1': ['#1', 'b9', 'b2', '#15'],
    '2': ['2', '9'],
    '3': ['b3', '#9'],
    '4': ['3'],
    '5': ['4', '11'],
    '6': ['#11', '#4', 'b5'],
    '7': ['5'],
    '8': ['#5', 'b13'],
    '9': ['6', '13', 'bb7'],
    '10': ['b7'],
    '11': ['7']
}

def random_pitch(): 
    return math.floor((random() * 7))

def random_acci():
    return math.floor((random() * 3))

def compare(p1, p2):
    return tension_names[str((p2.val - p1.val + 12) % 12)]

class PitchClass():
    def __init__(self):
        self.num = random_pitch()
        self.acc = random_acci()
        self.name = pitches[self.num] + accidentals[self.acc]
        self.val = chord_tones[pitches[self.num]] + self.acc - 1

root = PitchClass()
tension = PitchClass()

user_answer = input('If {0} is the root, what is the tension number for {1}?\n'.format(root.name, tension.name))
answer = compare(root, tension)
if user_answer in answer:
    print('Correct! Possible answers are: {}'.format(', '.join(map(str, answer))))
else:
    print('Wrong, and the answers are: {}'.format(', '.join(map(str, answer))))

