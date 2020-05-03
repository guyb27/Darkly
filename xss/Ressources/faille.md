# XSS

## Detection des failles

Essayer dans les differents input une balise html pour voir si le code est interpreter.
Dans le premier champ je rentre la command:
```
<h1>yo</h1>
```
Le code est interpreter. Essayons avec une balise script. Nous pouvons ecrire que la premiere balise, l'admin a certainement filtrer le nombre de caractere.
la command ressemble a cela:
```
<script>al
```
Un flag s'affiche.

## Conclusion:

Nous avons trouvé une faille xss stockée:  


## Comment s'en premunir

Il faut absolument utiliser les fonctions php
```
htmlentities()
```
qui filtre toutes les entités html.
OU
```

htmlspecialchars()
```
qui filtre toutes les entités html, permet par exemple de filtrer les symboles du type <, & ou encore ", en les remplaçant par leur équivalent en HTML. Par exemple :
 ```
Le symbole & devient &amp;

Le symbole " devient &quot;

Le symbole ' devient &#39;
```
Au possible, il faut placer des cookies avec le paramètre HttpOnly, empêchant leur récupération avec JavaScript (Attention elle n’est pas forcément supportée par tous les navigateurs).
