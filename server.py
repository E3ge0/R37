import http.server
import time

class StartServer():
	def __init__(self, key, resultat):
		try:
			self.key = key
			PORT = 8888
			server_address = ("", PORT)

			title = "index.html"

			with open(title, "x") as fic:
				fic.write("<!DOCTYPE html><html><head><title>DECRYPT R37</title></head><body><div>Decrypt Key : " + self.key + "</div></br></br><div>Mot décrypté : " + resultat + "</body></html>")
			fic.close()
			server = http.server.HTTPServer
			handler = http.server.CGIHTTPRequestHandler
			handler.cgi_directories = [""]
			print()
			print("Allez a l'adresse 'http://localhost:8888' pour obtenir la clée de décryptage, les dictionnaires de décryptage et le mot décrypté !")
			print()
			print("--------")
			print()
			httpd = server(server_address, handler)
			httpd.serve_forever()
		except KeyboardInterrupt:
			print()
			print("--------")
			print("Raccourci clavier detecté, fermeture du serveur Internet ...")
			print()
			time.sleep(2)
			httpd.shutdown()
			print("A bientot !")
		except:
			print("Erreur détectée ! Par mesure de sécurité, le serveur ne sera plus accessible jusqu'au prochain décryptage !")
			time.sleep(2)