# TOOL that scrapes the web, extracting data from websites, to aid the agent in decision-making
# Faster run-time and can be plugged into multiple agents, as needed

import requests
from bs4 import BeautifulSoup
import re
from urllib.parse import urljoin
from pathlib import Path


def scrap():
    urls = [
        'https://npr.org/', 
        #'https://bbc.com/', 
        #'https://www.cnn.com/world/asia', (iffy)
        #'https://weforum.org/' (does not work)
    ] # Systematically determined from most frequently used Emerging Disruptor - Societal websites

    headers = {'User-Agent': 'Mozilla/5.0'}
    all_articles = []

    for url in urls:
        response = requests.get(url, headers=headers)

        if response.status_code == 200:
            print('Selected URL: ', url)

            soup = BeautifulSoup(response.text, 'html.parser')
            #print(soup.find_all('div'))
            #print(soup.find('meta', {'name': 'author'})) 

            # Collect all <article> tags first
            articles = soup.find_all('article')

            # Also collect <div> tags that have common article-related classes
            divs = soup.find_all('div')
            article_divs = [div for div in divs if any('story' in c or 'card' in c or 'promo' in c for c in div.get('class', []))]

            # Combine all elements to parse
            elements_to_parse = articles + article_divs

            home = Path.home()  # this is automatically /Users/yourname
            path = home / 'AI_agent_team' / 'scrapper' / 'ws_output.html'

            with open(path , 'w', encoding='utf-8') as f:
                for elem in elements_to_parse:
                    info = extract_article_info(elem, url)
                    tag_type = elem.name.upper()
                    f.write(f"[{tag_type} TAG]\n")
                    f.write(f"Title: {info['title']}\n")
                    #f.write(f"Author: {info['author']}\n")
                    f.write(f"URL: {info['url'] or 'No link found'}\n")
                    f.write(f"Date from URL: {info['date_from_url'] or 'Not found'}\n")
                    f.write(f"Category: {info['category']}\n")
                    f.write(f"Teaser: {info['teaser']}\n")
                    f.write(f"Body: {info['body']}\n")
                    f.write(f"Image: {info['image_url']}\n\n")

                    all_articles.append({
                        "title": (f"Title: {info['title']}\n"),
                        "url": (f"URL: {info['url'] or 'No link found'}\n"),
                        "date": (f"Date from URL: {info['date_from_url'] or 'Not found'}\n"),
                        "category": (f"Category: {info['category']}\n"),
                        "teaser": (f"Teaser: {info['teaser']}\n"),
                        "body": f.write(f"Body: {info['body']}\n"),
                        "image": (f"Image: {info['image_url']}\n\n"),
                    })
        else:
            print(f"Failed to fetch {url} with status code {response.status_code}")
        
    # Return a list of article dicts like:
    return all_articles

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

    # Author
    #author_tag = soup.find('meta', {'name': 'author'}) or soup.find('meta', {'name': 'cXenseParse:author'})
    #print("DEBUG author_tag:", author_tag)  # Debug line
    #author = author_tag['content'].strip() if author_tag and author_tag.has_attr('content') else 'No author found'

    # URL
    link_tag = elem.find('a', href=True)
    url = urljoin(base_url, link_tag['href']) if link_tag else 'No link found'

    # Date
    date_from_url = extract_date_from_url(url)

    # Category
    category_tag = elem.find('h2', class_='slug')
    category = category_tag.get_text(strip=True) if category_tag else 'No category found'
    
    # Teaser
    teaser_tag = elem.find('p')
    teaser = teaser_tag.get_text(strip=True) if teaser_tag else 'No teaser found'

    # Body
    body_tag = elem.find_all(class_='story-text')
    body = ' '.join(p.get_text(strip=True) for p in body_tag) if body_tag else 'No body found'

    # Image
    image_tag = elem.find('img')
    image_url = image_tag['src'] if image_tag and 'src' in image_tag.attrs else 'No image found'

    return {
        'title': title,
        #'author': author,
        'url': url,
        'date_from_url': date_from_url,
        'category': category,
        'teaser': teaser,
        'body': body,
        'image_url': image_url
    }

# if __name__ == '__main__':
    # scrap()



