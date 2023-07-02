from tkinter import *
import pyqrcode
from PIL import ImageTk, Image
from tkinter import colorchooser
from tkinter import filedialog

root = Tk()
root.configure(bg="#F7F7F7")  # Set GUI background color
root.attributes('-fullscreen', True)  # Enable fullscreen mode
root.title("QR Code Generator")  # Set window title
root.attributes('-topmost', True)  # Make the window always on top
root.attributes('-toolwindow', True)  # Set the window as a tool window

def generate():
    link_name = name_entry.get()
    link = link_entry.get()
    file_name = link_name + ".png"
    url = pyqrcode.create(link)
    foreground_color = fore_color.get()
    background_color = back_color.get()
    url.png(file_name, scale=9, module_color=foreground_color, background=background_color)
    image = ImageTk.PhotoImage(Image.open(file_name))
    qr_code_label.configure(image=image)
    qr_code_label.image = image

def choose_foreground_color():
    color = colorchooser.askcolor(title="Select Foreground Color")
    if color:
        fore_color.set(color[1])

def choose_background_color():
    color = colorchooser.askcolor(title="Select Background Color")
    if color:
        back_color.set(color[1])

def save_qr_code():
    file_path = filedialog.asksaveasfilename(defaultextension=".png")
    if file_path:
        qr_code_label.image.save(file_path)

canvas = Canvas(root, width=400, height=600)
canvas.pack()

app_label = Label(root, text="QR Code Generator", fg="#333333", font=("Arial", 30), bg="#F7F7F7")  # Set logo name color
canvas.create_window(200, 50, window=app_label)

name_label = Label(root, text='Link Name', bg="#F7F7F7")  # Set label background color
link_label = Label(root, text="Link", bg="#F7F7F7")  # Set label background color
canvas.create_window(200, 100, window=name_label)
canvas.create_window(200, 160, window=link_label)

name_entry = Entry(root)
link_entry = Entry(root)
canvas.create_window(200, 130, window=name_entry)
canvas.create_window(200, 180, window=link_entry)

fore_color = StringVar()
back_color = StringVar()

fore_color.set("#000000")  # Default foreground color
back_color.set("#FFFFFF")  # Default background color

fore_color_button = Button(text="Select Foreground Color", command=choose_foreground_color, bg="#5F9EA0", fg="#FFFFFF")
back_color_button = Button(text="Select Background Color", command=choose_background_color, bg="#5F9EA0", fg="#FFFFFF")

canvas.create_window(200, 250, window=fore_color_button)
canvas.create_window(200, 280, window=back_color_button)

button = Button(text="Generate QR Code", command=generate, bg="#5F9EA0", fg="#FFFFFF")
canvas.create_window(200, 320, window=button)

qr_code_frame = Frame(root, width=300, height=300, bg="#FFFFFF", bd=1, relief=SOLID)  # Adjust the dimensions as desired
canvas.create_window(200, 450, window=qr_code_frame)  # Adjusted y-coordinate for the QR code frame
qr_code_label = Label(qr_code_frame, bg="#FFFFFF")
qr_code_label.pack()

save_button = Button(text="Save QR Code", command=save_qr_code, bg="#5F9EA0", fg="#FFFFFF")
canvas.create_window(200, 520, window=save_button)  # Adjusted y-coordinate for the save button

root.mainloop()
