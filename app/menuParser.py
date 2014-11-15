import string
from lxml import html
import requests
from pymongo import MongoClient

client = MongoClient('mongodb://norfrosh:food@ds051110.mongolab.com:51110/dining')
db = client.dining
collection = db.dinner


def main():
    fb = muddBreakfast()
    for i in range(len(fb)):
        print "Food:", fb[i]
        tags = string.split(raw_input("tags: "),',')
        post = {"name": fb[i],"tags": tags,"value": 0}
        collection.insert(post)    

def add(menu):
    for i in range(len(menu)):
        print "Food:",menu[i]
        tags = string.split(input("tags: ",','))
        doc = {"name": menu[i],"tags": tags,}
        
def fraryBreakfast():
    page = requests.get('https://aspc.pomona.edu/menu/',verify=False)
    tree = html.fragments_fromstring(page.text)
    frary = tree[1].xpath('//*[@id="frary_menu"]/td[1]/ul')
    fraryItems = []
    for i in range(len(frary[0])):
        fraryItems += [frary[0][i].text_content()]
    return fraryItems

def fraryLunch():
    page = requests.get('https://aspc.pomona.edu/menu/',verify=False)
    tree = html.fragments_fromstring(page.text)
    frary = tree[1].xpath('//*[@id="frary_menu"]/td[2]/ul')
    fraryItems = []
    for i in range(len(frary[0])):
        fraryItems += [frary[0][i].text_content()]
    return fraryItems
        
def fraryDinner():
    page = requests.get('https://aspc.pomona.edu/menu/',verify=False)
    tree = html.fragments_fromstring(page.text)
    frary = tree[1].xpath('//*[@id="frary_menu"]/td[3]/ul')
    fraryItems = []
    for i in range(len(frary[0])):
        fraryItems += [frary[0][i].text_content()]
    return fraryItems
    
def frankBreakfast():
    page = requests.get('https://aspc.pomona.edu/menu/',verify=False)
    tree = html.fragments_fromstring(page.text)
    frank = tree[1].xpath('//*[@id="frank_menu"]/td[1]/ul')
    frankItems = []
    for i in range(len(frank[0])):
        frankItems += [frank[0][i].text_content()]
    return frankItems

def frankLunch():
    page = requests.get('https://aspc.pomona.edu/menu/',verify=False)
    tree = html.fragments_fromstring(page.text)
    frank = tree[1].xpath('//*[@id="frank_menu"]/td[2]/ul')
    frankItems = []
    for i in range(len(frank[0])):
        frankItems += [frank[0][i].text_content()]
    return frankItems
    
def frankDinner():
    page = requests.get('https://aspc.pomona.edu/menu/',verify=False)
    tree = html.fragments_fromstring(page.text)
    frank = tree[1].xpath('//*[@id="frank_menu"]/td[3]/ul')
    frankItems = []
    for i in range(len(frank[0])):
        frankItems += [frank[0][i].text_content()]
    return frankItems
    
def oldenborgBreakfast():
    page = requests.get('https://aspc.pomona.edu/menu/',verify=False)
    tree = html.fragments_fromstring(page.text)
    oldenborg = tree[1].xpath('//*[@id="oldenborg_menu"]/td[1]/ul')
    oldenborgItems = []
    for i in range(len(oldenborg[0])):
        oldenborgItems += [oldenborg[0][i].text_content()]
    return oldenborgItems

def oldenborgLunch():
    page = requests.get('https://aspc.pomona.edu/menu/',verify=False)
    tree = html.fragments_fromstring(page.text)
    oldenborg = tree[1].xpath('//*[@id="oldenborg_menu"]/td[2]/ul')
    oldenborgItems = []
    for i in range(len(oldenborg[0])):
        oldenborgItems += [oldenborg[0][i].text_content()]
    return oldenborgItems

def oldenborgDinner():
    page = requests.get('https://aspc.pomona.edu/menu/',verify=False)
    tree = html.fragments_fromstring(page.text)
    oldenborg = tree[1].xpath('//*[@id="oldenborg_menu"]/td[3]/ul')
    oldenborgItems = []
    for i in range(len(oldenborg[0])):
        oldenborgItems += [oldenborg[0][i].text_content()]
    return oldenborgItems
    
def cmcBreakfast():
    page = requests.get('https://aspc.pomona.edu/menu/',verify=False)
    tree = html.fragments_fromstring(page.text)
    cmc = tree[1].xpath('//*[@id="cmc_menu"]/td[1]/ul')
    cmcItems = []
    for i in range(len(cmc[0])):
        cmcItems += [cmc[0][i].text_content()]
    return cmcItems

def cmcLunch():
    page = requests.get('https://aspc.pomona.edu/menu/',verify=False)
    tree = html.fragments_fromstring(page.text)
    cmc = tree[1].xpath('//*[@id="cmc_menu"]/td[2]/ul')
    cmcItems = []
    for i in range(len(cmc[0])):
        cmcItems += [cmc[0][i].text_content()]
    return cmcItems
    
def cmcDinner():
    page = requests.get('https://aspc.pomona.edu/menu/',verify=False)
    tree = html.fragments_fromstring(page.text)
    cmc = tree[1].xpath('//*[@id="cmc_menu"]/td[3]/ul')
    cmcItems = []
    for i in range(len(cmc[0])):
        cmcItems += [cmc[0][i].text_content()]
    return cmcItems

def scrippsBreakfast():
    page = requests.get('https://aspc.pomona.edu/menu/',verify=False)
    tree = html.fragments_fromstring(page.text)
    scripps = tree[1].xpath('//*[@id="scripps_menu"]/td[1]/ul')
    scrippsItems = []
    for i in range(len(scripps[0])):
        scrippsItems += [scripps[0][i].text_content()]
    return scrippsItems
    
def scrippsLunch():
    page = requests.get('https://aspc.pomona.edu/menu/',verify=False)
    tree = html.fragments_fromstring(page.text)
    scripps = tree[1].xpath('//*[@id="scripps_menu"]/td[2]/ul')
    scrippsItems = []
    for i in range(len(scripps[0])):
        scrippsItems += [scripps[0][i].text_content()]
    return scrippsItems

def scrippsDinner():
    page = requests.get('https://aspc.pomona.edu/menu/',verify=False)
    tree = html.fragments_fromstring(page.text)
    scripps = tree[1].xpath('//*[@id="scripps_menu"]/td[3]/ul')
    scrippsItems = []
    for i in range(len(scripps[0])):
        scrippsItems += [scripps[0][i].text_content()]
    return scrippsItems
    
def pitzerBreakfast():
    page = requests.get('https://aspc.pomona.edu/menu/',verify=False)
    tree = html.fragments_fromstring(page.text)
    pitzer = tree[1].xpath('//*[@id="pitzer_menu"]/td[1]/ul')
    pitzerItems = []
    for i in range(len(pitzer[0])):
        pitzerItems += [pitzer[0][i].text_content()]
    return pitzerItems
    
def pitzerLunch():
    page = requests.get('https://aspc.pomona.edu/menu/',verify=False)
    tree = html.fragments_fromstring(page.text)
    pitzer = tree[1].xpath('//*[@id="pitzer_menu"]/td[2]/ul')
    pitzerItems = []
    for i in range(len(pitzer[0])):
        pitzerItems += [pitzer[0][i].text_content()]
    return pitzerItems

def pitzerDinner():
    page = requests.get('https://aspc.pomona.edu/menu/',verify=False)
    tree = html.fragments_fromstring(page.text)
    pitzer = tree[1].xpath('//*[@id="pitzer_menu"]/td[3]/ul')
    pitzerItems = []
    for i in range(len(pitzer[0])):
        pitzerItems += [pitzer[0][i].text_content()]
    return pitzerItems
    
def muddBreakfast():
    page = requests.get('https://aspc.pomona.edu/menu/',verify=False)
    tree = html.fragments_fromstring(page.text)
    mudd = tree[1].xpath('//*[@id="mudd_menu"]/td[1]/ul')
    muddItems = []
    for i in range(len(mudd[0])):
        muddItems += [mudd[0][i].text_content()]
    return muddItems
    
def muddLunch():
    page = requests.get('https://aspc.pomona.edu/menu/',verify=False)
    tree = html.fragments_fromstring(page.text)
    mudd = tree[1].xpath('//*[@id="mudd_menu"]/td[2]/ul')
    muddItems = []
    for i in range(len(mudd[0])):
        muddItems += [mudd[0][i].text_content()]
    return muddItems

def muddDinner():
    page = requests.get('https://aspc.pomona.edu/menu/',verify=False)
    tree = html.fragments_fromstring(page.text)
    mudd = tree[1].xpath('//*[@id="mudd_menu"]/td[3]/ul')
    muddItems = []
    for i in range(len(mudd[0])):
        muddItems += [mudd[0][i].text_content()]
    return muddItems


def allMeals():
    bigList = muddBreakfast() + muddLunch() + pitzerBreakfast() + pitzerLunch() + fraryBreakfast() + fraryLunch() + cmcBreakfast() + cmcLunch()
    return bigList
    
if __name__ == "__main__":
   main()
