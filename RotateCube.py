import numpy as np
import math 
import turtle

turtle.pensize(1)
turtle.hideturtle()
turtle.speed(0)

for i in range(100):
        theta=i*0.05 #rotation along y-axis
        phi=2*theta #rotation along z-axis
        beta=3*theta #rotation along x-axis
        shift=10
        scale=1000

        A=np.array([[math.cos(theta),0,-math.sin(theta)],[0,1,0],[math.sin(theta),0,math.cos(theta)]])
        B=np.array([[math.cos(phi),-math.sin(phi),0],[math.sin(phi),math.cos(phi),0],[0,0,1]])
        C=np.array([[1,0,0],[0,math.cos(beta),math.sin(beta)],[0,-math.sin(beta),math.cos(beta)]])

        coordinates=np.array([[-1,-1,-1],[-1,-1,1],[-1,1,-1],[-1,1,1],[1,-1,-1],[1,-1,1],[1,1,-1],[1,1,1]])

        newcoord=A.dot(B.dot(C.dot(coordinates.T)))
        newcoord=newcoord.T+[0,0,shift]

        for i in range(8):
            newcoord[i,0]=scale*newcoord[i,0]/newcoord[i,2]
            newcoord[i,1]=scale*newcoord[i,1]/newcoord[i,2]

        newcoord=newcoord-newcoord[0]
        seq=[1,3,2,0,4,5,7,6,4,5,1,5,7,3,7,6,2,6]

        for i in range(18):
            turtle.goto(newcoord[seq[i],0],newcoord[seq[i],1])

        turtle.penup()
        turtle.goto(newcoord[0][0],newcoord[0][1])    
        turtle.pendown()
        turtle.clear()    

turtle.done()