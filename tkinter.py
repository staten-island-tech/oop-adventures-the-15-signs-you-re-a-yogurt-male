# Import necessary libraries
from PIL import ImageTk, Image
import tkinter as tk
import urllib.request
import io

def display_image_from_url(url):
    with urllib.request.urlopen(url) as u:
        raw_data = u.read()

    image = Image.open(io.BytesIO(raw_data))
    photo = ImageTk.PhotoImage(image)

    # Create a Tkinter window
    root = tk.Tk()
    root.title("Image from URL")

    # Create a label widget to display the image
    label = tk.Label(root, image=photo)
    label.pack()

    # Start the Tkinter event loop
    root.mainloop()

# Example usage
display_image_from_url("https://www.tutorialspoint.com/python_pillow/images/tutorials_point.jpg")