#!/usr/bin/env python3
import os
from argparse import ArgumentParser
from datetime import datetime

from selenium import webdriver

URL: str = 'https://www.random1.ru/generator-pasportnyh-dannyh'
NAMES: tuple = (
    'LastName',
    'FirstName',
    'FatherName',
    'DateOfBirth',
    'PasportNum',
    'PasportCode',
    'PasportOtd',
    'PasportDate',
    'Address',
    'City',)


def get_data(browser: str, path_driver: str, number_requests: int) -> dict:
    """
    This function returns a dict with unique downloaded data from requests.
    browser: type browser - Chrome or Firefox.
    path_driver: driver location.
    number_requests: number requests from https://www.random1.ru/generator-pasportnyh-dannyh.
    return: Dict with unique downloaded data from requests.
    """
    if browser == 'Firefox':
        driver = webdriver.Firefox(executable_path=path_driver)
    elif browser == 'Chrome':
        driver = webdriver.Chrome(executable_path=path_driver)
    else:
        raise ValueError('use browser Chrome or Firefox')

    data = {name: set() for name in NAMES}

    driver.get(URL)
    # Extract passport data generated on the web page.
    for _ in range(number_requests):
        driver.find_element_by_xpath("//div[@class='people_buttons']/button").click()
        for name in NAMES:
            if name != 'City':
                # Information about accommodation is divided into the city and the address itself
                if name == 'Address':
                    address = driver.find_element_by_xpath(f'//input[@id="{name}"]').get_attribute('value')
                    new_address = ",".join(address.split(",")[2:])
                    city = address.split(",")[1]

                    data['Address'].add(new_address)
                    data['City'].add(city)
                else:
                    data[name].add(driver.find_element_by_xpath(f'//input[@id="{name}"]').get_attribute('value'))

    return data

def _split_address(self, addres:str):
    new_address = addres.split(",")[2][1:]
    city = addres.split(",")[1]


def save_data(data: dict, filename: str) -> None:
    """
    This function saves the dictionary by key into a separate file.
    data: dict with dataset.
    filename: file name with path.
    return: None.
    """
    with open(filename, 'w', newline='') as file:
        for line in data:
            file.write(line + '\n')


def init_argparse():
    """
    Initializes argparse
    Returns parser.
    """
    parser = ArgumentParser(
        description='Load passport data generated on: https://www.random1.ru/generator-pasportnyh-dannyh')
    parser.add_argument(
        '--browser',
        nargs='?',
        help='Web browser: Chrome or Firefox',
        default='Firefox',
        type=str)
    parser.add_argument(
        '--webdriver_path',
        nargs='?',
        help='Path to Web driver',
        default='./geckodriver',
        type=str)
    parser.add_argument(
        '--number_requests',
        nargs='?',
        help='Number of requests to Web site',
        default=20,
        type=int)
    parser.add_argument(
        '--output_path',
        nargs='?',
        help='Path to save files',
        default='output/',
        type=str)

    return parser


if __name__ == '__main__':
    args = init_argparse().parse_args()
    data = get_data(args.browser, args.webdriver_path, args.number_requests)

    if not os.path.exists(args.output_path):
        os.makedirs(args.output_path)
    today = datetime.today()

    for name in data.keys():
        save_data(data[name], f'{args.output_path}/{name}_{today.strftime("%Y-%m-%d-%H.%M.%S")}.txt')
