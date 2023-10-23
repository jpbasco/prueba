print("hola mundo")
print("hello world")
cantantes_argentinos=["Carlos Gardel", "Luis Alberto Spinetta","Chaly Garcia","Mercedes Sosa","Soda Stereo","Andres Calamaro","Gustavo Cerati","Fito Paez","Abel Pintos","Patricio Rey y sus Redonditos de Ricota","Lali Esposito","Vicentico","Diego Torres","Tini Stoessel","Luciano Pereyra"]
for cantantes in cantantes_argentinos:
    if "a" in cantantes.lower():
        print(cantantes.upper())
print("#"*50)
for cantantes in cantantes_argentinos:
    if len(cantantes)>14:
        print(cantantes)
print("#"*50)
for cantantes in cantantes_argentinos:
    if cantantes.count("o")>=2:
        print(cantantes)


        