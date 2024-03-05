import pygame

def PlaySound():
    pygame.init()
    pygame.mixer.init()

    try:
        pygame.mixer.music.load("SOUND.mp3")  
        pygame.mixer.music.play(1)  

        clock = pygame.time.Clock()
        while pygame.mixer.music.get_busy():
            clock.tick(30)  

    except pygame.error as e:
        print(f"Error loading or playing the sound file: {e}")

    pygame.mixer.quit()
    pygame.quit()

PlaySound()
