import cv2
import matplotlib.pyplot as plt
import numpy as np 
from tkinter import * 
from PIL import Image, ImageTk
import tkinter as tkinter

# without GUI

img1 = cv2.imread('dp.jpg', 0)
[m,n] = img1.shape
print('Image Shape: ', m, n)
print('Original Image: ')
plt.imshow(img1, cmap="gray")
# plt.figure()
plt.show()
# going to down sample through the factor of 4
# print(" ")
f = int(input("Enter the down sampling rate f :"))
print(f)
img2 = np.zeros((m//f, n//f), dtype= int)
# Assign the down sampled values from the original
# image according to the down sampling frequency.
# For example, if the down sampling rate f=2, take
# pixel values from alternate rows and columns
# and assign them in the matrix created above
for i in range(0, m, f):
    for j in range(0, n, f):
        try:
            img2[i//f][j//f] = img1[i][j]
        except IndexError:
            pass
plt.imshow(img2, cmap="gray")
plt.show()


# window = Tk()
# window.title("Down Sampling")
# window.geometry("800x800")



# canv = Canvas(root, width=80, height=80, bg='white')
# canv.grid(row=2, column=3)

# img = PhotoImage(file=image)

# canvas_width = 800
# canvas_height = 800

# canvas = Canvas(window, height= canvas_height, width= canvas_width)
# window.update()
# # canvas.pack(fill=tkinter.BOTH, expand=1)
# # colored_image =  cv2.imread('dp.jpg', 0)
# # gray_image = cv2.cvtColor(colored_image, cv2.COLOR_BGR2GRAY)
# label = Label(text= 'Enter the fraction through which you want to down-sample= ')
# nos = tkinter.Entry()
# nos.pack()
# nums = nos.get()
# print(nums)
# window.update()

# # inputtxt = tkinter.Text(window, height = 5, width = 20)
# # print(inputtxt.get(1.0, "end-1c"))  
# # inputtxt.pack()
# # cv2.imwrite("colored_image.jpeg", colored_image)
# # Load an image in script
# img = ImageTk.PhotoImage(Image.open("colored_image.jpeg"))
# # canvas.bind("<Button-1>")
# # add image to canvas

# canvas.create_image(0,0, anchor= NW, image= img)
# window.mainloop()






