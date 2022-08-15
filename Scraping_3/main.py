
import requests, os, csv, json
from datetime import datetime

def collect_data():
    t_date = datetime.now().strftime('%d_%m_%Y')

    response = requests.get(url="https://www.lifetime.plus/api/analysis2")

    with open(f"Scraping_3/data/info_{t_date}.json", "w", encoding="utf-8", newline='') as file:
        json.dump(response.json(), file, indent=4, ensure_ascii=False)

    categories = response.json()['categories']
    result = []

    for c in categories:
        c_name = c.get('name').strip()
        c_items = c.get('items')

        for item in c_items:
            item_name = item.get('name').strip()
            item_price = item.get('price')
            item_desc = item.get('description').strip()

            item_wt = item.get('days')
            item_bio = item.get('biomaterial')

            result.append(
                [c_name, item_name, item_bio, item_desc, item_price, item_wt]
            )  

    with open(f"Scraping_3/data/result_{t_date}.csv", "a", encoding="utf-8", newline='') as file:
        writer1 = csv.writer(file)

        writer1.writerow(
            (
                'Категория',
                'Анализ',
                'Биоматериал',
                'Описание',
                'Стоимость',
                'Готовность в течение'
            )
        )
        
        writer1.writerows(
            result
        )

def main():
    collect_data()

if __name__ == '__main__':
    main()