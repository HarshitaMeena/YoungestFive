from flask import Flask
import urllib
import urllib.request, json

class FetchIds(object):
    def __init__(self, link):
        """ intialize the url from
             args:
             link(str): link from where the ids need to be fetched.
        """
        self.link = link
        self.listOfIds = []

    def get_all_ids(self):
        """
            takes an initial link, collect ids of 10 users,
            redirects to another link if token exist else it stops processing further
        """
              
        req = urllib.request.Request(self.link)

        try:
            check_url = urllib.request.urlopen(req)
        except urllib.error.HTTPError as e:
            print("Bad URL")
            return

        the_page = check_url.read()
        data = json.loads(the_page.decode())

        if 'result' in data:
            self.listOfIds += data['result']
            while 'token' in data:
                print(data['token'])
                req = urllib.request.Request(self.link+'?token='+data['token'])
                the_page = urllib.request.urlopen(req).read()
                data = json.loads(the_page.decode())
                if 'result' in data:
                    self.listOfIds += data['result']
