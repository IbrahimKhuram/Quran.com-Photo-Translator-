def GetArabicTextfromImage(absolute_path):
    from selenium import webdriver
    from webdriver_manager.chrome import ChromeDriverManager
    from selenium.webdriver.chrome.service import Service
    from selenium.webdriver.chrome.options import Options
    from selenium.webdriver.common.by import By
    from selenium.webdriver import ActionChains
    from selenium.webdriver.support.wait import WebDriverWait
    from selenium.webdriver.support import expected_conditions as ec
    from time import sleep
    import os

    # get filename from absolute path of file
    head, filename = os.path.split(absolute_path)

    #service = Service(executable_path=ChromeDriverManager().install()) # uncomment if running in updated selenium

    options = Options()
    options.add_experimental_option("detach", True)     # uncomment to keep chrome open after execution is finished
    options.add_experimental_option('w3c', True)
    #options.headless = True                # uncomment to run in background

    # open chrome and log into nanonets
    driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(), options=options)
    driver.get('https://app.nanonets.com/#/login')
    driver.find_element(By.XPATH, '//*[@id="logInEmail"]').send_keys("translation00001@gmail.com")
    driver.find_element(By.XPATH, '//*[@id="logInPassword"]').send_keys("translation12321")
    driver.find_element(By.XPATH, '//*[@id="logInButton"]').click()

    # wait for nanonets dashboard to load (otherwise throws back to log in page)
    sleep(4)
    driver.get(
        'https://app.nanonets.com/#/ocr/annotate/ec81df5d-fd7e-41d3-9f01-c29067a2603b?query=&page=1&rowsPerPage=50&sortedBy=uploadedAt&sortOrder=DESC&filters=%5B%5D')
    sleep(2)
    driver.get(
        'https://app.nanonets.com/#/ocr/annotate/ec81df5d-fd7e-41d3-9f01-c29067a2603b?query=&page=1&rowsPerPage=50&sortedBy=uploadedAt&sortOrder=DESC&filters=%5B%5D')

    # wait for upload drop box to load, then upload file
    driver.execute_script("arguments[0].click();", WebDriverWait(driver, 20).until(
        ec.element_to_be_clickable((By.XPATH, '//button[@id="uploadFiles"]'))))
    driver.find_element(By.XPATH, '//input[@accept="image/*,application/pdf, application/vnd.openxmlformats-officedocument.spreadsheetml.sheet, .csv, application/vnd.ms-excel"]').send_keys(absolute_path)

    # wait for file to be uploaded, then click on uploaded file to go to extraction screen
    sleep(2)
    driver.get(
        'https://app.nanonets.com/#/ocr/annotate/ec81df5d-fd7e-41d3-9f01-c29067a2603b?query=&page=1&rowsPerPage=50&sortedBy=uploadedAt&sortOrder=DESC&filters=%5B%5D')
    driver.execute_script("arguments[0].click();", WebDriverWait(driver, 20).until(
        ec.element_to_be_clickable((By.XPATH, '//*[@title="' + filename + '"]'))))

    # dismiss alerts
    sleep(3)
    mouse_tracker1 = driver.find_element(By.XPATH, '//div[@style="flex: 1 1 0%;"]')
    ActionChains(driver) \
        .click(mouse_tracker1) \
        .perform()

    # process to extract Arabic text
    mouse_tracker = WebDriverWait(driver,20).until(ec.visibility_of_element_located((By.XPATH, '//div[@class="canvas-container"]')))
    size = mouse_tracker.size
    w, h = size['width'], size['height']
    ActionChains(driver) \
        .move_to_element_with_offset(mouse_tracker, 3, 0) \
        .click_and_hold() \
        .move_to_element_with_offset(mouse_tracker, w, h) \
        .release() \
        .perform()
    sleep(1)
    arabic_text = driver.find_element(By.XPATH, '//textarea[@aria-invalid="false"]').text
    '''
    # delete file from nanonets after extracting
    driver.back()
    sleep(1)
    mouse_tracker = driver.find_element(By.XPATH, '//*[@title="' + filename + '"]')
    ActionChains(driver)\
        .move_to_element_with_offset(mouse_tracker, 327, 0)\
        .click()\
        .perform()
    driver.execute_script("arguments[0].click();", WebDriverWait(driver, 20).until(
        ec.element_to_be_clickable((By.XPATH, '//*[@id="deleteFiles"]/span[1]'))))
    '''
    return arabic_text


def GetAyahKeyArrayFromArabicText(arabic_text):

    import requests
    import json

    ayah_key_array = []

    for each_line in arabic_text.splitlines():

        url = "https://quran-com.p.rapidapi.com/search"
        querystring = {"size": "1", "q": each_line, "language": "en"}

        headers = {
            "X-RapidAPI-Key": "dcc1710453msh39437a709d81a78p1c896ajsnc4e1ef72e1ca",
            "X-RapidAPI-Host": "quran-com.p.rapidapi.com"
        }

        response = requests.request("GET", url, headers=headers, params=querystring)
        print(response.json())
        data = json.loads(response.text)

        if data['search']['results'] != []:
            verse_key = data['search']['results'][0]['verse_key']
            ayah_key_array.append(verse_key)

    return ayah_key_array

def GetTranslationFromAyahKeyArray(ayah_key_value_array):

    from collections import defaultdict
    import requests
    import json

    # count frequency of each surah
    surah_freq = defaultdict(int)
    for ayah in ayah_key_value_array:
        surah = ayah.split(':')[0]
        surah_freq[surah] += 1

    # find the mode surah
    mode_surah = max(surah_freq, key=surah_freq.get)

    # extract ayah values for the mode surah
    mode_ayahs = [int(ayah.split(':')[1]) for ayah in ayah_key_value_array if ayah.startswith(mode_surah + ':')]

    # find the minimum and maximum ayah of the mode surah
    min_ayah = min(mode_ayahs)
    max_ayah = max(mode_ayahs)

    translation = ""

    for i in range(min_ayah, max_ayah+1):
        url = "https://quran-com.p.rapidapi.com/verses/by_key/" + str(mode_surah) + ":" + str(i)

        querystring = {"translations": "131", "language": "en"}

        headers = {
            "X-RapidAPI-Key": "dcc1710453msh39437a709d81a78p1c896ajsnc4e1ef72e1ca",
            "X-RapidAPI-Host": "quran-com.p.rapidapi.com"
        }

        response = requests.request("GET", url, headers=headers, params=querystring)
        data = json.loads(response.text)
        translation = translation + data['verse']['verse_key'] + "\n" + data['verse']['translations'][0]['text'] + "\n\n"

    return translation

absolute_path = "C:/Users/ibrah/Downloads/surah ash shuara.png"

arabic_text = GetArabicTextfromImage(absolute_path)
print(arabic_text)
ayah_key_array = GetAyahKeyArrayFromArabicText(arabic_text)
translation = GetTranslationFromAyahKeyArray(ayah_key_array)

print(translation)
