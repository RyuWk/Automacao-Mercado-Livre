from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep
import os
from random import randint

def inciar_driver():
    chrome_options = Options()
    arguments = ['--lang=pt-BR', '--window-size=1300x1000', '--incognito']
    for argumento in arguments:
        chrome_options.add_argument(argumento)

    chrome_options.add_experimental_option('prefs', {
        'download.default_directory': 'C:\\Users\\raeni\\OneDrive\\Documentos\\Curso Python\\projeto-teste\\downloads python',
        'download.directory_upgrade': True,
        'download.prompt_for_download' : False,
        'profile.default_content_settings_values.notifications' : 2,
        'profile.default_content_settings_values.automatic_downloads' : 1
    })
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=chrome_options)
    return driver


driver = inciar_driver()
driver.get('') #pesquise o produto no site e coloque o link entre as aspas simples
sleep(4)
while True:
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    tempo1 = randint(2,20)
    sleep(tempo1)
    driver.execute_script("window.scrollTo(0, document.body.scrollTop);")
    tempo2 = randint(2,20)
    sleep(tempo2)
    nomes = driver.find_elements(By.XPATH, "//a[@class='ui-search-item__group__element shops__items-group-details ui-search-link']")
    links = driver.find_elements(By.XPATH, "//a[@class='ui-search-item__group__element shops__items-group-details ui-search-link']")
    precos = driver.find_elements(By.XPATH, "//div[@class='ui-search-price ui-search-price--size-medium shops__price']//span[@class='price-tag ui-search-price__part shops__price-part']//span[@class='price-tag-text-sr-only']")
    for nome, link, preco in zip(nomes, links, precos):
        with open('precos.csv', 'a', encoding='utf-8', newline= '') as arquivo:
            nome_processado = nome.get_attribute('title')
            link_processado = link.get_attribute('href')
            arquivo.write(f'{nome_processado}; {preco.text}; {link_processado}; {os.linesep}')
    sleep(5)
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    sleep(3)
    try:
        proxima_pagina = driver.find_element(By.LINK_TEXT, 'Seguinte')
        sleep(20)
        proxima_pagina.click()
        sleep(5)
    except:
        print('Fim das paginas')
        break

driver.close()