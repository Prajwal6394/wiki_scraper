import re
import string
import codecs
from bs4 import BeautifulSoup
import re
import requests

def tagSearch(soup):
    reg_str = "<" + 'h2' + ">(.*?)</" + 'h2' + ">"
    res = re.findall(reg_str,soup)
    for i in range(len(res)):
        res[i] = '<h2>'+res[i]+'</h2>'

    return(res)


def tagName(s):
    start = s.find('">') + len('">')
    end = s.find('</')
    substring = s[start:end]
    print(substring)
    saveOutput(substring)
    print("")
    saveOutput('\n')


def ask_name():
    while True:
        name = input("What is your name? ")
        if name.isalpha():
            return name
        else:
            print("Please use only letters, try again")

def saveOutput(s):
    file = codecs.open("Output.txt", "a", "utf-8")
    file.write(s)
    file.close()


inp = ask_name()
page = requests.get("https://en.wikipedia.org/wiki/"+inp[0])

soup = BeautifulSoup(page.content,"lxml")

#converting html to string for parsing
string = str(soup)
lst = tagSearch(string)

tot_no_of_time_toPrint = 3 #bydefault and should not be more than total number 
                             #of subheading in the page

for i in range(tot_no_of_time_toPrint):
    substrS = lst[i]
    substrE = lst[i+1]

    sb1s = string.find(substrS)
    sb1e = string.find(substrE)
    contentString = string[sb1s:sb1e]
    contentString = re.sub(r"(\{(.*?)\})(\s.{0,})", "", contentString)  #using regular expression to filter anomalies

    #printing captured tag name
    tagName(substrS)

    soup = BeautifulSoup(contentString,'lxml')
    tmp = soup.select('p')
    contentFinale = '\n'.join([ para.text for para in tmp[:]])
    print(contentFinale)
    saveOutput(contentFinale)    
