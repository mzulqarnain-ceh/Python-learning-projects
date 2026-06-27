import os
import csv
import requests
from bs4 import BeautifulSoup
folder=os.path.dirname(__file__)
path=os.path.join(folder,"quotes.csv")
def fetch_html(url):
    try:
        response=requests.get(url)
        if response.status_code ==200:
            return response.text
        else:
            print(f"Error: Page failed to load with status code {response.status_code}")
            return None
    except requests.exceptions.RequestException as e:
        print(f"Error: Network related error {e}")
        return None
def parse_quotes(html):
    soup= BeautifulSoup(html,"html.parser")
    parse_data=[]
    #Find all quote elements
    quote_elements=soup.find_all("div",class_="quote")
    for element in quote_elements:
        text=element.find("span", class_="text").text
        author=element.find("small",class_="author").text
        tag_elements=element.find_all("a",class_="tag")
        tags=[tag.text for tag in tag_elements]
        quote_dict={
            "text": text,
            "author": author,
            "tags": tags,
        }
        parse_data.append(quote_dict)
    return parse_data
def display_quotes(quotes):
    print("\n--- SCRAPED QUOTES ---\n")
    for i,quote in enumerate(quotes):
        tags_string= ", ".join(quote["tags"])
        print(f"{i+1}. {quote['text']}")
        print(f"    - {quote['author']} | Tags: {tags_string} \n")
    print(f"Total Quotes Extracted: {len(quotes)}")
def save_to_csv(quotes):
    with open(path,"w",newline="",encoding="utf-8") as file:
        writer=csv.writer(file)
        writer.writerow(["Quote","Author","Tags"])
        for quote in quotes:
            tags_string= ", ".join(quote["tags"])
            writer.writerow([quote["text"],quote["author"],tags_string])
    print(f"\nData successfully saved to: {path}")
if __name__=="__main__":
    url="http://quotes.toscrape.com/"
    print(f"Scraping data from: {url} ....\n")
    html_data= fetch_html(url)
    if html_data:
        extracted_quotes=parse_quotes(html_data)
        display_quotes(extracted_quotes)
        save_to_csv(extracted_quotes)
    else:
        print("Failed to fetch page.")
