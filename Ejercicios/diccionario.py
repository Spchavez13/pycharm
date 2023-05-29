#Diccionarios

dogs=['Spayky', 'Hunter', 'Loki', 'Astro', 'Sarky', 'Rocky', 'Rocky', 'Toby', 'Rocky',
                  'Chelsea', 'Maple', 'Maya', 'Loki', 'Sparky', 'Toby', 'sparky', 'Dexter', 'Fido', 'Sparky']

# contador_rocky = Mi_diccionario.count('Rocky')
# contador_Sparky = Mi_diccionario.count('Sparky')
# nombres_perros = (set(Mi_diccionario))

# from collections import defaultdic


# print(f"Cantidad de veces que se repite la palabra Rocky:{contador_rocky}")
# print(f"Cantidad de veces que se repite la palabra Sparky:{contador_Sparky}")
# print("Lista de diferentes nombres de perros:")
# print(nombres_perros)

from collections import  defaultdict

dog_dict = defaultdict(int)
for dog in dogs:
    dog_dict[dog]+= 1
print('Rocky', dog_dict['Rocky'])
print('Sparky', dog_dict['Sparky'])
print(list(dog_dict.keys()))


# segudo cambio o comentario

#jfkewjfkjdeqkdjw

