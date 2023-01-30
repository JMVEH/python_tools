from googlesearch import search

o = input("Que necesitas buscar?: ")

for pwd in search(o, num_results=20):
    print(pwd)
