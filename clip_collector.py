from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
import os
import shutil
import glob

class App(Tk):
    def __init__(self):
        super().__init__()
        self.title("Slippi Clip Collector")
        self.geometry("800x500+900+250")
        self.resizable(width=False, height=False)
        self.screen = Frame(self, width=800, height=500)
        self.screen.grid()

        self.moved_count = 0
        self.deleted_count = 0
        self.replay_path = ""
        self.clip_path = ""
    
        self.create_gui()

    def create_gui(self):
        self.replay_folder_button = Button(self.screen, text="Select Replays Folder", command=self.select_replay_folder)
        self.replay_folder_button.place(x=50, y=75, height=75, width=200)

        self.clip_folder_button = Button(self.screen, text="Select Clips Folder", command=self.select_clips_folder)
        self.clip_folder_button.place(x=50, y=200, height=75, width=200)

        self.save_replay_button = Button(self.screen, text="Save", command=self.move_file_to_clips_folder)
        self.save_replay_button.place(x=100, y=325, height=75, width=200)

        self.delete_replay_button = Button(self.screen, text="Delete", command=self.delete_file)
        self.delete_replay_button.place(x=500, y=325, height=75, width=200)
    
    def select_replay_folder(self) -> None:
        self.replay_path = StringVar()
        replay_folder = filedialog.askdirectory(title="Select Replay Folder")
        self.replay_path.set(replay_folder)
        replay_path_label = Label(self.screen, textvariable=self.replay_path)
        replay_path_label.place(x=275, y=95)

    def select_clips_folder(self) -> None:
        self.clip_path = StringVar()
        clip_folder = filedialog.askdirectory(title="Select Clips Folder")
        self.clip_path.set(clip_folder)
        clip_path_label = Label(self.screen, textvariable=self.clip_path)
        clip_path_label.place(x=275, y=220)

    def move_file_to_clips_folder(self) -> None:
        replay_path_string = self.replay_path.get() + '/'
        clip_path_string = self.clip_path.get() + '/'

        for _ in os.listdir(replay_path_string):
            file_path = replay_path_string + "*.slp"
            file_list = glob.iglob(file_path)
            newest_file = max(file_list, key=os.path.getmtime)

        self.moved_count += 1
        saved_msg = Label(self.screen, text=f"Moved {self.moved_count} files")
        saved_msg.place(x=100, y=425)
        shutil.move(newest_file, clip_path_string)

    def delete_file(self) -> None:
        replay_path_string = self.replay_path.get() + '/'

        for _ in os.listdir(replay_path_string):
            file_path = replay_path_string + "*.slp"
            file_list = glob.iglob(file_path)
            newest_file = max(file_list, key=os.path.getmtime)
        
        self.deleted_count += 1
        deleted_msg = Label(self.screen, text=f"Deleted {self.deleted_count} files")
        deleted_msg.place(x=500, y=425)
        os.remove(newest_file)

if __name__ == "__main__":
    app = App()
    app.mainloop()
