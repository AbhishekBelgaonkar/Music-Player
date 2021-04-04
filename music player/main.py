from tkinter import *
from pygame import mixer

mixer.init()

root = Tk()
root.configure(bg="black")
root.title("musica")
#root.iconbitmap("Iconshock-Super-Vista-General-Music.ico")
root.geometry("300x300")
def play_music():
    mixer.music.load("music/Giorno Theme (Trap Remix).mp3")
    mixer.music.play()
playPhoto = PhotoImage(file="images/Play-Music-icon.png")
playBtn = Button(root, image=playPhoto, borderwidth=0, command = play_music)
playBtn.pack()

root.mainloop()