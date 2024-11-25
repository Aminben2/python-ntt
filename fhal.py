class Client:
    def __init__(self,code,nom,address):
        self.__code = code 
        self.__nom = nom 
        self.__address = address
    
    @property
    def code(self):
        return self.__code
    
    @code.setter
    def code(self,p):
        self.__code = p
    
    @property
    def nom(self):
        return self.__nom
    
    @nom.setter
    def nom(self,p):
        self.__nom = p
    
    @property
    def address(self):
        return self.__address
    
    @address.setter
    def address(self,p):
        self.__address = p

    def __str__(self):
        return f"code client : {self.code}, nom client : {self.nom}, address client : {self.address}"
    
    def equals(self,obj):
        return self.nom == obj.nom and self.code == obj.code
    
l = []

def add_client(client):
    check = False 
    for i in l :
        if i.equals(client) : check = True ; break
    if not check :
        l.append(client)
    else :
        print("Client deja exist")

def print_clients():
    if len(l) == 0 : print("There are no client , add some"); return
    for i in range(len(l)) :
        print(f"client {i}: {l[i]}")
    
def delete_client_by_nom(nom):
    tmp = l[:]
    deleted = False
    for i in range(len(tmp)) :
        if tmp[i].nom ==  nom : del l[i];deleted = True
    if deleted : print(f"client with nom {nom} Deleted")
    else : print(f"Failed to delete client with nom {nom}/ does not exists")


def find_client_by_nom(nom):
    check = False 
    for i in l :
        if i.nom ==  nom : print(i);check = True ; break
    if not check : print(f"does not exist a client with nom: {nom}")

def update_client_address_by_nom(nom,add):
    check = False 
    for i in l :
        if i.nom ==  nom :
            i.address = add
            print(i)
            check = True 
            break
    if not check : 
        print(f"does not exist a client with nom: {nom}")

while True :
    print("""1 Ajouter Client
2 Afficher tous les clients
3 Supprimer Client par son nom
4 Rechercher un client par son nom
5 Modifier l’adresse d’un client par son nom.
6 Quitter le programme.\n""")
    try :
        c = int(input("Enter your choice :"))
    except ValueError :
        print("Please a valid option from the list")
    match c:
        case 1 :
            code = input("Enter code plaese :")
            nom = input("Enter nom plaese :")
            ad = input("Enter address plaese :")
            client = Client(code,nom,ad)
            add_client(client)
        case 2 : print_clients()
        case 3 : 
            nom = input("Enter nom plaese :")
            delete_client_by_nom(nom)
        case 4 :
            nom = input("Enter nom plaese :")
            find_client_by_nom(nom)
        case 5 :
            nom = input("Enter nom plaese :")
            ad = input("Enter address plaese :")
            update_client_address_by_nom(nom,ad)
        case 6 :
            ch = input("Are you sure you want to quit? yes/NO : ")
            if ch == "yes": 
                print("Byeeeeee")
                break
    print()



