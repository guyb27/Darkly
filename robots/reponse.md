# FILE ROBOTS.TXT

Si on accede a la page au robtos.txt dans le lien url. on obtient un deux dossiers.
On peut aller dans le dossier /whatever/. Dans celui ci se trouve un fichier htpasswd

si on ouvre le ficheir, celui ci contient un identifiant et un hash md5 root:8621ffdbc5698829397d97767ac13db3.

si on en deduis que se sont les parametre de connexion, il suffit de se rendre dans la section admin, et essayer les identifiant avec le hash md5 decrpyté.

on obtient alors le flag final: d19b4823e0d5600ceed56d5e896ef328d7a2b9e7ac7e80f4fcdb9b10bcb3e7ff
