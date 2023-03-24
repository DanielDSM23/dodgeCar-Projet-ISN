import pygame, sys
from pygame.locals import *
import random
import math
# ------------------------------------------------------------ 
#couleurs
# ------------------------------------------------------------
argent = (192, 192, 192)
blanc = (255, 255, 255)
bleu = (0, 0, 255)
bleuFonce = (0, 0, 155)
bordeaux = (128, 0, 0)
cyan = (0, 255, 255)
gris = (128, 128, 128)
grisFonce= (40, 40, 40)
jaune = (255, 255, 0)
magenta = (255, 0, 255)
navy= ( 60,  60, 100)
noir = (0, 0, 0)
olive = (128, 128, 0)
orange = (255, 165, 0)
rose = (252, 174, 255)
rouge = (255, 0, 0)
rougeFonce = (155, 0, 0)
sarcelle = (0, 128, 128)
turquoise = (3,54,73)
vert = (0, 255, 0)
vertFonce = (0, 155, 0)
violet = (128, 0, 128)

		
# ------------------------------------------------------------ 
#fonctions
# ------------------------------------------------------------

#Creation de la fenetre graphique
def screen(width=680, height=440):
	pygame.init()
	surface = pygame.display.set_mode((width, height), 0, 32)
	pygame.display.set_caption('Pygame')
	print("Fenetre graphique de " +str(width)+"x"+str(height))
	return surface

#fermeture de la fenetre graphique par touche escape ou click sur croix
def getExit():
	for event in pygame.event.get():
		if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
			pygame.quit()
			sys.exit()

#boucle en ATTENTE d1 touche
def waitKey():
	print("En attente d'appui sur une touche ...")
	run=True
	while run == True:
		for event in pygame.event.get():
			if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
				pygame.quit()
				sys.exit()
			elif event.type == KEYDOWN:
				run = False
	return None

#boucle en ATTENTE de la touche ESPACE
def waitK_SPACE():
	print("En attente de la touche barre espace ...")
	run=True
	while run == True:
		for event in pygame.event.get():
			if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
				pygame.quit()
				sys.exit()
			elif event.type == KEYDOWN and event.key == K_SPACE:
				run = False
	return None

#boucle en ATTENTE d1 click gauche
def waitClick():
	mousex, mousey = 0, 0
	print("En attente de click ...")
	run=True
	while run == True:
		for event in pygame.event.get():
			if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
				pygame.quit()
				sys.exit()
			elif event.type == MOUSEBUTTONUP and event.button == 1:
				mousex, mousey = event.pos
				print("Click en ("+str(mousex)+","+str(mousey)+")")
				run = False
	return mousex, mousey

#Creation image texte sans fond
def texte(letexte="hello", fontsize=20, color=orange):
	#Create a pygame.font.Font object
	fontObj = pygame.font.Font('freesansbold.ttf', fontsize)
	#Create a Surface object with the text drawn on it 
	textSurfaceObj = fontObj.render(letexte, True, color)
	return textSurfaceObj

def texte2(letexte="hello", fontsize=20, color=orange):
	#Create a pygame.font.Font object
	#Personnalisation de la police
	fontObj = pygame.font.Font('./Caracteres L4.ttf', fontsize)
	#Create a Surface object with the text drawn on it 
	textSurfaceObj = fontObj.render(letexte, True, color)
	return textSurfaceObj

#Creation image texte avec fond
def texteBg(letexte="hello", fontsize=20, color=orange, bgcolor=noir):
	#Create a pygame.font.Font object
	fontObj = pygame.font.Font('freesansbold.ttf', fontsize)
	#Create a Surface object with the text drawn on it 
	textSurfaceObj = fontObj.render(letexte, True, color, bgcolor)
	return textSurfaceObj

#Calcul distance
def distance(ax,ay,bx,by):
        """Returns the length of this vector."""
#   return sqrt((ax-bx)*(ax-bx) + (ay-by)*(ay-by))

