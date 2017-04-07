#The program parses the news from the news portal "Globo.com" and returns the news titles one by one to the user. 
#After starting the program, user needs to press the button (made with Tkinter) to get the news.
from lxml import html
import requests
from bs4 import BeautifulSoup
import io 
from tkinter import *
import tkinter
from tkinter import messagebox
def news():
    page = requests.get('http://www.globo.com/index.html')
    
    soup = BeautifulSoup(page.content, 'html.parser')
    bbb = soup.find_all('p', class_='hui-premium__title')
    
    for item in bbb:
        ccc = item.get_text('p')
       
        messagebox.showinfo('Read the news and press OK',ccc)
    messagebox.showinfo("Done","You've just read all the latest news from Globo.com")
    
master = Tk()

b = Button(master, height=7, width=38, text='Show me the latest Globo.com news, one by one', command=news)
b.pack()

mainloop()
