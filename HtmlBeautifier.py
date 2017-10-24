# Python 3.6.3
# Created 10/20/2017

from appJar import gui
from bs4 import BeautifulSoup
import codecs
import pyperclip


def beautify(btn):
    html_file = codecs.open(app.getEntry("html"))
    read = html_file.read()
    soup = BeautifulSoup(read, "html.parser")
    app.setTextArea("formatted", soup.prettify())


def clear(btn):
    app.clearTextArea("formatted")
    app.clearEntry("html")


def copy(btn):
    pyperclip.copy(app.getTextArea("formatted"))


app = gui("HTML BEAUTIFIER", "600x362")
app.setFont(20)
app.setGuiPadding(10,10)
app.setBg("grey")
app.addEntry("html")
app.setEntryDefault("html", "Enter file path to HTML document to beautify!")
app.addTextArea("formatted")
app.addButtons(["beautify", "clear", "copy"], [beautify, clear, copy])

app.go()
