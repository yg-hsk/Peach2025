import tkinter as tk
from tkinter import font as tkfont

root = tk.Tk()
root.title("THE WORLD'S HARDEST GAME")
root.configure(bg="black")

try:
    retro_font = tkfont.Font(family="Press Start 2P", size=10)
except:
    retro_font = tkfont.Font(family="Courier", size=10, weight="bold")

def light_up(button, active_color, original_color):
    button.config(bg=active_color)
    root.after(200, lambda: button.config(bg=original_color))

marquee = tk.Label(root, text="THE WORLD'S HARDEST GAME", bg="red", fg="yellow", font=retro_font)
marquee.pack(fill="x", pady=(10, 5))

screen_frame = tk.Frame(root, bg="black", bd=10, relief="ridge", highlightbackground="red", highlightthickness=4)
screen_frame.pack(pady=10)

screen = tk.Label(
    screen_frame,
    text="LEVEL 1\nAVOID THE OBSTACLES",
    bg="black",
    fg="cyan",
    font=retro_font,
    width=50,
    height=10,
    justify="center"
)
screen.pack()

control_panel = tk.Frame(root, bg="gray20", bd=5, relief="sunken")
control_panel.pack(pady=20)

tk.Label(control_panel, text="PLAYER 1", fg="white", bg="gray20", font=retro_font).pack()

button_frame = tk.Frame(control_panel, bg="gray20")
button_frame.pack()

try:
    w_img = tk.PhotoImage(file="w.png")
    a_img = tk.PhotoImage(file="a.png")
    s_img = tk.PhotoImage(file="s.png")
    d_img = tk.PhotoImage(file="d.png")  
    button_A = tk.Button(button_frame, image=w_img, borderwidth=0, highlightthickness=0, 
                         bg="gray20", activebackground="gray20")
    button_B = tk.Button(button_frame, image=a_img, borderwidth=0, highlightthickness=0, 
                         bg="gray20", activebackground="gray20")
    button_C = tk.Button(button_frame, image=s_img, borderwidth=0, highlightthickness=0, 
                         bg="gray20", activebackground="gray20")
    button_D = tk.Button(button_frame, image=d_img, borderwidth=0, highlightthickness=0, 
                         bg="gray20", activebackground="gray20")
    button_A.image = w_img
    button_B.image = a_img
    button_C.image = s_img
    button_D.image = d_img
    
except:
    button_A = tk.Button(button_frame, text="W", bg="red", fg="white", font=retro_font, width=4)
    button_B = tk.Button(button_frame, text="A", bg="orange", fg="white", font=retro_font, width=4)
    button_C = tk.Button(button_frame, text="S", bg="yellow", fg="black", font=retro_font, width=4)
    button_D = tk.Button(button_frame, text="D", bg="green", fg="white", font=retro_font, width=4)

button_A.grid(row=0, column=0, padx=5, pady=5)
button_B.grid(row=0, column=1, padx=5, pady=5)
button_C.grid(row=1, column=0, padx=5, pady=5)
button_D.grid(row=1, column=1, padx=5, pady=5)

start_button = tk.Button(root, text="START", bg="red", fg="white", font=retro_font)
start_button.pack(pady=10)

def on_key(event):
    key = event.keysym.lower()
    if key == "w":
        light_up(button_A, "white", "gray20")
    elif key == "a":
        light_up(button_B, "white", "gray20")
    elif key == "s":
        light_up(button_C, "white", "gray20")
    elif key == "d":
        light_up(button_D, "white", "gray20")

root.bind("<KeyPress>", on_key)

root.mainloop()