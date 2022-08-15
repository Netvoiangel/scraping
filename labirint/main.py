from bs4 import BeautifulSoup
import requests, os, json, csv, datetime, lxml, csv

def get_data():
    headers = {
        "Accept": "*/*",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:103.0) Gecko/20100101 Firefox/103.0"
    }
    # url = "https://www.labirint.ru/search/%D0%BF%D1%80%D0%BE%D0%B3%D1%80%D0%B0%D0%BC%D0%BC%D0%B8%D1%80%D0%BE%D0%B2%D0%B0%D0%BD%D0%B8%D0%B5/?stype=0"

    # if not os.path.exists("labirint/data"):
    #     os.mkdir("labirint/data")

    # req = requests.get(url=url, headers=headers)

    # with open("labirint/page_0.html", "w", encoding="utf-8", newline='') as file:
    #     file.write(req.text)
    
    with open("labirint/page_0.html", "r", encoding="utf-8", newline='') as file:
        src = file.read()

    soup = BeautifulSoup(src, "lxml")

    page_count = soup.find_all("a", class_="pagination-number__text")
    pages_count = int(page_count[-1].text)

    # for i in range(1, pages_count+1):
    #     url = f"https://www.labirint.ru/search/%D0%BF%D1%80%D0%BE%D0%B3%D1%80%D0%B0%D0%BC%D0%BC%D0%B8%D1%80%D0%BE%D0%B2%D0%B0%D0%BD%D0%B8%D0%B5/?stype=0&page={i}"
    #     req = requests.get(url=url, headers=headers)

    #     with open(f"labirint/data/page_{i}.html", 'w', encoding="utf-8", newline ='') as file:
    #         file.write(req.text)

    return pages_count


def collect_data(pages_count):
    data = []
    time = datetime.datetime.now().strftime("%d_%m_%Y")
    num = 1
    for i in range(1, pages_count+1):
        with open(f"labirint/data/page_{i}.html", 'r', encoding="utf-8", newline ='') as file:
            src = file.read()
        
        soup = BeautifulSoup(src, "lxml")

        items_cards = soup.find_all(class_="genres-carousel__item")
        # print(items_cards)
        for item in items_cards:
            prod_title = item.find("a", class_="product-title-link").text.strip()
            prod_price = item.find("span", class_="price-val").find("span").text.strip()
            prod_url = item.find("a", class_="product-title-link").get("href")
            prod_url = f"https://www.labirint.ru{prod_url}"

            # print(prod_title, prod_price, prod_url)
            data.append(
                {
                    "number": num,
                    "product_article": prod_title,
                    "product_price": prod_price,
                    "product_url": prod_url
                }
            )
            num += 1
    with open(f"labirint/json_{time}.json", "w", encoding="utf-8", newline='') as file:
        json.dump(data, file, indent=4, ensure_ascii=False)


def main():
    pages_count = get_data()
    collect_data(pages_count=pages_count)

if __name__ == "__main__":
    main()