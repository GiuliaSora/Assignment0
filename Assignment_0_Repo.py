# -*- coding: utf-8 -*-
#Assignment 0
#Exercise B


H=0.8   #Highness of the glass
W=1.5   #Width of the glass
L=0.008 #Thickness of the glass
A=H*W   #Area 
k=0.78  #Thermal Conductivity 
Ti=20   #Temperature of the inside
Te=-10  #Temperature of the outside
h1=10   #Thermal Convection Coefficient of the inner surface
h2=40   #Thermal Convection Coefficient of the outer surface

R=L/(k*A)   #Conductive Resistance
R1=1/(h1*A) #Inner Convective Resistance
R2=1/(h2*A) #Outer Convective Resistance

Rtot=R+R1+R2 #Total Resistance
U=1/Rtot     #Overall Heat Transfer Coefficient
 
Q=U*(Ti-Te)    #Steady Rate of Heat Transfer
T1=Q*(R2+R)+Te #Temperature of the inner surface
print("The Total Resistance is:"+str(Rtot)+"[°C/W]")
print("The Steady Rate of Heat Transfer is:"+str(Q)+"[W]")
print("The Temperature of th Inner Surface is:"+str(T1)+"[°C]")