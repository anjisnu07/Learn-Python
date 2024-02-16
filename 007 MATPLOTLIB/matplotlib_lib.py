#MATPLOTLIB:->used for making plots and graphs
import matplotlib.pyplot as plt
import numpy as np

a=np.linspace(0,10,100)
b=np.sin(a)
c=np.cos(b)
print(a)
print(b)
print(c)

# plotting sine wave wrt a and b
plt.plot(a,b)
plt.show()

# plot cosine curve

plt.plot(a,c)
plt.show()

# Adding title x,y axis lable
plt.plot(a,b)
plt.xlabel('Angel')
plt.ylabel('Values')
plt.title("Sine wave")
plt.show()

# PLotting a parabola
a=np.linspace(-10,10,20)
b=a**2
plt.plot(a,b)
plt.show()

# PLotting using color/symbol we want 
a=np.linspace(-10,10,20)
b=a**2
plt.plot(a,b,'r*') #* symbol of red color
plt.show()

# Multiple graphs in a single plot
a=np.linspace(-5,5,50)
plt.plot(a,np.sin(a),'r+')
plt.plot(a,np.cos(a),'g-')
plt.show()

# BAR plot
fig=plt.figure() #create new fig or canvas for plot
ax=fig.add_axes([0,0,1,1]) # area of axes,[left,bottom,width,height] fomat
language=["beng","ENG","Hindi","urdu"]
person=[10,20,30,1]
ax.bar(language,person)
plt.xlabel("Language")
plt.ylabel("Person")
plt.title("Language Distribution") 
plt.show()

# Pie chart

fig1=plt.figure()
ax=fig1.add_axes([0,0,1,1])
language=["beng","ENG","Hindi","urdu"]
person=[10,20,30,1]
ax.pie(person,labels=language,autopct="%1.1f%%")
plt.show()

#Scatter plot
a=np.linspace(0,10,100)
b=np.sin(a)
c=np.cos(b)
fig3=plt.figure()
ax=fig3.add_axes([0,0,1,1])
ax.scatter(a,b,color='g')
ax.scatter(a,c,color='b')
plt.show()

#3D plot
fig3=plt.figure()
ax=plt.axes(projection='3d')
x=20*np.random.random(100)
y=np.sin(x)
z=np.cos(x)
ax.scatter(x,y,z,c=z,cmap='Blues')
plt.show()
