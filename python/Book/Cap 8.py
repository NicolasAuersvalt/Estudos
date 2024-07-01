"""


"""
from tkinter import *
import pygame.mixer
from sound_panel import *

app = Tk()
app.title("Fale daora")

mixer = pygame.mixer
mixer.init()

panel = SoundPanel(app, mixer, "AI_welcome.wav")
panel.pack()
panel = SoundPanel(app, mixer, "AI_welcome_attention.wav")
panel.pack()
app.mainloop()