#import du module pickle pour la sauvegarde et la restitution de variable dans un fichier
import pickle

listContact=[['Mamadou Ndiaye','774016666'],
             ['Khadim Ndiaye','766827592']];
#l'Ouvertuire Avec le mode binaire est tres important dans ce cas
fichier=open("contact","ab")
pickle.dump(listContact, fichier)
fichier.close()
def listeContact():
    fichier=open("contact","rb")
    listContact = pickle.load(fichier)
    if(len(listContact)==0):
       print("==============Liste de contact Vide==============")
    else:
        print(listContact);
    fichier.close()
     
##    for elt in listContact:
##        print(elt);
    menu()
         
def  ajouter():
   #  while len(phone) != 9 :
   #     phone = input("Entrer la valeur correcte du téléphone : ")
   try :
     
      contact=[]
      nom=input("Donnez votre nom : ")
      contact.append(nom);
      phone=int(input("Donnez votre numero de telephone : "))
      contact.append(phone)
      listContact.append(contact);
       
      #Ecrire dans le fichier 
      fichier=open("contact","wb")
      pickle.dump(listContact, fichier)
      fichier.close()
      
      #Au moment de l'ouverture j'ecrasse la variable ensuite je la reajoute dans le fichier
      #Pour que la variable existe une seule fois dans le fichier
      #Sinon la variable listContact existe plus qu'une fois dans le fichier et du coups lors
      #de la lecture il va lire la premiere variable listContact rencontrer
      fichier=open("contact","ab")
      pickle.dump(listContact, fichier)
      
      fichier.close()
      menu()
   except ValueError:
        print("Vous devez donner un nombre ")
        menu()
##    for elt in carnet.keys():
##        if phone == elt:
##              print("le numero existe deja")
##        else:
    #carnet[phone] = "nom"

def rechercher():
    try:
        print("1:Rechercher par nom")
        print("2:Rechercher par numero")
        choice=int(input("Donnez votre choix "))
        if (choice==1):
            nom=input("Donnez le nom: ")
            for contact in listContact:
                if nom in contact:
                    print("le contact existe bien dans la liste")
                    print(contact)
                    break
                else:
                    print("------il n existe pas de numero pour ce nom--------------")
                break
        else:
            number=int(input("Donnez le numero de telephone: "));
            for contact in listContact:
                if number in contact:
                    print("Le numero existe bel et bien")
                    print(contact)
                    break;
                else:
                    print("==================il n y a pas de correspondant nomuro=====================")
                break
        menu()
    except ValueError:
         print("Vous devez dooner un nombre ")


def supprimer():
        if(len(listContact)==0):
          print("Liste de contact Vide")
        else:
            print("======Bienvenue dans le menu de Suppression======");
            print("Voici la liste des contacts")
            index=0
            for elt in listContact:
                print(index, elt)
                index=index+1
            indice=int(input("Entrez la position du contact que vous voulez supprimer: "))
            listContact.pop(indice)
            fichier=open("contact","wb")
            pickle.dump(listContact, fichier)
            fichier.close()
          
            print("======Contact supprime======")
        menu()

def modifier():
        nom=input("Enter le nom du contact que vous souhaiter modiifer: ")
        for contact in listContact:
            if(nom in contact):
                contact.pop(1)
                newNumber=input("Donner le nouveau numero")
                contact.append(newNumber)
                print("Modification effectuer avec succes")

        fichier=open("contact","wb")
        pickle.dump(listContact, fichier)
        fichier.close()
        menu()


def  quitter():
    print("AU REVOIR")
    print("Merci d'avoir essayer a notre application console gestion de contact")

def menu():
      try:
            print("""Bienvenue dans le repertoire telephonique
                1 -> Lister Contact
                2 -> Ajouter Contact
                3 -> Supprimer Contact 
                4 -> Rechercher Contact
                5 -> Modifier Contact
                0 -> Quitter""");
            
            choix=int(input("Entrer votre choix : "))
            if choix == 1:
                 listeContact();
            elif choix ==2 :
                ajouter();    
            elif choix == 3 :
                 supprimer();
            elif choix==4:
                 rechercher()
            elif choix==5:
                 modifier()
            else:
                quitter();
      except ValueError:
            print("Vous devez donner un nombre ")
            menu()

menu();
