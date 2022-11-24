from tkinter import *
import mysql.connector
import sys

############### CONNECTION SECTION ################
try:
    conn = mysql.connector.connect(
        user="root",
        password="FzrTscd0aGODkVIUXtsa",
        host="containers-us-west-44.railway.app",
        port=5960,
        database="railway"
    )

    cur = conn.cursor()
except mysql.connector.Error as e:
    print(f"Error connecting to Mysql Platform: {e}")
    conn.rollback()
    sys.exit(1)


def btn_clicked():
    print("Button Clicked")

def btn_clicked2():
    plane_root = Tk()
    plane_root.title('DBMS Project')
    plane_root.geometry("400x600")
    plane_id_label = Label(plane_root, text="Plane ID")
    plane_id_label.grid(row=0, column=0)


plane_window = Tk()

plane_window.geometry("600x900")
plane_window.configure(bg = "#9ba4b4")
plane_window.title('Plane Management')
plane_canvas = Canvas(
    plane_window,
    bg = "#9ba4b4",
    height = 900,
    width = 600,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge")
plane_canvas.place(x = 0, y = 0)

plane_background_img = PhotoImage(file = f"img/Plane/background.png")
plane_canvas.create_image(
    165.0, 423.5,
    image=plane_background_img)

plane_entry0_img = PhotoImage(file = f"img/Plane/img_textBox0.png")
plane_entry0_bg = plane_canvas.create_image(
    290.0, 91.5,
    image = plane_entry0_img)

plane_entry0 = Entry(
    bd = 0,
    bg = "#d9d9d9",
    highlightthickness = 0)

plane_entry0.place(
    x = 82, y = 73,
    width = 416,
    height = 35)

plane_entry1_img = PhotoImage(file = f"img/Plane/img_textBox1.png")
plane_entry1_bg = plane_canvas.create_image(
    290.0, 169.5,
    image = plane_entry1_img)

plane_entry1 = Entry(
    bd = 0,
    bg = "#d9d9d9",
    highlightthickness = 0)

plane_entry1.place(
    x = 82, y = 151,
    width = 416,
    height = 35)

plane_entry2_img = PhotoImage(file = f"img/Plane/img_textBox2.png")
plane_entry2_bg = plane_canvas.create_image(
    291.0, 246.5,
    image = plane_entry2_img)

plane_entry2 = Entry(
    bd = 0,
    bg = "#d9d9d9",
    highlightthickness = 0)

plane_entry2.place(
    x = 83, y = 228,
    width = 416,
    height = 35)

plane_entry3_img = PhotoImage(file = f"img/Plane/img_textBox3.png")
plane_entry3_bg = plane_canvas.create_image(
    176.5, 323.5,
    image = plane_entry3_img)

plane_entry3 = Entry(
    bd = 0,
    bg = "#d9d9d9",
    highlightthickness = 0)

plane_entry3.place(
    x = 83, y = 305,
    width = 187,
    height = 35)

plane_entry4_img = PhotoImage(file = f"img/Plane/img_textBox4.png")
plane_entry4_bg = plane_canvas.create_image(
    405.5, 323.5,
    image = plane_entry4_img)

plane_entry4 = Entry(
    bd = 0,
    bg = "#d9d9d9",
    highlightthickness = 0)

plane_entry4.place(
    x = 312, y = 305,
    width = 187,
    height = 35)

plane_entry5_img = PhotoImage(file = f"img/Plane/img_textBox5.png")
plane_entry5_bg = plane_canvas.create_image(
    290.0, 401.5,
    image = plane_entry5_img)

plane_entry5 = Entry(
    bd = 0,
    bg = "#d9d9d9",
    highlightthickness = 0)

plane_entry5.place(
    x = 82, y = 383,
    width = 416,
    height = 35)

plane_img0 = PhotoImage(file = f"img/Plane/img0.png")
plane_b0 = Button(
    image = plane_img0,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked2,
    relief = "flat")

plane_b0.place(
    x = 144, y = 452,
    width = 293,
    height = 62)

plane_img1 = PhotoImage(file = f"img/Plane/img1.png")
plane_b1 = Button(
    image = plane_img1,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

plane_b1.place(
    x = 144, y = 530,
    width = 293,
    height = 62)

plane_entry6_img = PhotoImage(file = f"img/Plane/img_textBox6.png")
plane_entry6_bg = plane_canvas.create_image(
    290.0, 674.5,
    image = plane_entry6_img)

plane_entry6 = Entry(
    bd = 0,
    bg = "#d9d9d9",
    highlightthickness = 0)

plane_entry6.place(
    x = 82, y = 656,
    width = 416,
    height = 35)

plane_img2 = PhotoImage(file = f"img/Plane/img2.png")
plane_b2 = Button(
    image = plane_img2,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

plane_b2.place(
    x = 83, y = 741,
    width = 187,
    height = 62)

plane_img3 = PhotoImage(file = f"img/Plane/img3.png")
plane_b3 = Button(
    image = plane_img3,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

plane_b3.place(
    x = 308, y = 741,
    width = 187,
    height = 62)

plane_window.resizable(False, False)
plane_window.mainloop()
