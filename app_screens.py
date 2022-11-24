import tkinter as tk

class Main_Screen(tk.Tk):

    def __init__(self, root, action_draw_record, action_draw_load):
        self.root = root

        # Window Property
        self.root.geometry("270x100")
        self.root.title("Pancha Bot")

        # Commands
        self.action_draw_record = action_draw_record
        self.action_draw_load = action_draw_load

        # Grid Config
        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_rowconfigure(1, weight=1)

        # Record button
        self.btn_record = tk.Button(self.root, text="Record", command=self.action_draw_record)
        self.btn_record.grid(column=0, row=0, ipadx=100, padx=5, pady=5)

        # Load button
        self.btn_load = tk.Button(self.root, text="Load",command=self.action_draw_load)
        self.btn_load.grid(column=0, row=1, ipadx=107, padx=5, pady=5)


class Record_Screen(tk.Tk):

    def __init__(self, root, action_start_recording):
        self.root = root

        # Window property
        self.root.geometry("280x100")
        self.root.title("Pancha Bot")

        # Commands
        self.action_start_recording = action_start_recording

        # Grid config
        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_rowconfigure(1, weight=1)

        # Label
        self.lbl_filename = tk.Label(self.root, text="Filename: ")
        self.lbl_filename.grid(column=0, row=0)

        # Filename
        self.txt_filename = tk.Entry(self.root)
        self.txt_filename.grid(column=1, row=0, sticky="we")

        # Record Button
        self.btn_record = tk.Button(self.root, text="Record",command= lambda: self.action_start_recording(self.txt_filename.get()))
        self.btn_record.grid(column=0, row=1, sticky="we", ipadx=100, padx=5, pady=5, columnspan=2)

    def clear(self):
        self.txt_filename.set("")

class Play_Screen(tk.Tk):

    def __init__(self, root, action_choose_recording, action_play_recording):
        self.root = root

        # Window Property
        self.root.geometry("280x100")
        self.root.title("Pancha Bot")

        # Commands
        self.action_choose_recording = action_choose_recording
        self.action_play_recording = action_play_recording

        # Grid config
        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_rowconfigure(1, weight=1)

        # Record Button
        self.btn_play = tk.Button(self.root, text="Play",command=self.action_play_recording)
        self.btn_play.grid(column=0, row=0, padx=5, pady=5, ipadx=114)

        # Choose Action Button
        self.btn_record = tk.Button(self.root, text="Choose Recording", command=self.action_choose_recording)
        self.btn_record.grid(column=0, row=1, padx=5, pady=5, ipadx=67)