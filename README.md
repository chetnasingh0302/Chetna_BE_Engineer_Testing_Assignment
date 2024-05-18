
# Scraping tool project using python FastApi

Welcome to scraping tool project using python FastApi by Chetna Singh

## Table of Contents

1. [Introduction](#introduction)
2. [Getting Started](#getting-started)

## Introduction

Developed a scraping tool using Python FastAPI framework to automate the information scraping process from the target [website](https://dentalstall.com/shop/). The tool:

1. Scraped the product name, price, and image from each page of the catalogue.
2. Implemented settings:
    1. The first one limited the number of pages from which we need to scrape the information (for example, `5` means that we want to scrape only products from the first 5 pages).
    2. The second one provided a proxy string that tool can use for scraping
2. Stored the scraped information in a database. For simplicity, stored it on the PC's local storage as a JSON file in the following format:

```jsx
[
{
"product_title":"",
"product_price":0,
"path_to_image":"", # path to image at your PC
}
]
```


1. At the end of the scraping cycle, notified designated recipients about the scraping status - send a simple message that will state how many products were scraped and updated in DB during the current session. For simplicity, printed this info in the console.

Designed and implemented this tool, keeping in mind the following guidelines:

- Ensured type validation and data integrity using appropriate methods. 
- Considered adding a simple retry mechanism for the scraping part. For example, if a page cannot be reached because of a destination site server error, we would like to retry it in N seconds.
- Added simple authentication to the endpoint using a static token.
- Added a scraping results caching mechanism using favourite in-memory DB. If the scraped product price has not changed, we don’t want to update the data of such a product in the DB.




## Getting Started

To get started with this project, follow these steps:

1. clone repository

2. Install the necessary dependencies by running the given commad to your terminal-

```bash
pip install python3
pip install -r requirements.txt
```
Note: Restart your IDE


3. Run uvicorn at port 8000-

```bash
uvicorn main:app --reload 
```
The application must have been started on port http://127.0.0.1:8000

4. Swagger UI to use project APIs-

http://127.0.0.1:8000/docs

5. Output will be stored in file named scarpped_data.json

your authentication token is `SECRET_TOKEN`


