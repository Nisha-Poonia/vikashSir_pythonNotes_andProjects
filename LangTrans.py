from googletrans import Translator
from tkinter import *
def convert(e):
    lang=e.widget["text"]
    # print(lang)
    code = Lang[lang]
    # print(code)
    # print(msg.get())
    s = t.translate(msg.get(),code)

    convmsg.set(s.text)

root=Tk()
root.title("CETPA Language Translator")
root.geometry("500x500")
root["bg"]="orange"
t = Translator()
lbl=Label(root,text="Enter Text in Any Language",font=1)
lbl.grid(row=0,column=0,columnspan=3,sticky=E+W+N+S,padx=20,pady=10)
msg=StringVar()
entMsg=Entry(root,textvariable=msg,font=1)
entMsg.grid(row=1,column=0,columnspan=3,sticky=E+W+N+S,padx=20)
Lang={"Hindi":"hi","English":"en","Punjabi":"pa","German":"de","Russian":"ru","French":"fr"}
LangNames=list(Lang.keys())

for i in range(3):
    btn=Button(root,text=f"{LangNames[i]}",font=1,bg="yellow",width=10)
    btn.bind("<1>",convert)
    btn.grid(row=2,column=i,padx=20,pady=30)
for i in range(3):
    btn=Button(root,text=f"{LangNames[i+3]}",font=1,bg="yellow",width=10)
    btn.bind("<1>",convert)
    btn.grid(row=3,column=i,padx=20,pady=30)
convmsg=StringVar()
entconvMsg=Entry(root,textvariable=convmsg,font=1)
entconvMsg.grid(row=4,column=0,columnspan=3,sticky=E+W+N+S,padx=20,pady=20)

root.mainloop()


