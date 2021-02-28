from tkinter import *
from tkinter import messagebox

window = Tk()

prev_text = ""


def timer():
    global prev_text
    if len(text.get("1.0", END)) != 1:
        if text.get("1.0", END) == prev_text:
            messagebox.showerror("No more time", "You ran out of time!")
            window.destroy()
        prev_text = text.get("1.0", END)
    window.after(5000, timer)


window.title("Disappearing Text")

canvas = Canvas(width=700, height=200)

title = canvas.create_text(350, 30, text="Welcome to the disappearing text desktop app!", width=6000,
                           font=("Arial", 20, "bold"))
subtitle = canvas.create_text(350, 55, text="Get started by writing in the box below! Text will be deleted after 5 "
                                            "seconds of inactivity!", width=6000, font=("Arial", 13),
                              fill="gray")
canvas.pack()

text = Text(window, height=30, width=90)
text.focus()
text.pack()
timer()


window.mainloop()
