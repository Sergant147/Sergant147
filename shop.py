from datetime import datetime as dt
import os


def show_products(products):
    for i in products:
        print(f'* {i}')


def add_product(products, product):
    products.append(product)


def remove_product(products, product):
    products.remove(product)


def generate_id():
    return dt.strftime(dt.now(), '%Y-%m-%d %H-%M-%S')


def make_order(products):
    order_id = generate_id()
    with open(f'orders/{order_id}.txt', 'w', encoding='UTF-8') as f:
        for idx, prod in enumerate(products):
            if idx != len(products) - 1:
                f.write(f'{prod}\n')
            else:
                f.write(f'{prod}')


def get_orders_ids():
    return [path.removesuffix('.txt')
            for path in os.listdir('orders/')]


def read_order(order_id):
    with open(f'orders/{order_id}.txt', 'r', encoding='UTF-8') as f:
        products = f.readlines()
        for index in range(len(products)):
            products[index] = products[index].replace('\n', '')
    return products


def see_orders():
    ids = get_orders_ids()
    orders = {}
    for order_id in ids:
        orders[order_id] = read_order(order_id)
    for key, value in orders.items():
        print(f'Order {key}: ')
        for item_idx, item in enumerate(value):
            print(f'Item {item_idx + 1}: {item}')
        print()


def show_order(order_id):
    for item_idx, item in enumerate(read_order(order_id)):
        print(f'Item {item_idx + 1}: {item}')


def run():
    products = []
    while True:
        print('1. Показать список продуктов')
        print('2. Добавить продукт в корзину')
        print('3. Удалить продукт из корзины')
        print('4. Сформировать заказ из текущей корзины')
        print('5. Просмотреть историю заказов')
        print('6. Просмотреть конкретный заказ из истории')
        print('7. Кончить шоппинг')
        try:
            choice = int(input('Выберите пункт меню (1-7): '))

            if choice == 1:
                show_products(products)

            elif choice == 2:
                new_product = input('Новый Продукт: ')
                add_product(products, new_product)

            elif choice == 3:
                old_product = input('Удаляемый Продукт: ')
                remove_product(products, old_product)

            elif choice == 4:
                make_order(products)
                products = []

            elif choice == 5:
                see_orders()

            elif choice == 6:
                order_id = input('ID заказа: ')
                show_order(order_id)

            elif choice == 7:
                break

            else:
                print('Некорректный выбор. Попробуйте снова.')

            print()

        except BaseException as e:
            print('Некорректный выбор. Попробуйте снова.')


if __name__ == '__main__':
    run()
