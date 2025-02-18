import requests
import json

def check_product_api_items_avd(product_id):
    api_url = "https://www.avdmotors.ru/api"
    url_site = f"https://www.avdmotors.ru/price/{product_id}"
    response = requests.get(f"{api_url}/items/{product_id}")

    if response.status_code == 200:
        data = response.json()
        offers = [item for item in data if "price" in item]
        for offer in offers:
            safe_number = offer.get("safe_number", "Не указано")
            name = offer.get("name", "Без названия")
            price = offer.get("price", "Цена не указана")

            return (f"Сайт: {url_site} Арктикул: {safe_number} \nНаименование: {name} \nЦена: {price} руб")

def check_product_api_autopiter(product_id):
    pass

def check_product_api_sputnik(product_id):
    print(product_id)
    api_url = "https://auto-sputnik.ru/"
    api_api = "https://autopiter.ru/api/api/appraise/getcosts?idArticles"
    response = requests.get(f"{api_url}/price/{product_id}")
    exit_list = []
    if response.status_code == 200:
        data = response.json()
        items = data.get("data", [])
        if items:  # Проверяем, есть ли предложения
                for item in items:
                    price = item.get("originalPrice", "Цена не указана")
                    supplier_name = item.get("id", {}).get("id", "Неизвестный поставщик")
                    exit_list.append(f"Товар: {supplier_name}, Цена: {price}")
    return len(exit_list)

def check_product_api_autopiter(product_id):
    url_presence = "https://autopiter.ru/api/api/appraise/getcosts"
    url_goods = "https://autopiter.ru/api/api/searchdetails"
    url_site = f"https://autopiter.ru/goods/{product_id}"

    r_goods = requests.get(url=url_goods, params={"detailNumber": product_id}).text
    goods_data = json.loads(r_goods)

    for item in goods_data["data"].get("catalogs", []):
        if (item["rank"]) != 0:
            uuid = int(item["uid"])
            name = item["name"]
            orig_price = 0
            analog_price = 0

            r_presence = requests.get(url=url_presence, params={"idArticles": uuid}).text
            presence_data = json.loads(r_presence)
            for price in presence_data.get("data", []):
                orig_price = price["originalPrice"]
                analog_price = price["analogPrice"]
            
            return f"Сайт: {url_site}\nНаименование: {name} \nОригинальная цена: {orig_price} руб \nАналоговая цена: {analog_price} руб \nID: {product_id} "




# check_product_api_sputnik("812345H000TH")
# product_id = "0805"
# check_product_api(product_id)

# https://www.avdmotors.ru/api/price?number=WD40&catalog=WD-40
# https://www.avdmotors.ru/api/items/WD40

# def websitesWithDetails(name):
#     format_answer = f"AVD:{check_product_api_avd(name)} \n AutoPiter: {check_product_api_autopiter(name)} \n Sputnik: {check_product_api_sputnik(name)}"

# Проверка по айди в каждой функции реализовать свой собстевенный словарь, созвомжно вынести словари в функции  отдельно, скорее всего так правильно будет
# Покопаться в двух других сайтах, просмотреть структуру АПИ, а также найти возможность объединить поиск по арктикула
# Поиск определенного арктикула хендай
# реализовать поиск по сайту с автоматической прокруткой