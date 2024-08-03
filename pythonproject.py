import tkinter as tk
from tkinter import messagebox

from PIL import Image, ImageTk  # pip install pillow
import random
import ctypes
from timeit import default_timer 
import difflib
import ttkthemes
from timeit import default_timer as timer

import timeit
from timeit import default_timer

from datetime import datetime
from datetime import date

import sys
import time

import pygame
from pygame.locals import *

import threading
from time import sleep

###################################   FIRST CODE     #####################################################33

class FirstPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        
        load = Image.open("C:\A\speed.png")
        photo = ImageTk.PhotoImage(load)
        label = tk.Label(self, image=photo)
        label.image=photo
        label.place(x=0,y=0)
        
        #border = tk.LabelFrame    self, text='Login', bg='cadet blue', bd = 10, font=("Arial", 20))
        #border.pack(fill="both", expand="yes", padx = 100, pady=100)
        
        #L1 = tk.Label    self, text="NAME", font=("Arial Bold", 15), bg='cadet blue')
        #L1.place(x=50, y=20)
        #T1 = tk.Entry    self, width = 30, bd = 10, font=(' arial bold',15))
        #T1.place(x=180, y=20)


        Button = tk.Button(self, text="LETS GO", font=("Arial", 25), fg='sky blue',bg='mint cream',command=lambda: controller.show_frame(SecondPage))
        Button.place(x=480, y=230)


#######################################     SECOND  PAGE      ###################################################3


class SecondPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

       
        
        load = Image.open("C:\A\spark1.png")
        photo = ImageTk.PhotoImage(load)
        label = tk.Label(self, image=photo)
        label.image=photo
        label.place(x=0,y=0)
        
        #border = tk.LabelFrame    self, text='Login', bg='cadet blue', bd = 10, font=("Arial", 20))
        #border.pack(fill="both", expand="yes", padx = 150, pady=150)
        
        #L1 = tk.Label    self, text="NAME", font=(" Bold", 20), bg='dark slate blue',fg='white')
        #L1.place(x=320, y=210)
        T1 = tk.Entry(self, width = 30, bd = 10, font=(" Bold", 20))
        T1.place(x=120, y=250)   


        def save_info():
            if T1.get():
               

                T1_info= T1.get()
                print(T1_info)
                def change_text(): 
                    but2.config(command=sub)   
                   

                file = open("user.txt","w")
                file.write("name="+T1_info)

                file.close() 
                but2['text']='START TEST'
                but2.config(command=verify)   
               

            else:
                 messagebox.showinfo("invalid"," Enter Details")

    
        def verify():
           if T1.get():
                
                with open("data.txt", "w") as f:
                    f.write(T1.get()+"\n")
                    controller.show_frame(ThirdPage)    
                    
           else:
                messagebox.showinfo("invalid"," Enter Details")    

        


        but2 = tk.Button(self, text="Submit",fg= 'dark olive green',bg='floral white', font=("Arial Bold", 15), command= save_info )#lambda: controller.show_frame(ThirdPage))
        but2.place(x=250, y=350)  

        def sub():

         Button1 = tk.Button(self, text="START TEST",fg= 'dark olive green',bg='floral white', font=("Arial Bold", 15), command= verify)#lambda: controller.show_frame(ThirdPage))
         Button1.place(x=230, y=450)    

  
        button2 = tk.Button(self, text="Back",height=1,width=7, bg='seashell' ,fg='salmon' ,font=('Arial Bold',15),
                            command=lambda: controller.show_frame(FirstPage))  
        button2.place(x=975, y=460) 



################################    THIRD PAGE     ##############################################################

class ThirdPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        
        load = Image.open("C:\A\speed3.png")
        photo = ImageTk.PhotoImage(load)
        label = tk.Label(self, image=photo)
        label.image=photo
        label.place(x=0,y=0)
        
        bl1 = tk.Button(self, text='EASY',height=3, width=12,bg='mint cream', fg='black', font=('helvetica', 15, 'bold'),command=lambda: controller.show_frame(FourthPage))
        
        bl1.place(x=500, y=100)   

        bl2 = tk.Button(self, text='MEDIUM',height=3, width=12,bg='cadet blue', fg='black', font=('helvetica', 15, 'bold'),command=lambda: controller.show_frame(FifthPage))
        bl2.place(x= 500, y=250)


        bl3 = tk.Button(self, text='HARD',height=3, width=12,bg='cornflower blue', fg='black', font=('helvetica', 15, 'bold'),command=lambda: controller.show_frame(SixthPage) )
        bl3.place(x=500, y=400)
  
        button1 = tk.Button(self, text="Back",height=2,width=7,  bg='white',fg='dark olive green', font=('Bold',15),
                            command=lambda: controller.show_frame(SecondPage))  
        button1.place(x=530, y=550) 


#########################################     FOURTH PAGE    ##################################################3
         
class FourthPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        load = Image.open("C:\A\gb.jpg")
        photo = ImageTk.PhotoImage(load)
        label = tk.Label(self, image=photo)
        label.image=photo
        label.place(x=0,y=0)
        
        
        mainframe=tk.Frame(self,bd=4)
        mainframe.grid()

        titleframe=tk.Frame(mainframe)
        titleframe.grid()

        paragraph_frame=tk.Frame(self)
        paragraph_frame.place(x=100,y=50)
      
        paragraph_list=['A S @ ; D F h J K % L','Q W E # R U I ! O P','# Z X C & *V B N M < K', 'A S ^ $ D R L K ~ J Y','9 O K M 1 Q A Z','2 W S & X 8 U H B','3 E D % C 7 Y @ G V']
        random.shuffle(paragraph_list)
        label_paragraph=tk.Label(paragraph_frame,text=paragraph_list[0],width=53,bg='black',fg='white',wraplength=912,justify='left',font=('arial',20,'bold'))
        label_paragraph.grid()

        textarea_frame=tk.Frame(self)
        textarea_frame.place(x=135,y=130)
      
        textarea=tk.Text(textarea_frame,font=('arial',12,'bold'),width=92,height=2,bd=1,relief='groove',wrap='word'
                  )
        textarea.grid()

                 
         

# functions

        totaltime=60
        time=0
        elapsedtimeinminutes=0
        
        
        def start_timer():

            
            startButton.config(state='disabled')
            time=0
            textarea.config(state='normal')
            textarea.focus()

            #for time in range(1,21):
            #    elapsed_timer_label.config(text=time)
            #    remainingtime=totaltime-time
            #    remaining_timer_label.config(text=remainingtime)
            #    sleep(1)
            #    self.update()

            textarea.config(state='normal')
            resetButton.config(state='normal')


        def count():
          wrongwords=0
          while time!=totaltime:
              entered_paragraph=textarea.get(1.0,'end').split()
              totalwords=len(entered_paragraph)
      
          totalwords_count_label.config(text=totalwords)
      
          para_word_list=label_paragraph['text'].split()
      
          for pair in list(zip(para_word_list,entered_paragraph)):
              if pair[0]!=pair[1]:
                  wrongwords+=1
      
          wrongwords_count_label.config(text=wrongwords)
      
          elapsedtimeinminutes=time/20
          #wpm=(totalwords-wrongwords)/elapsedtimeinminutes
          wpm = ((totalwords/ 5) - (totalwords - wrongwords)) / (self.time[0] + (self.time[1] / 60))
          wpm_count_label.config(text=wpm)
          gross_wpm=totalwords/elapsedtimeinminutes
          accuracy=wpm/gross_wpm*100
          accuracy=round(accuracy)
          accuracy_percent_label.config(text=str(accuracy)+'%')


        def start():
            t1=threading.Thread(target=start_timer)
            t1.start()
        
            t2 = threading.Thread(target=count)
            t2.start()

        def cal():

            wrongwords=0
        
            entered_paragraph=textarea.get(1.0,'end').split()
            totalwords=len(entered_paragraph)
           

            para_word_list=label_paragraph['text'].split()

            for pair in list(zip(para_word_list,entered_paragraph)):
                if pair[0]!=pair[1]:
                    wrongwords+=1
                    wrongwords_count_label.config(text=wrongwords)
    
            entered_paragraph=textarea.get(1.0,'end').split()
            totalwords=len(entered_paragraph)
            totalwords_count_label.config(text=totalwords)

            for time in range(1,21):
             elapsedtimeinminutes=time/60
             wpm = ((totalwords - wrongwords)) / elapsedtimeinminutes
             wpm_count_label.config(text=wpm)

             gross_wpm=totalwords/elapsedtimeinminutes
             accuracy=wpm/gross_wpm*100
             accuracy=round(accuracy)
             accuracy_percent_label.config(text=str(accuracy)+'%')  

        def start():
            t1=threading.Thread(target=start_timer)
            t1.start()

            t2 = threading.Thread(target=count)
            t2.start()

        def reset():
            global time,elapsedtimeinminutes
            time=0
            elapsedtimeinminutes=0
            startButton.config(state='normal')
            resetButton.config(state='disabled')
            textarea.config(state='normal',textarea_frame=random.shuffle(paragraph_list))
            textarea.delete(1.0,'end')
            textarea.config(state='disabled')
            textarea.config(text=random.shuffle(paragraph_list))

            #elapsed_timer_label.config(text='0')
            #remaining_timer_label.config(text='0')
            wpm_count_label.config(text='0')
            accuracy_percent_label.config(text='0')
            totalwords_count_label.config(text='0')
            wrongwords_count_label.config(text='0')


        #frame_output=tk.Frame(mainframe)
        #frame_output.grid(row=1,column=9,sticky='ew')

        #elapsed_time_label=tk.Label(self,text='ElapsedTime',font=('Tahoma',12,'bold'),fg='PaleGreen',bg='black')
        #elapsed_time_label.place(x=135,y=200)
#
        #elapsed_timer_label=tk.Label(self,text='0',font=('Tahoma',12,'bold'),fg='white',bg='black')
        #elapsed_timer_label.place(x=250,y=200)

        #remaining_time_label=tk.Label(self,text='RemainingTime',font=('Tahoma',12,'bold'),fg='PaleGreen',bg='black')
        #remaining_time_label.place(x=135,y=250)
#
        #remaining_timer_label=tk.Label(self,text='60',font=('Tahoma',12,'bold'),fg='white',bg='black')
        #remaining_timer_label.place(x=275,y=250)

########        

        wpm_label=tk.Label(self,text='CPM',font=('Tahoma',12,'bold'),fg='PaleGreen',bg='black')
        wpm_label.place(x=135,y=200)

        wpm_count_label=tk.Label(self,text='0',font=('Tahoma',12,'bold'),fg='white',bg='black')
        wpm_count_label.place(x=200,y=200)

        accuracy_label=tk.Label(self,text='Accuracy',font=('Tahoma',12,'bold'),fg='PaleGreen',bg='black')
        accuracy_label.place(x=135,y=250)

        accuracy_percent_label=tk.Label(self,text='0',font=('Tahoma',12,'bold'),fg='white',bg='black')
        accuracy_percent_label.place(x=250,y=250)

########        

        totalwords_label=tk.Label(self,text='TotalCharacters',font=('Tahoma',12,'bold'),fg='PaleGreen',bg='black')
        totalwords_label.place(x=800,y=200)

        totalwords_count_label=tk.Label(self,text='0',font=('Tahoma',12,'bold'),fg='white',bg='black')
        totalwords_count_label.place(x=950,y=200)

        wrongwords_label=tk.Label(self,text='WrongCharacters',font=('Tahoma',12,'bold'),fg='PaleGreen',bg='black')
        wrongwords_label.place(x=800,y=250)

        wrongwords_count_label=tk.Label(self,text='0',font=('Tahoma',12,'bold'),fg='white',bg='black')
        wrongwords_count_label.place(x=960,y=250)

#########        

        #buttons_Frame=tk.Frame(mainframe)
        #buttons_Frame.grid(row=4,column=0)

        startButton=tk.Button(self,text='Start',bg='green',font=('Tahoma',12,'bold'),fg='black',command=start)
        startButton.place(x=400,y=225)

        resetButton=tk.Button(self,text='Reset',bg='powder blue',font=('Tahoma',12,'bold'),fg='dark olive green',state='disabled',command=reset)
        resetButton.place(x=530,y=600)

        
        b=tk.Button(self,text="Submit",fg='white',bg='black',font=('bold',12),command=cal)
        b.place(x=525,y=226)

        button6 = tk.Button(self, text="Back",  bg='red',fg='black', font=('Bold',13),
                         command=lambda: controller.show_frame(ThirdPage))  
        button6.place(x=660, y=225) 

                
        keyboard_frame=tk.Frame(self,bg='white')
        keyboard_frame.place(x=135,y=300)
           
        frame1toBackspace=tk.Frame(keyboard_frame)
        frame1toBackspace.grid(row=0,column=0,pady=3)
        label1=tk.Label(frame1toBackspace,text='1',bg='black',fg='white',font=('arial',10,'bold'),width=5,height=2,bd=10,relief='groove')
        label2=tk.Label(frame1toBackspace,text='2',bg='black',fg='white',font=('arial',10,'bold'),width=5,height=2,bd=10,relief='groove')
        label3=tk.Label(frame1toBackspace,text='3',bg='black',fg='white',font=('arial',10,'bold'),width=5,height=2,bd=10,relief='groove')
        label4=tk.Label(frame1toBackspace,text='4',bg='black',fg='white',font=('arial',10,'bold'),width=5,height=2,bd=10,relief='groove')
        label5=tk.Label(frame1toBackspace,text='5',bg='black',fg='white',font=('arial',10,'bold'),width=5,height=2,bd=10,relief='groove')
        label6=tk.Label(frame1toBackspace,text='6',bg='black',fg='white',font=('arial',10,'bold'),width=5,height=2,bd=10,relief='groove')
        label7=tk.Label(frame1toBackspace,text='7',bg='black',fg='white',font=('arial',10,'bold'),width=5,height=2,bd=10,relief='groove')
        label8=tk.Label(frame1toBackspace,text='8',bg='black',fg='white',font=('arial',10,'bold'),width=5,height=2,bd=10,relief='groove')
        label9=tk.Label(frame1toBackspace,text='9',bg='black',fg='white',font=('arial',10,'bold'),width=5,height=2,bd=10,relief='groove')
        label0=tk.Label(frame1toBackspace,text='0',bg='black',fg='white',font=('arial',10,'bold'),width=5,height=2,bd=10,relief='groove')
        labelBackspace=tk.Label(frame1toBackspace,text='backspace',bg='black',fg='white',font=('arial',10,'bold'),width=8,height=2,bd=10,relief='groove')
        label1.grid(row=0,column=0,padx=5)
        label2.grid(row=0,column=1,padx=5)
        label3.grid(row=0,column=2,padx=5)
        label4.grid(row=0,column=3,padx=5)
        label5.grid(row=0,column=4,padx=5)
        label6.grid(row=0,column=5,padx=5)
        label7.grid(row=0,column=6,padx=5)
        label8.grid(row=0,column=7,padx=5)
        label9.grid(row=0,column=8,padx=5)
        label0.grid(row=0,column=9,padx=5)
        labelBackspace.grid(row=0,column=10,padx=5)
        frametabtop=tk.Frame(keyboard_frame)
        frametabtop.grid(row=1,column=0,pady=3)
        labeltab=tk.Label(frametabtop,text='tab',bg='black',fg='white',font=('arial',10,'bold'),width=6,height=2,bd=10,relief='groove')
        labelQ=tk.Label(frametabtop,text='Q',bg='black',fg='white',font=('arial',10,'bold'),width=5,height=2,bd=10,relief='groove')
        labelW=tk.Label(frametabtop,text='W',bg='black',fg='white',font=('arial',10,'bold'),width=5,height=2,bd=10,relief='groove')
        labelE=tk.Label(frametabtop,text='E',bg='black',fg='white',font=('arial',10,'bold'),width=5,height=2,bd=10,relief='groove')
        labelR=tk.Label(frametabtop,text='R',bg='black',fg='white',font=('arial',10,'bold'),width=5,height=2,bd=10,relief='groove')
        labelT=tk.Label(frametabtop,text='T',bg='black',fg='white',font=('arial',10,'bold'),width=5,height=2,bd=10,relief='groove')
        labelY=tk.Label(frametabtop,text='Y',bg='black',fg='white',font=('arial',10,'bold'),width=5,height=2,bd=10,relief='groove')
        labelU=tk.Label(frametabtop,text='U',bg='black',fg='white',font=('arial',10,'bold'),width=5,height=2,bd=10,relief='groove')
        labelI=tk.Label(frametabtop,text='I',bg='black',fg='white',font=('arial',10,'bold'),width=5,height=2,bd=10,relief='groove')
        labelO=tk.Label(frametabtop,text='O',bg='black',fg='white',font=('arial',10,'bold'),width=5,height=2,bd=10,relief='groove')
        labelP=tk.Label(frametabtop,text='P',bg='black',fg='white',font=('arial',10,'bold'),width=5,height=2,bd=10,relief='groove')
        labeltab.grid(row=0,column=0,padx=5)
        labelQ.grid(row=0,column=1,padx=5)
        labelW.grid(row=0,column=2,padx=5)
        labelE.grid(row=0,column=3,padx=5)
        labelR.grid(row=0,column=4,padx=5)
        labelT.grid(row=0,column=5,padx=5)
        labelY.grid(row=0,column=6,padx=5)
        labelU.grid(row=0,column=7,padx=5)
        labelI.grid(row=0,column=8,padx=5)
        labelO.grid(row=0,column=9,padx=5)
        labelP.grid(row=0,column=10,padx=5)
        framecapstoenter=tk.Frame(keyboard_frame)
        framecapstoenter.grid(row=2,column=0,pady=3)
        labelcaps=tk.Label(framecapstoenter,text='caps',bg='black',fg='white',font=('arial',10,'bold'),width=5,height=2,bd=10,relief='groove')
        labelA=tk.Label(framecapstoenter,text='A',bg='black',fg='white',font=('arial',10,'bold'),width=5,height=2,bd=10,relief='groove')
        labelS=tk.Label(framecapstoenter,text='S',bg='black',fg='white',font=('arial',10,'bold'),width=5,height=2,bd=10,relief='groove')
        labelD=tk.Label(framecapstoenter,text='D',bg='black',fg='white',font=('arial',10,'bold'),width=5,height=2,bd=10,relief='groove')
        labelF=tk.Label(framecapstoenter,text='F',bg='black',fg='white',font=('arial',10,'bold'),width=5,height=2,bd=10,relief='groove')
        labelG=tk.Label(framecapstoenter,text='G',bg='black',fg='white',font=('arial',10,'bold'),width=5,height=2,bd=10,relief='groove')
        labelH=tk.Label(framecapstoenter,text='H',bg='black',fg='white',font=('arial',10,'bold'),width=5,height=2,bd=10,relief='groove')
        labelJ=tk.Label(framecapstoenter,text='J',bg='black',fg='white',font=('arial',10,'bold'),width=5,height=2,bd=10,relief='groove')
        labelK=tk.Label(framecapstoenter,text='K',bg='black',fg='white',font=('arial',10,'bold'),width=5,height=2,bd=10,relief='groove')
        labelL=tk.Label(framecapstoenter,text='L',bg='black',fg='white',font=('arial',10,'bold'),width=5,height=2,bd=10,relief='groove')
        labelenter=tk.Label(framecapstoenter,text='enter',bg='black',fg='white',font=('arial',10,'bold'),width=10,height=2,bd=10,relief='groove')
        labelcaps.grid(row=0,column=0,padx=5)
        labelA.grid(row=0,column=1,padx=5)
        labelS.grid(row=0,column=2,padx=5)
        labelD.grid(row=0,column=3,padx=5)
        labelF.grid(row=0,column=4,padx=5)
        labelG.grid(row=0,column=5,padx=5)
        labelH.grid(row=0,column=6,padx=5)
        labelJ.grid(row=0,column=7,padx=5)
        labelK.grid(row=0,column=8,padx=5)
        labelL.grid(row=0,column=9,padx=5)
        labelenter.grid(row=0,column=10,padx=5)
        frameshifttoshift1=tk.Frame(keyboard_frame)
        frameshifttoshift1.grid(row=3,column=0,pady=3)
        labelshift=tk.Label(frameshifttoshift1,text='shift',bg='black',fg='white',font=('arial',10,'bold'),width=5,height=2,bd=10,relief='groove')
        labelZ=tk.Label(frameshifttoshift1,text='Z',bg='black',fg='white',font=('arial',10,'bold'),width=5,height=2,bd=10,relief='groove')
        labelX=tk.Label(frameshifttoshift1,text='X',bg='black',fg='white',font=('arial',10,'bold'),width=5,height=2,bd=10,relief='groove')
        labelC=tk.Label(frameshifttoshift1,text='C',bg='black',fg='white',font=('arial',10,'bold'),width=5,height=2,bd=10,relief='groove')
        labelV=tk.Label(frameshifttoshift1,text='V',bg='black',fg='white',font=('arial',10,'bold'),width=5,height=2,bd=10,relief='groove')
        labelB=tk.Label(frameshifttoshift1,text='B',bg='black',fg='white',font=('arial',10,'bold'),width=5,height=2,bd=10,relief='groove')
        labelN=tk.Label(frameshifttoshift1,text='N',bg='black',fg='white',font=('arial',10,'bold'),width=5,height=2,bd=10,relief='groove')
        labelM=tk.Label(frameshifttoshift1,text='M',bg='black',fg='white',font=('arial',10,'bold'),width=5,height=2,bd=10,relief='groove')
        labelshift1=tk.Label(frameshifttoshift1,text='shift1',bg='black',fg='white',font=('arial',10,'bold'),width=5,height=2,bd=10,relief='groove')
        labelshift.grid(row=0,column=0,padx=5)
        labelZ.grid(row=0,column=1,padx=5)
        labelX.grid(row=0,column=2,padx=5)
        labelC.grid(row=0,column=3,padx=5)
        labelV.grid(row=0,column=4,padx=5)
        labelB.grid(row=0,column=5,padx=5)
        labelN.grid(row=0,column=6,padx=5)
        labelM.grid(row=0,column=7,padx=5)
        labelshift1.grid(row=0,column=8,padx=5)
        framectrltoalt=tk.Frame(keyboard_frame)
        framectrltoalt.grid(row=4,column=0,pady=3)
        labelctrl=tk.Label(framectrltoalt,text='ctrl',bg='black',fg='white',font=('arial',10,'bold'),width=3,height=1,bd=10,relief="groove")
        labelSpace=tk.Label(framectrltoalt,text='',bg='black',fg='white',font=('arial',10,'bold'),width='30',height=1,bd=10,relief="groove")
        labelalt=tk.Label(framectrltoalt,text='alt',bg='black',fg='white',font=('arial',10,'bold'),width='3',height=1,bd=10,relief="groove")
        labelctrl.grid(row=0,column=0,padx=5)
        labelSpace.grid(row=0,column=1,padx=5)
        labelalt.grid(row=0,column=2,padx=5)
         
        def changeBG(widget):
         widget.config(bg='green')
         widget.after(100,lambda :widget.config(bg='black'))
         label_numbers=[label1,label2,label3,label4,label5,label6,label7,label8,label9,label0]      
         label_alphabets=[labelA,labelB,labelC,labelD,labelE,labelF,labelG,labelH,labelI,labelJ,labelK,labelL,labelM,labelN,
                      labelO,labelP,labelQ,labelR,labelS,labelT,labelU,labelV,labelW,labelX,labelY,labelZ]
         space_label=[labelSpace]
         Backspace_label=[labelBackspace]
         tab_label=[labeltab]
         caps_label=[labelcaps]
         enter_label=[labelenter]
         shift_label=[labelshift]
         shift1_label=[labelshift1]
         ctrl_label=[labelctrl]
         alt_label=[labelalt]
         binding_numbers=['1','2','3','4','5','6','7','8','9','0']      
         binding_capital_alphabets=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T',
                                'U','V','W','X','Y','Z']      
         binding_small_alphabets=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t',
                              'u','v','w','x','y','z']      
         for numbers in range(len(binding_numbers)):
             keyboard_frame.bind(binding_numbers[numbers],lambda event,label=label_numbers[numbers]:changeBG(label))      
         for capital_alphabets in range(len(binding_capital_alphabets)):
             keyboard_frame.bind(binding_capital_alphabets[capital_alphabets],lambda event,label=label_alphabets[capital_alphabets]:changeBG(label))      
         for small_alphabets in range(len(binding_small_alphabets)):
             keyboard_frame.bind(binding_small_alphabets[small_alphabets],lambda event,label=label_alphabets[small_alphabets]:changeBG(label))      
         keyboard_frame.bind('<space>',lambda event:changeBG(space_label[0]))
         keyboard_frame.bind('<BackSpace>',lambda event:changeBG(Backspace_label[0]))
         keyboard_frame.bind('<Tab>',lambda event:changeBG(tab_label[0]))
         keyboard_frame.bind('<Caps_Lock>',lambda event:changeBG(caps_label[0]))
         keyboard_frame.bind('<Return>',lambda event:changeBG(enter_label[0]))
         keyboard_frame.bind('<Shift_L>',lambda event:changeBG(shift_label[0]))
         keyboard_frame.bind('<Shift_R>',lambda event:changeBG(shift1_label[0]))
         keyboard_frame.bind('<Control_R>',lambda event:changeBG(ctrl_label[0]))
         keyboard_frame.bind('<Alt_R>',lambda event:changeBG(alt_label[0] ))          

         keyboard_frame.mainloop()
            
########################################################   FIFTH PAGE    ###########################################################3    

class FifthPage(tk.Frame):
    def __init__(self,parent,controller):
        tk.Frame.__init__(self, parent)
        load = Image.open("C:\A\gb.jpg")
        photo = ImageTk.PhotoImage(load)
        label = tk.Label(self, image=photo)
        label.image=photo
        label.place(x=0,y=0)  

        paragraph_frame=tk.Frame(self)
        paragraph_frame.place(x=100,y=50)
      
        paragraph_list=['Worry is a misuse of imagination',
                         'Somewhere, something incredible is waiting to be known',
                        'Success is stumbling from failure to failure with no loss of enthusiasm',
                        'Optimism is the faith that leads to achievement.',
                        'Resilience is when you address uncertainty with flexibility',
                        'True freedom is impossible without a mind made free by discipline',
                        'Experience is a hard teacher because she gives the test first, the lesson afterwards',
                        'Some people want it to happen, some wish it would happen, others make it happen',
                        'The only difference between ordinary and extraordinary is that little extra',
                        '']
        random.shuffle(paragraph_list)
        label_paragraph=tk.Label(paragraph_frame,text=paragraph_list[0],width=53,bg='black',fg='white',wraplength=912,justify='left',font=('arial',20,'bold'))
        label_paragraph.grid()

        textarea_frame=tk.Frame(self)
        textarea_frame.place(x=135,y=130)
      
        textarea=tk.Text(textarea_frame,font=('arial',12,'bold'),width=92,height=2,bd=1,relief='groove',wrap='word'
                  )
        textarea.grid()
        
# functions

        totaltime=20
        time=0
        elapsedtimeinminutes=0
        
        
        def start_timer():

            
            startButton.config(state='disabled')
            time=0
            textarea.config(state='normal')
            textarea.focus()

            #for time in range(1,21):
            #    elapsed_timer_label.config(text=time)
            #    remainingtime=totaltime-time
            #    remaining_timer_label.config(text=remainingtime)
            #    sleep(1)
            #    self.update()

            textarea.config(state='normal')
            resetButton.config(state='normal')


        def count():
          wrongwords=0
          while time!=totaltime:
              entered_paragraph=textarea.get(1.0,'end').split()
              totalwords=len(entered_paragraph)
      
          totalwords_count_label.config(text=totalwords)
      
          para_word_list=label_paragraph['text'].split()
      
          for pair in list(zip(para_word_list,entered_paragraph)):
              if pair[0]!=pair[1]:
                  wrongwords+=1
      
          wrongwords_count_label.config(text=wrongwords)
      
          elapsedtimeinminutes=time/20
          #wpm=(totalwords-wrongwords)/elapsedtimeinminutes
          wpm = ((totalwords/ 5) - (totalwords - wrongwords)) / (self.time[0] + (self.time[1] / 60))
          wpm_count_label.config(text=wpm)
          gross_wpm=totalwords/elapsedtimeinminutes
          accuracy=wpm/gross_wpm*100
          accuracy=round(accuracy)
          accuracy_percent_label.config(text=str(accuracy)+'%')


        def start():
            t1=threading.Thread(target=start_timer)
            t1.start()
        
            t2 = threading.Thread(target=count)
            t2.start()

        def cal():

            wrongwords=0
        
            entered_paragraph=textarea.get(1.0,'end').split()
            totalwords=len(entered_paragraph)
           

            para_word_list=label_paragraph['text'].split()

            for pair in list(zip(para_word_list,entered_paragraph)):
                if pair[0]!=pair[1]:
                    wrongwords+=1
                    wrongwords_count_label.config(text=wrongwords)
    
            entered_paragraph=textarea.get(1.0,'end').split()
            totalwords=len(entered_paragraph)
            totalwords_count_label.config(text=totalwords)

            for time in range(1,21):
             elapsedtimeinminutes=time/60
             wpm = ((totalwords - wrongwords)) / elapsedtimeinminutes
             wpm_count_label.config(text=wpm)

             gross_wpm=totalwords/elapsedtimeinminutes
             accuracy=wpm/gross_wpm*100
             accuracy=round(accuracy)
             accuracy_percent_label.config(text=str(accuracy)+'%')  

        def start():
            t1=threading.Thread(target=start_timer)
            t1.start()

            t2 = threading.Thread(target=count)
            t2.start()

        def reset():
            global time,elapsedtimeinminutes
            time=0
            elapsedtimeinminutes=0
            startButton.config(state='normal')
            resetButton.config(state='disabled')
            textarea.config(state='normal')
            textarea.delete(1.0,'end')
            textarea.config(state='disabled')

            #elapsed_timer_label.config(text='0')
            #remaining_timer_label.config(text='0')
            wpm_count_label.config(text='0')
            accuracy_percent_label.config(text='0')
            totalwords_count_label.config(text='0')
            wrongwords_count_label.config(text='0')


        #frame_output=tk.Frame(mainframe)
        #frame_output.grid(row=1,column=9,sticky='ew')

        #elapsed_time_label=tk.Label(self,text='ElapsedTime',font=('Tahoma',12,'bold'),fg='PaleGreen',bg='black')
        #elapsed_time_label.place(x=135,y=200)

        #elapsed_timer_label=tk.Label(self,text='0',font=('Tahoma',12,'bold'),fg='white',bg='black')
        #elapsed_timer_label.place(x=250,y=200)

        #remaining_time_label=tk.Label(self,text='RemainingTime',font=('Tahoma',12,'bold'),fg='PaleGreen',bg='black')
        #remaining_time_label.place(x=135,y=250)

        #remaining_timer_label=tk.Label(self,text='60',font=('Tahoma',12,'bold'),fg='white',bg='black')
        #remaining_timer_label.place(x=275,y=250)

########        

        wpm_label=tk.Label(self,text='WPM',font=('Tahoma',12,'bold'),fg='PaleGreen',bg='black')
        wpm_label.place(x=135,y=200)

        wpm_count_label=tk.Label(self,text='0',font=('Tahoma',12,'bold'),fg='white',bg='black')
        wpm_count_label.place(x=200,y=200)

        accuracy_label=tk.Label(self,text='Accuracy',font=('Tahoma',12,'bold'),fg='PaleGreen',bg='black')
        accuracy_label.place(x=135,y=250)

        accuracy_percent_label=tk.Label(self,text='0',font=('Tahoma',12,'bold'),fg='white',bg='black')
        accuracy_percent_label.place(x=250,y=250)

########        

        totalwords_label=tk.Label(self,text='TotalWords',font=('Tahoma',12,'bold'),fg='PaleGreen',bg='black')
        totalwords_label.place(x=800,y=200)

        totalwords_count_label=tk.Label(self,text='0',font=('Tahoma',12,'bold'),fg='white',bg='black')
        totalwords_count_label.place(x=920,y=200)

        wrongwords_label=tk.Label(self,text='WrongWords',font=('Tahoma',12,'bold'),fg='PaleGreen',bg='black')
        wrongwords_label.place(x=800,y=250)

        wrongwords_count_label=tk.Label(self,text='0',font=('Tahoma',12,'bold'),fg='white',bg='black')
        wrongwords_count_label.place(x=920,y=250)

#########        

        #buttons_Frame=tk.Frame(mainframe)
        #buttons_Frame.grid(row=4,column=0)

        startButton=tk.Button(self,text='Start',bg='green',font=('Tahoma',12,'bold'),fg='black',command=start)
        startButton.place(x=400,y=225)

        resetButton=tk.Button(self,text='Reset',bg='powder blue',font=('Tahoma',12,'bold'),fg='dark olive green',state='disabled',command=reset)
        resetButton.place(x=530,y=600)

        
        b=tk.Button(self,text="Submit",fg='white',bg='black',font=('bold',12),command=cal)
        b.place(x=525,y=226)

        button6 = tk.Button(self, text="Back",  bg='red',fg='black', font=('Bold',13),
                         command=lambda: controller.show_frame(ThirdPage))  
        button6.place(x=660, y=225)

                
        keyboard_frame=tk.Frame(self,bg='white')
        keyboard_frame.place(x=135,y=300)
           
        frame1toBackspace=tk.Frame(keyboard_frame)
        frame1toBackspace.grid(row=0,column=0,pady=3)
        label1=tk.Label(frame1toBackspace,text='1',bg='black',fg='white',font=('arial',10,'bold'),width=5,height=2,bd=10,relief='groove')
        label2=tk.Label(frame1toBackspace,text='2',bg='black',fg='white',font=('arial',10,'bold'),width=5,height=2,bd=10,relief='groove')
        label3=tk.Label(frame1toBackspace,text='3',bg='black',fg='white',font=('arial',10,'bold'),width=5,height=2,bd=10,relief='groove')
        label4=tk.Label(frame1toBackspace,text='4',bg='black',fg='white',font=('arial',10,'bold'),width=5,height=2,bd=10,relief='groove')
        label5=tk.Label(frame1toBackspace,text='5',bg='black',fg='white',font=('arial',10,'bold'),width=5,height=2,bd=10,relief='groove')
        label6=tk.Label(frame1toBackspace,text='6',bg='black',fg='white',font=('arial',10,'bold'),width=5,height=2,bd=10,relief='groove')
        label7=tk.Label(frame1toBackspace,text='7',bg='black',fg='white',font=('arial',10,'bold'),width=5,height=2,bd=10,relief='groove')
        label8=tk.Label(frame1toBackspace,text='8',bg='black',fg='white',font=('arial',10,'bold'),width=5,height=2,bd=10,relief='groove')
        label9=tk.Label(frame1toBackspace,text='9',bg='black',fg='white',font=('arial',10,'bold'),width=5,height=2,bd=10,relief='groove')
        label0=tk.Label(frame1toBackspace,text='0',bg='black',fg='white',font=('arial',10,'bold'),width=5,height=2,bd=10,relief='groove')
        labelBackspace=tk.Label(frame1toBackspace,text='backspace',bg='black',fg='white',font=('arial',10,'bold'),width=8,height=2,bd=10,relief='groove')
        label1.grid(row=0,column=0,padx=5)
        label2.grid(row=0,column=1,padx=5)
        label3.grid(row=0,column=2,padx=5)
        label4.grid(row=0,column=3,padx=5)
        label5.grid(row=0,column=4,padx=5)
        label6.grid(row=0,column=5,padx=5)
        label7.grid(row=0,column=6,padx=5)
        label8.grid(row=0,column=7,padx=5)
        label9.grid(row=0,column=8,padx=5)
        label0.grid(row=0,column=9,padx=5)
        labelBackspace.grid(row=0,column=10,padx=5)
        frametabtop=tk.Frame(keyboard_frame)
        frametabtop.grid(row=1,column=0,pady=3)
        labeltab=tk.Label(frametabtop,text='tab',bg='black',fg='white',font=('arial',10,'bold'),width=6,height=2,bd=10,relief='groove')
        labelQ=tk.Label(frametabtop,text='Q',bg='black',fg='white',font=('arial',10,'bold'),width=5,height=2,bd=10,relief='groove')
        labelW=tk.Label(frametabtop,text='W',bg='black',fg='white',font=('arial',10,'bold'),width=5,height=2,bd=10,relief='groove')
        labelE=tk.Label(frametabtop,text='E',bg='black',fg='white',font=('arial',10,'bold'),width=5,height=2,bd=10,relief='groove')
        labelR=tk.Label(frametabtop,text='R',bg='black',fg='white',font=('arial',10,'bold'),width=5,height=2,bd=10,relief='groove')
        labelT=tk.Label(frametabtop,text='T',bg='black',fg='white',font=('arial',10,'bold'),width=5,height=2,bd=10,relief='groove')
        labelY=tk.Label(frametabtop,text='Y',bg='black',fg='white',font=('arial',10,'bold'),width=5,height=2,bd=10,relief='groove')
        labelU=tk.Label(frametabtop,text='U',bg='black',fg='white',font=('arial',10,'bold'),width=5,height=2,bd=10,relief='groove')
        labelI=tk.Label(frametabtop,text='I',bg='black',fg='white',font=('arial',10,'bold'),width=5,height=2,bd=10,relief='groove')
        labelO=tk.Label(frametabtop,text='O',bg='black',fg='white',font=('arial',10,'bold'),width=5,height=2,bd=10,relief='groove')
        labelP=tk.Label(frametabtop,text='P',bg='black',fg='white',font=('arial',10,'bold'),width=5,height=2,bd=10,relief='groove')
        labeltab.grid(row=0,column=0,padx=5)
        labelQ.grid(row=0,column=1,padx=5)
        labelW.grid(row=0,column=2,padx=5)
        labelE.grid(row=0,column=3,padx=5)
        labelR.grid(row=0,column=4,padx=5)
        labelT.grid(row=0,column=5,padx=5)
        labelY.grid(row=0,column=6,padx=5)
        labelU.grid(row=0,column=7,padx=5)
        labelI.grid(row=0,column=8,padx=5)
        labelO.grid(row=0,column=9,padx=5)
        labelP.grid(row=0,column=10,padx=5)
        framecapstoenter=tk.Frame(keyboard_frame)
        framecapstoenter.grid(row=2,column=0,pady=3)
        labelcaps=tk.Label(framecapstoenter,text='caps',bg='black',fg='white',font=('arial',10,'bold'),width=5,height=2,bd=10,relief='groove')
        labelA=tk.Label(framecapstoenter,text='A',bg='black',fg='white',font=('arial',10,'bold'),width=5,height=2,bd=10,relief='groove')
        labelS=tk.Label(framecapstoenter,text='S',bg='black',fg='white',font=('arial',10,'bold'),width=5,height=2,bd=10,relief='groove')
        labelD=tk.Label(framecapstoenter,text='D',bg='black',fg='white',font=('arial',10,'bold'),width=5,height=2,bd=10,relief='groove')
        labelF=tk.Label(framecapstoenter,text='F',bg='black',fg='white',font=('arial',10,'bold'),width=5,height=2,bd=10,relief='groove')
        labelG=tk.Label(framecapstoenter,text='G',bg='black',fg='white',font=('arial',10,'bold'),width=5,height=2,bd=10,relief='groove')
        labelH=tk.Label(framecapstoenter,text='H',bg='black',fg='white',font=('arial',10,'bold'),width=5,height=2,bd=10,relief='groove')
        labelJ=tk.Label(framecapstoenter,text='J',bg='black',fg='white',font=('arial',10,'bold'),width=5,height=2,bd=10,relief='groove')
        labelK=tk.Label(framecapstoenter,text='K',bg='black',fg='white',font=('arial',10,'bold'),width=5,height=2,bd=10,relief='groove')
        labelL=tk.Label(framecapstoenter,text='L',bg='black',fg='white',font=('arial',10,'bold'),width=5,height=2,bd=10,relief='groove')
        labelenter=tk.Label(framecapstoenter,text='enter',bg='black',fg='white',font=('arial',10,'bold'),width=10,height=2,bd=10,relief='groove')
        labelcaps.grid(row=0,column=0,padx=5)
        labelA.grid(row=0,column=1,padx=5)
        labelS.grid(row=0,column=2,padx=5)
        labelD.grid(row=0,column=3,padx=5)
        labelF.grid(row=0,column=4,padx=5)
        labelG.grid(row=0,column=5,padx=5)
        labelH.grid(row=0,column=6,padx=5)
        labelJ.grid(row=0,column=7,padx=5)
        labelK.grid(row=0,column=8,padx=5)
        labelL.grid(row=0,column=9,padx=5)
        labelenter.grid(row=0,column=10,padx=5)
        frameshifttoshift1=tk.Frame(keyboard_frame)
        frameshifttoshift1.grid(row=3,column=0,pady=3)
        labelshift=tk.Label(frameshifttoshift1,text='shift',bg='black',fg='white',font=('arial',10,'bold'),width=5,height=2,bd=10,relief='groove')
        labelZ=tk.Label(frameshifttoshift1,text='Z',bg='black',fg='white',font=('arial',10,'bold'),width=5,height=2,bd=10,relief='groove')
        labelX=tk.Label(frameshifttoshift1,text='X',bg='black',fg='white',font=('arial',10,'bold'),width=5,height=2,bd=10,relief='groove')
        labelC=tk.Label(frameshifttoshift1,text='C',bg='black',fg='white',font=('arial',10,'bold'),width=5,height=2,bd=10,relief='groove')
        labelV=tk.Label(frameshifttoshift1,text='V',bg='black',fg='white',font=('arial',10,'bold'),width=5,height=2,bd=10,relief='groove')
        labelB=tk.Label(frameshifttoshift1,text='B',bg='black',fg='white',font=('arial',10,'bold'),width=5,height=2,bd=10,relief='groove')
        labelN=tk.Label(frameshifttoshift1,text='N',bg='black',fg='white',font=('arial',10,'bold'),width=5,height=2,bd=10,relief='groove')
        labelM=tk.Label(frameshifttoshift1,text='M',bg='black',fg='white',font=('arial',10,'bold'),width=5,height=2,bd=10,relief='groove')
        labelshift1=tk.Label(frameshifttoshift1,text='shift1',bg='black',fg='white',font=('arial',10,'bold'),width=5,height=2,bd=10,relief='groove')
        labelshift.grid(row=0,column=0,padx=5)
        labelZ.grid(row=0,column=1,padx=5)
        labelX.grid(row=0,column=2,padx=5)
        labelC.grid(row=0,column=3,padx=5)
        labelV.grid(row=0,column=4,padx=5)
        labelB.grid(row=0,column=5,padx=5)
        labelN.grid(row=0,column=6,padx=5)
        labelM.grid(row=0,column=7,padx=5)
        labelshift1.grid(row=0,column=8,padx=5)
        framectrltoalt=tk.Frame(keyboard_frame)
        framectrltoalt.grid(row=4,column=0,pady=3)
        labelctrl=tk.Label(framectrltoalt,text='ctrl',bg='black',fg='white',font=('arial',10,'bold'),width=3,height=1,bd=10,relief="groove")
        labelSpace=tk.Label(framectrltoalt,text='',bg='black',fg='white',font=('arial',10,'bold'),width='30',height=1,bd=10,relief="groove")
        labelalt=tk.Label(framectrltoalt,text='alt',bg='black',fg='white',font=('arial',10,'bold'),width='3',height=1,bd=10,relief="groove")
        labelctrl.grid(row=0,column=0,padx=5)
        labelSpace.grid(row=0,column=1,padx=5)
        labelalt.grid(row=0,column=2,padx=5)
         
        def changeBG(widget):
         widget.config(bg='green')
         widget.after(100,lambda :widget.config(bg='black'))
         label_numbers=[label1,label2,label3,label4,label5,label6,label7,label8,label9,label0]      
         label_alphabets=[labelA,labelB,labelC,labelD,labelE,labelF,labelG,labelH,labelI,labelJ,labelK,labelL,labelM,labelN,
                      labelO,labelP,labelQ,labelR,labelS,labelT,labelU,labelV,labelW,labelX,labelY,labelZ]
         space_label=[labelSpace]
         Backspace_label=[labelBackspace]
         tab_label=[labeltab]
         caps_label=[labelcaps]
         enter_label=[labelenter]
         shift_label=[labelshift]
         shift1_label=[labelshift1]
         ctrl_label=[labelctrl]
         alt_label=[labelalt]
         binding_numbers=['1','2','3','4','5','6','7','8','9','0']      
         binding_capital_alphabets=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T',
                                'U','V','W','X','Y','Z']      
         binding_small_alphabets=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t',
                              'u','v','w','x','y','z']      
         for numbers in range(len(binding_numbers)):
             keyboard_frame.bind(binding_numbers[numbers],lambda event,label=label_numbers[numbers]:changeBG(label))      
         for capital_alphabets in range(len(binding_capital_alphabets)):
             keyboard_frame.bind(binding_capital_alphabets[capital_alphabets],lambda event,label=label_alphabets[capital_alphabets]:changeBG(label))      
         for small_alphabets in range(len(binding_small_alphabets)):
             keyboard_frame.bind(binding_small_alphabets[small_alphabets],lambda event,label=label_alphabets[small_alphabets]:changeBG(label))      
         keyboard_frame.bind('<space>',lambda event:changeBG(space_label[0]))
         keyboard_frame.bind('<BackSpace>',lambda event:changeBG(Backspace_label[0]))
         keyboard_frame.bind('<Tab>',lambda event:changeBG(tab_label[0]))
         keyboard_frame.bind('<Caps_Lock>',lambda event:changeBG(caps_label[0]))
         keyboard_frame.bind('<Return>',lambda event:changeBG(enter_label[0]))
         keyboard_frame.bind('<Shift_L>',lambda event:changeBG(shift_label[0]))
         keyboard_frame.bind('<Shift_R>',lambda event:changeBG(shift1_label[0]))
         keyboard_frame.bind('<Control_R>',lambda event:changeBG(ctrl_label[0]))
         keyboard_frame.bind('<Alt_R>',lambda event:changeBG(alt_label[0] ))          

         keyboard_frame.mainloop()
            
        
###########################################      SIXTH PAGE     ##################################################5

class SixthPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        load = Image.open("C:\A\gb.jpg")
        photo = ImageTk.PhotoImage(load)
        label = tk.Label(self, image=photo)
        label.image=photo
        label.place(x=0,y=0)

       
     
        #button6 = tk.Button(self, text="Back",height=1,width=7,  bg='white',fg='dark olive green', font=('Bold',15),
        #                    command=lambda: controller.show_frame(ThirdPage))  
        #button6.place(x=1000, y=600) 

        
        paragraph_frame=tk.Frame(self)
        paragraph_frame.place(x=100,y=50)
      
        paragraph_list=['pizazz obstinance piazzas pizzas linol urban aluminum foramens assuming molybdenum',
                        'well-to-do adjoining guttural jog vacuous pastoral electric squalid',
                        'penitent thinkable crow overjoyed real breath bustling command narrow',
                        'connoisseur meretricious sash opaqueness Honeybee',
                        'disingenuous slate plethora acclaimed presumption turbid'
                          ]
        random.shuffle(paragraph_list)
        label_paragraph=tk.Label(paragraph_frame,text=paragraph_list[0],bg='black',fg='white',width=53,wraplength=912,justify='left',font=('arial',20,'bold'))
        label_paragraph.grid()

        textarea_frame=tk.Frame(self)
        textarea_frame.place(x=135,y=130)
      
        textarea=tk.Text(textarea_frame,font=('arial',12,'bold'),width=92,height=2,bd=1,relief='groove',wrap='word'
                  )
        textarea.grid()

        #button6 = tk.Button(self, text="Back",height=1,width=7,  bg='black',fg='dark olive green', font=('Bold',15),
        #                 command=lambda: controller.show_frame(ThirdPage))  
        #button6.place(x=1020, y=600)  

# functions

        totaltime=20
        time=0
        elapsedtimeinminutes=0
        
        
        def start_timer():

            
            startButton.config(state='disabled')
            time=0
            textarea.config(state='normal')
            textarea.focus()

            #for time in range(1,21):
            #    elapsed_timer_label.config(text=time)
            #    remainingtime=totaltime-time
            #    remaining_timer_label.config(text=remainingtime)
            #    sleep(1)
            #    self.update()

            textarea.config(state='normal')
            resetButton.config(state='normal')


        def count():
          wrongwords=0
          while time!=totaltime:
              entered_paragraph=textarea.get(1.0,'end').split()
              totalwords=len(entered_paragraph)
      
          totalwords_count_label.config(text=totalwords)
      
          para_word_list=label_paragraph['text'].split()
      
          for pair in list(zip(para_word_list,entered_paragraph)):
              if pair[0]!=pair[1]:
                  wrongwords+=1
      
          wrongwords_count_label.config(text=wrongwords)
      
          elapsedtimeinminutes=time/20
          #wpm=(totalwords-wrongwords)/elapsedtimeinminutes
          wpm = ((totalwords/ 5) - (totalwords - wrongwords)) / (self.time[0] + (self.time[1] / 60))
          wpm_count_label.config(text=wpm)
          gross_wpm=totalwords/elapsedtimeinminutes
          accuracy=wpm/gross_wpm*100
          accuracy=round(accuracy)
          accuracy_percent_label.config(text=str(accuracy)+'%')


        def start():
            t1=threading.Thread(target=start_timer)
            t1.start()
        
            t2 = threading.Thread(target=count)
            t2.start()

        def cal():

            wrongwords=0
        
            entered_paragraph=textarea.get(1.0,'end').split()
            totalwords=len(entered_paragraph)
           

            para_word_list=label_paragraph['text'].split()

            for pair in list(zip(para_word_list,entered_paragraph)):
                if pair[0]!=pair[1]:
                    wrongwords+=1
                    wrongwords_count_label.config(text=wrongwords)
    
            entered_paragraph=textarea.get(1.0,'end').split()
            totalwords=len(entered_paragraph)
            totalwords_count_label.config(text=totalwords)

            for time in range(1,21):
             elapsedtimeinminutes=time/60
             wpm = ((totalwords - wrongwords)) / elapsedtimeinminutes
             wpm_count_label.config(text=wpm)

             gross_wpm=totalwords/elapsedtimeinminutes
             accuracy=wpm/gross_wpm*100
             accuracy=round(accuracy)
             accuracy_percent_label.config(text=str(accuracy)+'%')  

        def start():
            t1=threading.Thread(target=start_timer)
            t1.start()

            t2 = threading.Thread(target=count)
            t2.start()

        def reset():
            global time,elapsedtimeinminutes
            time=0
            elapsedtimeinminutes=0
            startButton.config(state='normal')
            resetButton.config(state='disabled')
            textarea.config(state='normal')
            textarea.delete(1.0,'end')
            textarea.config(state='disabled')

            #elapsed_timer_label.config(text='0')
            #remaining_timer_label.config(text='0')
            wpm_count_label.config(text='0')
            accuracy_percent_label.config(text='0')
            totalwords_count_label.config(text='0')
            wrongwords_count_label.config(text='0')


        #frame_output=tk.Frame(mainframe)
        #frame_output.grid(row=1,column=9,sticky='ew')

        #elapsed_time_label=tk.Label(self,text='ElapsedTime',font=('Tahoma',12,'bold'),fg='PaleGreen',bg='black')
        #elapsed_time_label.place(x=135,y=200)
#
        #elapsed_timer_label=tk.Label(self,text='0',font=('Tahoma',12,'bold'),fg='white',bg='black')
        #elapsed_timer_label.place(x=250,y=200)

        #remaining_time_label=tk.Label(self,text='RemainingTime',font=('Tahoma',12,'bold'),fg='PaleGreen',bg='black')
        #remaining_time_label.place(x=135,y=250)
#
        #remaining_timer_label=tk.Label(self,text='60',font=('Tahoma',12,'bold'),fg='white',bg='black')
        #remaining_timer_label.place(x=275,y=250)

########        

        wpm_label=tk.Label(self,text='WPM',font=('Tahoma',12,'bold'),fg='PaleGreen',bg='black')
        wpm_label.place(x=135,y=200)

        wpm_count_label=tk.Label(self,text='0',font=('Tahoma',12,'bold'),fg='white',bg='black')
        wpm_count_label.place(x=200,y=200)

        accuracy_label=tk.Label(self,text='Accuracy',font=('Tahoma',12,'bold'),fg='PaleGreen',bg='black')
        accuracy_label.place(x=135,y=250)

        accuracy_percent_label=tk.Label(self,text='0',font=('Tahoma',12,'bold'),fg='white',bg='black')
        accuracy_percent_label.place(x=250,y=250)

########        

        totalwords_label=tk.Label(self,text='TotalWords',font=('Tahoma',12,'bold'),fg='PaleGreen',bg='black')
        totalwords_label.place(x=800,y=200)

        totalwords_count_label=tk.Label(self,text='0',font=('Tahoma',12,'bold'),fg='white',bg='black')
        totalwords_count_label.place(x=920,y=200)

        wrongwords_label=tk.Label(self,text='WrongWords',font=('Tahoma',12,'bold'),fg='PaleGreen',bg='black')
        wrongwords_label.place(x=800,y=250)

        wrongwords_count_label=tk.Label(self,text='0',font=('Tahoma',12,'bold'),fg='white',bg='black')
        wrongwords_count_label.place(x=920,y=250)

#########        

        #buttons_Frame=tk.Frame(mainframe)
        #buttons_Frame.grid(row=4,column=0)

        startButton=tk.Button(self,text='Start',bg='green',font=('Tahoma',12,'bold'),fg='black',command=start)
        startButton.place(x=400,y=225)

        resetButton=tk.Button(self,text='Reset',bg='powder blue',font=('Tahoma',12,'bold'),fg='dark olive green',state='disabled',command=reset)
        resetButton.place(x=530,y=600)

        
        b=tk.Button(self,text="Submit",fg='white',bg='black',font=('bold',12),command=cal)
        b.place(x=525,y=226)

        button6 = tk.Button(self, text="Back",  bg='red',fg='black', font=('Bold',13),
                         command=lambda: controller.show_frame(ThirdPage))  
        button6.place(x=660, y=225)

                
        keyboard_frame=tk.Frame(self,bg='white')
        keyboard_frame.place(x=135,y=300)
           
        frame1toBackspace=tk.Frame(keyboard_frame)
        frame1toBackspace.grid(row=0,column=0,pady=3)

        def changeBG(widget):
         widget.config(bg='green')
         widget.after(100,lambda :widget.config(bg='black'))
         label_numbers=[label1,label2,label3,label4,label5,label6,label7,label8,label9,label0]      
         label_alphabets=[labelA,labelB,labelC,labelD,labelE,labelF,labelG,labelH,labelI,labelJ,labelK,labelL,labelM,labelN,
                      labelO,labelP,labelQ,labelR,labelS,labelT,labelU,labelV,labelW,labelX,labelY,labelZ]
         space_label=[labelSpace]
         Backspace_label=[labelBackspace]
         tab_label=[labeltab]
         caps_label=[labelcaps]
         enter_label=[labelenter]
         shift_label=[labelshift]
         shift1_label=[labelshift1]
         ctrl_label=[labelctrl]
         alt_label=[labelalt]
         binding_numbers=['1','2','3','4','5','6','7','8','9','0']      
         binding_capital_alphabets=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T',
                                'U','V','W','X','Y','Z']      
         binding_small_alphabets=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t',
                              'u','v','w','x','y','z']      
         for numbers in range(len(binding_numbers)):
             keyboard_frame.bind(binding_numbers[numbers],lambda event,label=label_numbers[numbers]:changeBG(label))      
         for capital_alphabets in range(len(binding_capital_alphabets)):
             keyboard_frame.bind(binding_capital_alphabets[capital_alphabets],lambda event,label=label_alphabets[capital_alphabets]:changeBG(label))      
         for small_alphabets in range(len(binding_small_alphabets)):
             keyboard_frame.bind(binding_small_alphabets[small_alphabets],lambda event,label=label_alphabets[small_alphabets]:changeBG(label))      
         keyboard_frame.bind('<space>',lambda event:changeBG(space_label[0]))
         keyboard_frame.bind('<BackSpace>',lambda event:changeBG(Backspace_label[0]))
         keyboard_frame.bind('<Tab>',lambda event:changeBG(tab_label[0]))
         keyboard_frame.bind('<Caps_Lock>',lambda event:changeBG(caps_label[0]))
         keyboard_frame.bind('<Return>',lambda event:changeBG(enter_label[0]))
         keyboard_frame.bind('<Shift_L>',lambda event:changeBG(shift_label[0]))
         keyboard_frame.bind('<Shift_R>',lambda event:changeBG(shift1_label[0]))
         keyboard_frame.bind('<Control_R>',lambda event:changeBG(ctrl_label[0]))
         keyboard_frame.bind('<Alt_R>',lambda event:changeBG(alt_label[0] ))    
        label1=tk.Label(frame1toBackspace,text='1',bg='black',fg='white',font=('arial',10,'bold'),width=5,height=2,bd=10,relief='groove')
        label2=tk.Label(frame1toBackspace,text='2',bg='black',fg='white',font=('arial',10,'bold'),width=5,height=2,bd=10,relief='groove')
        label3=tk.Label(frame1toBackspace,text='3',bg='black',fg='white',font=('arial',10,'bold'),width=5,height=2,bd=10,relief='groove')
        label4=tk.Label(frame1toBackspace,text='4',bg='black',fg='white',font=('arial',10,'bold'),width=5,height=2,bd=10,relief='groove')
        label5=tk.Label(frame1toBackspace,text='5',bg='black',fg='white',font=('arial',10,'bold'),width=5,height=2,bd=10,relief='groove')
        label6=tk.Label(frame1toBackspace,text='6',bg='black',fg='white',font=('arial',10,'bold'),width=5,height=2,bd=10,relief='groove')
        label7=tk.Label(frame1toBackspace,text='7',bg='black',fg='white',font=('arial',10,'bold'),width=5,height=2,bd=10,relief='groove')
        label8=tk.Label(frame1toBackspace,text='8',bg='black',fg='white',font=('arial',10,'bold'),width=5,height=2,bd=10,relief='groove')
        label9=tk.Label(frame1toBackspace,text='9',bg='black',fg='white',font=('arial',10,'bold'),width=5,height=2,bd=10,relief='groove')
        label0=tk.Label(frame1toBackspace,text='0',bg='black',fg='white',font=('arial',10,'bold'),width=5,height=2,bd=10,relief='groove')
        labelBackspace=tk.Label(frame1toBackspace,text='backspace',bg='black',fg='white',font=('arial',10,'bold'),width=8,height=2,bd=10,relief='groove')
        label1.grid(row=0,column=0,padx=5)
        label2.grid(row=0,column=1,padx=5)
        label3.grid(row=0,column=2,padx=5)
        label4.grid(row=0,column=3,padx=5)
        label5.grid(row=0,column=4,padx=5)
        label6.grid(row=0,column=5,padx=5)
        label7.grid(row=0,column=6,padx=5)
        label8.grid(row=0,column=7,padx=5)
        label9.grid(row=0,column=8,padx=5)
        label0.grid(row=0,column=9,padx=5)
        labelBackspace.grid(row=0,column=10,padx=5)
        frametabtop=tk.Frame(keyboard_frame)
        frametabtop.grid(row=1,column=0,pady=3)
        labeltab=tk.Label(frametabtop,text='tab',bg='black',fg='white',font=('arial',10,'bold'),width=6,height=2,bd=10,relief='groove')
        labelQ=tk.Label(frametabtop,text='Q',bg='black',fg='white',font=('arial',10,'bold'),width=5,height=2,bd=10,relief='groove')
        labelW=tk.Label(frametabtop,text='W',bg='black',fg='white',font=('arial',10,'bold'),width=5,height=2,bd=10,relief='groove')
        labelE=tk.Label(frametabtop,text='E',bg='black',fg='white',font=('arial',10,'bold'),width=5,height=2,bd=10,relief='groove')
        labelR=tk.Label(frametabtop,text='R',bg='black',fg='white',font=('arial',10,'bold'),width=5,height=2,bd=10,relief='groove')
        labelT=tk.Label(frametabtop,text='T',bg='black',fg='white',font=('arial',10,'bold'),width=5,height=2,bd=10,relief='groove')
        labelY=tk.Label(frametabtop,text='Y',bg='black',fg='white',font=('arial',10,'bold'),width=5,height=2,bd=10,relief='groove')
        labelU=tk.Label(frametabtop,text='U',bg='black',fg='white',font=('arial',10,'bold'),width=5,height=2,bd=10,relief='groove')
        labelI=tk.Label(frametabtop,text='I',bg='black',fg='white',font=('arial',10,'bold'),width=5,height=2,bd=10,relief='groove')
        labelO=tk.Label(frametabtop,text='O',bg='black',fg='white',font=('arial',10,'bold'),width=5,height=2,bd=10,relief='groove')
        labelP=tk.Label(frametabtop,text='P',bg='black',fg='white',font=('arial',10,'bold'),width=5,height=2,bd=10,relief='groove')
        labeltab.grid(row=0,column=0,padx=5)
        labelQ.grid(row=0,column=1,padx=5)
        labelW.grid(row=0,column=2,padx=5)
        labelE.grid(row=0,column=3,padx=5)
        labelR.grid(row=0,column=4,padx=5)
        labelT.grid(row=0,column=5,padx=5)
        labelY.grid(row=0,column=6,padx=5)
        labelU.grid(row=0,column=7,padx=5)
        labelI.grid(row=0,column=8,padx=5)
        labelO.grid(row=0,column=9,padx=5)
        labelP.grid(row=0,column=10,padx=5)
        framecapstoenter=tk.Frame(keyboard_frame)
        framecapstoenter.grid(row=2,column=0,pady=3)
        labelcaps=tk.Label(framecapstoenter,text='caps',bg='black',fg='white',font=('arial',10,'bold'),width=5,height=2,bd=10,relief='groove')
        labelA=tk.Label(framecapstoenter,text='A',bg='black',fg='white',font=('arial',10,'bold'),width=5,height=2,bd=10,relief='groove')
        labelS=tk.Label(framecapstoenter,text='S',bg='black',fg='white',font=('arial',10,'bold'),width=5,height=2,bd=10,relief='groove')
        labelD=tk.Label(framecapstoenter,text='D',bg='black',fg='white',font=('arial',10,'bold'),width=5,height=2,bd=10,relief='groove')
        labelF=tk.Label(framecapstoenter,text='F',bg='black',fg='white',font=('arial',10,'bold'),width=5,height=2,bd=10,relief='groove')
        labelG=tk.Label(framecapstoenter,text='G',bg='black',fg='white',font=('arial',10,'bold'),width=5,height=2,bd=10,relief='groove')
        labelH=tk.Label(framecapstoenter,text='H',bg='black',fg='white',font=('arial',10,'bold'),width=5,height=2,bd=10,relief='groove')
        labelJ=tk.Label(framecapstoenter,text='J',bg='black',fg='white',font=('arial',10,'bold'),width=5,height=2,bd=10,relief='groove')
        labelK=tk.Label(framecapstoenter,text='K',bg='black',fg='white',font=('arial',10,'bold'),width=5,height=2,bd=10,relief='groove')
        labelL=tk.Label(framecapstoenter,text='L',bg='black',fg='white',font=('arial',10,'bold'),width=5,height=2,bd=10,relief='groove')
        labelenter=tk.Label(framecapstoenter,text='enter',bg='black',fg='white',font=('arial',10,'bold'),width=10,height=2,bd=10,relief='groove')
        labelcaps.grid(row=0,column=0,padx=5)
        labelA.grid(row=0,column=1,padx=5)
        labelS.grid(row=0,column=2,padx=5)
        labelD.grid(row=0,column=3,padx=5)
        labelF.grid(row=0,column=4,padx=5)
        labelG.grid(row=0,column=5,padx=5)
        labelH.grid(row=0,column=6,padx=5)
        labelJ.grid(row=0,column=7,padx=5)
        labelK.grid(row=0,column=8,padx=5)
        labelL.grid(row=0,column=9,padx=5)
        labelenter.grid(row=0,column=10,padx=5)
        frameshifttoshift1=tk.Frame(keyboard_frame)
        frameshifttoshift1.grid(row=3,column=0,pady=3)
        labelshift=tk.Label(frameshifttoshift1,text='shift',bg='black',fg='white',font=('arial',10,'bold'),width=5,height=2,bd=10,relief='groove')
        labelZ=tk.Label(frameshifttoshift1,text='Z',bg='black',fg='white',font=('arial',10,'bold'),width=5,height=2,bd=10,relief='groove')
        labelX=tk.Label(frameshifttoshift1,text='X',bg='black',fg='white',font=('arial',10,'bold'),width=5,height=2,bd=10,relief='groove')
        labelC=tk.Label(frameshifttoshift1,text='C',bg='black',fg='white',font=('arial',10,'bold'),width=5,height=2,bd=10,relief='groove')
        labelV=tk.Label(frameshifttoshift1,text='V',bg='black',fg='white',font=('arial',10,'bold'),width=5,height=2,bd=10,relief='groove')
        labelB=tk.Label(frameshifttoshift1,text='B',bg='black',fg='white',font=('arial',10,'bold'),width=5,height=2,bd=10,relief='groove')
        labelN=tk.Label(frameshifttoshift1,text='N',bg='black',fg='white',font=('arial',10,'bold'),width=5,height=2,bd=10,relief='groove')
        labelM=tk.Label(frameshifttoshift1,text='M',bg='black',fg='white',font=('arial',10,'bold'),width=5,height=2,bd=10,relief='groove')
        labelshift1=tk.Label(frameshifttoshift1,text='shift1',bg='black',fg='white',font=('arial',10,'bold'),width=5,height=2,bd=10,relief='groove')
        labelshift.grid(row=0,column=0,padx=5)
        labelZ.grid(row=0,column=1,padx=5)
        labelX.grid(row=0,column=2,padx=5)
        labelC.grid(row=0,column=3,padx=5)
        labelV.grid(row=0,column=4,padx=5)
        labelB.grid(row=0,column=5,padx=5)
        labelN.grid(row=0,column=6,padx=5)
        labelM.grid(row=0,column=7,padx=5)
        labelshift1.grid(row=0,column=8,padx=5)
        framectrltoalt=tk.Frame(keyboard_frame)
        framectrltoalt.grid(row=4,column=0,pady=3)
        labelctrl=tk.Label(framectrltoalt,text='ctrl',bg='black',fg='white',font=('arial',10,'bold'),width=3,height=1,bd=10,relief="groove")
        labelSpace=tk.Label(framectrltoalt,text='',bg='black',fg='white',font=('arial',10,'bold'),width='30',height=1,bd=10,relief="groove")
        labelalt=tk.Label(framectrltoalt,text='alt',bg='black',fg='white',font=('arial',10,'bold'),width='3',height=1,bd=10,relief="groove")
        labelctrl.grid(row=0,column=0,padx=5)
        labelSpace.grid(row=0,column=1,padx=5)
        labelalt.grid(row=0,column=2,padx=5)
         
        

        

##################################       MAIN     #############################################################
               
class Application(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        
        #creating a window
        window = tk.Frame(self)
        window.pack()
        
        window.grid_rowconfigure(0, minsize = 647)
        window.grid_columnconfigure(0, minsize = 1142)
        
        self.frames = {}
        for F in (FirstPage, SecondPage, ThirdPage,FourthPage,FifthPage,SixthPage):
            frame = F(window,self)
            self.frames[F] = frame
            frame.grid(row = 0, column=0, sticky="nsew")
            
        self.show_frame(FirstPage)
        
    def show_frame(self, page):
        frame = self.frames[page]
        frame.tkraise()
        self.title("TypingSpeedTest")

app = Application()
app.maxsize(1142,647)
app.mainloop()
