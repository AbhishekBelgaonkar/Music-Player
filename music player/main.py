from tkinter import *
from pygame import mixer
import pygame
from tkinter import filedialog
pygame.mixer.init()
root = Tk()
root.title("MP3 Player")
root.configure(bg="black")
icon = pygame.image.load("images/play.png")
pygame.display.set_icon(icon)
root.geometry("500x300")

# add song function
def addsong():
	song = filedialog.askopenfilename(initialdir = 'music/', title = "choose a song", filetypes = (("mp3 files", "*.mp3"),))
	song = song.replace("C:/Users/abhis/Documents/GitHub/Music-Player/music player/music/", "")
	song = song.replace(".mp3","")
	songbox.insert(END, song)
songbox = Listbox(root, bg= "white", fg="red", width = 60)
songbox.pack(pady = 20)
# music control buttons
back_btn_img = PhotoImage(file = 'images/back.png')
forward_btn_img = PhotoImage(file = 'images/forward.png')
play_btn_img = PhotoImage(file = 'images/play.png')
pause_btn_img = PhotoImage(file = 'images/pause.png')
stop_btn_img = PhotoImage(file = 'images/stop.png')
# create pplayer control frame
controls_frame = Frame(root)
controls_frame.pack()
# music button work
back_button = Button(controls_frame, image = back_btn_img, borderwidth = 0)
forward_button = Button(controls_frame, image = forward_btn_img , borderwidth = 0)
stop_button = Button(controls_frame, image = stop_btn_img, borderwidth = 0)
pause_button = Button(controls_frame, image = pause_btn_img, borderwidth = 0)
play_button = Button(controls_frame, image = play_btn_img, borderwidth = 0)

back_button.grid(row = 0, column = 0, padx = 10)
stop_button.grid(row = 0, column = 1, padx = 10)
play_button.grid(row = 0, column = 2, padx = 10)
pause_button.grid(row = 0, column = 3, padx = 10)
forward_button.grid(row = 0, column = 4, padx = 10)

# create menu
my_menu = Menu(root)
root.config(menu = my_menu)

# add song

add_song_menu = Menu(my_menu)
my_menu.add_cascade(label = "add songs", menu = add_song_menu)
add_song_menu.add_command(label = "add 1 song to playlist", command = addsong)




'''
def play_music():
    mixer.music.load("music/Giorno Theme (Trap Remix).mp3")
    mixer.music.play()
playPhoto = PhotoImage(file="images/Play-Music-icon.png")
playBtn = Button(root, image=playPhoto, borderwidth=0, command = play_music)
playBtn.pack()
'''
root.mainloop()