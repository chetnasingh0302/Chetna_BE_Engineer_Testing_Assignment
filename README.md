
# BE engineer testing assigment

Welcome to the BE engineer testing assigment by Chetna Singh

## Table of Contents

1. [Introduction](#introduction)
2. [Getting Started](#getting-started)

## Introduction

You are tasked with developing a scraping tool using Python FastAPI framework to automate the information scraping process from the target [website](https://dentalstall.com/shop/). Your tool should be able to:

1. Scrape the product name, price, and image from each page of the catalogue (it’s not necessary to open each product card).
Different settings can be provided as input, so your tool should be able to recognize them and work accordingly. For the current task, you can implement only two optional settings:
    1. The first one will limit the number of pages from which we need to scrape the information (for example, `5` means that we want to scrape only products from the first 5 pages).
    2. The secod one will provide a proxy string that tool can use for scraping
2. Store the scraped information in a database. For simplicity, you can store it on your PC's local storage as a JSON file in the following format:

```jsx
[
{
"product_title":"",
"product_price":0,
"path_to_image":"", # path to image at your PC
}
]
```

However, be aware that there should be an easy way to use another storage strategy.

1. At the end of the scraping cycle, you need to notify designated recipients about the scraping status - send a simple message that will state how many products were scraped and updated in DB during the current session. For simplicity, you can just print this info in the console.

Your task is to design and implement this tool, keeping in mind the following guidelines:

- Ensure type validation and data integrity using appropriate methods. Remember, accurate typing is crucial for data validation and processing efficiency.
- Consider adding a simple retry mechanism for the scraping part. For example, if a page cannot be reached because of a destination site server error, we would like to retry it in N seconds.
- Add simple authentication to the endpoint using a static token.
- Add a scraping results caching mechanism using your favourite in-memory DB. If the scraped product price has not changed, we don’t want to update the data of such a product in the DB.

You are encouraged to make design decisions based on your understanding of the problem and the requirements provided.



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


