#!/usr/bin/env python3
from selenium import webdriver

driver = webdriver.Firefox(executable_path=r'./geckodriver')


def get_data(url, count_update=20000):
    # Получение страницы
    set_LastName = set()
    set_FirstName = set()
    set_FatherName = set()

    set_DateOfBirth = set()
    set_PasportNum = set()
    set_PasportCode = set()

    set_PasportOtd = set()
    set_PasportDate = set()
    set_Address = set()
    driver.get(url)
    for _ in range(count_update):
        driver.find_element_by_xpath(
            "//div[@class='people_buttons']/button").click()

        LastName = driver.find_element_by_xpath('//input[@id="LastName"]').get_attribute('value')
        set_LastName.add(LastName)
        FirstName = driver.find_element_by_xpath('//input[@id="FirstName"]').get_attribute('value')
        set_FirstName.add(FirstName)
        FatherName = driver.find_element_by_xpath('//input[@id="FatherName"]').get_attribute('value')
        set_FatherName.add(FatherName)

        DateOfBirth = driver.find_element_by_xpath('//input[@id="DateOfBirth"]').get_attribute('value')
        set_DateOfBirth.add(DateOfBirth)
        PasportNum = driver.find_element_by_xpath('//input[@id="PasportNum"]').get_attribute('value')
        set_PasportNum.add(PasportNum)
        PasportCode = driver.find_element_by_xpath('//input[@id="PasportCode"]').get_attribute('value')
        set_PasportCode.add(PasportCode)

        PasportOtd = driver.find_element_by_xpath('//input[@id="PasportOtd"]').get_attribute('value')
        set_PasportOtd.add(PasportOtd)
        PasportDate = driver.find_element_by_xpath('//input[@id="PasportDate"]').get_attribute('value')
        set_PasportDate.add(PasportDate)
        Address = driver.find_element_by_xpath('//input[@id="Address"]').get_attribute('value')
        set_Address.add(Address)

    print(len(set_LastName),
          len(set_FirstName),
          len(set_FatherName),

          len(set_DateOfBirth),
          len(set_PasportNum),
          len(set_PasportCode),

          len(set_PasportOtd),
          len(set_PasportDate),
          len(set_Address))

    save_data(set_LastName, 'LastName.txt')
    save_data(set_FirstName, 'FirstName.txt')
    save_data(set_FatherName, 'FatherName.txt')

    save_data(set_DateOfBirth, 'DateOfBirth.txt')
    save_data(set_PasportNum, 'PasportNum.txt')
    save_data(set_PasportCode, 'PasportCode.txt')

    save_data(set_PasportOtd, 'PasportOtd.txt' )
    save_data(set_PasportDate, 'PasportDate.txt')
    save_data(set_Address, 'Address.txt')

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
