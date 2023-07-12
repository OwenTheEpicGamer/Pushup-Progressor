# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer


from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"/Users/owen_guo/pushup/build/assets/frame6")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()

window.geometry("1680x1050")
window.configure(bg="#FFFFFF")


canvas = Canvas(
    window,
    bg="#FFFFFF",
    height=1050,
    width=1680,
    bd=0,
    highlightthickness=0,
    relief="ridge",
)

canvas.place(x=0, y=0)
image_image_1 = PhotoImage(file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(960.0, 525.0, image=image_image_1)

canvas.create_rectangle(801.0, 839.0, 1229.0, 928.0, fill="#C74747", outline="")

canvas.create_text(
    849.0,
    860.0,
    anchor="nw",
    text="Start Form Check",
    fill="#FFFFFF",
    font=("RalewayRoman Bold", 40 * -1),
)

canvas.create_rectangle(481.0, 220.0, 1538.0, 803.0, fill="#000000", outline="")

canvas.create_rectangle(
    469.0, 199.0, 480.17822265625, 804.0, fill="#FFFFFF", outline=""
)

canvas.create_rectangle(
    1526.81005859375,
    199.0,
    1537.9988403320312,
    803.9999389648438,
    fill="#FFFFFF",
    outline="",
)

canvas.create_rectangle(
    470.0, 792.2178344726562, 1548.0, 802.2178344726562, fill="#FFFFFF", outline=""
)

canvas.create_rectangle(
    471.188720703125, 199.0, 1537.998779296875, 209.0, fill="#FFFFFF", outline=""
)

canvas.create_rectangle(481.0, 81.0, 796.0, 156.0, fill="#938383", outline="")

canvas.create_rectangle(857.0, 81.0, 1172.0, 156.0, fill="#EE7D7D", outline="")

canvas.create_text(
    589.0,
    95.0,
    anchor="nw",
    text="Knee",
    fill="#FFFFFF",
    font=("RalewayRoman Bold", 40 * -1),
)

canvas.create_text(
    943.0,
    95.0,
    anchor="nw",
    text="Normal",
    fill="#FFFFFF",
    font=("RalewayRoman Bold", 40 * -1),
)

canvas.create_rectangle(1233.0, 81.0, 1548.0, 156.0, fill="#938383", outline="")

canvas.create_text(
    1304.0,
    92.0,
    anchor="nw",
    text="Clapping",
    fill="#FFFFFF",
    font=("RalewayRoman Bold", 40 * -1),
)

canvas.create_rectangle(0.0, 0.0, 349.0, 1050.0, fill="#EE7C7C", outline="")

canvas.create_rectangle(0.0, 202.0, 349.0, 285.0, fill="#C74747", outline="")

"""canvas.create_rectangle(
    0.0,
    285.0,
    349.0,
    368.0,
    fill="#C74747",
    outline="")

canvas.create_rectangle(
    0.0,
    368.0,
    349.0,
    451.0,
    fill="#C74747",
    outline="")

canvas.create_rectangle(
    0.0,
    452.0,
    349.0,
    535.0,
    fill="#C74747",
    outline="")"""

canvas.create_text(
    51.0,
    469.0,
    anchor="nw",
    text="Progressions",
    fill="#FFFFFF",
    font=("RalewayRoman Bold", 40 * -1),
)

canvas.create_text(
    86.0,
    386.0,
    anchor="nw",
    text="Statistics",
    fill="#FFFFFF",
    font=("RalewayRoman Bold", 40 * -1),
)

canvas.create_text(
    92.0,
    303.0,
    anchor="nw",
    text="Workout",
    fill="#FFFFFF",
    font=("RalewayRoman Bold", 40 * -1),
)

canvas.create_text(
    117.0,
    220.0,
    anchor="nw",
    text="Home",
    fill="#FFFFFF",
    font=("RalewayRoman Bold", 40 * -1),
)

canvas.create_text(
    32.0,
    40.0,
    anchor="nw",
    text="Pushup \nProgressor",
    fill="#FFFFFF",
    font=("RalewayRoman Bold", 55 * -1),
)

canvas.create_rectangle(
    -4.99981689453125,
    193.9786376953125,
    349.0,
    205.02142333984375,
    fill="#FFFFFF",
    outline="",
)
window.resizable(False, False)
window.mainloop()