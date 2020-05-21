import speech_recognition as sr
import os
from gtts import gTTS 
import datetime
import warnings
import calendar
import random
import wikipedia
warnings.filterwarnings('ignore')


def recordAudio():
    r = sr.Recognizer()
    with sr.Microphone() as source :
        print('say something!!!')
        audio=r.listen(source)
    data = ''
    try:
        data = r.recognize_google(audio) 
        print('your messege : '+data)
    except sr.UnknownValueError:
        print('could not understand audio')
    except sr.RequestError as e:
        print('service error'+e)
    return data
def assiresp(text):
    print(text)
    myobj=gTTS(text = text,lang = 'en',slow = False)
    myobj.save('assresp.mp3')
    os.system('start assresp.mp3')  
def wake(text):
    w=['hey system','hi system','hello system'] 
    text=text.lower()  
    for phrase in w:
        if phrase in text :
            return True
    return False
def getDate():
    now=datetime.datetime.now()
    my_date=datetime.datetime.today()
    weekday=calendar.day_name[my_date.weekday()]
    monthNum=now.month
    dayNum=now.day   
    month_names=['jan','feb','mar','a','may','j','ju','a','se','o' ,'n','d']
    ordinalNumbers=['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20th','21','22','23','24','25','26','27','28','29','30']       
    return 'Today is '+weekday+' '+month_names[monthNum-1]+' the '+ordinalNumbers[dayNum-1] +''
def greeting(text):
    GREETING_INPUT=['hi','hey','hello','whatsupp','good morning']
    GREETING_RESPONSES=['hello','hi','Hi','Heloo','good']
    for word in text.split():
        if word.lower():
            return random.choice(GREETING_RESPONSES) + '.'
    return ''
def getperson(text):
    wordlist=text.split()
    for i in range(0,len(wordlist)):
        if i+3<=len(wordlist )-1 and wordlist[i].lower()=='who' and wordlist[i+1].lower()=='is':
            return wordlist[i+2] + '' +  wordlist[i+3]     
while True:
    text=recordAudio()    
    response=''
    if(wake(text)==True):
       response=response + greeting(text)
       if('date'in text):
           get_data=getDate()
           response=response +'' + get_data  
       if('time' in text):
           now = datetime.datatime.now()
           meridiem=''
           if now.hour>=12:
               merdiem='p.m'
               hour=now.hour-12
           else:
                merdiem='a.m'
                hour=now.hour  

           if now.hour <10:
               minute = '0'+str(now.minute)
           else:
               minute=str(now.minute)
           response=response +''+'it is ' + str(hour)+ ':' + minute+ ''+merdiem+' .'         
       if('who is' in text):
            person=getperson(text)
            wiki=wikipedia.summary(person,sentences=2)
            response=response + '' + wiki
       assiresp(response)       
          



