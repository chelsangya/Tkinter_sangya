from tkinter import *
from PIL import Image, ImageTk

app = Tk()
app.title("Image Viewer")
app.resizable(0, 0)
app["bg"]="#554f57"

#setting frames and variables
frame=Frame(app, width=600, height=600, relief=GROOVE, bd=2)
frame.pack(padx=10, pady=10)
btn_font=("Bickham Script Pro",11,"bold")
btn_bg="black"
btn_fg="#554f57"

#adding images to thumbnails
img1 = Image.open("H:\Tkinter_sangya\Image Viewer\Keep Sailing.jpg")
img1.thumbnail((550, 450))
img2 = Image.open("H:\Tkinter_sangya\Image Viewer\Strong World.jpg")
img2.thumbnail((550, 450))
img3 = Image.open("H:\Tkinter_sangya\Image Viewer\Portgas D Ace.jpg")
img3.thumbnail((550, 450))
img4 = Image.open("H:\Tkinter_sangya\Image Viewer\Ronoroa Zoro.jpg")
img4.thumbnail((550, 450))

#open images for label
image1 = ImageTk.PhotoImage(img1)
image2 = ImageTk.PhotoImage(img2)
image3 = ImageTk.PhotoImage(img3)
image4 = ImageTk.PhotoImage(img4)
images = [image1, image2, image3, image4]

#adding labels 
n = 0
image_label = Label(frame, image=images[n])
image_label.pack()

#defining functions for different buttons
def previous():
    global n
    n = n - 1
    try:
        image_label.config(image=images[n]) 
    except:
        n = 0
        previous()
def next():
    global n
    n = n + 1
    try:
        image_label.config(image=images[n])
    except:
        n = -1
        next()

#setting buttons
previous_btn = Button(app, text="Previous", bg=btn_bg, fg=btn_fg, font=btn_font, relief=GROOVE, command=previous)
previous_btn.pack(side=LEFT, padx=60, pady=5)
exit_btn = Button(app, text="Exit", width=8, bg=btn_bg, fg=btn_fg, font=btn_font, relief=GROOVE, command=app.destroy)
exit_btn.pack(side=LEFT, padx=60, pady=5)
next_btn = Button(app, text="Next", width=8, bg=btn_bg, fg=btn_fg, font=btn_font, relief=GROOVE, command=next)
next_btn.pack(side=LEFT, padx=60, pady=5)

app.mainloop()