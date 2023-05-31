import requests 
import time
from bs4 import BeautifulSoup
import os

def acesses_pages_content(urls):

    list_of_pages_with_articles = []
    for url in urls:
        response = requests.get(url)
        print(url, response.status_code)

        list_of_pages_with_articles.append({'url': url,
                                            'content': response.text})

        time.sleep(2)

    return list_of_pages_with_articles

def extract_links_to_articles_pages(list_of_pages_with_articles):
    links = []
    for page in list_of_pages_with_articles:
        soup = BeautifulSoup(page['content'], 'html.parser')
        link_elements = soup.find_all('td', headers='t3')

        links_of_on_page = ['https://repositorio.enap.gov.br'+link_element.find('a')['href'] for link_element in link_elements]
        links = links + links_of_on_page   

    return links

def extract_link_to_pdf_file(html):
    soup = BeautifulSoup(html, 'html.parser')
    link_element = soup.find('td', headers='t1')

    link  = 'https://repositorio.enap.gov.br' + link_element.find('a')['href']
    
    return link

def download_pdf_file(link_to_pdf_file, file_name):
    try:
        response = requests.get(link_to_pdf_file)
        print(response.status_code)

        with open(os.path.join(OUTPUT_PATH, file_name), 'wb') as output:
            output.write(response.content)
        save_log(link_to_pdf_file, response.status_code, file_name)
    
    except Exception as e:
        print(e)
        save_log(link_to_pdf_file, response.status_code, file_name)
    
    finally:
        time.sleep(2)

def download_articles(urls_from_articles_pages):

    i = 1
    for link in urls_from_articles_pages:
        response = requests.get(link)
        print(f"Acessando página do artigo {i} de {len(urls_from_articles_pages)}",response.status_code)
        
        link_to_pdf_file = extract_link_to_pdf_file(response.text)

        download_pdf_file(link_to_pdf_file, f"arquivo-{i}.pdf")

        i = i + 1

def save_log(link, status_code, file_name):
    with open(os.path.join(LOG_PATH, 'log.txt'), 'a') as log:
        log.write(f"{link};{status_code};{file_name}\n")
    
if __name__ == '__main__':
    
    OUTPUT_PATH = 'data'
    LOG_PATH = 'log'
 
    # Passo 1: Acessar as urls e extrair os links para as páginas dos 47 artigos
  
    urls = ['https://repositorio.enap.gov.br/handle/1/6939',
            'https://repositorio.enap.gov.br/handle/1/6939?offset=20',
            'https://repositorio.enap.gov.br/handle/1/6939?offset=40']

    list_of_pages_with_articles = acesses_pages_content(urls)

    # Passo 2: Acessar cada página dos 47 artigos e extrair os links para os arquivos pdf
   
    urls_from_articles_pages = extract_links_to_articles_pages(list_of_pages_with_articles)

    # Passo 3: Acessar cada link para os arquivos pdf e realizar o download dos arquivos
   
    download_articles(urls_from_articles_pages)
 

        