################# DICCIONARIOS ####################

# sensors = {"living room": 21, "kitchen": 23, "bedroom": 20, "pantry": 22}  # Diccionario con temperaturas
# num_cameras = {"backyard": 6, "garage": 2, "driveway": 1}  # Diccionario con cantidad de cámaras

# print(sensors)  # Mostramos el diccionario
# print(num_cameras)  # Mostramos las cámaras

# translations = {"mountain": "orod", "bread": "bass", "friend": "mellon", "horse": "roch"}  # Diccionario de traducciones
# print(translations)  # Mostramos las traducciones


################# VERIFICANDO UN ERROR ####################

# powers = {[1, 2, 4, 8, 16]: 2, [1, 3, 9, 27, 81]: 3}  # Da error porque las listas no pueden ser claves
# print(powers)  # Mostramos el diccionario


################# DICCIONARIOS CON LISTAS ####################

# children = {"von Trapp": ["Johannes", "Rosmarie", "Eleonore"], "Corleone": ["Sonny", "Fredo", "Michael"]}  # Diccionario con listas como valores
# print(children)  # Mostramos el diccionario


################# DICCIONARIO VACÍO ####################

# my_empty_dictionary = {}  # Creamos un diccionario vacío
# print(my_empty_dictionary)  # Mostramos el diccionario vacío


################# AGREGAR ELEMENTOS ####################

# menu = {"oatmeal": 3, "avocado toast": 6, "carrot juice": 5, "blueberry muffin": 2}  # Creamos un menú
# print("Before: ", menu)  # Mostramos el menú antes de modificarlo

# menu["cheesecake"] = 8  # Agregamos una nueva clave con su valor
# print("After", menu)  # Mostramos el menú actualizado


################# MODIFICAR VALORES ####################

# animals_in_zoo = {"dinosaurs": 0}  # Creamos un diccionario
# animals_in_zoo = {"dinosaurs": 0}  # Asignamos nuevamente el diccionario
# animals_in_zoo = {"horses": 2}  # Reemplazamos el diccionario anterior
# print(animals_in_zoo)  # Mostramos el resultado


################# AGREGAR VARIAS CLAVES ####################

# sensors = {"living room": 21, "kitchen": 23, "bedroom": 20}  # Creamos un diccionario con sensores
# print("Before", sensors)  # Mostramos el diccionario antes de modificarlo

# sensors.update({"pantry": 22, "guest room": 25, "patio": 34})  # Agregamos varias claves y valores
# print("After", sensors)  # Mostramos el diccionario actualizado


################# UPDATE ####################

# user_ids = {"teraCoder": 9018293, "proProgrammer": 119238}  # Diccionario con usuarios
# print(user_ids)  # Mostramos los usuarios

# user_ids.update({"theLooper": 138475, "stringQueen": 85739})  # Agregamos nuevos usuarios
# print(user_ids)  # Mostramos el resultado


################# SOBRESCRIBIR VALORES ####################

# menu["banana"] = 3  # Podemos agregar una nueva clave llamada banana

# menu = {"oatmeal": 3, "avocado toast": 6, "carrot juice": 5, "blueberry muffin": 2}  # Creamos el menú
# print("Before: ", menu)  # Mostramos el menú original

# menu["oatmeal"] = 5  # Cambiamos el valor de oatmeal
# print("After", menu)  # Mostramos el menú actualizado


################# UPDATE Y MODIFICACIÓN ####################

# oscar_winners = {"Best Picture": "La La Land", "Best Actor": "Casey Affleck", "Best Actress": "Emma Stone", "Animated Feature": "Zootopia"}  # Creamos un diccionario con premios
# print("Before", oscar_winners)  # Mostramos el diccionario original
# print()  # Línea en blanco

# oscar_winners.update({"Supporting Actress": "Viola Davis"})  # Agregamos una nueva categoría
# print("After1", oscar_winners)  # Mostramos el diccionario actualizado
# print()  # Línea en blanco

# oscar_winners["Best Picture"] = "Moonlight"  # Cambiamos el ganador de Best Picture
# print("After2", oscar_winners)  # Mostramos el resultado final


################# DICT COMPREHENSIONS ####################

# names = ['Jenny', 'Alexus', 'Sam', 'Grace']  # Lista con nombres
# heights = [61, 70, 67, 64]  # Lista con alturas

names = ['Jenny', 'Alexus', 'Sam', 'Grace']  # Lista de nombres
heights = [61, 70, 67, 64]  # Lista de alturas


################# ZIP ####################

# zip() permite unir elementos de dos listas por posición
# zipStudents = zip(names, heights)  # Unimos nombres y alturas
# print("zipStudents: ", zipStudents)  # Mostramos el resultado


################# CREAR DICCIONARIO ####################

# students = {key:value for key, value in zip(names, heights)}  # Creamos un diccionario usando las dos listas
# print(students)  # Mostramos el diccionario


################# OTRO EJEMPLO CON ZIP ####################

# drinks = ["espresso", "chai", "decaf", "drip"]  # Lista de bebidas
# caffeine = [64, 40, 0, 120]  # Cantidad de cafeína

# zipped_drinks = zip(drinks, caffeine)  # Unimos las bebidas con la cafeína
# print(zipped_drinks)  # Mostramos el objeto zip

# drinks_to_caffeine = {key:value for key, value in zipped_drinks}  # Creamos un diccionario con las bebidas y su cafeína
# print(drinks_to_caffeine)  # Mostramos el diccionario


################# CANCIONES ####################

songs = ["Like a Rolling Stone", "Satisfaction", "Imagine", "What's Going On", "Respect", "Good Vibrations"]  # Lista de canciones
playcounts = [78, 29, 44, 21, 89, 5]  # Cantidad de reproducciones de cada canción

plays = {key:value for key, value in zip(songs, playcounts)}  # Creamos un diccionario relacionando canción y reproducciones
print(plays)  # Mostramos el diccionario


################# ACTUALIZAR DICCIONARIO ####################

plays.update({"Purple Haze": 1})  # Agregamos una nueva canción
plays.update({"Respect": 94})  # Cambiamos las reproducciones de Respect

print("After: ", plays)  # Mostramos el diccionario actualizado


################# DICCIONARIO DENTRO DE OTRO DICCIONARIO ####################

library = {"The Best Songs": plays, "Sunday Feelings": {}}  # Creamos un diccionario que contiene otro diccionario
print(library)  # Mostramos la biblioteca
