# Initializing required modules
import os
import sys
import tkinter as tk
from tkinter import ttk, messagebox, simpledialog, filedialog, font
import logging
import shutil
from core import AdminLogin, AdminSetup
from backend import InterfaceDB

# Defining Object
class WelcomingMessage(tk.Tk):
  # Constructing Interface
  def __init__(self):
    super().__init__()

    # Grab Screen Size
    size_screen_width = self.winfo_screenwidth()
    size_screen_height = self.winfo_screenheight()

    # Configure Window
    self.geometry("<X>x<Y>")
    self.title("<Insert Your Title Here>")
    self.iconbitmap("<Locate Your Icon.ico>")
    self.iconphoto(False, tk.PhotoImage(file="<Locate Your Icon.png>"))
    self.resizable(False, False) # preventing window to be rescaled

    # Generate Frame
    self.framework = tk.Frame(self, bg=self.cget("bg")) # Important to define background just in case you apply any theme
    self.framework.pack(side="<left/top/right>", fill="both", ipadx=0, ipady=0) # Check documentation of tkinter
    
    # Initialize Text
    self.generaltext = tk.Label(self.framework, text="<Insert Your Text Here>", anchor="w/e/...", bg=self.cget("bg"), font=font.Font(weight="bold", size=11)) # font.Font enable the style of text to be changed, weight="bold" for bold and slant="italic" for italic)
    self.generaltext.pack(side="<left/top/right>", fill="x", padx=0, pady=0)

    # Initialize Button
    self.continueButton = tk.Button(self.framework, text="<Insert Your Text Here>"), command=self.go)
    self.continueButton.pack(#)

  def go(self):
    # Call AdminLogin.py

  #
  #
  #
    

if __name__ == "__main__":
  app = WelcomingMessage()
  app.mainloop()
