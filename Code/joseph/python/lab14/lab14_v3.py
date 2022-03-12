# Lab 14 - Version 3 - Personal Project
# Retrieve a random joke as an image file
# and display it on the users screen in it's own window
# Uses tkinter and requires requests and pillow be installed

import tkinter as tk
import PIL.Image
import PIL.ImageTk
import requests

response_json = requests.get(
    "https://icanhazdadjoke.com",
    headers={"Accept": "application/json"}
).json()

joke_id = response_json["id"]
joke_image = "https://icanhazdadjoke.com/j/" + joke_id + ".png"

im = PIL.Image.open(requests.get(joke_image, stream=True).raw)

root = tk.Tk()
root.title("Dad's Joke World")
root.eval('tk::PlaceWindow . center')

class JokeImage:
    def __init__(self, im):
            self.image = PIL.ImageTk.PhotoImage(im)
        
    def get(self):
        return self.image

img = JokeImage(im).get()
imagelab = tk.Label(root, image = img)
imagelab.grid(row = 0, column = 0)

windowWidth = root.winfo_reqwidth()
windowHeight = root.winfo_reqheight()

positionRight = int(root.winfo_screenwidth()/2 - windowWidth/2)
positionDown = int(root.winfo_screenheight()/2 - windowHeight/2)

root.geometry("+{}+{}".format(positionRight, positionDown))

root.mainloop()
