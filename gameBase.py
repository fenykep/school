import pygame

size=[25,25]
rsize=[size[0]*16,size[1]*16]

sw={273:[0,-1],
	274:[0,1]}

def bigPx(x,y,c):
	x=x-2
	y=y-2
	print("x:",x,"y:",y)
	for i in range(4):
		for j in range(4):
			pxarray[4*x+i+1,4*y+j+1]=c

def step():

	pygame.display.flip()
	clock.tick(40)

surface = pygame.display.set_mode(size=(rsize[0],rsize[1]))
pxarray = pygame.PixelArray(surface)

clock=pygame.time.Clock()
while True:
	step()	
	for event in pygame.event.get():
		if event.type == pygame.KEYDOWN:
			dirval=sw.get(event.key)
