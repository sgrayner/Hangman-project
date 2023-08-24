import math
import numpy as np
import matplotlib.patches as patches
import matplotlib.pyplot as plt


'''base = plt.plot((-7, -1), (-8, -8)) # Base
pole = plt.plot((-4, -4), (-8, 8)) # Vertical pole
#plt.plot((-6, -4), (-8, -6)) # Left support at base
#plt.plot((-2, -4), (-8, -6)) # Right support at base
bracket = plt.plot((-4, 0), (8, 8)) # top bracket
rope = plt.plot((0, 0), (8, 2.5)) # rope
head = plt.Circle((0, 0), 0.2, color='r')


fig, ax = plt.subplots() # note we must use plt.subplots, not plt.subplot
# (or if you have an existing figure)
# fig = plt.gcf()
# ax = fig.gca()

ax.add_patch(head)



plt.axis([-10, 10, -10, 10])
plt.show()'''


'''fig=plt.figure()
ax=fig.add_subplot(1,1,1)
plt.plot([-7,-1],[-8,-8], color="black") # base
plt.plot([-4,-4],[-8,8], color="black") # vertical pole
plt.plot([-6,-4],[-8,-6], color="black") # left support at base
plt.plot([-2,-4],[-8,-6], color="black") # right support at base
plt.plot([-4,0],[8,8], color="black") # top bracket
plt.plot([0,0],[8,4], color="black") # rope
centreCircle = plt.Circle((0,3),1,color="black",fill=False) # head
ax.add_patch(centreCircle)
plt.plot([0,0],[2,-1], color="black") # body
plt.plot([0,-1],[2,0], color="black") # right arm
plt.plot([0,1],[2,0], color="black") # left arm
plt.plot([0,-1],[-1,-4.5], color="black") # right leg
plt.plot([0,1],[-1,-4.5], color="black") # left leg

plt.axis([-10, 10, -10, 10])

plt.show()'''

'''fig=plt.figure()
ax=fig.add_subplot(1,1,1)
picture_parts = [plt.plot([-7,-1],[-8,-8], color="black"), plt.plot([-4,-4],[-8,8], color="black"), plt.plot([-6,-4],[-8,-6], color="black"), plt.plot([-2,-4],[-8,-6], color="black"),
                plt.plot([-4,0],[8,8], color="black"), plt.plot([0,0],[8,4], color="black"), plt.Circle((0,3),1,color="black",fill=False), ax.add_patch(plt.Circle((0,3),1,color="black",fill=False)),
                plt.plot([0,0],[2,-1], color="black"), plt.plot([0,-1],[2,0], color="black"), plt.plot([0,1],[2,0], color="black"), plt.plot([0,-1],[-1,-4.5], color="black"), 
                plt.plot([0,1],[-1,-4.5], color="black")]
current_parts = picture_parts[0:5]
print(len(current_parts))
'''
def picture():
        fig=plt.figure()
        ax=fig.add_subplot(1,1,1)
        def picture_parts():
                picture_parts = [plt.plot([-7,-1],[-8,-8], color="black"), plt.plot([-4,-4],[-8,8], color="black"), plt.plot([-6,-4],[-8,-6], color="black"), plt.plot([-2,-4],[-8,-6], color="black"),
                                plt.plot([-4,0],[8,8], color="black"), plt.plot([0,0],[8,4], color="black"), plt.Circle((0,3),1,color="black",fill=False), ax.add_patch(plt.Circle((0,3),1,color="black",fill=False)),
                                plt.plot([0,0],[2,-1], color="black"), plt.plot([0,-1],[2,0], color="black"), plt.plot([0,1],[2,0], color="black"), plt.plot([0,-1],[-1,-4.5], color="black"), 
                                plt.plot([0,1],[-1,-4.5], color="black")]
                
                current_parts = picture_parts[0:5]
                plt.close()
                return current_parts
        picture_parts()
        plt.axis([-10, 10, -10, 10])
        plt.show()

picture()

'''def picture():
        fig=plt.figure()
        ax=fig.add_subplot(1,1,1)
        plt.plot([-7,-1],[-8,-8], color="black")
        plt.axis([-10, 10, -10, 10])
        yield plt.show()
        plt.plot([-7,-1],[-8,-8], color="black")
        plt.plot([-4,-4],[-8,8], color="black")
        plt.axis([-10, 10, -10, 10])
        yield plt.show()
        plt.plot([-7,-1],[-8,-8], color="black")
        plt.plot([-4,-4],[-8,8], color="black")
        plt.plot([-6,-4],[-8,-6], color="black")
        plt.axis([-10, 10, -10, 10])
        yield plt.show()
        plt.plot([-7,-1],[-8,-8], color="black")
        plt.plot([-4,-4],[-8,8], color="black")
        plt.plot([-6,-4],[-8,-6], color="black")
        plt.plot([-2,-4],[-8,-6], color="black")
        plt.axis([-10, 10, -10, 10])
        yield plt.show()
        plt.plot([-7,-1],[-8,-8], color="black")
        plt.plot([-4,-4],[-8,8], color="black")
        plt.plot([-6,-4],[-8,-6], color="black")
        plt.plot([-2,-4],[-8,-6], color="black")
        plt.plot([-4,0],[8,8], color="black")
        plt.axis([-10, 10, -10, 10])
        yield plt.show()
        plt.plot([-7,-1],[-8,-8], color="black")
        plt.plot([-4,-4],[-8,8], color="black")
        plt.plot([-6,-4],[-8,-6], color="black")
        plt.plot([-2,-4],[-8,-6], color="black")
        plt.plot([-4,0],[8,8], color="black")
        plt.plot([0,0],[8,4], color="black")
        plt.axis([-10, 10, -10, 10])
        yield plt.show()
        plt.plot([-7,-1],[-8,-8], color="black")
        plt.plot([-4,-4],[-8,8], color="black")
        plt.plot([-6,-4],[-8,-6], color="black")
        plt.plot([-2,-4],[-8,-6], color="black")
        plt.plot([-4,0],[8,8], color="black")
        plt.plot([0,0],[8,4], color="black")
        plt.Circle((0,3),1,color="black",fill=False) 
        ax.add_patch(plt.Circle((0,3),1,color="black",fill=False))
        plt.axis([-10, 10, -10, 10])
        yield plt.show()
        plt.plot([-7,-1],[-8,-8], color="black")
        plt.plot([-4,-4],[-8,8], color="black")
        plt.plot([-6,-4],[-8,-6], color="black")
        plt.plot([-2,-4],[-8,-6], color="black")
        plt.plot([-4,0],[8,8], color="black")
        plt.plot([0,0],[8,4], color="black")
        plt.Circle((0,3),1,color="black",fill=False) 
        ax.add_patch(plt.Circle((0,3),1,color="black",fill=False))
        plt.plot([0,0],[2,-1], color="black")
        plt.axis([-10, 10, -10, 10])
        yield plt.show()
        plt.plot([-7,-1],[-8,-8], color="black")
        plt.plot([-4,-4],[-8,8], color="black")
        plt.plot([-6,-4],[-8,-6], color="black")
        plt.plot([-2,-4],[-8,-6], color="black")
        plt.plot([-4,0],[8,8], color="black")
        plt.plot([0,0],[8,4], color="black")
        plt.Circle((0,3),1,color="black",fill=False) 
        ax.add_patch(plt.Circle((0,3),1,color="black",fill=False))
        plt.plot([0,0],[2,-1], color="black")
        plt.plot([0,-1],[2,0], color="black")
        plt.axis([-10, 10, -10, 10])
        yield plt.show()
        plt.plot([-7,-1],[-8,-8], color="black")
        plt.plot([-4,-4],[-8,8], color="black")
        plt.plot([-6,-4],[-8,-6], color="black")
        plt.plot([-2,-4],[-8,-6], color="black")
        plt.plot([-4,0],[8,8], color="black")
        plt.plot([0,0],[8,4], color="black")
        plt.Circle((0,3),1,color="black",fill=False) 
        ax.add_patch(plt.Circle((0,3),1,color="black",fill=False))
        plt.plot([0,0],[2,-1], color="black")
        plt.plot([0,-1],[2,0], color="black")
        plt.plot([0,1],[2,0], color="black")
        plt.axis([-10, 10, -10, 10])
        yield plt.show()
        plt.plot([-7,-1],[-8,-8], color="black")
        plt.plot([-4,-4],[-8,8], color="black")
        plt.plot([-6,-4],[-8,-6], color="black")
        plt.plot([-2,-4],[-8,-6], color="black")
        plt.plot([-4,0],[8,8], color="black")
        plt.plot([0,0],[8,4], color="black")
        plt.Circle((0,3),1,color="black",fill=False) 
        ax.add_patch(plt.Circle((0,3),1,color="black",fill=False))
        plt.plot([0,0],[2,-1], color="black")
        plt.plot([0,-1],[2,0], color="black")
        plt.plot([0,1],[2,0], color="black")
        plt.plot([0,-1],[-1,-4.5], color="black")
        plt.axis([-10, 10, -10, 10])
        yield plt.show()
        plt.plot([-7,-1],[-8,-8], color="black")
        plt.plot([-4,-4],[-8,8], color="black")
        plt.plot([-6,-4],[-8,-6], color="black")
        plt.plot([-2,-4],[-8,-6], color="black")
        plt.plot([-4,0],[8,8], color="black")
        plt.plot([0,0],[8,4], color="black")
        plt.Circle((0,3),1,color="black",fill=False) 
        ax.add_patch(plt.Circle((0,3),1,color="black",fill=False))
        plt.plot([0,0],[2,-1], color="black")
        plt.plot([0,-1],[2,0], color="black")
        plt.plot([0,1],[2,0], color="black")
        plt.plot([0,-1],[-1,-4.5], color="black")
        plt.plot([0,1],[-1,-4.5], color="black")
        plt.axis([-10, 10, -10, 10])
        yield plt.show()

gen = picture()
next(gen)
next(gen)
next(gen)
next(gen)
next(gen)
next(gen)
next(gen)
next(gen)
next(gen)
next(gen)
next(gen)
next(gen)'''

def picture():
        fig=plt.figure()
        ax=fig.add_subplot(1,1,1)
        