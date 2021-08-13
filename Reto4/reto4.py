from datetime import date

def catalogacion_peliculas(inventario: list)->tuple:
    current_year = date.today().year

    filter_DVDs_delete = lambda x : x["tipo"] == "DVD" and x["genero"] == "Terror" and current_year - x["año"] >= 21
    DVDs_delete = [ x["id"] for x in list(filter(filter_DVDs_delete, inventario))]

    def filter_CDs_delete(movie):
        if movie["tipo"] == "CD":
            if movie["genero"] == "Terror":
                return current_year - movie["año"] >= 11
            else:
                return current_year - movie["año"] >= 16
        return False
    CDs_delete = [ x["id"] for x in list(filter(filter_CDs_delete, inventario))]

    keep_movies = [ x for x in inventario if x["id"] not in DVDs_delete and x["id"] not in CDs_delete]
        
    def adjust_name_actors(movie):
        from functools import reduce
        list_actors = list(map(lambda x: f"{x.split()[1]},{x.split()[0]}", movie["actor"].split(",")))
        movie["actor"] = reduce(lambda x, y : x + ";" + y, list_actors)
        return movie
    keep_movies = list(map(adjust_name_actors, keep_movies))

    return keep_movies, DVDs_delete, CDs_delete

inventario = [
    {'id': '45125', 'titulo': 'The Shawshank Redemption', 'tipo': 'DVD', 'genero': 'Drama', 'actor': 'Tim Robbins,Morgan Freeman,Bob Gunton', 'año': 1994, 'duración': '2h22min'},
    {'id': '54217', 'titulo': 'The Dark Knight', 'tipo': 'DVD', 'genero': 'Acción', 'actor': 'Christian Bale,Heath Ledger,Aaron Eckhart', 'año': 2008, 'duración': '2h32min'},
    {'id': '63587', 'titulo': 'El bueno, El malo y El feo', 'tipo': 'DVD', 'genero': 'Acción', 'actor': 'Clint Eastwood,Eli Wallach,Lee VanCleef', 'año': 1996, 'duración': '2h41min'},
    {'id': '75698', 'titulo': 'Forrest Gump', 'tipo': 'DVD', 'genero': 'Comedia', 'actor': 'Tom Hanks', 'año': 1994, 'duración': '2h22min'},
    {'id': '87556', 'titulo': 'Alien - El octavo pasajero', 'tipo': 'DVD', 'genero': 'Terror', 'actor': 'Sigourney Weaver,Tom Skerritt', 'año': 1994, 'duración': '1h57min'},
    {'id': '96587', 'titulo': 'El gran dictador', 'tipo': 'CD', 'genero': 'Comedia', 'actor': 'Charles Chaplin', 'año': 1940, 'duración':'2h5min'}
]

print(catalogacion_peliculas(inventario))

inventario = [
    {'id': '75698', 'titulo': 'Forrest Gump', 'tipo': 'CD', 'genero': 'Comedia', 'actor': 'Tom Hanks', 'año': 1994, 'duración': '2h22min'},
    {'id': '87556', 'titulo': 'Alien - El octavo pasajero', 'tipo': 'DVD', 'genero': 'Terror', 'actor': 'Sigourney Weaver,Tom Skerritt', 'año': 1994, 'duración': '1h57min'},
    {'id': '45125', 'titulo': 'The Shawshank Redemption', 'tipo': 'CD', 'genero': 'Drama', 'actor': 'Tim Robbins,Morgan Freeman,Bob Gunton', 'año': 1994, 'duración': '2h22min'}, 
    {'id': '54547', 'titulo': 'Apocalypse Now', 'tipo': 'DVD', 'genero': 'Terror', 'actor': 'Martin Sheen,Marlon Brando,Robert Duvall', 'año': 1979, 'duración': '2h27min'}, 
    {'id': '63587', 'titulo': 'El bueno, El malo y El feo', 'tipo': 'CD', 'genero': 'Acción', 'actor': 'Clint Eastwood,Eli Wallach,Lee VanCleef', 'año': 1996, 'duración': '2h41min'}, 
    {'id': '96587', 'titulo': 'El gran dictador', 'tipo': 'CD', 'genero': 'Comedia', 'actor': 'Charles Chaplin', 'año': 1940, 'duración': '2h5min'}
]

print(catalogacion_peliculas(inventario))


