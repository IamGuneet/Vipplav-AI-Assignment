import requests
from bs4 import BeautifulSoup
import json
import re
import os

def extract_elements(soup, tags):
    extracted_data = {}
    for tag in tags:
        elements = soup.find_all(tag)
        extracted_data[tag] = [element.get_text(strip=True) for element in elements]
    return extracted_data

def save_to_json(data, filename,output_dir):
    filename = os.path.join(output_dir, f"{filename}.json")
    os.makedirs(output_dir, exist_ok=True)
    with open(filename, 'w') as f:
        json.dump(data, f, indent=4)

def scrape_website(url, tags,output_filename, output_dir):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    extracted_data = extract_elements(soup, tags)
    save_to_json(extracted_data, output_filename,output_dir)

def get_first_word_of_url(url):
    first_word = re.findall(r'http[s]?://([^/]+)', url)[0].split('.')[0]
    return first_word
output_dir = "all_elements"
url = 'https://groww.in/indices/nifty'
tags = ['p', 'h1', 'h2', 'h3', 'a', 'table', 'tr', 'td', 'form', 'ul', 'ol', 'li', 'data', 'json']
output_filename = f"{get_first_word_of_url(url)}_.txt"

scrape_website(url, tags, output_filename,output_dir)