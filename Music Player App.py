from pygame import mixer
from tkinter import *
import tkinter.font as font
from tkinter import filedialog
root = Tk()
root.title('Music player App')
root.attributes('-fullscreen', True)  
root.configure(bg="black")  
mixer.init()

current_song = None  # To store the current song path
song_position = 0    # To store the current position in seconds

def addsongs():
    temp_songs = filedialog.askopenfilenames(initialdir="Music/", title="Choose a song", filetypes=(("mp3 Files", "*.mp3"),))
    for s in temp_songs:
        songs_list.insert(END, s)

def deletesong():
    curr_song = songs_list.curselection()
    songs_list.delete(curr_song[0])

def Play():
    global current_song, song_position
    current_song = songs_list.get(ACTIVE)
    song_position = 0  # Reset position to start
    mixer.music.load(current_song)
    mixer.music.play()

def Pause():
    global song_position
    song_position = mixer.music.get_pos() // 1000  # Store current position in seconds
    mixer.music.pause()

def Stop():
    global song_position
    song_position = 0  # Reset position
    mixer.music.stop()
    songs_list.selection_clear(ACTIVE)

def Resume():
    global song_position
    mixer.music.load(current_song)  
    mixer.music.play(start=song_position)  

def Previous():
    current_index = songs_list.curselection()[0]
    previous_index = current_index - 1 if current_index > 0 else songs_list.size() - 1
    previous_song = songs_list.get(previous_index)
    mixer.music.load(previous_song)
    mixer.music.play()
    songs_list.selection_clear(0, END)
    songs_list.activate(previous_index)
    songs_list.selection_set(previous_index)

def Next():
    current_index = songs_list.curselection()[0]
    next_index = current_index + 1 if current_index < songs_list.size() - 1 else 0
    next_song = songs_list.get(next_index)
    mixer.music.load(next_song)
    mixer.music.play()
    songs_list.selection_clear(0, END)
    songs_list.activate(next_index)
    songs_list.selection_set(next_index)


def Forward():
    global song_position
    song_position += 10  
    mixer.music.load(current_song)
    mixer.music.play(start=song_position)  


def Backward():
    global song_position
    song_position = max(0, song_position - 10)  # Decrease by 10 seconds, ensuring it doesn’t go below 0
    mixer.music.load(current_song)
    mixer.music.play(start=song_position)


songs_list = Listbox(root, selectmode=SINGLE, bg="black", fg="white", font=('arial', 15), selectbackground="gray", selectforeground="black")
songs_list.grid(row=0, column=0, columnspan=5, padx=20, pady=20, sticky="nsew")


root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)

defined_font = font.Font(family='Helvetica', size=12, weight='bold')
button_frame = Frame(root, bg="black")
button_frame.grid(row=1, column=0, columnspan=5, pady=20)


play_button = Button(button_frame, text="Play", width=7, command=Play, font=defined_font)
pause_button = Button(button_frame, text="Pause", width=7, command=Pause, font=defined_font)
stop_button = Button(button_frame, text="Stop", width=7, command=Stop, font=defined_font)
resume_button = Button(button_frame, text="Resume", width=7, command=Resume, font=defined_font)
previous_button = Button(button_frame, text="Prev", width=7, command=Previous, font=defined_font)
next_button = Button(button_frame, text="Next", width=7, command=Next, font=defined_font)
backward_button = Button(button_frame, text="<< 10s", width=7, command=Backward, font=defined_font)
forward_button = Button(button_frame, text="10s >>", width=7, command=Forward, font=defined_font)
backward_button.grid(row=0, column=0, padx=10, pady=5)
previous_button.grid(row=0, column=1, padx=10, pady=5)
play_button.grid(row=0, column=2, padx=10, pady=5)
pause_button.grid(row=0, column=3, padx=10, pady=5)
stop_button.grid(row=0, column=4, padx=10, pady=5)
resume_button.grid(row=0, column=5, padx=10, pady=5)
next_button.grid(row=0, column=6, padx=10, pady=5)
forward_button.grid(row=0, column=7, padx=10, pady=5)
my_menu = Menu(root)
root.config(menu=my_menu)
add_song_menu = Menu(my_menu)
my_menu.add_cascade(label="Menu", menu=add_song_menu)
add_song_menu.add_command(label="Add songs", command=addsongs)
add_song_menu.add_command(label="Delete song", command=deletesong)
mainloop()
