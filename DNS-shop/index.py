from bs4 import BeautifulSoup
import requests, lxml, json

def get_data():
   cookies = {
      'MVID_CITY_ID': 'CityCZ_2534',
      'MVID_GUEST_ID': '19266122230',
      'MVID_REGION_ID': '10',
      'searchType2': '1',
      'MVID_TIMEZONE_OFFSET': '5',
      'MVID_KLADR_ID': '0200000100000',
      'MVID_REGION_SHOP': 'S906',
      'MVID_GEOLOCATION_NEEDED': 'false',
      'MVID_ABC_TEST_WIDGET': '0',
      'MVID_AB_TEST_COMPARE_ONBOARDING': 'true',
      'MVID_ADDRESS_COMMENT_AB_TEST': '2',
      'MVID_BLACK_FRIDAY_ENABLED': 'true',
      'MVID_CALC_BONUS_RUBLES_PROFIT': 'false',
      'MVID_CART_MULTI_DELETE': 'false',
      'MVID_FILTER_TOOLTIP': '1',
      'MVID_IS_NEW_BR_WIDGET': 'true',
      'MVID_LAYOUT_TYPE': '1',
      'MVID_NEW_MBONUS_BLOCK': 'true',
      'MVID_PRICE_FIRST': '2',
      'MVID_PRM20_CMS': 'true',
      'PRESELECT_COURIER_DELIVERY_FOR_KBT': 'true',
      'PROMOLISTING_WITHOUT_STOCK_AB_TEST': '2',
      'MVID_FLOCKTORY_ON': 'true',
      'MVID_NEW_ACCESSORY': 'true',
      'MVID_SERVICES': '111',
      'MVID_SERVICES_DESCRIPTION': 'true',
      '__lhash_': 'a0488e1735f1ba62e4eae675a7eade66',
      'CACHE_INDICATOR': 'false',
      'COMPARISON_INDICATOR': 'false',
      'HINTS_FIO_COOKIE_NAME': '1',
      'JSESSIONID': 'CpGTvqBLLKF33cYZ943j9xX7nJQCL5TGB12jrS72TpnYbLcylmQ0!94126264',
      'MVID_AB_SERVICES_DESCRIPTION': 'var2',
      'MVID_CART_AVAILABILITY': '1',
      'MVID_CATALOG_STATE': '1',
      'MVID_CREDIT_AVAILABILITY': 'true',
      'MVID_FILTER_CODES': 'true',
      'MVID_GET_LOCATION_BY_DADATA': 'DaData',
      'MVID_GTM_DELAY': 'true',
      'MVID_HANDOVER_SUMMARY': 'true',
      'MVID_LP_HANDOVER': '2',
      'MVID_LP_SOLD_VARIANTS': '3',
      'MVID_MCLICK': 'true',
      'MVID_MINI_PDP': 'true',
      'MVID_NEW_DESKTOP_FILTERS': 'true',
      'MVID_NEW_LK': 'true',
      'MVID_NEW_LK_CHECK_CAPTCHA': 'true',
      'MVID_NEW_LK_LOGIN': 'true',
      'MVID_NEW_LK_OTP_TIMER': 'true',
      'MVID_SERVICES_MINI_BLOCK': 'var1',
      'MVID_SMART_BANNER_BOTTOM': 'true',
      'MVID_SUPER_FILTERS': 'false',
      'MVID_TAXI_DELIVERY_INTERVALS_VIEW': 'new',
      'MVID_WEBP_ENABLED': 'true',
      'NEED_REQUIRE_APPLY_DISCOUNT': 'true',
      'bIPs': '-1323973254',
      'flacktory': 'no',
      'MVID_ENVCLOUD': 'prod2',
      'BIGipServeratg-ps-prod_tcp80': '2953108490.20480.0000',
      'Old_Browser_Accept_the_Risk_and_Continue': '1',
   }

   headers = {
      'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:103.0) Gecko/20100101 Firefox/103.0',
      'Accept': 'application/json',
      'Accept-Language': 'ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3',
      # 'Accept-Encoding': 'gzip, deflate, br',
      'x-set-application-id': '77c7a513-1a99-4722-bd25-f944d5821d30',
      'Connection': 'keep-alive',
      'Referer': 'https://www.mvideo.ru/noutbuki-planshety-komputery-8/planshety-195/f/skidka=da/tolko-v-nalichii=da',
      # Requests sorts cookies= alphabetically
      # 'Cookie': 'MVID_CITY_ID=CityCZ_2534; MVID_GUEST_ID=19266122230; MVID_REGION_ID=10; searchType2=1; MVID_TIMEZONE_OFFSET=5; MVID_KLADR_ID=0200000100000; MVID_REGION_SHOP=S906; MVID_GEOLOCATION_NEEDED=false; MVID_ABC_TEST_WIDGET=0; MVID_AB_TEST_COMPARE_ONBOARDING=true; MVID_ADDRESS_COMMENT_AB_TEST=2; MVID_BLACK_FRIDAY_ENABLED=true; MVID_CALC_BONUS_RUBLES_PROFIT=false; MVID_CART_MULTI_DELETE=false; MVID_FILTER_TOOLTIP=1; MVID_IS_NEW_BR_WIDGET=true; MVID_LAYOUT_TYPE=1; MVID_NEW_MBONUS_BLOCK=true; MVID_PRICE_FIRST=2; MVID_PRM20_CMS=true; PRESELECT_COURIER_DELIVERY_FOR_KBT=true; PROMOLISTING_WITHOUT_STOCK_AB_TEST=2; MVID_FLOCKTORY_ON=true; MVID_NEW_ACCESSORY=true; MVID_SERVICES=111; MVID_SERVICES_DESCRIPTION=true; __lhash_=a0488e1735f1ba62e4eae675a7eade66; CACHE_INDICATOR=false; COMPARISON_INDICATOR=false; HINTS_FIO_COOKIE_NAME=1; JSESSIONID=CpGTvqBLLKF33cYZ943j9xX7nJQCL5TGB12jrS72TpnYbLcylmQ0!94126264; MVID_AB_SERVICES_DESCRIPTION=var2; MVID_CART_AVAILABILITY=1; MVID_CATALOG_STATE=1; MVID_CREDIT_AVAILABILITY=true; MVID_FILTER_CODES=true; MVID_GET_LOCATION_BY_DADATA=DaData; MVID_GTM_DELAY=true; MVID_HANDOVER_SUMMARY=true; MVID_LP_HANDOVER=2; MVID_LP_SOLD_VARIANTS=3; MVID_MCLICK=true; MVID_MINI_PDP=true; MVID_NEW_DESKTOP_FILTERS=true; MVID_NEW_LK=true; MVID_NEW_LK_CHECK_CAPTCHA=true; MVID_NEW_LK_LOGIN=true; MVID_NEW_LK_OTP_TIMER=true; MVID_SERVICES_MINI_BLOCK=var1; MVID_SMART_BANNER_BOTTOM=true; MVID_SUPER_FILTERS=false; MVID_TAXI_DELIVERY_INTERVALS_VIEW=new; MVID_WEBP_ENABLED=true; NEED_REQUIRE_APPLY_DISCOUNT=true; bIPs=-1323973254; flacktory=no; MVID_ENVCLOUD=prod2; BIGipServeratg-ps-prod_tcp80=2953108490.20480.0000; Old_Browser_Accept_the_Risk_and_Continue=1',
      'Sec-Fetch-Dest': 'empty',
      'Sec-Fetch-Mode': 'cors',
      'Sec-Fetch-Site': 'same-origin',
      # Requests doesn't support trailers
      # 'TE': 'trailers',
   }

   params = {
      'categoryId': '195', # Категория планшетов - 195
      'offset': '0',
      'limit': '24',
      'filterParams': [
         'WyJza2lka2EiLCIiLCJkYSJd',
         'WyJ0b2xrby12LW5hbGljaGlpIiwiIiwiZGEiXQ==',
      ],
      'doTranslit': 'true',
   }

   response = requests.get('https://www.mvideo.ru/bff/products/listing', params=params, cookies=cookies, headers=headers).json()
   # print(response)

   products_ids = response.get('body').get('products')
   with open("DNS-shop/1_products_ids.json", "w", encoding="utf-8", newline='') as file:
      json.dump(products_ids, file, indent=4, ensure_ascii=False)

   data = {
      'productIds': products_ids,
      'mediaTypes': [
         'images'
      ],
      'category':True,
      'status':True,
      'brand':True,
      'propertyTypes': [
         'KEY'
      ],
      'propertiesConfig': {
         'propertiesPortionSize': 5
      },
      'multioffer':False
   }

   response = requests.post('https://www.mvideo.ru/bff/product-details/list', cookies=cookies, headers=headers, json=data).json()
   
   with open("DNS-shop/2_products.json", "w", encoding="utf-8", newline='') as file:
      json.dump(response, file, indent = 4, ensure_ascii=False)

   # print(len(response.get('body').get('products'))) 18

   products_ids_str = ','.join(products_ids)

   params = {
    'productIds': products_ids_str,
    'addBonusRubles': 'true',
    'isPromoApplied': 'true',
}

   response = requests.get('https://www.mvideo.ru/bff/products/prices', params=params, cookies=cookies, headers=headers).json()

   with open("DNS-shop/3-prices_for_items.json", "w", encoding="utf-8", newline = '') as file:
      json.dump(response, file, indent=4, ensure_ascii=False)

   # print(len(response.get('body').get('materialPrices')))

   items_prices = {}

   material_prices = response.get('body').get('materialPrices')
   
   for item in material_prices:
         item_id = item.get('price').get("productId")
         item_base_price = item.get('price').get('basePrice')
         item_sale_price = item.get('price').get('salePrice')
         item_bonus = item.get('bonusRubles').get('total')

         items_prices[item_id] = {
           'item_basePrice': item_base_price,
           'item_salePrice': item_sale_price,
           'item_bonus': item_bonus
         }

   with open("DNS-shop/4_items_rices_bonus.json", "w", encoding="utf-8", newline='') as file:
      json.dump(items_prices, file, indent=4, ensure_ascii=False)

def get_result():
      with open('DNS-shop/2_products.json', encoding='utf-8', newline='') as file:
         products_data = json.load(file)

      with open('DNS-shop/4_items_rices_bonus.json', encoding='utf-8', newline='') as file:
         products_prices = json.load(file)
      
      products_data = products_data.get('body').get('products')

      for item in products_data:
            product_id = item.get('productId')

            if product_id in products_prices:
                   prices = products_prices[product_id]
            
            item['item_basePrice'] = prices.get('item_basePrice')
            item['item_salePrice'] = prices.get('item_salePrice')
            item['item_bonus'] = prices.get('item_bonus')
      
      with open("DNS-shop/5_result.json", "w", encoding="utf-8", newline='') as file:
         json.dump(products_data, file, indent=4, ensure_ascii=False)

def main():
   get_data()
   get_result()

if __name__ == '__main__':
   main()