#!/usr/bin/env python3
from selenium import webdriver

driver = webdriver.Firefox(executable_path=r'./geckodriver')


def get_data(url, number_requests=20):
    # Получение страницы
    names = ('LastName', 'FirstName', 'FatherName', 'DateOfBirth', 'PasportNum', 'PasportCode', 'PasportOtd',
             'PasportDate', 'Address')

    data = dict.fromkeys(names, set)

    driver.get(url)
    for _ in range(number_requests):
        driver.find_element_by_xpath(
            "//div[@class='people_buttons']/button").click()
        for name in names:
            data[name].add(driver.find_element_by_xpath(f'//input[@id="{name}"]').get_attribute('value'))
    for name in names:
        save_data(data[name], f'{name}_data.txt')
    return driver.page_source


def save_data(data, filename):
    with open(filename, 'w', newline='') as file:
        for line in data:
            file.write(line + '\n')


def main():
    page_url = 'https://www.random1.ru/generator-pasportnyh-dannyh'
    get_data(page_url)


if __name__ == '__main__':
    main()
