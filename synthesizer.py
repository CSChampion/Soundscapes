import pygame
import sys
from pygame import*
import time
def play (x):
    mixer.music.load(x+".WAV")
    mixer.music.play()
    mixer.music.stop
def playint (x,y):
    mixer.music.load(str(x)+str(y)+".WAV")
    mixer.music.play()
    mixer.music.stop
mixer.init()
ans=int(input("""If you wish to use:
interactive mode, type 1.
script mode, type 2
multiple voice, type 3
 :"""))
q = []
pygame.init()
display = pygame.display.set_mode((300, 300))
if ans==1:
    while True:
        if len(q) >= 2:
            q = []
        p=[]
        if len (q)==0:
            for event in pygame.event.get():
            
                if event.type == pygame.QUIT:
                      pygame.quit()
                      sys.exit()
#            if event.type==pygame.KEYDOWN:
#               while True:
#                       ke=int(event.key)
#                       key=(chr(ke))
#                       print(key)
#                       playint(key)
#                       break
                if event.type==pygame.KEYDOWN:
                        print("1")
                        ke=int(event.key)
                        if ke not in p:
                            p.append(ke)
                            print(p)
                        if len(q) == 0:
                            key=(chr(ke))
                            q.append(key)
                        print(q,"qq")
        if len(q)==1:
            for event in pygame.event.get():
                print("12")
                if event.type==pygame.KEYDOWN:
                        ke=int(event.key)
                        if ke not in p:
                            q.append(ke-48)
                            print(q,"q")
                        if len(q)==2:
                            playint(q[0],q[1])
                            break
                        print("1")            

k=[]
r=[]
if ans ==2:
    tempo=float(input("Enter tempo"))
    song=input("Enter the notes of the song(c for lower c and C for higher)")
    k.extend(song.split(" "))
    while True:
        for i in range (0,len(k)):
            if k[i]==".":
                break
            else:
                play(str(k[i]))
                time.sleep(tempo)
                continue
        break
voices=[]
q=[]
if ans ==3:
    num=int(input("Enter the number of voices"))
    for i in range(0,num):
        voice=input("Enter notes of voice")
        q.extend(voice.split(" "))
    for i in range(int(len(q)/2)):
            a=q[i]
            b=q[i+int(len(q)/2)]
            A=a+'.wav'
            B=b+'.wav'
            pygame.mixer.Channel(0).play(pygame.mixer.Sound(A))
            pygame.mixer.Channel(1).play(pygame.mixer.Sound(B))
            time.sleep(0.5)
