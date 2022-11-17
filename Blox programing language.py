#Blox programing language 
#Aliasghar Fahmide kar & Amirali Ziyaie

import bloxlib

class language:#میتونه کتابخونه بشه
    def printer(self,info):#این ها رو اس\لیت نکردم چون قراره توی حلقه آخر اس\لیت بشه 
        return exec(info)
    def inter(self,valcode):#این اینت
        intag = valcode[1]
        intag += "="
        intag += valcode[3]
        exec(intag)
    def strer(self,strcode):#این استرینک
        strin = strcode[1]
        strin += "='"
        strin += strcode[3]
        strin += "'"
        exec(strin)
    def lister(self,listcode):#این لیسته
        listcode = bloxlib.splitor(listcode)
        liste = listcode[1]
        liste += "="
        mylist= []
        for i in listcode[3:] :
            i = str(listcode).split(",")
            for n in i[:len(i)]:
                mylist.append(n)
        liste += str(mylist[3:])
        return exec(liste)

blox = language()
#عژب
            


while True :
    code = input()
    code = bloxlib.splitor(code)
    #تکمیل نشده هنوز