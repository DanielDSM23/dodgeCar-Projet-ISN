from toolBox import *
import time
#---------------------------
#Constantes
#---------------------------
WIDTH = 630
HEIGHT= 975
montemps=time.time()
depvoie = random.randint(-1,1)
aleat = random.randint(0,10)
ttemps = 1
im = 0
numclign=0
horloge = pygame.time.Clock()
#---------------------------
#Fonctions
#---------------------------
fenetre = screen(WIDTH, HEIGHT)
fenetre.fill(noir)
#############################################################Charger les images##################################################################################


def ChargerImages():
	global background, backgroundbis, Police, Score, maskPolice, MPerdu, MPerdu2, menuprinc, exit2, freins
	background = pygame.image.load("./Cars/background1.png")
	backgroundbis = pygame.image.load("./Cars/background1.png")
	Police = pygame.image.load("./Cars/Police.png")
	Score = pygame.image.load("./Cars/score.png")
	MPerdu = pygame.image.load("./Cars/VOUSAVEZPERDU.png")
	MPerdu2 = pygame.image.load("./Cars/CLICK.png")
	menuprinc = pygame.image.load("./Cars/MENUPRINC.png")
	exit2 = pygame.image.load("./Cars/exit.png")
	freins = pygame.image.load("./Cars/Freins.png")
	###masques
	maskPolice = pygame.mask.from_surface(Police)
	return


def GetRect():
	global Amb, Po, back1, back2, menuprinci, exitg
	Po = Police.get_rect()
	back1 = background.get_rect()
	back2 = backgroundbis.get_rect()
	back2.y = HEIGHT
	sc = Score.get_rect()
	sc.x, sc.y
	menuprinci = menuprinc.get_rect()
	menuprinci.x = 0
	menuprinci.y = 3*HEIGHT/4
	exitg = exit2.get_rect()
	exitg.x, exitg.y = (WIDTH/2)-(1/2*89), HEIGHT-38
	return
#################################################Afficher images##############################################################################################

def AfficherImages():
	global xtexts, ytexts, xscore, yscore, im
	fenetre.blit(background, back1)
	fenetre.blit(backgroundbis, back2)
	fenetre.blit(Police, Po)
	for i in range(0,12):
		fenetre.blit(carIA[i], pos[i])
	xscore, yscore = WIDTH-300, 0
	fenetre.blit(Score, (xscore, yscore))
	if score < 100:
		xtexts, ytexts = WIDTH-81, 4
		fenetre.blit(texscore, (xtexts, ytexts))
	if score >= 100:
		xtexts, ytexts = WIDTH-77, 16
		fenetre.blit(texscore, (xtexts, ytexts))
	if clavier[K_DOWN]==1:
		fenetre.blit(freins, Po)
	if time.localtime(y).tm_sec>-1:
		if im==26:
			im = 0
		im = im + 1
		fenetre.blit(gifphares[im], (Po.x-170, Po.y-25))
		fenetre.blit(gif[im], (Po.x-170, Po.y-25))
	return

##################################################################Charger "IA"########################################################################################
def initIA():
	global score, carIA, pos, IA, imIA
	score = 0
	pos = []
	carIA = []
	for i in range(0,12):
		imIA = pygame.image.load("./Cars/Num/"+str(i)+".png")
		IA = imIA.get_rect()
		IA.x = random.randint(60,385) 
		IA.y = (3 + pasbonus) - 400*(i+1)
		pos.append(IA)
		carIA.append(imIA)
	return
############################################################################Deplacement des objets################################################################################

def deplaceCar():
	global Po, pasbonus, clavier
	######Deplacement horizontal##########
	Po.y = HEIGHT - Police.get_height()
	clavier = pygame.key.get_pressed()
	if clavier[K_LEFT]==1:
		Po.x = Po.x - 2
	if clavier[K_RIGHT]==1:
		Po.x = Po.x + 2
	if Po.x < 60:
		Po.x =60
	if Po.x > 385:
		Po.x=385
	######Deplacement vertical###########
	pasbonus = 0
	if clavier[K_UP]==1:
		pasbonus = 2
	if clavier[K_DOWN]==1:
		pasbonus = -2
	return


def deplaceFonds():
	back1.y = back1.y + 7 + pasbonus
	back2.y = back2.y + 7 + pasbonus
	if back1.y > HEIGHT:
		back1.y = -HEIGHT
	if back2.y > HEIGHT:
		back2.y = -HEIGHT
	return


def deplaceIA():
	global score
	for i in range(0,12):
		pos[i].y = pos[i].y + 5 + pasbonus
		if pos[i].y > HEIGHT:
			score = score+1
			pos[i].y = -3800
			pos[i].x = random.randint(60,385)
	return

def msgscore():
	global texscore
	if score < 100:
		texscore = texte2(str(score), 60, blanc)
	if score >= 100:
		texscore = texte2(str(score), 40, blanc)

	return

def ChoisirAl():
	global depvoie, aleat, ttemps
	depvoie = random.randint(-1,1)
	aleat = random.randint(0,11)
	ttemps = 1
	return

def viragesIA(): 
	global y, depvoie, numclign
	for al in range(aleat, aleat+1):
		pos[al].x = pos[al].x + depvoie
		if depvoie==1:
			if 0<=aleat<3 or 7<=aleat<=10:
				if time.localtime(y).tm_sec>-1:
					if numclign==14:
						numclign = 0
					numclign = numclign + 1
					fenetre.blit(gifClignoD[numclign], pos[al])
					if 0<Po.x-(pos[al].x+carIA[al].get_height())<=120:
						if 0<Po.y-pos[al].y<=HEIGHT/5:
							depvoie=-2
							pygame.mixer.music.load('./Sound/klaxondoppler.mp3')
							pygame.mixer.music.play()
							if pos[al].x < 60:
								pos[al].x =60
								viragesif()
							if pos[al].x > 385:
								viragesif()
								pos[al].x=385
			if 3<=aleat<7:
				if time.localtime(y).tm_sec>-1:
					if numclign==14:
						numclign = 0
					numclign = numclign + 1
					fenetre.blit(gifClignoDsi[numclign], pos[al])
					if 0<Po.x-(pos[al].x+carIA[al].get_height())<=120:
						if 0<Po.y-pos[al].y<=HEIGHT/5:
							depvoie=-2
							pygame.mixer.music.load('./Sound/klaxondoppler.mp3')
							pygame.mixer.music.play()
							if pos[al].x < 60:
								pos[al].x =60
								viragesif()
							if pos[al].x > 385:
								viragesif()
								pos[al].x=385
			if aleat==11:
				if time.localtime(y).tm_sec>-1:
					if numclign==14:
						numclign = 0
					numclign = numclign + 1
					fenetre.blit(gifTruckD[numclign], pos[al])
					if 0<Po.x-(pos[al].x+carIA[al].get_height())<=120:
						if 0<Po.y-pos[al].y<=HEIGHT/5:
							depvoie=-2
							pygame.mixer.music.load('./Sound/klaxondoppler.mp3')
							pygame.mixer.music.play()
							if pos[al].x < 60:
								pos[al].x =60
								viragesif()
							if pos[al].x > 385:
								viragesif()
								pos[al].x=385


		if depvoie==-1:
			if 0<=aleat<=3 or 8<=aleat<=11:
				if time.localtime(y).tm_sec>-1:
					if numclign==14:
						numclign = 0
					numclign = numclign + 1
					fenetre.blit(gifClignoG[numclign], pos[al])
					if 0<pos[al].x-(Po.x+Police.get_height())<=120:
						if 0<Po.y-pos[al].y<=HEIGHT/5:
							depvoie=2
							pygame.mixer.music.load('./Sound/klaxondoppler.mp3')
							pygame.mixer.music.play()
							if pos[al].x < 60:
								pos[al].x =60
								viragesif()
							if pos[al].x > 385:
								viragesif()
								pos[al].x=385
			if 4<=aleat<=7:
				if time.localtime(y).tm_sec>-1:
					if numclign==14:
						numclign = 0
					numclign = numclign + 1
					fenetre.blit(gifClignoGsi[numclign], pos[al])
					if 0<pos[al].x-(Po.x+Police.get_height())<=120:
						if 0<Po.y-pos[al].y<=HEIGHT/5:
							depvoie=2
							pygame.mixer.music.load('./Sound/klaxondoppler.mp3')
							pygame.mixer.music.play()
							if pos[al].x < 60:
								pos[al].x =60
								viragesif()
							if pos[al].x > 385:
								viragesif()
								pos[al].x=385
			if aleat==11:
				if time.localtime(y).tm_sec>-1:
					if numclign==14:
						numclign = 0
					numclign = numclign + 1
					fenetre.blit(gifTruckG[numclign], pos[al])
					if 0<pos[al].x-(Po.x+Police.get_height())<=120:
						if 0<Po.y-pos[al].y<=HEIGHT/5:
							depvoie=2
							pygame.mixer.music.load('./Sound/klaxondoppler.mp3')
							pygame.mixer.music.play()
							if pos[al].x < 60:
								pos[al].x =60
								viragesif()
							if pos[al].x > 385:
								viragesif()
								pos[al].x=385
		if pos[al].x < 60:
			pos[al].x =60
			viragesif()
		if pos[al].x > 385:
			viragesif()
			pos[al].x=385
	return


def viragesif():
	global depvoie, aleat, ttemps
	depvoie = random.randint(-1,1)
	if depvoie==0:
		depvoie = random.randint(-1,1)
	aleat = random.randint(0,11)
	montemps=time.time()
	ttemps = 1
	return

######################################################SON#######################################################################################################
def imagesgif():
	global gif, gifphares, gifClignoG, gifClignoD, gifClignoGsi, gifClignoDsi, gifTruckD, gifTruckG
	gif=[]
	gifphares=[]
	gifClignoD=[]
	gifClignoG=[]
	gifClignoGsi=[]
	gifClignoDsi=[]
	gifTruckD=[]
	gifTruckG=[]
	for i in range(0,27):
		gifIm = pygame.image.load("./Cars/Gyros/"+str(i+1)+".png")
		gif.append(gifIm)
		gifpharesIm = pygame.image.load("./Cars/Pharesgyros/"+str(i+1)+".png")
		gifphares.append(gifpharesIm)
	for i in range(0,15):
		gifClignoDIm = pygame.image.load("./Cars/Clignotants/Droite/"+str(i+1)+".png")
		gifClignoD.append(gifClignoDIm)
		gifClignoGIm = pygame.image.load("./Cars/Clignotants/Gauche/"+str(i+1)+".png")
		gifClignoG.append(gifClignoGIm)
		gifClignoGImsi = pygame.image.load("./Cars/Clignotants/Gauchesi4567/"+str(i+1)+".png")
		gifClignoGsi.append(gifClignoGImsi)
		gifClignoDImsi = pygame.image.load("./Cars/Clignotants/Droitesi4567/"+str(i+1)+".png")
		gifClignoDsi.append(gifClignoDImsi)
		gifTruckDIm = pygame.image.load("./Cars/Clignotants/DroiteTruck/"+str(i+1)+".png")
		gifTruckD.append(gifTruckDIm)
		gifTruckGIm = pygame.image.load("./Cars/Clignotants/GaucheTruck/"+str(i+1)+".png")
		gifTruckG.append(gifTruckGIm)
	return

	
def gyrophare():
	if clavier[K_SPACE]==1:
		pygame.mixer.music.load('./Sound/siren.mp3')
		pygame.mixer.music.play()
	if clavier[K_b]==1:
		pygame.mixer.music.stop()
	return


def collision():
	for i in range(0,len(pos)):
		maskIA = pygame.mask.from_surface(carIA[i])
		choc = maskIA.overlap(maskPolice, (Po.x-pos[i].x, Po.y-pos[i].y))
		if choc != None:
			return True
	return False


def messagePerdu():
	pygame.mixer.music.load('./Sound/carcrash.mp3')
	pygame.mixer.music.play()
	fenetre.blit(MPerdu, (0,HEIGHT/4))
	fenetre.blit(MPerdu2, (0,(2*HEIGHT/4)))
	#fenetre.blit(menuprinc, menuprinci)
	fenetre.blit(exit2, exitg)
	pygame.display.update()
	return


##############################
#Programme Principal
##############################

######lancer depuis Menu.py pour commencer le jeu#####
imagesgif()
ChargerImages()
GetRect()
deplaceCar()
initIA()
while True:
	getExit()
	if collision()==False:
		y=time.time()-montemps
		if time.localtime(y).tm_sec>=ttemps:
			viragesif()
			montemps=time.time()
		deplaceCar()
		gyrophare()
		deplaceFonds()
		msgscore()
		AfficherImages()
		deplaceIA()
		viragesIA()
		pygame.display.update()
	else :
		initIA()
		messagePerdu()
		waitKey()
		ChoisirAl()
	horloge.tick(120)