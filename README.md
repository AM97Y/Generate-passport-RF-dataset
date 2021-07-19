

# Generate passport RF dataset

This project is generate dataset from https://www.random1.ru/generator-pasportnyh-dannyh .

## Installation

    1) Create virtual environment:
        conda create -n load python=3.7 -y
        conda activate load
        
    2) Build virtual environment:
        pip install -r requirements.txt

## Launch

```
1) Download web driver https://sites.google.com/a/chromium.org/chromedriver/home or https://github.com/mozilla/geckodriver/releases

2) python main.py --browser Firefox --path_driver ./geckodriver --number_requests 100 --output ./output
```
