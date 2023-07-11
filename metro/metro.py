import os
import select
import termios
import sys
from time import sleep

os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"

import pygame

from .sound import create_sound


UP = "\x1B[3A"
CLR = "\x1B[0K"


def metronome(bpm, seconds):
    pygame.init()   
    clock = pygame.time.Clock()

    print_intro()

    sound = create_sound(bpm)
    sound.play(loops=-1)

    if seconds is not None:
        play_for_specified_time(bpm, seconds)
    else:
        play_indefinitely(bpm)

    termios.tcflush(sys.stdin, termios.TCIOFLUSH)
    
    pygame.quit()


def play_for_specified_time(bpm, seconds):
    for i in range(seconds):
        print(f"\r{UP}Playing tick at {bpm} bpm for {seconds - i} seconds{CLR}\nPress Enter to stop...{CLR}\n")
        i, o, e = select.select( [sys.stdin], [], [], 1)
        if i:
            return


def play_indefinitely(bpm):
    while True:
        print(f"\r{UP}Playing tick at {bpm} bpm{CLR}\nPress Enter to stop...{CLR}\n")
        i, o, e = select.select( [sys.stdin], [], [], 1)
        if i:
            return


def print_intro():
    print("\n\n\n")
    for i in range(3):
        print(f"\r{UP}Starting in {3-i} seconds..{CLR}\n\n")
        sleep(1)