import tkinter as tk
from tkinter import *
from tkinter import messagebox
from tkinter.font import Font
import subprocess
import os

#configuring root window
root = tk.Tk()
root.geometry("425x500")
root.title("KeyLog")
root.attributes('-alpha', 0.8)
root.configure(bg="#262187")

#defining font
heading_font = Font(family="Helvetica", size=21, slant="italic", weight="bold")
heading = tk.Label(root, text="KeyLog.", bg=root["bg"], font=heading_font, fg="#ffffff")
heading.grid(row = 1, column=0, columnspan=3, pady=10, padx=0)

#loading animation for Tkinter
animation_frames = ["|", "/", "-", "\\"]
current_frame_index = 0
animation_label = tk.Label(root, text="", font=("Arial", 24))
animation_text = tk.StringVar()
animation_label.config(textvariable=animation_text, fg="white")
animation_label.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
animation_id = None

def update_animation(): #buffering animation
    global current_frame_index, animation_id
    animation_text.set(animation_frames[current_frame_index])
    current_frame_index = (current_frame_index + 1) % len(animation_frames)
    animation_id = root.after(100, update_animation)

def open_file_json(): #function for button that opens json file
    file_path = "strokes.json"
    try:
        with open(file_path):
            subprocess.Popen(["notepad.exe", file_path])
    except FileNotFoundError:
        messagebox.showerror("File not found", "No keystrokes were logged!")

def open_file_txt(): #function that opens txt file
    file_path = "strokes.txt"
    try:
        with open(file_path):
            subprocess.Popen(["notepad.exe", file_path])
    except FileNotFoundError:
        messagebox.showerror("File not found", "No keystrokes were logged!")


def start_execution(): #function for the start button
    global process
    file_path = "keylogger.py" #give path for the keylogger.py file
    process = subprocess.Popen(["python", file_path])
    start_button.config(state=tk.DISABLED)
    stop_button.config(state=tk.NORMAL)
    update_animation()


def stop_execution(): #function for stop button
    global process, current_frame_index
    if process:
        process.terminate()
        print("[-] Keylogger Stopped Execution.")

    start_button.config(state=tk.NORMAL)
    stop_button.config(state=tk.DISABLED)
    current_frame_index = 0
    animation_text.set("")
    if animation_id:
        root.after_cancel(animation_id)
    
    open_file_button.grid(row=4, column=0, padx=50, pady=45, columnspan=2)
    open_file_button_2.grid(row=4, column=2, padx=90, pady=45)

#buttons
start_button = tk.Button(root, text="Start Logging", command=start_execution)
stop_button = tk.Button(root, text="Stop Logging", command=stop_execution, state=tk.DISABLED)
start_button.grid(row=2, column=0, padx=50, pady=45, columnspan=2)
stop_button.grid(row=2, column=2, padx=90, pady=45)

open_file_button = tk.Button(root, text="Open Json File", command=open_file_json)
open_file_button.grid(row=4, column=0, padx=50, pady=45, columnspan=2)
open_file_button.grid_remove()

open_file_button_2 = tk.Button(root, text="Open Text File", command=open_file_txt)
open_file_button_2.grid(row=4, column=2, padx=90, pady=45)
open_file_button_2.grid_remove()

animation_label.config(textvariable=animation_text,bg=root['bg'])
animation_label.grid(row=3, column=0, columnspan=2, padx=10, pady=15)

root.mainloop()
