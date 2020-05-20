from itertools import combinations

items = (
   ('свитер', 3, 50),
   ('спички', 0.1, 80),
   ('нож', 0.2, 60),
   ('футболка', 1, 30),
   ('носки', 0.5, 40),
   ('фонарик', 0.3, 35),
   ('консерва1', 0.4, 40),
   ('консерва2', 0.7, 60),
   ('джинсы', 2.8, 20),
   ('книга', 2.2, 15),
   ('компас', 0.25, 45),
   ('дождевик', 2.9, 40),
   ('сухофрукты', 0.9, 60),
   ('печенье', 0.8, 40),
)

total_volume = 0
for item in items:
   total_volume += item[1]


VOLUME = 7#макс объем рюкзака


def calcBackPackVol(backpack):#считаем объем комбинации
   total_volume = 0
   for item in backpack:
       total_volume += item[1]

   return total_volume


def calcBackPackCost(backpack):#считаем цену комбинации
   total_cost = 0
   for item in backpack:
       total_cost += item[2]

   return total_cost


print("в распоряжении {} предметов общим объемом {} л,\
которые необходимо уложить в рюкзак {} литров".\
     format(len(items), total_volume, VOLUME))


counter = 0
max_cost = 0
result_items = []
result_costs = []

for num in range(1, len(items) + 1):#проход по всем предметам
   for i, combination in enumerate(combinations(items, num), 1):#перебираем все возможные комбинации, enumerate используем для пронумеровки комбинаций. і-номер комбинации, combination-сама комбинация
       current_volume = calcBackPackVol(combination)#считаем объем текущей комбинации
       current_cost = calcBackPackCost(combination)#считаем цену текущей комбинации
       if current_volume <= VOLUME and current_cost >= max_cost:#фильтруем комбинации, если текущая комбинация <= максимального объема и текущая цена >= максимальной цены, которая изначально 0
           counter += 1#счетчик считает какая комбинация по счету
           max_cost = current_cost#присваивается новое (большее) значение максимальной цены рюкзака
           result_items.append(combination)#добавляем комбинацию в отфильтрованный список
           result_costs.append(current_cost)#добавляем текущую цену в отфильтрованный список
           print("комбинация {} набрала цену {} и объем {:3.2f} л: {}".\
                 format(counter, current_cost, current_volume, combination))

max_cost_count = result_costs.count(max_cost)

print("удалось {} раз добиться максимальной ценности {}".\
     format(max_cost_count, max_cost))


best_result = result_items[result_costs.index(max_cost)]


print(calcBackPackVol(best_result))

[print(item) for item in best_result]
