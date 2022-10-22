import tkinter as tk

import custom_button

from twilio.rest import Client
import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

import utils
from PIL import ImageTk, Image
import random


root = tk.Tk()


def start(window):
    window.title("Graphical Authentication System")
    window.geometry("1280x600")

    segments_frame = tk.Frame(window, height=600, width=1280)
    segments_frame.pack(fill='both', expand=1)

    label = tk.Label(segments_frame, text="Please select the pictures in correct order", font=('Calibri', 20))
    label.pack(padx=400, pady=10)

    ## Draw order image

    canvas = tk.Canvas(segments_frame, width=300, height=250)
    canvas.bind("<Button-1>", utils.callback)
    img = (Image.open("order.jpg"))
    img = img.resize((300, 250), Image.ANTIALIAS)
    img = ImageTk.PhotoImage(img)
    canvas.create_image(10, 10, anchor=tk.NW, image=img)
    canvas.pack(padx=10, pady=10)

    imgList = utils.getSegmentedImages("circle")
    random.shuffle(imgList)
    imgClickData = []

    for imgPath in imgList:
        var = utils.imageClick(imgPath)
        imgClickData.append(var)

    # Draw shuffled segments

    canvas2 = tk.Canvas(segments_frame, width=200, height=150)
    canvas2.bind("<Button-1>", imgClickData[0].clicked)
    canvas2.place(x=100, y=400)
    img2 = (Image.open(imgList[0]))
    img2 = img2.resize((200, 150), Image.ANTIALIAS)
    img2 = ImageTk.PhotoImage(img2)
    canvas2.create_image(10, 10, anchor=tk.NW, image=img2)

    canvas3 = tk.Canvas(segments_frame, width=200, height=150)
    canvas3.bind("<Button-1>", imgClickData[1].clicked)
    canvas3.place(x=400, y=400)
    img3 = (Image.open(imgList[1]))
    img3 = img3.resize((200, 150), Image.ANTIALIAS)
    img3 = ImageTk.PhotoImage(img3)
    canvas3.create_image(10, 10, anchor=tk.NW, image=img3)

    canvas4 = tk.Canvas(segments_frame, width=200, height=150)
    canvas4.bind("<Button-1>", imgClickData[2].clicked)
    canvas4.place(x=700, y=400)
    img4 = (Image.open(imgList[2]))
    img4 = img4.resize((200, 150), Image.ANTIALIAS)
    img4 = ImageTk.PhotoImage(img4)
    canvas4.create_image(10, 10, anchor=tk.NW, image=img4)

    canvas5 = tk.Canvas(segments_frame, width=200, height=150)
    canvas5.bind("<Button-1>", imgClickData[3].clicked)
    canvas5.place(x=1000, y=400)
    img5 = (Image.open(imgList[3]))
    img5 = img5.resize((200, 150), Image.ANTIALIAS)
    img5 = ImageTk.PhotoImage(img5)
    canvas5.create_image(10, 10, anchor=tk.NW, image=img5)

    
    count = 0
    while True:
        window.update_idletasks()
        window.update()

        if utils.checkAllClicked(imgClickData):
            sortedClickList = sorted(imgClickData)
            print(sortedClickList[1].id)

            if (sortedClickList[0].id == 1) and (sortedClickList[1].id == 3) and (sortedClickList[2].id == 2) and (
                    sortedClickList[3].id == 4):
                window.destroy()
                import main
            else:
                utils.create_popup(msg="wrong password >_<", font="Gabriola 28 bold")
                count +=1
                if(count>=2):
                   
                    client = Client('AC43ed8984c32d4bc8fd2f7f0d66838bf4', '8e18bdd4907f283ffb2a6a6ba839c38c')
                    message = client.messages.create(
                     body="Join Earth's mightiest heroes. Like Kevin Bacon.",
                     from_='+13143505351',
                     to='+919725268531')
                    print(message.sid)

                    break

            utils.setAllUnclicked(imgClickData)

start(root)