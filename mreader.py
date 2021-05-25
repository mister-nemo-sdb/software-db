#!/usr/bin/env python3
from tkinter import filedialog
from tkinter import *
import getpass
import PIL.Image
import PIL.ImageTk
import os

#Window
root = Tk()
root.title('mreader')
root.geometry('500x500')
root.configure(background='gray10')

#Variables
mfont = 'Courier 15'
bg_color = 'gray10'
font_color = 'white'
#=======================
user = getpass.getuser()
directory = None
pg_img = None
index = 0
brightness = 5
zoom = 0
pages = []
#Commands

def load_page():
	global pg_img
	image = PIL.Image.open(pages[index])
	size = image.size
	resized = image.resize((size[0]+(zoom * 20),size[1]+(zoom * 20)))
	recolor = resized.point(lambda p: p * brightness/10)
	pg_img = PIL.ImageTk.PhotoImage(recolor)
	page_img.configure(image=pg_img)
	lb_page.configure(text='Page: '+str(index+1)+'/'+str(len(pages)))
	lb_zoom.configure(text='Zoom: '+str(zoom)+'/20')
	lb_brightness.configure(text='Brightness: '+str(brightness * 10)+'%')

def open_dir(event=None):
	global directory
	directory = filedialog.askdirectory(initialdir='/home/'+user)
	for file in sorted(os.listdir(directory)):
		page = directory+'/'+file
		pages.append(page)
	load_page()

def next_page(event=None):
	global index
	if index +1 < len(pages):
		index += 1
		load_page()

def prev_page(event=None):
	global index
	if index > 0:
		index -= 1
		load_page()

def up_zoom(event=None):
	global zoom
	if zoom < 20:
		zoom += 1
		load_page()

def down_zoom(event=None):
	global zoom
	if zoom > 0:
		zoom -= 1
		load_page()

def up_brightness(event=None):
	global brightness
	if brightness < 10:
		brightness += 1
		load_page()

def down_brightness(event=None):
	global brightness
	if brightness > 1:
		brightness -= 1
		load_page()

#Interface
painel = Frame(root,bg='gray10')
lb_page = Label(painel, text='Page: 0/0', bg=bg_color, fg=font_color, font=mfont)
lb_zoom = Label(painel, text='Zoom: 0/20', bg=bg_color, fg=font_color, font=mfont)
lb_brightness = Label(painel, text='Brightness: 50%', bg=bg_color, fg=font_color, font=mfont)
page_img = Label(root,image=None, bg=bg_color)

#Shotcuts
root.bind('<o>', open_dir)
root.bind('<Right>', next_page)
root.bind('<Left>', prev_page)
root.bind('<Up>', up_zoom)
root.bind('<Down>', down_zoom)
root.bind('<KP_Add>', up_brightness)
root.bind('<KP_Subtract>', down_brightness)

#Positions
painel.pack(side=TOP, fill=X)
lb_page.pack(side=LEFT, padx=20, pady=10)
lb_zoom.pack(side=RIGHT, padx=20, pady=10)
lb_brightness.pack(side=RIGHT, padx=20, pady=10)
page_img.pack()

root.mainloop()
