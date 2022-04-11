from tkinter import *
import pygame.mixer

class SoundPanel(Frame):
    def __init__(self, app, mixer, sound_file):
        Frame.__init__(self, app)
        self.track = mixer.Sound(sound_file)
        self.flipper = IntVar()  # StringVar mantém um valor de String, em vez de int como IntVar
        self.flipper.set(None)
        track_button = Checkbutton(self, variable=self.flipper,
                                   command=self.flip_it,
                                   text="Welcome Aboard, Captain")
        self.volume = DoubleVar()
        self.volume.set(self.track.get_volume())
        volume_scale = Scale(self, variable=self.volume,
                             from_=0.1, to=0.9,
                             resolution=0.1, command=self.change_volume,
                             label="Volume",
                             orient=HORIZONTAL)
        volume_scale.pack()
        track_button.pack()

    def flip_it(self):
        if self.flipper.get() == 1:
            self.track.play(loops=-1)

        else:
            self.track.stop()

    def change_volume(self, v):
        self.track.set_volume(self.volume.get())

