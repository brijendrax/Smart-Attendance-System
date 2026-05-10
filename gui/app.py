import tkinter as tk
from tkinter import messagebox
import os

window = tk.Tk()

window.title("Smart Attendance System")

window.geometry("600x400")

window.config(bg="#1e1e1e")

title = tk.Label(
    window,
    text="SMART ATTENDANCE SYSTEM",
    font=("Arial", 20, "bold"),
    bg="#1e1e1e",
    fg="white"
)

title.pack(pady=20)

def capture_faces():

    os.system("python src/capture.py")

def train_model():

    os.system("python src/train.py")

    messagebox.showinfo(
        "Success",
        "Model Trained Successfully"
    )

def start_attendance():

    os.system("python src/recognize.py")

capture_btn = tk.Button(
    window,
    text="Capture Faces",
    font=("Arial", 14),
    width=20,
    bg="#4CAF50",
    fg="white",
    command=capture_faces
)

capture_btn.pack(pady=10)

train_btn = tk.Button(
    window,
    text="Train Model",
    font=("Arial", 14),
    width=20,
    bg="#2196F3",
    fg="white",
    command=train_model
)

train_btn.pack(pady=10)

attendance_btn = tk.Button(
    window,
    text="Start Attendance",
    font=("Arial", 14),
    width=20,
    bg="#FF9800",
    fg="white",
    command=start_attendance
)

attendance_btn.pack(pady=10)

exit_btn = tk.Button(
    window,
    text="Exit",
    font=("Arial", 14),
    width=20,
    bg="red",
    fg="white",
    command=window.destroy
)

exit_btn.pack(pady=20)

window.mainloop()