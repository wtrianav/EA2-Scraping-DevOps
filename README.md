# Evidencia 2: Proyecto de Scraping con DevOps CI/CD

## Descripción
Este repositorio contiene la implementación de un pipeline de Integración Continua y Despliegue Continuo (CI/CD) aplicando metodologías DevOps para un proyecto de recolección de datos (Web Scraping). El código extrae información del catálogo de libros de la plataforma de pruebas [Books to Scrape](https://books.toscrape.com/) y la estructura para su posterior análisis.

## Características implementadas
- **Control de Versiones:** Uso efectivo de Git y GitHub mediante estrategia de ramificación (`dev` y `main`).
- **Web Scraping:** Extracción de metadatos (títulos y precios) utilizando `BeautifulSoup` y estructuración tabular con `pandas`.
- **Integración Continua (CI):** Ejecución de pruebas unitarias automatizadas con `pytest` a través de GitHub Actions para garantizar la integridad del código en cada iteración.
- **Despliegue Continuo (CD):** Generación y almacenamiento automático de un artefacto descargable (`libros.csv`) en el servidor, condicionado a la superación exitosa de las pruebas.

## Estructura del Repositorio
- `.github/workflows/ci_cd.yml`: Definición del pipeline de automatización.
- `scraper.py`: Script principal de extracción y procesamiento de datos.
- `test_scraper.py`: Suite de pruebas automatizadas.
- `requirements.txt`: Listado de dependencias requeridas por el proyecto.

## Ejecución Local

1. **Clonar el repositorio:**
   ```bash
   git clone https://github.com/wtrianav/EA2-Scraping-DevOps.git
   cd EA2-Scraping-DevOps
   ```

2. **Instalar las dependencias:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Ejecutar el programa:**
   ```bash
   python scraper.py
   ```
   *Esto generará el archivo local `libros.csv` con los datos extraídos.*

4. **Ejecutar las pruebas (Opcional):**
   ```bash
   pytest test_scraper.py
   ```