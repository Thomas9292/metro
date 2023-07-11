import sys

from .metro import metronome

def main():
    bpm = int(sys.argv[1])
    seconds = int(sys.argv[2]) if len(sys.argv) > 2 else None

    metronome(bpm, seconds)


    