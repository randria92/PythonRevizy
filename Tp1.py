import csv

def open_csv(filename='books.csv'):
    with open(filename, 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        header = next(csv_reader)
        books = []
        # Loop over each row in the CSV file
        for row in csv_reader:
            d = {header[i]: row[i] for i in range(len(header))}
            books.append(d)
    return books

def recherche_titre_auteur(books):
    inpt = input("donnez un titre ou un auteur").lower()
    output = []
    for b in books:
        if inpt in b["auteur"].lower():
            output.append(b)
        elif inpt in b["titre"].lower():
            output.append(b)
    return output


def recherche_genre(books):
    inpt = input("Veuillez saisir un genre :").lower()
    output = []
    for b in books:
        if inpt in b["genre"].lower():
            output.append(b)
    return output

def recherche_annee(books):
    inpt = int(input("Veuillez saisir une annee :"))
    output = []
    for b in books:
        if "BC" in b["annee"]:
            v = "-" + b["annee"].replace("BC","")
            if int(v) > inpt:
                output.append(b)
        elif int(b["annee"]) > inpt:
            output.append(b)
    return output

def recherche_prix(books):
    mini = float(input("Veuillez saisir un prix minimum :"))
    maxi = float(input("Veuillez saisir un prix maximum :"))
    output = []
    if maxi < mini : 
        return recherche_prix(books)
    for b in books:
        if mini <= float(b["prix"]) <= maxi:
            output.append(b)
    return output

def update_quantite(books, filename="books_update.csv"):
    titre = input("Veuillez saisir le titre du livre : ")
    q = input("Veuillez saisir la quantite: ")
    v = False
    with open(filename, 'w', newline='') as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow(list(books[0]))
        for b in books : 
            if titre.lower() == b["titre"].lower():
                b["quantite"] = q
                v  = True
            # Write rows to the CSV file
            csv_writer.writerow([b[i] for i in list(b)])
    if v:
        return "Mise à jour bien effectuer"
    else : 
        return "Le livre n'a pas etait trouver"
    
def add_book(books, filename):
    book = input("Veuillez saisir les informations du livre : ").split(",")
    print(book)
    for b in books:
        if book[0] == b["titre"]:
            return "le livre exsiste deja veuillez mettre à jour la quantité"
        
    with open(filename, 'a', newline='') as csv_file:
        csv_writer = csv.writer(csv_file)

        # Append rows to the CSV file
        csv_writer.writerow(book)


def filtered_books_csv(books, filtered_file="fichier_filtre.csv"):
    
    books_annee_after_two_thousand = recherche_annee(books)
    
    books_less_than_twenty = recherche_prix(books_annee_after_two_thousand)
    
    books_filtered_sorted = sorted(books_less_than_twenty, key=lambda cle:cle['annee'])
    
    with open(filtered_file, 'w', newline='') as csv_file:
        
        csv_writer = csv.writer(csv_file)
        
        header = list(books[0])
        
        csv_writer.writerow(header)
        
        for book in books_filtered_sorted:
            csv_writer.writerow([book[i] for i in list(book)])
            
def library(books_filename):
    label = """
    Veuillez choisir :
    
    a. Rechercher un livre par titre ou par auteur.

    b. Afficher tous les livres d'un certain genre.

    c. Afficher tous les livres publiés après une certaine année.

    d. Afficher tous les livres dont le prix est dans une certaine fourchette.

    e. Mettre à jour la quantité en stock d'un livre.

    f. Ajouter un nouveau livre à l'inventaire (l'utilisateur doit fournir des informations sur le livre).

    g. Créer un fichier "filtered_books.csv" qui contient uniquement les livres publiés après l'an 2000 et dont le prix est inférieur à 20$, trié par année de publication.
    
    """
    x = input(label)
    books = open_csv(books_filename)
    
    if x == 'a':
        return recherche_titre_auteur(books)
        
    elif x == 'b' : 
        return recherche_genre(books)
        
    elif x == 'c' : 
        return recherche_annee(books)
        
    elif x == 'd' : 
        return recherche_prix(books)
        
    elif x == 'e' : 
        return update_quantite(books)
        
    elif x == 'f' : 
        return add_book(books)

    elif x == 'g' : 
        return filtered_books_csv(books)

    else :
        print("Wrong Input, try again : ")
        library(books_filename)