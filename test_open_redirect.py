import urllib.request
import re
import hashlib

h = hashlib.md5()
h.update(b"1")
page = "http://challenge01.root-me.org/web-serveur/ch52/index.php?"
url = page + "url=1&h=" + h.hexdigest()
resultat=request.get_method(url)
r = resultat.text
if r.find('flag') != -1:
        print(r)
