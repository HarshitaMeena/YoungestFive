from flask import Flask
import urllib
import urllib.request, json
from fetch_ids import FetchIds
from youngest_five import YoungestFive
from template import front, end

app = Flask(__name__)

@app.route("/")

def main():
    link = "https://appsheettest1.azurewebsites.net/sample/"
    model = FetchIds(link+'list')
    model.get_all_ids()
    top_five = YoungestFive(link+'detail/', model.listOfIds)
    output = top_five.get_youngest_five()
    return front+output+end

if __name__ == "__main__":
    app.run()
