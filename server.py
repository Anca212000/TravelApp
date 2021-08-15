from bottle import route, run, template, static_file, request
import bottle
import files as file
import algorithmCost as alg
import algorithmBidiSearch as algBD


@route('/static/img/<filename>')
def server_static(filename):
    return static_file(filename, root='./static/images')


@route('/static/imgInfo/<filename>')
def server_static(filename):
    return static_file(filename, root='./static/images/infoCitiesImages')


@route('/static/css/<filename>')
def server_static(filename):
    return static_file(filename, root='./static/src/tailwindcss')


@route('/static/customcss/<filename>')
def server_static(filename):
    return static_file(filename, root='./static/src/dist/css')


@route('/static/js/<filename>')
def server_static(filename):
    return static_file(filename, root='./static/ts')


@route('/')
def index():
    file.initialize()
    file.read_files()
    return template('index', time_city=0, km_city=0, list_cities=None, list_EUstreets=None, info_cities=0, id_city=-1, destination='')


@route('/', method='POST')
def post_index():
    input_city = request.forms.get('text_dest')
    start_city = request.forms.get('text_start')
    input_city = input_city.upper()
    start_city = start_city.upper()

    file.id_start_city = list(file.hours.keys()).index(start_city)
    file.id_end_city = list(file.hours.keys()).index(input_city)

    route = []
    route, number_km = alg.uniform_cost_search(
        file.id_start_city, file.id_end_city, file.N, file.matrix)

    #print(f'route: {route}')
    list_name_cities = []

    if route:
        list_name_cities.append(start_city)
        keys = list(file.hours.keys())
        for id_town in route:
            list_name_cities.append(keys[id_town])
    else:
        list_name_cities.append("No cities")

    #print(f'IDX end city este: {file.id_end_city} si start city este {start_city}')
    # print(f'{list_name_cities}')

    graph = algBD.BidirectionalSearch(file.N)
    for idx_town in file.european_street:
        graph.add_edge(idx_town[0], idx_town[1])

    out = graph.bidirectional_search(file.id_start_city, file.id_end_city)
    #print(f'out: {out}')
    path_EUstreet = []

    if not out:
        #print(f"Path with european streets does not exist between {start_city} and {input_city}")
        path_EUstreet.append("No Nat streets")
    else:
        keys = list(file.hours.keys())
        for path in out:
            path_EUstreet.append(keys[int(path)])

    return template('index', time_city=file.hours[input_city] if start_city == "SUCEAVA" else 0, km_city=number_km, list_cities=list_name_cities, list_EUstreets=path_EUstreet, info_cities=file.all_info_cities, id_city=file.id_end_city, destination=input_city)


if __name__ == '__main__':
    bottle.TEMPLATES.clear()
    run(host="localhost", port=9000, debug=True, reloader=True)
