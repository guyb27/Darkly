# Include

## Detection de la faille

Si on navigue sur les page, on s'apercoit que les url contient des variable qui peuvent etre sensible a l'inclusion, si on teste une rediction vers google par exemple, le site a l'air protegé, mais si on essaye de faire une epxloitation en local, on s'apercoit que le site reagit.

## Exploit de la faille

On va essayer la methode local. normalement la chemin de configuration apache est /var/www/html/(etc..), le fichier interessant sur la machine cible, est le fichier /etc/passwd contenant les users et les password hasher. Nous avons juste a reculer dans l'arboresence. au final cela donne:  
```
../../../../../../../etc/passwd
```
Voir script.sh pour l'expoitation.  

## Conclusion:

Nous avons trouvé une type d'attaque:  
-Inclusion local

## Comment s'en premunir

-Parametrer le .htaccess sur le server apache afin qu'il veille sur les fichiers importants.  
-Enlever tout les caractères qui permettent de naviguer entre les répertoires. exemple:
```
$fichier = str_replace("../","protection",$fichier);
$fichier = str_replace(";","protection",$fichier);
$fichier = str_replace("%","protection,$fichier);
```
-Enlever tout ce qui n'est pas lettre et chiffre et nettoyer la variable $GET
