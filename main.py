import wx
import sqlite3
from win32com.client import Dispatch
import time
import re
import ok1
import random
import scrape
import files
import speech_recognition as sr
import datetime
import google

#make a google scrape soon

#Create a segment that analyses the text so account or shortened words

r = sr.Recognizer()
mic = sr.Microphone()
speak = Dispatch("SAPI.SpVoice")
smt = ok1.mapping

bye_text=["good night", "go off", "bye", "switch off", "goodbye", "good bye"]
joke_text=["i'm bored", "tell me a joke", "make me laugh"]
time_text=["what is the time", "tell me the time", "what says the time"]
reptext = ["come again", "i did not get that", "what did you say", "please repeat", "repeat it", "say it again"]
q_text = ["I don't know, dou you want to check google"]


joke=['']

asked_questions = []
previous_answer = ""
code = 0 #code to know the segment where the joined question comes from

def get_time():
    current_time=datetime.datetime.now()
    hour = str(current_time.hour)
    minute = str(current_time.minute)
    ttime = hour + ' ' + minute
    speak.Speak(ttime)
    return ttime

class Intro(wx.Frame):
    def __init__(self, parent, title):
        wx.Frame.__init__(self, parent, title=title, pos=(300, 0), size=(350, 200),
                          style=wx.SYSTEM_MENU | wx.STAY_ON_TOP | wx.CAPTION | wx.MINIMIZE_BOX)
        self.panel = wx.Panel(self)
        self.panel.SetBackgroundColour('Purple')
        self.icon=wx.Icon('tech.ico', wx.BITMAP_TYPE_ICO)
        self.SetIcon(self.icon)
        static = wx.StaticText(self.panel, -1, 'A WIZITECH Product', style=wx.ALIGN_CENTER, pos=(60,200), size=(100,30))
        self.gauge = wx.Gauge(self.panel, -1, pos=(100,100), size=(140,30), range=10)
        self.timer = wx.Timer()
        wx.CallAfter(self.OnStart)
        font = wx.Font(18, wx.SWISS, wx.ITALIC, wx.BOLD)
        static.SetFont(font)

    def OnStart(self):
        count = 0
        while count <= 10:
            time.sleep(0.5)
            count = count + 1
            self.gauge.SetValue(count)
        if count == 11:
            button = wx.Button(self.panel, label='DONE', pos=(150,20), size=(40,40))
            self.Bind(wx.EVT_BUTTON, self.OnClick, button)

    def OnClick(self, event):
        self.Close()
        self.Destroy()


app = wx.App(False)
frame = Intro(None, "A.I")
frame.Show(True)
app.MainLoop()

def _function(command, text, text1):
    asked_questions.append(text)
    lenght = len(asked_questions)
#    if lenght >= 2:
#        if asked_questions[lenght - 1] == asked_questions[lenght - 2]:
#            speak.Speak("I've said it already, should i repeat myself")
#            return(previous_answer)
#    elif text == 'yes' and asked_questions[lenght - 2] == asked_questions[lenght - 3]:
#        speak.Speak(previous_answer)
#        return(previous_answer)
    if text in reptext:
        speak.Speak(previous_answer)
        return(previous_answer)
    elif text == 'no' and asked_questions[lenght - 2] == asked_questions[lenght - 3]:
        speak.Speak('ok')
        return('ok')
    elif text in ['how', 'why', 'where', 'when', 'what']:
        speak.Speak("I do not know, but you can check google. I can assist you with that")
        return("I do not know, but you can check google. I can assist you with that")
    elif command == 'calculation':
        speak.Speak('Will be in the next version')
        return('Will be in the next version')
    elif command == 'repeat':
        speak.Speak(text1)
        return(text1) 
    elif command == 'wiki':
        result = scrape.check_word(text1)
        speak.Speak(result)
        print(result)
        return(result)
    elif command == 'file':
        speak.Speak(files.start(text1))
    elif command == 'special':
        if text in bye_text:
            speak.Speak('Goodbye')
            return('exitcode')
        elif text in joke_text:
            speak.Speak(random.choice(joke))
        elif text in time_text:
            return(get_time())
    elif command == 'chat' and text in smt:
        ans = random.choice(smt[text])
        if len(ans) == 1:
            speak.Speak(smt[text])
            return(smt[text])
        else:
            speak.Speak(ans)
            return(ans)
    elif command == 'search':
        newlist = google.search(text)
        if len(newlist) == 1:
            speak.Speak(newlist[0])
            return('')
        else:
            speak.Speak("here is a link forwhat you want")
            return(newlist[0])
    elif command == '':
        if text in bye_text:
            speak.Speak('Goodbye')
            return('exitcode')
        elif text in joke_text:
            speak.Speak(random.choice(joke))
            return(random.choice(joke))
        elif text in time_text:
            return(get_time())
        elif text in smt:
            ans = random.choice(smt[text])
            if len(ans) == 1:
                speak.Speak(smt[text])
                return(smt[text])
            else:
                speak.Speak(ans)
                return(ans)
        else:
            speak.Speak('Not found')
            return('Not found')
    else:
        speak.Speak('Not in dictionary')
        return('Not in dictionary')

class about_frame(wx.Frame):
    def __init__(self, parent, title):
        wx.Frame.__init__(self, parent, title=title, pos=(300, 100), size=(240, 200),
                        style=wx.SYSTEM_MENU | wx.STAY_ON_TOP | wx.MINIMIZE_BOX | wx.CAPTION | wx.CLOSE_BOX)
        panel = wx.Panel(self)
        panel.SetBackgroundColour('Purple')
        static = wx.StaticText(panel, -1, 'Wizitech is an organization founded by Omodiagbe Wisdom Eden. It was created out of passion of a better future.'
+ 'That is why our motto is bringing the future closer. We imagine a future where everything is automated and manual labour almost completely eradicated.'
+ 'We intend on training young minds into achieving our desired future.', size=(200,300))
        self.icon = wx.Icon('tech.ico', wx.BITMAP_TYPE_ICO)
        self.SetIcon(self.icon)

class help_frame(wx.Frame):
    def __init__(self, parent, title):
        wx.Frame.__init__(self, parent, title=title, pos=(300, 100), size=(240, 270),
                        style=wx.SYSTEM_MENU | wx.STAY_ON_TOP | wx.MINIMIZE_BOX | wx.CAPTION | wx.CLOSE_BOX)
        panel = wx.Panel(self)
        panel.SetBackgroundColour('Purple')
        static = wx.StaticText(panel, -1, 'This is a windows assistant in progress. It will help you do things more easily. Typing in questions has a set of pre-built answers so you can also train the software with the teach button.'
+ 'For now, It has a few functions. The first is the repeat function which says whatever is typed in. The next is the check function which gives the definition of the inputed word.'
+ 'We also have the file function which you can use to open files with the inputed file path. If you have any suggestion, you can type it in the comment part.', size=(200,300))
        self.icon = wx.Icon('tech.ico', wx.BITMAP_TYPE_ICO)
        self.SetIcon(self.icon)

class commentFrame(wx.Frame):
    def __init__(self, parent, title):
        wx.Frame.__init__(self, parent, title=title, pos=(300, 100), size=(350, 350),
                          style=wx.SYSTEM_MENU | wx.STAY_ON_TOP | wx.MINIMIZE_BOX | wx.CAPTION | wx.CLOSE_BOX)
        panel = wx.Panel(self)
        panel.SetBackgroundColour('Purple')
        self.text1 = wx.TextCtrl(panel, -1, pos=(20, 20), size=(250, 250), style=wx.TE_MULTILINE)
        button = wx.Button(panel, label='DONE', pos=(280, 250), size=(40,40))
        self.Bind(wx.EVT_BUTTON, self.OnClickDone, button)
        self.icon = wx.Icon('tech.ico', wx.BITMAP_TYPE_ICO)
        self.SetIcon(self.icon)

    def OnClickDone(self, event):
        comment = self.text1.GetValue()
        newFile = open('comment.txt','a')
        newFile.write(comment + '\n' + '\n')
        newFile.close()
        self.Close()
        self.Destroy()

class MainWindow(wx.Frame):
    def __init__(self, parent, title):
        wx.Frame.__init__(self, parent, title=title, pos=(300, 100), size=(400, 400),
                          style=wx.SYSTEM_MENU | wx.STAY_ON_TOP | wx.CAPTION | wx.MINIMIZE_BOX | wx.CLOSE_BOX)
        panel = wx.Panel(self)
        panel.SetBackgroundColour('Red')
        self.text1 = wx.TextCtrl(panel, -1, pos=(80, 50), size=(150, 30))
        self.text2 = wx.TextCtrl(panel, -1, pos=(100,180), size=(150, 30))
        self.text3 = wx.TextCtrl(panel, -1, pos=(120, 120), size=(100,30))
        button1 = wx.Button(panel, label='OK', pos=(50,50), size=(30, 30))
        self.Bind(wx.EVT_BUTTON, self.OnClickOk, button1)
        button2 = wx.Button(panel, label='Teach', pos=(220,220), size=(50,30))
        self.Bind(wx.EVT_BUTTON, self.OnClickTeach, button2)
        button3 = wx.Button(panel, label='QUIT', pos=(300,270), size=(35,35))
        self.Bind(wx.EVT_BUTTON, self.OnClickExit, button3)
        self.icon = wx.Icon('tech.ico', wx.BITMAP_TYPE_ICO)
        self.SetIcon(self.icon)
        button_speak = wx.Button(panel, label='TALK', pos=(50, 90), size=(30,30))
        self.Bind(wx.EVT_BUTTON, self.OnClickTalk, button_speak)
        static1 = wx.StaticText(panel, -1, 'Tell me something', pos=(80,30))
        static2 = wx.StaticText(panel, -1, 'Output:', pos=(55,190))
        static3 = wx.StaticText(panel, -1, 'Command', pos=(130, 100))
        self.Bind(wx.EVT_CLOSE, self.OnClose)
        menuBar = wx.MenuBar()
        menu1 = wx.Menu()
        menu2 = wx.Menu()
        menu3 = wx.Menu()
        menuBar.Append(menu1, "&About Us")
        menuBar.Append(menu2, "&Help")
        menuBar.Append(menu3, "&Suggestion")
        item1 = menu1.Append(-1, 'about', 'about wizitech')
        item2 = menu2.Append(-1, 'help', 'how to use the commands')
        item3 = menu3.Append(-1, "Comment", '')
        self.Bind(wx.EVT_MENU, self.aboutframe, id=item1.GetId())
        self.Bind(wx.EVT_MENU, self.helpframe, id=item2.GetId())
        self.Bind(wx.EVT_MENU, self.commentframe, id=item3.GetId())
        self.SetMenuBar(menuBar)

    def commentframe(self, event):
        a = wx.App(False)
        frame = commentFrame(None, 'Comment')
        frame.Show(True)
        a.MainLoop()

    def aboutframe(self, event):
        a = wx.App(False)
        frame = about_frame(None, 'About')
        frame.Show(True)
        a.MainLoop()

    def helpframe(self, event):
        b = wx.App(False)
        frame = help_frame(None, 'Help')
        frame.Show(True)
        b.MainLoop()

    def OnClickTalk(self, event):
        with mic as source:
            r.adjust_for_ambient_noise(source, duration=0.5)
            speak.Speak("Talk")
            audio = r.listen(source)
        try:
            text = r.recognize_google(audio)
            self.text1.SetValue(text)
            a = self.text3.GetValue()
            command = a.lower()
            val = _function(command, text.lower(), text)
            previous_answer = val
            if val == 'exitcode':
                self.Close()
                self.Destroy()
            else:
                self.text2.SetValue(val)
        except:
            speak.Speak("I can't get what you are saying, or check your internet connection") 

    def OnClickOk(self, event):
        text1 = self.text1.GetValue()
        a = self.text3.GetValue()
        command = a.lower()
        text = text1.lower()
        text2 = self.text2.GetValue()
        print(smt)
        val = _function(command, text, text1)
        previous_answer = val
        if val == 'exitcode':
            self.Close()
            self.Destroy()
        else:
            self.text2.SetValue(val)

    def OnClickExit(self, event):
        self.Close()
        self.Destroy()

    def OnClickTeach(self, event):
        class New(wx.Frame):
            def __init__(self, parent, title):
                wx.Frame.__init__(self, parent, title='Teach',pos=(20,300), size=(200,250),
                                  style=wx.CAPTION | wx.CLOSE_BOX)
                panel1 = wx.Panel(self)
                panel1.SetBackgroundColour('Blue')
                button = wx.Button(panel1, label='OK', size=(30,30), pos=(150,180))
                self.Bind(wx.EVT_BUTTON, self.OnClick, button)
                self.text1 = wx.TextCtrl(panel1, -1, pos=(25,30), size=(120,25))
                self.text2 = wx.TextCtrl(panel1, -1, pos=(25, 80), size=(120,25))
                static1 = wx.StaticText(panel1, -1, 'Statement for the computer', pos=(25,15))
                static2 = wx.StaticText(panel1, -1, 'Statement from the computer', pos=(20,60))
                self.icon = wx.Icon('tech.ico', wx.BITMAP_TYPE_ICO)
                self.SetIcon(self.icon)

            def OnClick(self, event):
                text1 = self.text1.GetValue()
                text2 = self.text2.GetValue()
                text1 = text1.lower()
                text2 = text2.lower()
                myfile = open('info.txt','a')
                myfile.write('\n' + text1 + '\n')
                myfile.write(text2)
                myfile.close()
                myfile = open('info.txt', 'r')
                read = myfile.read()
                myfile.close()
                print(read)
                ok1.retreive_from_file()
                self.Close()
                self.Destroy()

        frame1 = New(None, 'Teach')
        frame1.Show(True)

    def OnClose(self, event):
        self.Destroy()
                


App = wx.App(False)
frame = MainWindow(None, "A.I")
frame.Show(True)
App.MainLoop()
