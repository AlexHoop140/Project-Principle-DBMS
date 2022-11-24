from tkinter import *


def btn_clicked():
    print("Button Clicked")


window = Tk()

window.geometry("600x900")
window.configure(bg = "#9ba4b4")
canvas = Canvas(
    window,
    bg = "#9ba4b4",
    height = 900,
    width = 600,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge")
canvas.place(x = 0, y = 0)

background_img = PhotoImage(file = f"background.png")
background = canvas.create_image(
    300.0, 445.0,
    image=background_img)

entry0_img = PhotoImage(file = f"img_textBox0.png")
entry0_bg = canvas.create_image(
    289.0, 99.5,
    image = entry0_img)

entry0 = Entry(
    bd = 0,
    bg = "#d9d9d9",
    highlightthickness = 0)

entry0.place(
    x = 81, y = 81,
    width = 416,
    height = 35)

entry1_img = PhotoImage(file = f"img_textBox1.png")
entry1_bg = canvas.create_image(
    289.0, 177.5,
    image = entry1_img)

entry1 = Entry(
    bd = 0,
    bg = "#d9d9d9",
    highlightthickness = 0)

entry1.place(
    x = 81, y = 159,
    width = 416,
    height = 35)

entry2_img = PhotoImage(file = f"img_textBox2.png")
entry2_bg = canvas.create_image(
    175.5, 254.5,
    image = entry2_img)

entry2 = Entry(
    bd = 0,
    bg = "#d9d9d9",
    highlightthickness = 0)

entry2.place(
    x = 82, y = 236,
    width = 187,
    height = 35)

entry3_img = PhotoImage(file = f"img_textBox3.png")
entry3_bg = canvas.create_image(
    404.5, 254.5,
    image = entry3_img)

entry3 = Entry(
    bd = 0,
    bg = "#d9d9d9",
    highlightthickness = 0)

entry3.place(
    x = 311, y = 236,
    width = 187,
    height = 35)

entry4_img = PhotoImage(file = f"img_textBox4.png")
entry4_bg = canvas.create_image(
    175.5, 331.5,
    image = entry4_img)

entry4 = Entry(
    bd = 0,
    bg = "#d9d9d9",
    highlightthickness = 0)

entry4.place(
    x = 82, y = 313,
    width = 187,
    height = 35)

entry5_img = PhotoImage(file = f"img_textBox5.png")
entry5_bg = canvas.create_image(
    404.5, 331.5,
    image = entry5_img)

entry5 = Entry(
    bd = 0,
    bg = "#d9d9d9",
    highlightthickness = 0)

entry5.place(
    x = 311, y = 313,
    width = 187,
    height = 35)

entry6_img = PhotoImage(file = f"img_textBox6.png")
entry6_bg = canvas.create_image(
    175.5, 407.5,
    image = entry6_img)

entry6 = Entry(
    bd = 0,
    bg = "#d9d9d9",
    highlightthickness = 0)

entry6.place(
    x = 82, y = 389,
    width = 187,
    height = 35)

entry7_img = PhotoImage(file = f"img_textBox7.png")
entry7_bg = canvas.create_image(
    404.5, 407.5,
    image = entry7_img)

entry7 = Entry(
    bd = 0,
    bg = "#d9d9d9",
    highlightthickness = 0)

entry7.place(
    x = 311, y = 389,
    width = 187,
    height = 35)

entry8_img = PhotoImage(file = f"img_textBox8.png")
entry8_bg = canvas.create_image(
    288.0, 483.5,
    image = entry8_img)

entry8 = Entry(
    bd = 0,
    bg = "#d9d9d9",
    highlightthickness = 0)

entry8.place(
    x = 80, y = 465,
    width = 416,
    height = 35)

img0 = PhotoImage(file = f"img0.png")
b0 = Button(
    image = img0,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b0.place(
    x = 83, y = 530,
    width = 187,
    height = 62)

img1 = PhotoImage(file = f"img1.png")
b1 = Button(
    image = img1,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b1.place(
    x = 306, y = 530,
    width = 187,
    height = 62)

entry9_img = PhotoImage(file = f"img_textBox9.png")
entry9_bg = canvas.create_image(
    290.0, 674.5,
    image = entry9_img)

entry9 = Entry(
    bd = 0,
    bg = "#d9d9d9",
    highlightthickness = 0)

entry9.place(
    x = 82, y = 656,
    width = 416,
    height = 35)

img2 = PhotoImage(file = f"img2.png")
b2 = Button(
    image = img2,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b2.place(
    x = 83, y = 741,
    width = 187,
    height = 62)

img3 = PhotoImage(file = f"img3.png")
b3 = Button(
    image = img3,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b3.place(
    x = 308, y = 741,
    width = 187,
    height = 62)

window.resizable(False, False)
window.mainloop()
