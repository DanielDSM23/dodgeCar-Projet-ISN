from toolBox import *
import time
#---------------------------
#Constantes
#---------------------------
WIDTH = 1280
HEIGHT= 720
#---------------------------
#Fonctions
#---------------------------
def ChargerImagesMenu():
	global ImMenu, Play, Controls, INS, INS2, exit, jaicompris, suivant, menuprinc, exit2
	ImMenu = pygame.image.load("./Cars/backpolice.jpg")
	Play = pygame.image.load("./Cars/PLAYGAME.png")
	Controls = pygame.image.load("./Cars/CONTROLS.png")
	INS = pygame.image.load("./Cars/Instructio.png")
	INS2 = pygame.image.load("./Cars/Instructio2.png")
	exit = pygame.image.load("./Cars/exit.png")
	jaicompris = pygame.image.load("./Cars/jaicompris.png")
	suivant = pygame.image.load("./Cars/fleche.png")
	menuprinc = pygame.image.load("./Cars/MENUPRINC.png")
	exit2 = pygame.image.load("./Cars/exit.png")
	return

def afficherMenu():
	fenetre1.blit(ImMenu,(0,0))
	fenetre1.blit(Play,p)
	fenetre1.blit(Controls,c)
	fenetre1.blit(exit,x)
	pygame.display.update()
	return

def GetRectMenu():
	global p, c, x, fer, suiv, menuprinci, exitg
	p = Play.get_rect()
	p.x = WIDTH/2-Play.get_width()/2
	p.y = HEIGHT/5
	c = Controls.get_rect()
	c.x = WIDTH/2-Controls.get_width()/2
	c.y = 3*HEIGHT/5
	x = exit.get_rect()
	x.x = WIDTH/2-exit.get_width()/2
	x.y = HEIGHT-38
	fer = jaicompris.get_rect()
	fer.x = WIDTH-245
	fer.y = HEIGHT-74
	suiv = suivant.get_rect()
	suiv.x = WIDTH-232
	suiv.y = 4
	menuprinci = menuprinc.get_rect()
	menuprinci.x = 0
	menuprinci.y = 3*HEIGHT/4
	exitg = exit2.get_rect()
	exitg.x, exitg.y = (WIDTH/2)-(1/2*89), HEIGHT-38
	return

def Music():
	pygame.mixer.init()
	pygame.mixer.music.load('./Sound/musicfinale.mp3')
	pygame.mixer.music.play()
	return

Music()
fenetre1 = screen(WIDTH, HEIGHT)
ChargerImagesMenu()
GetRectMenu()
afficherMenu()
while True:
	getExit()
	mx, my = waitClick()
	if c.collidepoint(mx,my) == True:
		fenetre1.blit(ImMenu,(0,0))
		fenetre1.blit(jaicompris,fer)
		fenetre1.blit(INS,(40,0))
		fenetre1.blit(suivant, suiv)
	if suiv.collidepoint(mx,my) == True:
		fenetre1.blit(ImMenu,(0,0))
		fenetre1.blit(jaicompris,fer)
		fenetre1.blit(INS2,(0,0))
	if fer.collidepoint(mx,my) == True:
		fenetre1.blit(ImMenu,(0,0))
		fenetre1.blit(Play,p)
		fenetre1.blit(Controls,c)
		fenetre1.blit(exit,x)
	if x.collidepoint(mx,my) == True:
		pygame.quit()
		sys.exit()
	if p.collidepoint(mx,my) == True:
		pygame.mixer.music.stop()
		##############################
		#Programme Principal
		##############################
		WIDTH = 630
		HEIGHT= 975
		fenetre = screen(WIDTH, HEIGHT)
		from PoliceCar import *
	pygame.display.update()