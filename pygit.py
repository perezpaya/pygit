#!/usr/bin/env python
# Imports
from Tkinter import *
import tkFileDialog
from os import popen
from os import path

# Windows

window = Tk()
window.title('PyGit')
window.minsize(500,500)
window.maxsize(1000,1000)
window.configure(background='white')
#window.iconify()
#window.deiconify()

# Vars

repoPath = StringVar()
msg = StringVar()
mainlabel = StringVar()
terminal = StringVar()
# Functions

def write (output):
	text.insert(END, output+'\n')

def pull ():
	pull = popen('cd '+ repoPath.get() +' && git pull')
	write(pull.read())

def commit ():
	if(msg):
		add = popen('cd '+repoPath.get()+' && git add .')
		write(add.read())
		commit = popen(('cd '+repoPath.get()+' && git commit -m \"' + msg.get()+'\"'))
		write(commit.read())
	else:
		write("needed msg in commit")

def push ():
	push = popen('cd '+repoPath.get()+' && git push')
	write(push.read())

def log ():
	log = popen('cd ' + repoPath.get() + ' && git log');
	write(log.read())

def showRemotes ():
	remotes = popen('cd ' + repoPath.get() + ' && git remote -v')
	write(remotes.read())

def selectPath ():
	openPath(tkFileDialog.askdirectory(parent=window, title="Select a Git Repository Path"))

def openPath (p):
	if(p != ""):
		if(path.exists(p)):
			repoPath.set(p)
			mainlabel.set(repoPath.get())
			commitLabel = Label(window, text="Commit message:")
			commitLabel.grid(row=2, column=1)
			commitLabel.configure(background='white')
			message = Entry(window, textvariable=msg)
			message.grid(row=3, column=1)
			message.configure(background='white')
			commitButton = Button(window, text="Commit", command=commit, width=20)
			commitButton.grid(row=4, column=1)
			commitButton.configure(background='white')
			pushButton = Button(window, text="Push", command=push, width=20)
			pushButton.grid(row=5, column=1)
			pushButton.configure(background='white')
			pullButton = Button(window, text="Pull", command=pull, width= 20)
			pullButton.grid(row=6, column=1)
			logButton = Button(window, text="Show log", command=log, width= 20)
			logButton.grid(row=7, column=1)
			logButton.configure(background='white')
			remotesButton = Button(window, text="Show remotes", command=showRemotes, width= 20)
			remotesButton.grid(row=8, column=1)
			remotesButton.configure(background='white')
			select.grid(row=7, column=1)
		else:
			mainlabel.set('Path does not exist')
	else:
		mainlabel.set('Please select a git repository')

# Code	

label = Label(window, textvariable=mainlabel)
label.grid(row=1, column=1)
label.configure(background='white')
select = Button(window, text="Select Repository", command=selectPath, width=20)
select.grid(row=2, column=1)
select.configure(background='white')
text = Text()
text.grid(row=10, column=1)
text.configure(background='white')

# Inits Window Loop

window.mainloop()