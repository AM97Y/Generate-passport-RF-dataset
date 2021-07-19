#!/usr/bin/env python3
import os
from argparse import ArgumentParser
from datetime import datetime

from selenium import webdriver

URL = 'https://www.random1.ru/generator-pasportnyh-dannyh'
NAMES = ('LastName', 'FirstName', 'FatherName', 'DateOfBirth', 'PasportNum', 'PasportCode', 'PasportOtd',
         'PasportDate', 'Address')


def get_data(browser, path_driver, number_requests):
    """
    browser: type browser - Chrome or Firefox
    path_driver: driver location
    number_requests: number requests from https://www.random1.ru/generator-pasportnyh-dannyh.
    Return dict of load data.
    """
    if browser == 'Firefox':
        driver = webdriver.Firefox(executable_path=path_driver)
    elif browser == 'Chrome':
        driver = webdriver.Chrome(executable_path=path_driver)
    else:
        raise ValueError('use browser Chrome or Firefox')

    data = {name: set() for name in NAMES}

    driver.get(URL)
    for _ in range(number_requests):
        driver.find_element_by_xpath(
            "//div[@class='people_buttons']/button").click()
        for key in NAMES:
            data[key].add(driver.find_element_by_xpath(f'//input[@id="{key}"]').get_attribute('value'))

    return data


def save_data(data, filename):
    """
    data: dict with dataset,
    filename: file name with path.
    """
    with open(filename, 'w', newline='') as file:
        for line in data:
            file.write(line + '\n')


def init_argparse():
    """
    Initializes argparse

    Returns parser
    """
    parser = ArgumentParser(description='Load data from site {}')
    parser.add_argument(
        '--browser',
        nargs='?',
        help='type browser Chrome or Firefox',
        default='Firefox',
        type=str)

    parser.add_argument(
        '--path_driver',
        nargs='?',
        help='path web driver, download https://sites.google.com/a/chromium.org/chromedriver/home or https://github.com/mozilla/geckodriver/releases',
        default='./geckodriver',
        type=str)
    parser.add_argument(
        '--number_requests',
        nargs='?',
        help='number requests from website',
        default=20,
        type=int)
    parser.add_argument(
        '--output',
        nargs='?',
        help='path to save files',
        default='output/',
        type=str)
    return parser


def makedirs(path):
    if not os.path.exists(path):
        os.makedirs(path)


if __name__ == '__main__':
    args = init_argparse().parse_args()
    data = get_data(args.browser, args.path_driver, args.number_requests)

    makedirs(args.output)
    today = datetime.today()
    for name in NAMES:
        save_data(data[name], f'{args.output}/{name}_{today.strftime("%Y-%m-%d-%H.%M.%S")}.txt')
