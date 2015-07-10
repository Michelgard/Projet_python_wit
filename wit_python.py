#!/usr/bin/env python
# -*- coding: utf-8 -*-

import wit
import json
import urllib
from espeak import espeak
import signal
import sys
import os
import time

access_token = 'K3RY7CDERSUFT5KJTYJH6IVKKDBSI2WH' # Code Wit

#Fonction appelée quand vient l'heure de fermer notre programme
def fermer_programme(signal, frame):
    parole("Fermeture programme au revoir a bientot")
    wit.close()
    sys.exit(0)
	
# Fonction lecture orale d'un texte
def parole(texte):
    cmd = 'espeak -v mb-fr1 \"%s\" -s 130'
    os.system(cmd % texte)
#    espeak.synth(texte)

# Fonction Mise en route de l'écoute
def ecoute(passage): # Valeurs passage: 1 Mise en route, 2 Ecoute OK en attente, 3 Commande pas comprise, 4 pas de message 
    response = None
	
    if passage == 1:
	parole("Je suis pret")
    if passage == 2:
	parole("Je suis prèt pour une autre commande")
    if passage == 3:
	parole("Merci de répéter la commande, je n\'ai pas compris")
    
    while response == None:
	response = wit.voice_query_auto(access_token)
             
    texte_json(response)

#Fonction analyse retour écoute micro en JSON
def texte_json(response):
    js= json.loads(response)
    print(js['_text'])
#    print(js[u'outcomes'][0][u'intent'])
    if js['_text'] == None:
        ecoute(4)
    else:
        analyse_texte(js)

#Fonction Analyse valeur texte
def analyse_texte(js):
    try:
	intent = js[u'outcomes'][0][u'intent']
    except NameError:
	ecoute(3)
		
    if intent == 'Jasper':
	parole('Je suis a ton service')
	ecoute(4)
    else:
	try:
		val_On_Off = js[u'outcomes'][0][u'entities'][u'on_off'][0][u'value']
    	except NameError:
		ecoute(3)
			
    	if intent == 'ecran':
		if  val_On_Off == 'on':
			sendurl('LED3=ON', "J'ai allumé l'écran")

		if val_On_Off == 'off':
			sendurl('LED3=OFF', "J'ai éteint l'écran")
				
	if intent == 'lampe_chambre':
		if  val_On_Off == 'on':
			sendurl('LED1=ON', "J'ai allumé la petite lampe de la chambre")

		if val_On_Off == 'off':
			sendurl('LED1=OFF', "J'ai éteint la petite lampe de la chambre")
				
	if intent == 'lustre_chambre':
		if  val_On_Off == 'on':
			sendurl('LEDA=ON', "J'ai allumé le lustre de la chambre")

		if val_On_Off == 'off':
			sendurl('LEDA=OFF', "J'ai éteint le lustre de la chambre")

    ecoute(2)

# Fonction envoie de l'URL
def sendurl(arg, texte): # arg argument passé à la requete URL, Texte = Texte parole suivant commande
	url = 'http://192.168.0.34/?' + arg
	request = urllib.urlopen(url)
	parole(texte)

# Connexion du signal à notre fonction
signal.signal(signal.SIGINT, fermer_programme)
	
espeak.set_voice('fr', '', 1, 0, 0) # Initialisation language
parole("Je me prépare")	
wit.init() #Lancement de wit

# Mise en route et lancement de l'écoute	
ecoute(1)

