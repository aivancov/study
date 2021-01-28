from pprint import pprint


class Goods:
    def __init__(self):
        self.array = []
        self._attributes = [
            'название',
            'цена',
            'количество',
            'ед'
        ]
        self._number_of_items = 0

    def insert_item(self):
        print('[INFO] Добавление нового товара:')
        item = {}
        for attr in self._attributes:
            item[attr] = input(f'Введите следующую характеристику - {attr}: ')
            try:
                item[attr] = int(item[attr])
            except ValueError:
                pass
        self._number_of_items += 1
        self.array.append( (self._number_of_items, item))
        pprint(self.array)

    def calculate_stats(self):
        stats ={attr: [] for attr in self._attributes}
        for i, item in self.array:
            for k, v in item.items():
                stats[k].append(v)
        return stats


goods = Goods()
while True:
    resp = input('Вы хотите добавить еще один товар? (д/н)  ')
    if resp == 'д':
        goods.insert_item()
    elif resp == 'н':
        stats = goods.calculate_stats()
        print('===== Аналитика о товарах =====')
        pprint(stats)
        break
