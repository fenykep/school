#Cleanup, error handling, pixel enlargment for next version

import pygame
import random

size=[100,100]
sn=[[50,51],[51,51]]
dirval=[1,0]
fCoords=[0,0]


sw={
	273:[0,-1],
	274:[0,1],
	276:[-1,0],
	275:[1,0]
}

def ham(a=False):
	#if (sn[-1][0]==fCoords[0] and sn[-1][1]==fCoords[1]):
	if(fCoords in sn):
		a = True
	return a

def step():
	print("sn elejen: ",sn)
	print("food ",fCoords)
	if(fCoords==sn[1]):
		print("Megalljoncsakamenet")
	pxarray[sn[0][0],sn[0][1]]=(0,0,0)
	for i in range(len(sn)-1):
		sn[i][0]=int(sn[i+1][0])
		sn[i][1]=int(sn[i+1][1])
		#print("tolas: ",sn)
	sn[-1][0]+=dirval[0]
	sn[-1][1]+=dirval[1]
	if ham():
		sn.append([sn[-1][0]+dirval[0],sn[-1][1]+dirval[1]])
		print("HamNyam")
		placefood()
		print("appended vals:",sn)
	#print("dirval passzintva: ",sn)
	temp=[sn[-1][0],sn[-1][1]]
	pxarray[temp[0],temp[1]]=(205,100,0)
	pygame.display.flip()
	clock.tick(20)
	
def placefood():
	global fCoords
	fCoords = [random.randint(0,size[0]),random.randint(0,size[1])]
	print("New fCoords set: ",fCoords)
	#while (coords in sn): #notsureifneccesary If yes, try to parralel compute
	#	coords=[random.randint(0,size[0]),random.randint(0,size[1])]
	pxarray[fCoords[0],fCoords[1]]=(0,205,50)
	pygame.display.flip()


surface = pygame.display.set_mode(size=(size[0],size[1]))
pxarray = pygame.PixelArray(surface)
pxarray[sn[0][0],sn[0][1]]=(205,100,0)
pxarray[sn[1][0],sn[1][1]]=(205,100,0)
placefood()
pygame.display.flip()#updates the screen

clock=pygame.time.Clock()

while True:
	step()
	for event in pygame.event.get():
		if event.type == pygame.KEYDOWN:
			print(sw.get(event.key))
			dirval=sw.get(event.key)


