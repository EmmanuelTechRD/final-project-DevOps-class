from bs4 import BeautifulSoup

def test_hola_mundo():
    with open("index.html", encoding='utf-8') as f:
        soup = BeautifulSoup(f, "html.parser")
    assert soup.h1.text == "Hola Mundo. Soy Emmanuel Soto 20222092."
