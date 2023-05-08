# Есть словарь координат городов
sites = {
    'Moscow': (550, 370),
    'London': (510, 510),
    'Paris': (480, 480),
}
# Составим словарь словарей расстояний между ними
# расстояние на координатной сетке - корень из (x1 - x2) ** 2 + (y1 - y2) ** 2

from pprint import pprint
distances = dict()

moscow = sites['Moscow']
london = sites['London']
paris = sites['Paris']
moscow_london = ((moscow[0] - london[0])**2 + (moscow[1] - london[1])**2)**.5
moscow_paris = ((moscow[0] - paris[0])**2 + (moscow[1] - paris[1])**2)**.5

distances['Moscow'] = {}
distances['Moscow']['London'] = moscow_london
distances['Moscow']['Paris'] = moscow_paris

london_paris = ((paris[0] - london[0])**2 + (paris[1] - london[1])**2)**.5

distances['London'] = {}
distances['London']['Moscow'] = moscow_london
distances['London']['Paris'] = london_paris

distances['Paris'] = {}
distances['Paris']['Moscow'] = moscow_paris
distances['Paris']['London'] = london_paris

print('\n')
pprint(distances)
print('\n')

import math
distances = {}
main_dict = {}
for i in range(len(sites)-1):
    dist = math.sqrt((sites[list(sites.keys())[i]][0] - sites[list(sites.keys())[i+1]][0]) ** 2 + (sites[list(sites.keys())[i]][1] - sites[list(sites.keys())[i+1]][1]) ** 2)
    distances[f'Расстояние между {list(sites.keys())[i]} и {list(sites.keys())[i+1]} равно'] = dist
    main_dict[i] ={list(distances.keys())[i] : distances[list(distances.keys())[i]]}

dist2 = math.sqrt((sites[list(sites.keys())[-1]][0] - sites[list(sites.keys())[0]][0]) ** 2 + (sites[list(sites.keys())[-1]][1] - sites[list(sites.keys())[0]][1]) ** 2)
distances[f'Расстояние между {list(sites.keys())[-1]} и {list(sites.keys())[0]} равно'] = dist2
main_dict[i+1] = {list(distances.keys())[i+1] : distances[list(distances.keys())[-1]]}
pprint(main_dict)




