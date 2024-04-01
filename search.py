from googlesearch import search
import requests
import os

EXTENSION = "practice questions and answers filetype:pdf"
PATH = "metadata/practice/"

def extractUrls(query: str):
    query += EXTENSION
    urls = []
    for result in search(query, num_results=1, timeout=3, sleep_interval=1, lang = "en"):
        urls.append(result)
    return urls

def accessPdf(url, filename):
    response = requests.get(url, stream=True)
    downloadPath = f"{PATH}{filename}.pdf"
    with open(downloadPath, 'wb') as file:
        for chunk in response.iter_content(chunk_size=200):
            file.write(chunk)

def clearDir():
    for filename in os.listdir(PATH):
        filepath = os.path.join(PATH, filename)
        os.remove(filepath)

def main(query):
    clearDir()
    urls = extractUrls(query)
    fileAppend = query.split()[0]
    for index, url in enumerate(urls):
        accessPdf(url, f"{fileAppend}{index+1}")

main("How to make a thesis statement")