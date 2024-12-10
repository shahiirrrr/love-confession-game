import tkinter as tk
import random

# Function to handle "YES" button click
def yes_clicked():
    response_label.config(text="I Love You, Too!", fg="red")

# Function to randomly move the "NO" button
def move_button(event):
    max_x = button_frame.winfo_width() - no_button.winfo_width()
    max_y = button_frame.winfo_height() - no_button.winfo_height()
    x = random.randint(0, max_x)
    y = random.randint(0, max_y)
    no_button.place(x=x, y=y)

# Main window setup
window = tk.Tk()
window.title("Love Confession")
window.geometry("600x400")
window.resizable(False, False)

# Label for the question
question_label = tk.Label(
    window, 
    text="I Love You, Do You Love Me?", 
    font=("Arial", 20)
)
question_label.pack(pady=30)

# Frame for the buttons
button_frame = tk.Frame(window, width=500, height=150)
button_frame.pack(pady=20)
button_frame.pack_propagate(False)

# "YES" button
yes_button = tk.Button(
    button_frame, 
    text="YES", 
    font=("Arial", 14), 
    command=yes_clicked
)
yes_button.place(x=150, y=50)

# "NO" button
no_button = tk.Button(
    button_frame, 
    text="NO", 
    font=("Arial", 14), 
)
no_button.place(x=300, y=50)
no_button.bind("<Enter>", move_button)  # Move the button when hovered

# Label to display the response
response_label = tk.Label(
    window, 
    text="", 
    font=("Arial", 18)
)
response_label.pack(pady=30)

# Run the application
window.mainloop()
