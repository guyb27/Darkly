# File Hidden_input

## Detection des failles

A l'adresse: http://192.168.0.10:8080/index.php?page=recover  
Quand on inspect l'élément, l'on peut voir l'adresse mail: webmaster@borntosec.com
Dans une input caché, sit l'on remplace "hidden" par text une input sauvage apparait.
L'on peut voir que maxlength est egal à 15, enlevons maxlength et rentrons une adresse mail valide
cliquons ensuite sur submit.
et le flag apparait.

## Comment s'en premunir
_Ne pas mettre ce genre d'information coté client, mais dans le serveur,
surtout que le webmaster à l'air de recevoir un lien pour confirmer
le reset du mot de passe