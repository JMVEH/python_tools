import dns.resolver

def main():
    try:
        objetivo = dns.resolver.query("...","NS")
        for x in objetivo:
            print(x)
    except:
        print("No se encontro información")

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        exit()    
