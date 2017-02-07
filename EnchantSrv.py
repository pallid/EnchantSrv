import enchant
import enchant.checker
from enchant.checker.CmdLineChecker import CmdLineChecker
from http.server import BaseHTTPRequestHandler, HTTPServer
import json


class HttpProcessor(BaseHTTPRequestHandler):
    def do_POST(self):

        result = list() 
       
        postVars = self.rfile.read(int(self.headers['Content-Length']))
        parametrs = json.loads(postVars.decode())

        word = parametrs.get('word')
        if not word is None:
            result = checkWord(word)

        text = parametrs.get('text')
        if not text is None:
            result = checkText(text)      
     
        self.send_response(200)
        self.send_header('content-type', 'text/html')
        self.end_headers()
        self.wfile.write(json.dumps(result, ensure_ascii=False).encode())

def checkWord(word): 
        result = eDict.check(word) 

        if not result : 
            result = eDict.suggest(word)
                
        return result  

def checkText(text): 
    
    chkr.set_text(text) 
    data = list()
    
    for err in chkr:
        data.append(err.word)
    
    if len(data)==0:
        return True
    else:
        result = list()
        i = 0
        while i < len(data):   
            resultCheck = eDict.suggest(data[i])
            res = [data[i], resultCheck]  
            result.append(res)
            i += 1
    return result 

eDict = enchant.Dict("ru_RU")
chkr = enchant.checker.SpellChecker("ru_RU")

serv = HTTPServer(('localhost', 8080), HttpProcessor)
serv.serve_forever()