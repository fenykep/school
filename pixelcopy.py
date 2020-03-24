from PIL import Image
import numpy as np
from numba import jit
import math
import rendezo

img = Image.new( 'L', (255,255)) # Create a new black image
px = img.load() # Create the pixel map

w=254
g=170
b=50

def cubePoints(x,y,z,s): #The cube is defined by its back, top, left pixel
	kords=[x,y,z,x,y,z]
	cubePixels=np.empty(shape=[s*12, 3],dtype='uint8')
	multmat=rendezo.purpose()
	for i in range(12):
		cubePixels[20*i:20*i+20]=linePoints(kords+s*multmat[i])
	return(cubePixels)
		
	


#write the left pixel first | whatever
def linePoints(cords): 
	x1,y1,z1,x2,y2,z2 = cords.astype(int)
	#sin(x)=a/b -> x=asin(a/b)
	#a=(y2-y1)
	#b=(x2-x1)
	#c=2D atlo, d=3D atlo
	d=int(math.ceil(math.sqrt((y2-y1)**2+(x2-x1)**2+(z2-z1)**2)))
	lps = np.empty(shape=[d,3],dtype='uint8')
	for i in range(d):
		lps[i]=[x1+int((x2-x1)*(i*(1/d))),y1+int((y2-y1)*(i*(1/d))),z1+int((z2-z1)*(i*(1/d)))]
		px[int(x1+int((x2-x1)*(i*(1/d)))),int(y1+int((y2-y1)*(i*(1/d))))]=int(z1+int((z2-z1)*(i*(1/d))))
	#print("Pxs in line: ",len(lps))
	return lps
	#linePoints([50,200,150,100,50,250])

def drawRect(x,y,s):
	for i in range(s):
		px[x+i,y]=(w)
		px[x+i,y+s]=(w)#horizontal lines
		px[x,y+i]=(w)
		px[x+s,y+i]=(w)

def linGrad(x,y,d,l):
	for i in range(l):
		for j in range(d):
			px[i+x,j+y]=i+(255-l)

def sinLine(x,y,amp,ln,res,trans=1):
	for i in range(ln*res):
		px[(i+x)/res,math.sin((i+x)/(trans*res))*amp+y]=255
		#sinLine(10,100,4,50,4)
def circle(x,y,r):
	for i in range(360):
		px[x+(r*math.cos(i/57.3)),y+(r*math.sin(i/57.3))]=220


def kors(r):
	frame = Image.new( 'L', (255,255),"black")
	apx = frame.load()
	for i in range(360):
		apx[122+(r*math.cos(i/57.3)),122+(r*math.sin(i/57.3))]=220
	return frame


@jit(nopython=True)
def tryThisSpeedShit(mxin,r,resolution=1,size=400,ripp=7.95): #although radius kinda became time
	for i in range(360*resolution):
		for j in range(int(size/2)):
			mxin[int((size/2)+j*math.cos(i/(180*resolution/math.pi)))][int((size/2)+j*math.sin(i/(180*resolution/math.pi)))]=int(122*math.cos(((r-j)/ripp))+122)
	return mxin

def coolCircleGifStuff(size=400,rips=10):
	frames=[]
	for i in range(int(size/rips)):
		matrix = np.zeros(shape=[size, size],dtype='byte')
		frames.append(Image.fromarray(tryThisSpeedShit(r=i,resolution=16,size=size,mxin=matrix,ripp=size/math.pi/rips/2)))
		print(i,"/",int(size/2))
	frames[0].save('gif/krok.gif', format='GIF', append_images=frames[1:], save_all=True, duration=10, loop=0)

def camera(dots,camera=[0,0,0]): #expecting an array of 3D points xyz
	projektor = Image.new( 'L', (255,255)) # Create a new black image
	Ppx = projektor.load() # Create the pixel map
	#distance=370
	display=[122,122,500]
	Ppixels=np.empty(shape=[len(dots),2],dtype='uint8')
	for i in range(len(dots)):
		dponts=dots[i]-camera
		#Ppixels[i]=int(distance/dots[i][2])*(dots[i][0],dots[i][1])
		Ppixels[i][0]=int(display[2]/dponts[2]*dponts[0]+display[0])
		Ppixels[i][1]=int(display[2]/dponts[2]*dponts[1]+display[1])
		Ppx[int(Ppixels[i][0]),int(Ppixels[i][1])]=250		
	#projektor.show()
	return projektor

#camera(cubePoints(50,10,120,20)).show()

def generate_a_fuckton_of_images():
	for i in range(20):
		name="gif/i"+str(i)+".png"
		camera(cubePoints(0,0,100,20),[10,10,i]).save(name)
					#2-12,10,120,20

generate_a_fuckton_of_images()

#img.show()