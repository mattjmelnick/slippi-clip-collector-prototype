from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
import os
import shutil

replay_path = ""
clip_path = ""

def select_replay_folder() -> str:
    global replay_path
    replay_path = StringVar()
    replay_folder = filedialog.askdirectory(title = "Select Replay Folder")
    replay_path.set(replay_folder)
    replay_path_label = Label(screen, textvariable = replay_path)
    replay_path_label.place(x = 275, y = 95)

def select_clips_folder() -> str:
    global clip_path
    clip_path = StringVar()
    clip_folder = filedialog.askdirectory(title = "Select Clips Folder")
    clip_path.set(clip_folder)
    clip_path_label = Label(screen, textvariable = clip_path)
    clip_path_label.place(x = 275, y = 220)

def move_file_to_clips_folder() -> None:
    print(replay_path.get())
    print(clip_path.get())

def delete_file() -> None:
    pass


root = Tk()
root.title("Slippi Clip Collector")
root.geometry("900x550+800+250")
root.resizable(width = False, height = False)
screen = Frame(root, width = 900, height = 550)
screen.grid()

replay_folder_button = Button(screen, text = "Select Replays Folder", command = select_replay_folder)
replay_folder_button.place(x = 50, y = 75, height = 75, width = 200)

clip_folder_button = Button(screen, text = "Select Clips Folder", command = select_clips_folder)
clip_folder_button.place(x = 50, y = 200, height = 75, width = 200)

save_replay_button = Button(screen, text = "Save", command = move_file_to_clips_folder)
save_replay_button.place(x = 100, y = 325, height = 75, width = 200)

delete_replay_button = Button(screen, text = "Delete", command = delete_file)
delete_replay_button.place(x = 500, y = 325, height = 75, width = 200)

root.mainloop()