# Select_box

## Detection des failles

A l'adresse suivante:
http://192.168.0.17:8080/index.php?page=survey

Dans le tableau, nous avons une colonne "Grade",
si l'on clique sur la selectbox,
l'on peut selectionner des valeurs de 1 à 10,
inspectons l'élément et modifions la valeur avec une valeur > 10,
cliquons dessus et la le flag apparait.

## Comment s'en premunir

Faire une verification coté serveur,
et afficher une erreur si la valeur ne respecte pas
les valeurs qui sont renseignées dans la vue.