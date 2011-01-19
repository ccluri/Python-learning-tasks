import pygame.mixer as mix
import string as st
from numpy import zeros, vstack
import wave

mix.init(frequency=11025, size=16)

dit=zeros((1000,1)) 
dah=zeros((3000,1))
ssp=zeros((1000,1)) #between symbols
lsp=zeros((10000,1)) #between letters
ssp=ssp+0.1
lsp=lsp+0.1

i=1 #dit
if (i<1000):
    dit[i]=0.4
    dit[i+1]=0.0
    dit[i+2]=-0.4
    dit[i+3]=0.0
    i=i+4
i=1 #dah
if (i<3000):
    dah[i]=0.4
    dah[i+1]=0.0
    dah[i+2]=-0.4
    dah[i+3]=0.0
    i=i+4
i=1 #ssp
if (i<1000):
    ssp[i]=0.1
    ssp[i+1]=0.0
    ssp[i+2]=-0.1
    ssp[i+3]=0.0
    i=i+4
i=1 #lsp    
if (i<10000):
    lsp[i]=0.1
    lsp[i+1]=0.0
    lsp[i+2]=-0.1
    lsp[i+3]=0.0
    i=i+4   
    
A = vstack((dit,ssp,dah))
B = vstack((dah,ssp,dit,ssp,dit,ssp,dit))
C = vstack((dah,ssp,dit,ssp,dah,ssp,dit))
D = vstack((dah,ssp,dit,ssp,dit))
E = vstack((dit))
F = vstack((dit,ssp,dit,ssp,dah,ssp,dit))
G = vstack((dah,ssp,dah,ssp,dit))
H = vstack((dit,ssp,dit,ssp,dit,ssp,dit))
I = vstack((dit,ssp,dit))
J = vstack((dit,ssp,dah,ssp,dah,ssp,dah))
K = vstack((dah,ssp,dit,ssp,dah))
L = vstack((dit,ssp,dah,ssp,dit,ssp,dit))
M = vstack((dah,ssp,dah))
N = vstack((dah,ssp,dit))
O = vstack((dah,ssp,dah,ssp,dah))
P = vstack((dit,ssp,dah,ssp,dah,ssp,dit))
Q = vstack((dah,ssp,dah,ssp,dit,ssp,dah))
R = vstack((dit,ssp,dah,ssp,dit))
S = vstack((dit,ssp,dit,ssp,dit))
T = vstack((dah))
U = vstack((dit,ssp,dit,ssp,dah))
V = vstack((dit,ssp,dit,ssp,dit,ssp,dah))
W = vstack((dit,ssp,dah,ssp,dah))
X = vstack((dah,ssp,dit,ssp,dit,ssp,dah))
Y = vstack((dah,ssp,dit,ssp,dah,ssp,dah))
Z = vstack((dah,ssp,dah,ssp,dit,ssp,dit))
period = vstack((dit,ssp,dah,ssp,dit,ssp,dah,ssp,dit,ssp,dah))
comma = vstack((dah,ssp,dah,ssp,dit,ssp,dit,ssp,dah,ssp,dah))
question = vstack((dit,ssp,dit,ssp,dah,ssp,dah,ssp,dit,ssp,dit))
slash_ = vstack((dah,ssp,dit,ssp,dit,ssp,dah,ssp,dit))
n1 = vstack((dit,ssp,dah,ssp,dah,ssp,dah,ssp,dah))
n2 = vstack((dit,ssp,dit,ssp,dah,ssp,dah,ssp,dah))
n3 = vstack((dit,ssp,dit,ssp,dit,ssp,dah,ssp,dah))
n4 = vstack((dit,ssp,dit,ssp,dit,ssp,dit,ssp,dah))
n5 = vstack((dit,ssp,dit,ssp,dit,ssp,dit,ssp,dit))
n6 = vstack((dah,ssp,dit,ssp,dit,ssp,dit,ssp,dit))
n7 = vstack((dah,ssp,dah,ssp,dit,ssp,dit,ssp,dit))
n8 = vstack((dah,ssp,dah,ssp,dah,ssp,dit,ssp,dit))
n9 = vstack((dah,ssp,dah,ssp,dah,ssp,dah,ssp,dit))
n0 = vstack((dah,ssp,dah,ssp,dah,ssp,dah,ssp,dah))

text = raw_input("Enter text:")
text = st.upper(text)
mc = zeros((1,1))
l_txt = len(text)

for i in range(0,l_txt):
    
    mc= vstack((mc,text[i],lsp))

#mix.Sound(mc).play()    

file =wave.open('morse.wav','wb')
file.setparams((1,2,11025,11025*4,'NONE','noncompressed'))
file.writeframes(mc)
file.close()

mix.Sound('morse.wav').play()



