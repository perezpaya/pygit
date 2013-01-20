#!/usr/bin/env python
# Imports
from Tkinter import *
import tkMessageBox
import tkFileDialog
import json
from os import popen
from os import path
import os

# Windows

__dirname = os.path.dirname(os.path.realpath(sys.argv[0]))

config = json.loads(open(__dirname + '/config.json', 'r').read())

window = Tk()
window.title('PyGit')
window.minsize(500,500)
window.maxsize(1000,1000)
window.configure(background=config['background-color'])
#window.iconify()
#window.deiconify()

# Vars

repoPath = StringVar()
msg = StringVar()
mainlabel = StringVar()
terminal = StringVar()
# Functions

def alert(_text):
	tkMessageBox.showinfo(message=_text)

def yesno(_text, _title):
	tkMessageBox.askyesno(message=_text, icon='question', title=_title)

def write (output):
	text.insert(END, output+'\n')

def cleanOutput ():
	print "Clear"

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
		alert("You must write a git commit description")

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
			message = Entry(window, textvariable=msg)
			message.grid(row=3, column=1)
			commitButton = Button(window, text="Commit", command=commit, width=20)
			commitButton.grid(row=4, column=1)
			pushButton = Button(window, text="Push", command=push, width=20)
			pushButton.grid(row=5, column=1)
			pullButton = Button(window, text="Pull", command=pull, width= 20)
			pullButton.grid(row=6, column=1)
			logButton = Button(window, text="Show log", command=log, width= 20)
			logButton.grid(row=7, column=1)
			remotesButton = Button(window, text="Show remotes", command=showRemotes, width= 20)
			remotesButton.grid(row=8, column=1)
			select.grid(row=7, column=1)
		else:
			alert('Path does not exist')
	else:
		mainlabel.set('Please select a git repository')

# Code	
label = Label(window, textvariable=mainlabel)
label.grid(row=1, column=1)
select = Button(window, text="Select Repository", command=selectPath, width=20)
select.grid(row=2, column=1)
text = Text()
text.grid(row=10, column=1)


# Inits Window Loop

window.mainloop()