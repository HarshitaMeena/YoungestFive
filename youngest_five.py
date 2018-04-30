from flask import Flask
import urllib
import urllib.request, json
import heapq

class YoungestFive(object):
    def __init__(self, link, lid):
        """ intialize the url from
             args:
             link(str): link from where the id details need to be fetched.
             lid(list): List of id candidates for youngest five users
        """
        self.link = link
        self.lid = lid

    def get_youngest_five(self):
        """
          we use min heap of length 5 to store top youngest studnts,
          we store negative of age so that the lowest value age will be left in the end
          Return(str) : with html tags of top five youngest candidates 
        """

        young_five = []
        for i in range(len(self.lid)):
            req = urllib.request.Request(self.link+str(self.lid[i]))
            try:
                the_page = urllib.request.urlopen(req)
            except urllib.error.HTTPError as e:
                continue

            val = the_page.read()
            data = json.loads(val.decode())

            if self.check_valid_numbers(data['number']):
                if len(young_five) < 5:
                    heapq.heappush(young_five, (-data['age'], data))
                else:
                    heapq.heappush(young_five, (-data['age'], data))
                    heapq.heappop(young_five)

        return self.pretty_print(young_five)

    def check_valid_numbers(self, number):
        """
          Args - numbers(str), check if number is valid of types like, 555-555-5555, (555) 555-5555, +1(555) 555-5555 etc
          Return(bool) 
        """
        number=number.replace(" ","").replace("-","",2).replace("+","",1).replace("(","",1).replace(")","",1).replace(".","",2)

        if number.isdigit():
            if len(number)==11:
                if number[0] =='1':
                    return True
                else:
                    return False 
            elif len(number) ==10:
                return True
        else:
            return False    

    def pretty_print(self, young_five):
        """
          Args -young_five(list of tuples): First value is negative of age,
          second is dictionary with details of the user 
          Return(str): With html tags to give it presentable look 
        """
        sorted_name = []
        for i in young_five:
            sorted_name.append((i[1]['name'], i[1])) #print(str(my_map['age']) + "	" + my_map['name'])

        sorted_name.sort()
        results = ""
        for i in sorted_name:
            my_map = i[1]
            print(str(my_map['age']) + " " + my_map['name'])
            results += "<tr>"
            results += "<th>" + str(my_map['id']) + "</th>"
            results += "<th><img src=" + my_map['photo']  + " height=\"100\" width=\"100\"></th>"
            results += "<th>" + my_map['name'].upper() + "</th>"
            results += "<th>" + str(my_map['age']) + "</th>"
            results += "<th>" + str(my_map['number']) + "</th>"
            results += "</tr>"

        return results
