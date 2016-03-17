# Projet_python_wit
Utilisation de wit.ai en python
Ce programme utilise wit.ai pour  reconnaitre des "ordres" associés à des commandes enregistrées sur le site de wit.ai.
Le code tourne sur un raspberry pi qui écoute. Si une phrase est reconnue elle est analysée pour savoir ce qu'il faut faire.
Ensuite une URL avec un argumnt est envoyée à un Arduino par l'intermédiaire d'une carte Ethernet.
Cet Arduino est connecté à un émetteur en 433Mhz pour envoyer le bon code au différent récepteur.

J'ai aussi une interface web qui permet d'envoyer les commandes.

Retrouver le bolg ici http://rasp-pi.fr.nf

