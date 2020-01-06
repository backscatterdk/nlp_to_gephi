import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


def split_by_n(seq, n):
    '''A generator to divide a sequence into chunks of n units.'''
    while seq:
        yield seq[:n]
        seq = seq[n:]


with open('quixote.txt') as f:
    texts = f.read()
texts = texts.replace('\n', '')
text_list = list(split_by_n(texts, 1000))[:1000]

driver = webdriver.Firefox()

for text in text_list:
    driver.get(
        "https://docs.google.com/forms/d/e/1FAIpQLSdBvThnsVCgxG0soED2RzvV2mGQIBqC-9528tv1kVlexYPQPA/viewform")

    box = driver.find_element_by_class_name(
        'quantumWizTextinputPapertextareaInput')
    box.send_keys(text)

    button = driver.find_element_by_class_name(
        'quantumWizButtonPaperbuttonLabel')
    button.click()

    time.sleep(1)
