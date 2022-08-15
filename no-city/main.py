from bs4 import BeautifulSoup
import lxml, json, os, csv, datetime, time, requests


def get_data():
    headers = {
        "Accept": "image/avif,image/webp,*/*",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:103.0) Gecko/20100101 Firefox/103.0"
    }
    # url = "https://no-city.ru/33-velosipedy-v-ufe"
    # req = requests.get(url = url, headers = headers)

    # with open("no-city/page_0.html", "w", encoding="utf-8", newline='') as file:
    #     file.write(req.text)

    with open("no-city/page_0.html", encoding="utf-8", newline = '') as file:
        src = file.read()
    
    # if not os.path.exists("data"):
    #     os.mkdir("no-city/data")

    soup = BeautifulSoup(src, "lxml")
    pages_count = soup.find("ul", class_="pagination").find_all("li")[-2].text.strip()
    pages_count = int(pages_count)
    
    # for i in range(1, pages_count+1):
    #     url = f"https://no-city.ru/33-velosipedy-v-ufe?p={i}"
    #     # print(url)
    #     req = requests.get(url = url, headers = headers)
    #     with open(f"no-city/data/page_{i}.html", "w", encoding="utf-8", newline = '') as file:
    #         file.write(req.text)
    return pages_count + 1

def collect_data(pages_count):

    cur_date = datetime.datetime.now().strftime("%d_%m_%Y")
    data = []

    with open(f"no-city/data/data_{cur_date}.csv", "w", encoding="utf-8", newline ='') as file:
        writer = csv.writer(file)

        writer.writerow(
            (
                "Артикул", 
                "Цена", 
                "Наличие",
                "Ссылка"
            )
        )

    for page in range(1, pages_count):
        with open(f"no-city/data/page_{page}.html", encoding="utf-8", newline='') as file:
            src = file.read()

        soup = BeautifulSoup(src, "lxml")
        items = soup.find_all("div", class_="product-container")

        for item in items:
            prod_article = item.find("a", class_="product-name").text.strip()
            prod_price = item.find("div", class_="content_price").find("span", class_="price product-price").text
            prod_availability = item.find("span", class_="availability").text.strip()
            prod_url = item.find("a", class_="product-name").get("href")

            # print(f"article: {prod_article}, price: {prod_price}, avai: {prod_availability}, url: {prod_url}")
            
            data.append(
                {
                    "prod_art": prod_article,
                    "prod_price": prod_price,
                    "prod_avail": prod_availability,
                    "prod_url": prod_url
                }
            )
            with open(f"no-city/data/data_{cur_date}.csv", "a", encoding="utf-8", newline ='') as file:
                writer = csv.writer(file)

                writer.writerow(
                    (
                        prod_article,
                        prod_price,
                        prod_availability,
                        prod_url
                    )
                )

        print(f"[INFO] Обработана страница {page}/{pages_count}")
    
    with open(f"no-city/data/data_{cur_date}.json", "a", encoding="utf-8", newline='') as file:
        json.dump(data, file, indent=4, ensure_ascii=False)

def main():
    pages_count = get_data()
    collect_data(pages_count=pages_count)


if __name__ == '__main__':
    main()