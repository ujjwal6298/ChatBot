import os
from tkinter import *
from chatterbot import ChatBot
from chatterbot.trainers import  ListTrainer
import pyttsx3
import speech_recognition as s
import threading


engine=pyttsx3.init()

voices=engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)




bot=ChatBot('My Bot')

convo = ['hello',
        'hi there !',
        'what is your name?',
        'My name is Jude I am a female bot created by Ujjwal',
        'how are you ?',
        'I am doing great these days',
        'thank you',
        'what is the capital of india?',
        'Delhi is the capital of India',
        'dont talk to me ',
        'i will talk to you',
        'are you intelligent?',
        'Yes i am intelligent',
        'Where do you live ?',
        'I live in India',
        'what you do?',
        'I do chatting',
        'Are you single or Marriad?',
        'marriad',

        'Say something',
        'No, you say something',

        'In which language you talk?',

        'I mostly talk in english',
        'what you do in free time?',
        'I memorize things in my free time',
        'ok bye take care see you again',
        'bye'
]

trainer = ListTrainer(bot)

trainer.train(convo)

def take_query():
    sr=s.Recognizer()
    sr.pause_threshold=1
    print("Your bot is listening try to speak")
    with s.Microphone()as m:
        try:
            audio = sr.listen(m)
            query = sr.recognize_google(audio, language='eng-in')
            print(query)
            questionField.delete(0, END)
            questionField.insert(0, query)
            askbot().audio=sr.listen(m)
        except Exception as e:
            print(e)

def askbot():
    query=questionField.get()

    answer=bot.get_response(query)

    textarea.insert(END,'You:'+query+'\n\n')
    textarea.insert(END,'Bot:'+str(answer)+'\n\n')
    engine.say(answer)
    engine.runAndWait()

    questionField.delete(0,END)
    textarea.yview(END)

bot=ChatBot('Bot')
trainer= ListTrainer(bot)



for files in os.listdir(r'C:/Users/Utsav/Downloads/chatbot__1_/chatbot/chatterbot-corpus-master/chatterbot_corpus/data/english/'):
    data=open(r'C:/Users/Utsav/Downloads/chatbot__1_/chatbot/chatterbot-corpus-master/chatterbot_corpus/data/english/'+files,'r').readlines()
    trainer.train(data)


root=Tk()
root.geometry('500x570+100+30')
root.resizable(0,0)
root.title('ChatBot Created bt Ujjwal')
root.config(bg='rosybrown2')

pic=PhotoImage(file='C:/Users/Utsav/Downloads/chatbot__1_/chatbot/pic.png')

picture_Label=Label(root,image=pic,bg='rosybrown2')
picture_Label.pack(pady=5)

center_Frame=Frame(root)
center_Frame.pack()

scrollbar=Scrollbar(center_Frame)
scrollbar.pack(side=RIGHT,fill=Y)

textarea=Text(center_Frame,font=('times new roman',20,'bold'),width=80,height=10,yscrollcommand=scrollbar.set,)
textarea.pack(side=LEFT,fill=BOTH)

questionField=Entry(root,font=('vardana',25,'bold'))
questionField.pack(fill=X,pady=15)

askimage=PhotoImage(file='C:/Users/Utsav/Downloads/chatbot__1_/chatbot/ask.png')
askButton=Button(root,image=askimage,bd=0,bg='rosybrown2',activebackground='rosybrown2',cursor='hand2',command=askbot)
askButton.pack()

def enter_function(event):
    askButton.invoke()

root.bind('<Return>',enter_function)

def repeat():
    while True:
        take_query()

t1=threading.Thread(target=repeat)
t1.start()

root.mainloop()