# TOOL that scrapes the web, extracting data from websites, to aid the agent in decision-making
# Faster run-time and can be plugged into multiple agents, as needed

import requests
from bs4 import BeautifulSoup
import re
from urllib.parse import urljoin

def scrap():
    urls = [
        'https://npr.org/', 
        #'https://bbc.com/', 
        #'https://www.cnn.com/world/asia', 
        #'https://weforum.org/'
    ] # Systematically determined from most frequently used Emerging Disruptor - Societal websites

    headers = {'User-Agent': 'Mozilla/5.0'}

    for url in urls:
        response = requests.get(url, headers=headers)

        if response.status_code == 200:
            print('Selected URL: ', url)

            soup = BeautifulSoup(response.text, 'html.parser')
            #print(soup.find_all('div'))

            # Collect all <article> tags first
            articles = soup.find_all('article')

            # Also collect <div> tags that have common article-related classes
            divs = soup.find_all('div')
            article_divs = [div for div in divs if any('story' in c or 'card' in c or 'promo' in c for c in div.get('class', []))]

            # Combine all elements to parse
            elements_to_parse = articles + article_divs
            
            with open('output.html', 'w', encoding='utf-8') as f:
                for elem in elements_to_parse:
                    info = extract_article_info(elem, url)
                    tag_type = elem.name.upper()
                    f.write(f"[{tag_type} TAG]\n")
                    f.write(f"Title: {info['title']}\n")
                    f.write(f"URL: {info['url'] or 'No link found'}\n")
                    f.write(f"Date from URL: {info['date_from_url'] or 'Not found'}\n")
                    f.write(f"Teaser: {info['teaser']}\n")
                    f.write(f"Image: {info['image_url']}\n\n")

                #tag_type = elem.name.upper()
                #print(f"[{tag_type} TAG]")
                #print(f"Title: {info['title']}")
                #print(f"URL: {info['url'] or 'No link found'}")
                #print(f"Date from URL: {info['date_from_url'] or 'Not found'}")
                #print(f"Teaser: {info['teaser']}")
                #print(f"Image: {info['image_url']}\n")
        else:
            print(f"Failed to fetch {url} with status code {response.status_code}")

# X
def extract_date_from_url(url):
    if not url:
        return None
    match = re.search(r'/(\d{4})/(\d{2})/(\d{2})', url)
    if match:
        return f"{match.group(1)}-{match.group(2)}-{match.group(3)}"
    return None

# X
def extract_article_info(elem, base_url):
    # Title
    title_tag = elem.find(class_='title') or elem.find(class_='headline') or elem.find('h1', class_='headline__text')
    title = title_tag.get_text(strip=True) if title_tag else 'No title found'

    # URL
    link_tag = elem.find('a', href=True)
    url = urljoin(base_url, link_tag['href']) if link_tag else 'No link found'

    # Date
    date_from_url = extract_date_from_url(url)

    # Teaser
    teaser_tag = elem.find('p')
    teaser = teaser_tag.get_text(strip=True) if teaser_tag else 'No teaser found'

    # Body
    body_tag = elem.find(class_='text')
    body = body_tag.get_text(strip=True) if body_tag else 'No body found'

    # Image
    image_tag = elem.find('img')
    image_url = image_tag['src'] if image_tag and 'src' in image_tag.attrs else 'No image found'

    return {
        'title': title,
        'url': url,
        'date_from_url': date_from_url,
        'teaser': teaser,
        'image_url': image_url
    }

if __name__ == '__main__':
    scrap()



