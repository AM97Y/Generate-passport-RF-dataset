

# Generate passport RF dataset

This project allows to generate data for RF passports which are received from [Random One site](https://www.random1.ru/generator-pasportnyh-dannyh). Collected data will be saved  separately, in text files according to passport fields: name, surname, sex etc.
## Installation

    1) Create virtual environment:
        conda create -n  <your_virtual_environment_name> python=3.7 -y
        conda activate  <your_virtual_environment_name>
        
    2) Build virtual environment:
        pip install -r requirements.txt

 ## Prerequisites

 * Web Browser: [Google Chrome](https://www.google.com/chrome) or [Mozilla Firefox](https://www.mozilla.org/en/firefox/new/)
 * Installed web driver (see [ChromeDriver](https://chromedriver.chromium.org/downloads) or [mozilla/geckodriver](https://github.com/mozilla/geckodriver/releases) for more information)
 * Installed [Python](https://www.python.org/downloads/) >= 3.6 or [Anaconda](https://www.anaconda.com/products/individual)  >= 4.10.1


## Launch

```
 
 1) By default start:
        python main.py
 2) Change web browser:
        python main.py --browser Chrome --webdriver_path <path_to_installed_webdriver>
 3) Set certain number of web requests to site which generates passport data:
        python main.py --number_requests 100
 4) Change the output path to save collected data:
        python main.py --output_path ./output

 For more information launch `python main.py -h`  

```
