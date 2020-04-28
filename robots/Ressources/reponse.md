
# Robots.txt

One Paragraph of project description goes here

## Etape 1: detection de la faille sql


Si on accede a la page au robtos.txt dans le lien url. on obtient un deux dossiers.

## Etape 2: Exploit

On peut aller dans le dossier /whatever/. Dans celui ci se trouve un fichier htpasswd

si on ouvre le fichier, celui ci contient un identifiant et un hash md5

```
root:8621ffdbc5698829397d97767ac13db3.
```
si on en deduis que se sont les parametre de connexion, il suffit de se rendre dans la section admin, et essayer les identifiant avec le hash md5 decrpyté.


## Comment s'en prémunir ?

-Securiser les repertoire, restreindre l'accés avec une authentification par exemple.
-Eviter les noms de dossier qui peuvent etre interessant (eviter les google dorks).
-Ne pas mettre des choses qui peuvent aidé un attaquant dans les dossiers.
