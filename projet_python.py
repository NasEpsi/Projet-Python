taches_en_cours=[]   #creation of the list of all the undone tasks until now
taches_terminees=[] #creation of the list of all the done tasks 

def ajouter_tache(tache): #function which add the task in the list of the undone tasks
    taches_en_cours.append(tache) #add the new task in the list 
ajouter_tache("devapp")


print(taches_en_cours)
def marquer_comme_terminer(nombre): #function which add a task from the undone task list and move it to the list of the done tasks
    if nombre >= len(taches_en_cours): #if someone press an index bigger than the lengh of the list
        print("l'index est trop grand")
    else:
        taches_terminees.append(taches_en_cours[nombre]) # add the tasks in the done tasks list
        taches_en_cours.pop(nombre) #remove it from the undone tasks

def afficher_taches(taches_en_cours,taches_terminees):      #print both lists
    print (f"Voici la liste des tâches en cours{taches_en_cours} et celle des taches terminees{taches_terminees}")
afficher_taches(taches_en_cours,taches_terminees)


menu=True

print("1. Ajouter une tâche")
print("2. Marquer une tâche comme terminée")
print("3. Afficher les tâches")
print("4. Quitter")

menu=True
while menu: #the menu will always be open if someone doesn't press the touch 4 
    choix = input("Choisissez une option (1-4): ")
    if choix == "1":
        tache = input("Entrez la nouvelle tâche : ")
        ajouter_tache(tache)

    elif choix == "2":
        index= int(input("Entrez la tâche terminée : ")) #int in order to precise its an index and not a string
        marquer_comme_terminer(index)

    elif choix == "3":
        afficher_taches(taches_en_cours,taches_terminees)

    elif choix == "4":
        print("Programme terminé. Au revoir!")
        menu= False
    else:
        print("Choix indisponible") #if someone select an option other that the one submitted








