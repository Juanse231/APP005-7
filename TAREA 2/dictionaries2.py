################# OBTENER UNA CLAVE ####################

# building_heights = {"Burj Khalifa": 828, "Shanghai Tower": 632, "Abraj Al Bait": 601, "Ping An": 599, "Lotte World Tower": 554.5, "One World Trade": 541.3}  # Diccionario con alturas de edificios
# print(building_heights["Burj Khalifa"])  # Obtenemos el valor usando la clave
# print(building_heights["Ping An"])  # Obtenemos la altura de Ping An

# zodiac_elements = {"water": ["Cancer", "Scorpio", "Pisces"], "fire": ["Aries", "Leo", "Sagittarius"], "earth": ["Taurus", "Virgo", "Capricorn"], "air": ["Gemini", "Libra", "Aquarius"]}  # Diccionario con signos zodiacales
# print(zodiac_elements["earth"])  # Mostramos los signos del elemento tierra
# print(zodiac_elements["fire"])  # Mostramos los signos del elemento fuego


################# CLAVE QUE NO EXISTE ####################

# building_heights = {"Burj Khalifa": 828, "Shanghai Tower": 632, "Abraj Al Bait": 601, "Ping An": 599, "Lotte World Tower": 554.5, "One World Trade": 541.3}  # Creamos el diccionario
# print(building_heights["Landmark 81"])  # Da error porque esta clave no existe


################# VERIFICAR SI EXISTE UNA CLAVE ####################

# key_to_check = "Landmark 81"  # Guardamos la clave que queremos buscar

# if key_to_check in building_heights:  # Verificamos si la clave existe
#     print(building_heights["Landmark 81"])  # Mostramos el valor si existe


# zodiac_elements = {"water": ["Cancer", "Scorpio", "Pisces"], "fire": ["Aries", "Leo", "Sagittarius"], "earth": ["Taurus", "Virgo", "Capricorn"], "air": ["Gemini", "Libra", "Aquarius"]}  # Creamos el diccionario

# zodiac_elements["energy"] = "Not a Zodiac element"  # Agregamos una nueva clave

# if "energy" in zodiac_elements:  # Verificamos si energy existe
#     print(zodiac_elements["energy"])  # Mostramos el valor de energy


################# OBTENER UNA CLAVE DE FORMA SEGURA ####################

# building_heights = {"Burj Khalifa": 828, "Shanghai Tower": 632, "Abraj Al Bait": 601, "Ping An": 599, "Lotte World Tower": 554.5, "One World Trade": 541.3}  # Creamos el diccionario

# building_heights.get("Shanghai Tower")  # get() obtiene el valor de una clave

# building_heights.get("My House")  # Si no existe, devuelve None


################# EJEMPLO CON GET() ####################

# user_ids = {"teraCoder": 100019, "pythonGuy": 182921, "samTheJavaMaam": 123112, "lyleLoop": 102931, "keysmithKeith": 129384}  # Diccionario de usuarios

# user_ids.get("teraCoder")  # Buscamos el ID de teraCoder

# if user_ids.get("teraCoder") == None:  # Verificamos si teraCoder no existe
#     tc_id = 1000  # Asignamos un ID por defecto
# else:
#     tc_id = user_ids.get("teraCoder")  # Guardamos el ID encontrado

# print(tc_id)  # Mostramos el ID


# if user_ids.get("superStackSmash") == None:  # Verificamos si el usuario no existe
#     stack_id = 100000  # Asignamos un ID por defecto

# print(stack_id)  # Mostramos el ID


################# ELIMINAR UNA CLAVE ####################

# pop() sirve para eliminar un elemento del diccionario usando su clave.

# raffle = {223842: "Teddy Bear", 872921: "Concert Tickets", 320291: "Gift Basket", 412123: "Necklace", 298787: "Pasta Maker"}  # Diccionario de premios

# print(raffle.pop(320291, "No Prize"))  # Eliminamos el premio con la clave 320291
# print(raffle)  # Mostramos el diccionario actualizado

# print(raffle.pop(100000, "No Prize"))  # Si la clave no existe, devuelve No Prize
# print(raffle)  # Mostramos el diccionario

# print(raffle.pop(872921, "No Prize"))  # Eliminamos el premio con la clave 872921
# print(raffle)  # Mostramos el diccionario actualizado


################# EJEMPLO CON POP() ####################

# available_items = {"health potion": 10, "cake of the cure": 5, "green elixir": 20, "strength sandwich": 25, "stamina grains": 15, "power stew": 30}  # Objetos disponibles
# health_points = 20  # Puntos de vida iniciales

# health_points += available_items.pop("stamina grains", 0)  # Sumamos los puntos de stamina grains
# health_points += available_items.pop("power stew", 0)  # Sumamos los puntos de power stew
# health_points += available_items.pop("mystic bread", 0)  # Si no existe, suma 0

# print(available_items)  # Mostramos los objetos restantes
# print(health_points)  # Mostramos los puntos de vida finales


################# OBTENER TODAS LAS CLAVES ####################

# test_scores = {"Grace": [80, 72, 90], "Jeffrey": [88, 68, 81], "Sylvia": [80, 82, 84], "Pedro": [98, 96, 95], "Martin": [78, 80, 78], "Dina": [64, 60, 75]}  # Diccionario con notas

# print(list(test_scores))  # Convertimos las claves en una lista


# for student in test_scores.keys():  # Recorremos todas las claves del diccionario
#     print(student)  # Mostramos el nombre de cada estudiante


################# KEYS() ####################

# user_ids = {"teraCoder": 100019, "pythonGuy": 182921, "samTheJavaMaam": 123112, "lyleLoop": 102931, "keysmithKeith": 129384}  # Diccionario de usuarios
# num_exercises = {"functions": 10, "syntax": 13, "control flow": 15, "loops": 22, "lists": 19, "classes": 18, "dictionaries": 18}  # Diccionario de ejercicios

# users = user_ids.keys()  # Obtenemos todas las claves de user_ids
# lessons = num_exercises.keys()  # Obtenemos todas las claves de num_exercises

# print(users)  # Mostramos las claves de usuarios
# print(lessons)  # Mostramos las claves de ejercicios


################# OBTENER TODOS LOS VALORES ####################

# test_scores = {"Grace": [80, 72, 90], "Jeffrey": [88, 68, 81], "Sylvia": [80, 82, 84], "Pedro": [98, 96, 95], "Martin": [78, 80, 78], "Dina": [64, 60, 75]}  # Diccionario con notas

# for score_list in test_scores.values():  # Recorremos todos los valores
#     print(score_list)  # Mostramos las notas de cada estudiante


# num_exercises = {"functions": 10, "syntax": 13, "control flow": 15, "loops": 22, "lists": 19, "classes": 18, "dictionaries": 18}  # Ejercicios por tema

# total_exercises = 0  # Iniciamos el contador en 0

# for exercises in num_exercises.values():  # Recorremos los valores del diccionario
#     total_exercises += exercises  # Sumamos cada cantidad al total

# print(total_exercises)  # Mostramos el total de ejercicios


################# OBTENER CLAVES Y VALORES ####################

# biggest_brands = {"Apple": 184, "Google": 141.7, "Microsoft": 80, "Coca-Cola": 69.7, "Amazon": 64.8}  # Diccionario con valores de marcas

# for company, value in biggest_brands.items():  # Recorremos claves y valores
#     print(company + " has a value of " + str(value) + " billion dollars.")  # Mostramos cada empresa y su valor


# pct_women_in_occupation = {"CEO": 28, "Engineering Manager": 9, "Pharmacist": 58, "Physician": 40, "Lawyer": 37, "Aerospace Engineer": 9}  # Porcentajes de mujeres por profesión

# for occupation, percentage in pct_women_in_occupation.items():  # Recorremos profesión y porcentaje
#     print("Women make up " + str(percentage) + " percent of " + occupation + "s.")  # Mostramos el porcentaje
