from selenium import webdriver
from bs4 import BeautifulSoup

# Отправить GET-запрос на страницу
url = 'https://web.archive.org/web/20210928062830/https://rosatom-career.ru/center/companies-of-rosatom#division_1'  # Замените на нужный URL
chrome_path = ""
options = webdriver.ChromeOptions()
options.add_argument('headless')
options.add_argument("--log-level=3")
options.add_experimental_option('excludeSwitches', ['enable-logging'])
browser = webdriver.Chrome(options=options)
# Создать объект BeautifulSoup для обработки содержимого страницы
browser.get(url)
html = browser.page_source
soup = BeautifulSoup(html, 'html.parser')

divisions = dict()

for div_html in soup.find_all('div', {'class': 'division_companies'}):
    h3 = div_html.find('h3')
    if h3:
        division_name = h3.text.strip()
        print(division_name)
        divisions[division_name] = []
        for company_html in div_html.find_all('div', {'class': 'division_companies--name'}):
            company_name = company_html.text.replace('"', '').strip()
            divisions[division_name].append(company_name)

print(divisions)
