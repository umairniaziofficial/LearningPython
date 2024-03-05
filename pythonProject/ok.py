import pygame
import time


def beepTimer(seconds):
    file = "Oh No Notification Ringtone.mp3"
    time.sleep(seconds)

    pygame.mixer.init()
    pygame.mixer.music.load(file)
    pygame.mixer.music.play()

    # Add a delay to allow the sound to finish playing
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)


seconds = int(input("Input Seconds: "))
beepTimer(seconds)
