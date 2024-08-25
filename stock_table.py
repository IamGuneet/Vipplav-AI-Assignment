import requests
from bs4 import BeautifulSoup
import csv
import os

def scrape_all_tables(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    
    tables = soup.find_all('table')
    
    if not tables:
        print("No tables found on the page.")
        return

    output_dir = "scraped_tables"
    os.makedirs(output_dir, exist_ok=True)

    for index, table in enumerate(tables):
        headers = [header.get_text(strip=True) for header in table.find_all('th')]
        
        rows = []
        for row in table.find_all('tr')[1:]:
            columns = row.find_all('td')
            row_data = [column.get_text(strip=True) for column in columns]
            rows.append(row_data)

        file_name = os.path.join(output_dir, f"table_{index + 1}.csv")
        with open(file_name, 'w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            if headers:
                writer.writerow(headers)  # Write headers if they exist
            writer.writerows(rows)  # Write data rows

        print(f"Table {index + 1} extracted and saved to {file_name}")

url = 'https://groww.in/indices/nifty' 

scrape_all_tables(url)
