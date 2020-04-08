# INCLUDE

Dans un lien URL du style: /?page= est  une faille include local. Nous pouvons donc les pages a l'interieur de l'index, et comme ça, nous allons pouvoir naviguer dans tout les répertoires du site

nous pouvons remonter jusqu’à la racine du serveur puis aller dans le répertoire qui nous intéresse jusqu’à voir un fichier sensible, par exemple :
/?page=../../../../../../../etc/passwd

on obtient alors le flag final: Congratulaton!! The flag is : b12c4b2cb8094750ae121a676269aa9e2872d07c06e429d25a63196ec1c8c1d0

