import requests
from bs4 import BeautifulSoup
from typing import List, Optional
import re


class Scraper:
    def __init__(self):
        self.base_url = "https://dentalstall.com/shop/"

    def scrape(
        self, pages_limit: Optional[int] = None, proxy: Optional[str] = None
    ) -> List[dict]:
        scraped_data = []
        page_count = 1
        while not pages_limit or page_count <= pages_limit:
            try:
                response = requests.get(
                    f"{self.base_url}?page={page_count}", proxies={"http": proxy} if proxy else None, timeout=5
                )
                if response.status_code == 200:
                    scrapped_html = BeautifulSoup(response.content, "html.parser")
                    products = scrapped_html.find_all("div", class_="product-inner")
                    for product in products:
                        product_title = product.find(
                            "div", class_="addtocart-buynow-btn"
                        )

                        price_string = product.find(
                            "span", class_="woocommerce-Price-amount"
                        )

                        if price_string and product_title:
                            product_title = product_title.a.get("data-title")
                            price = float(
                                re.sub(r"[^\d.]", "", price_string.bdi.text.strip())
                            )
                        
                            image_path = product.find(
                                "div", class_="mf-product-thumbnail"
                            )
                            if image_path:
                                image_path = image_path.a.img.get("src")
                            else:
                                image_path = None
                            scraped_data.append(
                                {
                                    "product_title": product_title,
                                    "product_price": price,
                                    "path_to_image": image_path,
                                }
                            )
                else:
                    raise Exception(
                        f"Failed to fetch page {page_count}, status code: {response.status_code}"
                    )
                page_count += 1
            except Exception as e:
                print(f"Error scraping page {page_count}: {e}")
                continue
        return scraped_data
