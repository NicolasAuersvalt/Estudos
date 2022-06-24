from tkinter import *
import tkinter.messagebox
import pygame.mixer

app = Tk()
app.title("Mixador")
app.geometry("205x100+200+100")
sound = r"C:\Users\nicol\Music\Cyclops\AI_welcome.wav"
mixer = pygame.mixer
mixer.init()
def track_start():
    track.play(loops=-1)

def track_stop():
    track.stop()

track = mixer.Sound(sound)

button = Button(app, text="Start", command=track_start)
button1 = Button(app, text="Stop", command=track_stop)

button.pack(), button1.pack()
track_stop()

app.mainloop()