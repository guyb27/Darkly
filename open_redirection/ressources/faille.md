# Open_redirection  

## Detection des failles  

sur la page d'acceuil, tout en bas de la page,
nous avons des boutons "Facebook", "Twitter" et "Instagram"
Remplacer la balise href d'un de ces boutons par:
href="index.php?page=redirect&site=de"
de=n'importe quoi
cliquons dessus et hop, le flag apparait.

## Comment s'en premunir
faire un script js afin de controler la valeur du href avant de le rediriger,
par exemple avec des regex afin qu'il ne sorte pas du site actuel