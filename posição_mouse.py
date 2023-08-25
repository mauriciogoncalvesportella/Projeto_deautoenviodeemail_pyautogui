import tkinter as tk
import pyautogui

def update_coordinates():
    x, y = pyautogui.position()
    coordinates_label.config(text=f'X: {x}, Y: {y}')
    root.after(100, update_coordinates)

root = tk.Tk()
root.title("Mouse Position Tracker")
root.geometry("300x50")

coordinates_label = tk.Label(root, text="", font=("Helvetica", 14))
coordinates_label.pack(pady=10)

update_coordinates()

root.mainloop()
