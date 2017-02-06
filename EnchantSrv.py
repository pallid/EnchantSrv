import enchant
from http.server import BaseHTTPRequestHandler, HTTPServer
import json


class HttpProcessor(BaseHTTPRequestHandler):
    def do_POST(self):

        result = list() 
       
        postVars = self.rfile.read(int(self.headers['Content-Length']))
        parametrs = json.loads(postVars.decode())

        word = parametrs.get('word')

        result = eDict.check(word) 

        if not result : 
           result = eDict.suggest(word)
     
        self.send_response(200)
        self.send_header('content-type', 'text/html')
        self.end_headers()
        self.wfile.write(json.dumps(result, ensure_ascii=False).encode())

eDict = enchant.Dict("ru_RU")

serv = HTTPServer(('localhost', 8080), HttpProcessor)
serv.serve_forever()