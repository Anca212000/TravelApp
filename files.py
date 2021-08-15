import numpy as np
import csv


def initialize():
    global matrix, hours, N
    global all_info_cities
    global european_street, M
    global id_start_city, id_end_city

    all_info_cities = [[]] * 23

    N = 23
    matrix = np.zeros((N, N), dtype=np.int32)

    hours = {
        "SUCEAVA": 0.00,
        "BOTOSANI": 0.47,
        "IASI": 2.43,
        "PIATRA NEAMT": 2.00,
        "VATRA DORNEI": 2.20,
        "BISTRITA": 3.43,
        "SATU MARE": 7.25,
        "BACAU": 2.38,
        "MIERCUREA CIUC": 4.50,
        "BRASOV": 6.08,
        "GALATI": 5.40,
        "CONSTANTA": 8.29,
        "BUCURESTI": 7.17,
        "CRAIOVA": 10.34,
        "TARGU JIU": 10.14,
        "SIBIU": 7.21,
        "CLUJ-NAPOCA": 5.52,
        "TARGU MURES": 5.05,
        "ALBA IULIA": 7.01,
        "HUNEDOARA": 8.06,
        "ORADEA": 7.30,
        "ARAD": 9.43,
        "TIMISOARA": 9.30
    }


def read_files():
    global matrix

    with open('./static/txt/cities.txt', 'r') as km_route_city:
        matrix = [[int(km) for km in line.split('\t')]
                  for line in km_route_city if line.strip() != ""]
    # print(matrix)

    id, nb_sights, title, img, description = 0, 0, '', '', ''
    with open('./static/txt/sights.txt', encoding="mbcs", buffering=100000) as doc_cities:
        for line in doc_cities:
            if line.strip().isdigit():
                id = int(line.strip())
                array = []
            if line.split(':')[0].strip() == "titlu":
                title = line.split(':')[-1].strip()
            elif line.split(':')[0].strip() == "imagine":
                img = line.split(':')[-1].strip()
            elif line.split(':')[0].strip() == "info":
                description = line.split(':')[-1].strip()
            if title != '' and img != '' and description != '':
                array.append(title)
                array.append(img)
                array.append(description)
                all_info_cities[id] = array
                title, img, description = '', '', ''

    global M, european_street
    nb_e_street = 0
    with open('./static/txt/streets.txt', 'r') as streets:
        for line in streets:
            if len(line.split()) == 1:
                M = int(line.strip())
                european_street = [[]] * M
            elif len(line.split()) == 2:
                array = []
                array.append(int(line.split()[0].strip()))
                array.append(int(line.split()[-1].strip()))
                european_street[nb_e_street] = array
                nb_e_street = nb_e_street + 1

    #print(f'M= {M}\n european_streets= {european_street}')
    # print(
    #     f'{all_info_cities[0][0]} + {all_info_cities[0][1]} + {all_info_cities[0]}')
    # print(f'{all_info_cities[1]}')
