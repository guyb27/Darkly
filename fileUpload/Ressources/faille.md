# File Upload

## Detection des failles

Dans file upload, nous pouvons envoyer un fichier jpg  
-Essayons d'envoyer un fichier.php.jpg, le code backend a accépté la requete, ce qui veut dire qu'il y a une faille upload avec double extension.  
-Cherchons plus encore voir si il y aurais une faille upload content type. Envoyons un fichier php et changeons son type MIME, pour trompé apache. Voir command: script.sh  

## Conclusion:

Nous avons trouvé 2 types d'attaques:  
-double extension  
-Content type  

## Comment s'en premunir

-Revoir la condition du code backend afin de verifier l'extension.  
-Générer un nom aleatoire, et ne pas afficher le chemin de l'upload.  
-Verifier le type MIME avec une fonction par exemple getimagesize().  
-Ne pas permettre l’écrasement de fichier.  
