from bs4 import BeautifulSoup
import requests, lxml, datetime, os, json, csv

def get_data():
    headers = {
        "Accept": "image/avif,image/webp,*/*",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:103.0) Gecko/20100101 Firefox/103.0"
    }
    # url = "https://roscarservis.ru/catalog/legkovye/"

    # req = requests.get(url=url, headers=headers)

    cur_date = datetime.datetime.now().strftime("%d_%m_%Y")

    # if not os.path.exists("roscar/data"):
    #     os.mkdir("roscar/data")
    
    # with open(f"roscar/data/page_{cur_date}.html", "w", encoding="utf-8", newline ='') as file:
    #     file.write(req.text)

    with open("roscar/data/page_08_08_2022.html", encoding="utf-8", newline ='') as file:
        src = file.read()

    soup = BeautifulSoup(src, "lxml")
    pages_count = soup.find("div", class_="pagination").find_all("a")[-2].text
    pages_count = int(pages_count)
    # print(pages_count)
    # for i in range(1, pages_count + 1):
    #     req = requests.get(url = f"https://roscarservis.ru/catalog/legkovye/?PAGEN_1={i}", headers=headers)

    #     with open(f"roscar/data/page_{i}_{cur_date}.html", "w", encoding="utf-8", newline = '') as file:
    #         file.write(req.text)
    return pages_count + 1

def collect_data(pages_count):
    data = []
    cur_date = datetime.datetime.now().strftime("%d_%m_%Y")

    for page in range(1, pages_count):
        with open(f"roscar/data/page_{page}_{cur_date}.html", encoding="utf-8", newline='') as file:
            src = file.read()

        soup = BeautifulSoup(src, "lxml")
        items_cards = soup.find_all("div", class_="catalog__item")

        for item in items_cards:
            prod_artice = item.find("a", class_="catalog-item__title").text.strip()
            prod_price = item.find("span", class_="catalog-item__price-val").text
            prod_url = item.get("href")

            data.append(
                {
                    "prod_article": prod_artice,
                    "prod_price": prod_price,
                    "prod_url": prod_url
                }
            )
    with open(f"roscar/data/json_{cur_date}.json", "a", encoding="utf-8", newline='') as file:
        json.dump(data, file, indent=4, ensure_ascii=False)


def main():
    pages_count = get_data()
    collect_data(pages_count=pages_count)

if __name__ == "__main__":
    main()