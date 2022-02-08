from tkinter import *
import random
from tkinter import messagebox

words = ['Grapes', 'Mango', 'Apple', 'gun', 'fan', 'door', 'tv', 'mobile', 'laptop']

def labelSlider():
    global count, sliderWords
    text = 'Welcome to typing Speed Increaser Game'
    if(count >= len(text)):
        count=0
        sliderWords=''
    sliderWords += text[count]
    count += 1
    fontLabel.configure(text=sliderWords)
    fontLabel.after(150, labelSlider)

def time():
    global time_left, score, miss
    if(time_left >= 11):
        pass
    else:
        timeLabelCount.configure(fg='red')
    if(time_left > 0):
        time_left -= 1
        timeLabelCount.configure(text=time_left)
        timeLabelCount.after(1000, time)
    else:
        gamePlayDetailLabel.configure(text='Hit = {} | Miss = {} | Total Score = {}'.format(score, miss, score-miss))
        rr = messagebox.askretrycancel('Notification', 'For Play Again Hit Retry Button')
        if(rr == True):
            score = 0
            time_left = 14
            miss = 0
            timeLabelCount.configure(text=time_left)
            wordLabel.configure(text=words[0])
            scoreLabelCount.configure(text=score)



def startGame(event):
    global score, miss
    if(time_left == 60):
        time()
    gamePlayDetailLabel.configure(text='')
    if(wordEntry.get() == wordLabel['text']):
        score += 1
        scoreLabelCount.configure(text=score)
        #print("Score ", score)
    else:
        miss += 1
        print("miss ", miss)
    random.shuffle(words)
    wordLabel.configure(text=words[0])
    wordEntry.delete(0, END)

#####____ROOT METHOD____#######
root = Tk()
root.geometry('800x600+400+100')
root.configure(bg = 'powder blue')
root.title('Typing Speed Increaser Game')
#root.iconbitmap('typingspeed.ico')


score = 0
time_left = 60
count = 0
sliderWords = ''
miss = 0
######______LABEL METHOD______#######
fontLabel = Label(root, text='Welcome to typing Speed Increaser game', font=('arial', 25, 'italic bold'),
                  bg='powder blue', fg='red', width=40)
fontLabel.place(x=10, y=10)
labelSlider()

random.shuffle(words)
wordLabel = Label(root, text=words[0], font=('arial', 25, 'italic bold'), bg='powder blue')
wordLabel.place(x=350, y=200)

scoreLabel = Label(root, text='Your Score : ', font=('arial', 25, 'italic bold'), bg='powder blue',
                   fg='blue')
scoreLabel.place(x=10, y=100)

scoreLabelCount = Label(root, text=score, font=('arial', 25, 'italic bold'), bg='powder blue',
                   fg='blue')
scoreLabelCount.place(x=80, y=180)

timerLabel = Label(root, text='Time left :', font=('arial', 25, 'italic bold'), bg='powder blue',
                   fg='blue')
timerLabel.place(x=600, y=100)

timeLabelCount = Label(root, text=time_left, font=('arial', 25, 'italic bold'), bg='powder blue',
                   fg='blue')
timeLabelCount.place(x=680, y=180)

gamePlayDetailLabel = Label(root, text='Type Word And Hit Enter Button', font=('arial', 30, 'italic bold'), bg='powder blue',
                   fg='dark grey')
gamePlayDetailLabel.place(x=120, y=450)


######______ENTRY METHOD______#######
wordEntry = Entry(root, font=('arial', 25, 'italic bold'), bd=10, justify='center')
wordEntry.place(x=250, y=300)
wordEntry.focus_set()


root.bind('<Return>', startGame)
root.mainloop()
