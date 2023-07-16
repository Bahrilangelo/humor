import tkinter as tk
from pydub import AudioSegment
from pydub.playback import play

def play_sound():
    sound = AudioSegment.from_file(".\wth.mp3", format="mp3")
    play(sound)

def create_interface():
    root = tk.Tk()
    root.title("What the heeeeeeell")

    button = tk.Button(root, text="What the hell", command=play_sound)
    button.pack(pady=20)

    root.mainloop()

create_interface()
