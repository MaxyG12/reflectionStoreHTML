from flask import Flask

app = Flask(__name__)

# Dictionary to store day numbers, code links, and reflections
myReflections = {}

myReflections["78"] = {"link": "https://replit.com/ai", "Reflection": "Was a bit of a head scratcher but I got there"}
myReflections["79"] = {"link": "https://replit.com/ai", "Reflection": "Oh. So. Easy."}
myReflections["80"] = {"link": "https://replit.com/ai", "Reflection": "Was a bit of a head scratcher but I got there"}
myReflections["81"] = {"link": "https://replit.com/ai", "Reflection": "Oh. So. Easy."}


@app.route('/<pageNumber>')
def index(pageNumber):
  global Reflections
  page = ""
  f=open("templates/reflection.html", "r")
  page = f.read()
  f.close()
  
  page = page.replace("{day}", pageNumber)
  page = page.replace("{link}", myReflections[pageNumber]["link"])
  page = page.replace("{reflection}", myReflections[pageNumber]["Reflection"])
  return page


app.run(host='0.0.0.0', port=81)