#TOOL that scrapes the web, extracting data from websites, to aid the agent in decision-making
#Faster run-time and can be plugged into multiple agents, as needed

import requests
import BeautifulSoup

def scrapper():
    urls = ['https://npr.org/', 'https://bbc.com/', 'https://cnn.com/', 'https://weforum.org/'] #Systematically determined from most frequently used Emerging Disruptor - Societal websites
    response = request.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

