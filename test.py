'''
Created on Jan 7, 2020

@author: Sicario

'''
import requests
import bs4
import csv
'''
response = requests.get("https://compscibits.com/mcq-questions/Networking/NET-computer-science-question-paper/")
soup = bs4.BeautifulSoup(response.content,'html.parser')
quotes = soup.find_all("td")
'''

with open("output.csv","w") as file:
    writer = csv.writer(file, delimiter=',', quoting=csv.QUOTE_MINIMAL)
    writer.writerow(['Question', 'Option1', 'Option2', 'Option3', 'Option4', 'Answer', ])
    page = 1
    while page <= 13:
        response = requests.get("https://compscibits.com/mcq-questions/Networking/GATE-cse-question-paper/{}".format(page))
        page += 1
        soup = bs4.BeautifulSoup(response.content, "html.parser")
        quotes = soup.find_all("td")
        length = len(quotes)
        i = 0
        while i <= length-12:
            writer.writerow([(quotes[i].get_text().encode('utf-8')+quotes[i+1].get_text().encode('utf-8')), (quotes[i+2].get_text().encode('utf-8')+quotes[i+3].get_text().encode('utf-8')),  (quotes[i+4].get_text().encode('utf-8')+quotes[i+5].get_text().encode('utf-8')), (quotes[i+6].get_text().encode('utf-8')+quotes[i+7].get_text().encode('utf-8')), (quotes[i+8].get_text().encode('utf-8')+quotes[i+9].get_text().encode('utf-8')),  (quotes[i+11].get_text().encode('utf-8'))])
            i+=12
        print("Page:",i,"finished")
    print("File Exported to Output.csv")
        

'''
i = 1
while i <= 33:
    response = requests.get("https://compscibits.com/mcq-questions/Networking/NET-computer-science-question-paper/{}".format(i))
    soup = bs4.BeautifulSoup(response.text.encode('utf-8'), "html.parser")
    quote = soup.select('td')
    for quote in quote:
        print((quote.text.encode('utf-8')))
    i+=1
'''
'''
with open('Network MCQs.csv','w') as f:
    thewriter = csv.writer(f)
    
    'thewriter.writerow(['Question','option1','option2','option3','option4','Bakchodi','Answer'])'
    i = 1
    while i <= 33:
        response = requests.get("https://compscibits.com/mcq-questions/Networking/NET-computer-science-question-paper/{}".format(i))
        soup = bs4.BeautifulSoup(response.text.encode('utf-8'), "html.parser")
        quotes = soup.select('td')
        for quote in quotes:
            thewriter.writerow([(quote[0].text.encode('utf-8')+" "+quote[1].text.encode('utf-8')),(quote[2].text.encode('utf-8')+" "+quote[3].text.encode('utf-8')),(quote[4].text.encode('utf-8')+" "+quote[5].text.encode('utf-8')),(quote[6].text.encode('utf-8')+" "+quote[7].text.encode('utf-8')),(quote[8].text.encode('utf-8')+" "+quote[9].text.encode('utf-8')),'Bakchodi',(quote[11].text.encode('utf-8'))])
            thewriter.writerow(quote[0].text,quote[1].text)
     
        i+=1
'''