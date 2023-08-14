#!/usr/bin/env python
# coding: utf-8

# # necessearry libaries

# In[2]:


from tkinter import *
from tkinter import ttk
from googletrans import Translator,LANGUAGES


# In[3]:


root = Tk()
root.geometry('1080x400')
root.resizable(0,0)
root.config(bg = 'ghost white')

# Tk() initialized tkinter which means window created,
#geometry() set the width and height of the window,
#resizable(0,0) set the fixed size of the window,
#bg = ‘’ use to set the background color
# In[4]:


root.title("Project Code Alpha--Language Translator_Ele K")
Label(root,text = "LANGUAGE TRANSLATOR", font ="arial 20 bold", bg='white smoke').pack()
Label(root,text = "@Code Alpha | Krishanu", font ='arial 15 bold', bg = 'white smoke',width ='25').pack(side = 'bottom')

#title() used to set the title of the window
#Label() widget use to display one or more than one line of text that users aren’t able to modify.
#root is the name which we refer to our window
#text which we display on the label
#font in which the text is written
#pack organized widget in block
# # Create an Input-output text widget

# In[5]:


Label(root,text ="Enter Text", font = 'arial 13 bold', bg ='white smoke').place(x=200,y=50)
Input_text = Text(root,font = 'arial 15', height = 11, wrap = WORD, padx=5, pady=5, width = 60)
Input_text.place(x=30,y = 100)
Label(root,text ="Output", font = 'arial 13 bold', bg ='white smoke').place(x=780,y=60)
Output_text = Text(root,font = 'arial 15', height = 11, wrap = WORD, padx=5, pady= 5, width =60)
Output_text.place(x = 600 , y = 100)

#Text() widget is used for multiple text lines.
#wrap = WORD will stop the line after the last word that will fit.
#padx puts an extra bit of space to the left and right of the widget.
#pady adds an extra bit of space to the top and bottom.
# # Define Combobox to select the language

# In[6]:


language = list(LANGUAGES.values())
src_lang = ttk.Combobox(root, values= language, width =22)
src_lang.place(x=20,y=60)
src_lang.set('choose input language')
dest_lang = ttk.Combobox(root, values= language, width =22)
dest_lang.place(x=890,y=60)
dest_lang.set('choose output language')

#language gets all the values from the ‘LANGUAGES’ dictionary in the form of a list.
#ttk.Combobox() widget is a class of ttk modules. It is a drop-down list, which can hold multi-value and show one item at a #time. Combobox is useful to select one option from many option.
# # Define Function

# In[7]:


def Translate():
    translator = Translator()
    translated=translator.translate(text= Input_text.get(1.0, END) , src = src_lang.get(), dest = dest_lang.get())
    Output_text.delete(1.0, END)
    Output_text.insert(END, translated.text)

#src gets the language selected as input text language
#dest gets the language select to translate
#text gets the input text entered by the user.”1.0″ means that the input should be read from zero characters to line one
#The END part means to read the text until the end is reached
#translator = Translator() used to create a Translator class object
#Output_text.delete(1.0, END) delete all the text from line one to end
#Output_text.insert (END, translated.text) will insert the translated text in Output_text
# # Create a translate button

# In[ ]:




#Button() widget used to display button on our window
#command is called when we click the button
#activebackground sets the background color to use when the button is active
#root.mainloop() is a method that executes when we want to run our program.
# In[8]:


trans_btn = Button(root, text = 'Translate', font = 'Georgia 12 bold', pady = 5, command = Translate, bg = 'royal blue', activebackground = 'sky blue')
trans_btn.place(x = 490, y = 300)


# In[9]:


root.mainloop()


# In[10]:


trans_btn = Button (root, text = 'Translate',font = 'arial 12 bold',pady = 5,command = Translate , bg = 'blue', activebackground = 'sky blue')
trans_btn.place(x = 490, y= 180 )


# In[ ]:




