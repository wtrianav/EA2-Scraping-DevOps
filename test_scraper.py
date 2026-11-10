from scraper import get_books

def test_get_books():
    libros = get_books()
    assert len(libros) > 0, "La lista de libros no debería estar vacía"
    assert 'Titulo' in libros[0], "Cada item debe tener la clave 'Titulo'"
    assert 'Precio' in libros[0], "Cada item debe tener la clave 'Precio'"
