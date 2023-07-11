import os

import numpy
import pygame

dir = os.path.dirname(__file__)

pygame.mixer.pre_init(44100, 16, 2, 4096)
pygame.mixer.init()

def create_sound(bpm: int):
    sound_path = os.path.join(dir,'sounds/tick.wav')
    tick = pygame.mixer.Sound(sound_path)
    return getResizedSound(tick, 60 / bpm);

# Helper function
def getResizedSound(sound, duration):

    frequency, bits, channels = pygame.mixer.get_init()

    # Determine silence value
    silence = 0 if bits < 0 else (2**bits / 2) - 1

    # Get raw sample array of original sound
    oldArray = pygame.sndarray.array(sound)

    # Create silent sample array with desired length
    newSampleCount = int(duration * frequency)
    newShape = (newSampleCount,) + oldArray.shape[1:]
    newArray = numpy.full(newShape, silence, dtype=oldArray.dtype)

    # Copy original sound to the beginning of the
    # silent array, clipping the sound if it is longer
    newArray[:oldArray.shape[0]] = oldArray[:newArray.shape[0]]

    return pygame.mixer.Sound(newArray)