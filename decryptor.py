import requests
from base64 import b64decode
import re
from cmd import Cmd


class Terminal(Cmd):
    def __init__(self):#override initialization to add a few things
        self.prompt = '>'
        self.cookies = {'phpsessionid' :  'cookieValue'}
        Cmd.__init__(self)#continue down what this terminal module would generally initiallize with

    def default(self,args):
        params={
            'cipher':'RC4'
            'url':args
        }
        r=requests.get('http://ip',cookies=cookies,params=params)
        #grabbing everything ending with > till textarea and r.text becoz we have to specify where it's searching in and (0) to grab the very first response 
        unknown_text=re.findall('>(.*?)</textarea>',r.text)(0)

        #to convertet to plain html use .deocde('UTF-8')

terminal=Terminal()
terminal.cmdloop()
