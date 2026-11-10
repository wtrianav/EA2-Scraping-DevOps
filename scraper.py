import requests
from bs4 import BeautifulSoup
import pandas as pd

def get_books(url='https://books.toscrape.com/'):
    response = requests.get(url)
    if response.status_code != 200:
        return []
    soup = BeautifulSoup(response.content, 'html.parser')
    productos = soup.find_all('article', class_='product_pod')
    
    items = []
    for item in productos[:5]:
        titulo = item.find('h3').find('a')['title']
        precio = item.find('p', class_='price_color').text
        items.append({'Titulo': titulo, 'Precio': precio})
    return items

def save_to_csv(data, filename='libros.csv'):
    df = pd.DataFrame(data)
    df.to_csv(filename, index=False)
    return filename

if __name__ == "__main__":
    libros = get_books()
    save_to_csv(libros)
    print("Datos guardados exitosamente en libros.csv")
