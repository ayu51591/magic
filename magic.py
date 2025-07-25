import requests
import json 
import sys
import wikipedia

topic = input("just something to  search -> ")

data = wikipedia.summary(topic)

try:
    
    data = wikipedia.summary(topic)
    
    # styling thing 
    sentence = data.split('. ')
    sentence = [sentence.strip() + '.' for sentence in sentence if sentence ]
    
    wiki_data = {
        "topic" : topic,
        "summary" : data
        
    } 
    # here
    with open("wiki_summary.json" , "w",encoding= "utf-8") as f:
        json.dump(wiki_data , f, indent = 4, ensure_ascii= False)
        
    print("summary saved to wiki_data.json")
    
except wikipedia.exceptions.DisambiguationError as e:
    print("too many request")    
    print(e.options)
except wikipedia.exceptions.PageError:
    print("not found")    
