import recorder
import playback
import app_screens
from tkinter import Tk, Toplevel, filedialog

def main():
    global root
    root = Tk()
    app_screens.Main_Screen(root, draw_record_page, draw_load_page)
    root.mainloop()

#=== MAIN SCREEN ==============================================
def draw_record_page():
    global root 
    recorder_screen = Toplevel(root)
    app_screens.Record_Screen(recorder_screen, start_recording)
    recorder_screen.mainloop()

def draw_load_page():
    global root
    player_screen = Toplevel(root)
    app_screens.Play_Screen(player_screen, choose_recording, play_recording)
    player_screen.mainloop()

#=== RECORD SCREEN ===========================================
def start_recording(filename):
    recorder.Recorder(filename=filename)

#=== PLAY SCREEN ===========================================
def choose_recording():
    global fpath
    fpath = filedialog.askopenfilename()

def play_recording():
    global fpath
    playback.Playback(fpath)

#=== MAIN ====================================================
if __name__ == "__main__":
    main()