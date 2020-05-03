# STEAL COOKIE

##  solution 1

Si on inspect l'element, le site internet contient un cookie nommé: I_am_admin,  pour value: 68934a3e9455fa72420237eb05902327  
On fait ensuite un find hash type, on obtient un hash de type md5.  
Si on le decrypt, on obtient: false.  
Dans la logic on imagine que le cookie admin est a faux, alors si on le passe a true, cela nous passera admin. on hash true, on obtient: b326b5062b2f0e69046810717534cb09  

on le rentre a la passe de false dans l'inspecteur.  

on obtient en resultat un pop up javascript avec le flag  


##  solution 2

dans le formulaire member, les xss sont possible, faire la commande:  
```
<script>alert(document.cookie)</script>
```
on obtient en resultat un pop up javascript avec le flag  


