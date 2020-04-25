
import selenium.webdriver
import csv

FILENAME = "auto.csv"
chromedriver = "/Users/artyom/Downloads/chromedriver"
driver = selenium.webdriver.Chrome(chromedriver)
driver.get("https://www.avito.ru/mordoviya/avtomobili")
links = driver.find_elements_by_class_name('snippet-link')
list = [['name', 'price', 'views']]
links_list = []
for link in links:
    links_list.append(link.get_attribute('href'))
for link in links_list:
    try:
        driver.get(link)
        name = driver.find_element_by_class_name('title-info-title-text').text
        list.append([
            name,
            driver.find_element_by_class_name('js-item-price').get_attribute('content'),
            driver.find_element_by_class_name('title-info-metadata-views').text
        ])
        for e in list:
            print(e)
        driver.get('https://www.avito.ru/mordoviya/avtomobili?q=' + name.replace(' ', '+').replace(',', '%2C'))
        new_links = driver.find_elements_by_class_name('snippet-link')
        new_links_list = []
        for new_link in new_links:
            new_links_list.append(new_link.get_attribute('href'))
        counter = 0
        for nlink in new_links_list:
            try:
                driver.get(nlink)
                new_name = driver.find_element_by_class_name('title-info-title-text').text
                if(new_name == name):
                    list.append([
                        new_name,
                        driver.find_element_by_class_name('js-item-price').get_attribute('content'),
                        driver.find_element_by_class_name('title-info-metadata-views').text
                    ])
                counter += 1
                if counter > 9: break
            except:
                print('ololo2')
                if counter > 9:
                    break
                counter += 1
    except:
        print('ololo')

with open(FILENAME, "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(list)


list = []

with open(FILENAME, "r", newline="") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)
        counter = 0
        str = ""
        for r in row:
            print(r)
            if r.find(" (") > -1:
                r = r.split(' (')[0]
            if counter < 3:
                str += r + ","
            else:
                str += r
            counter += 1

        list.append(str.split(','))

for l in list:
    print(l)

with open('dataset.csv', "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(list)
