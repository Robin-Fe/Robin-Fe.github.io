import os

#turoriel

def tutoriel():
    print("Bonjour et bienvenue dans ''Un voyage au Bord de la Ligne'' !")
    passer=input("(Entrez n'importe quelle touche pour continuer."
                 " Ecrivez ''passer'' pour passer le tutoriel)")
    os.system('cls')
    if passer!="passer" and passer!="Passer" :
        print("''Un voyage au Bord de la Ligne'' est une aventure interactive textuelle dans laquelle vous incarnerez un aventurier enfermé dans un manoir. Pour interragir avec le jeu, vous devrez choisir une des actions qui vous sont proposées et les écrire en minuscules.")
        passer=input("(Entrez n'importe quelle touche pour continuer."
                 " Ecrivez ''passer'' pour passer le tutoriel)")
        os.system('cls')
        if passer!="passer" and passer!="Passer" :
            print("Le jeu présente différentes phases qui sont l'exploration, la résolution d'énigmes et les phases de combat. IL est fortement conseillé, pour ne pas vous perdre, de dessiner sur une feuille de papier un plan du manoir (dans lequel chaque salle est un carré) au fur et à mesure de votre exploration")
            passer=input("(Entrez n'importe quelle touche pour continuer."
                 " Ecrivez ''passer'' pour passer le tutoriel)")
            os.system('cls')
            if passer!="passer" and passer!="Passer" :
                print("Les actions de base de l'exploration sont ''regarder'', ''utiliser'', ''prendre'', ''bouger'' et ''inventaire'', les objets de votre environnement avec lesquels vous pouvez interragir sont écrits en MAJUSCULES, entrez ''inventaire'' pour voir les notes que vous possedez ainsi que les objets utilisables tels que des potions de soin.")
                passer=input("(Entrez n'importe quelle touche pour continuer."
                 " Ecrivez ''passer'' pour passer le tutoriel)")
                os.system('cls')
                if passer!="passer" and passer!="Passer" :
                    print("Les actions de base du combat sont ''attaquer'', ''défendre'', ''fuir'' et le ''repos''. Attaquer vous donne une chance de toucher votre ennemi mais si il se défend il peut vous paralyser pour un tour. Défendre vous permet de tenter de paralyser votre ennemi pour un tour si il vous attaque (défendre vous coûtera un point d'endurance récuperable en vous reposant), et fuir vous donne 1 chance sur 5 de quitter le combat")
                    passer=input("(Entrez n'importe quelle touche pour continuer."
                 " Ecrivez ''passer'' pour passer le tutoriel)")
                    os.system('cls')
                    if passer!="passer" and passer!="Passer" :
                        print("Vos chances de réussir une action sont déterminées par le nombre de points de compétences en attaque pour l'action attaquer et défense pour l'action défendre. Vous avez également des points de vie. Si vos points de vie tombent à 0, vous mourrez et perdrez des points de score (Les points de score ne sont pas indispensables pour réussir le jeu, ce n'est qu'un indicateur de réussite). Pour gagner un combat, vous devrez faire descendre les points de vie de votre adversaire à 0.")
                        passer=input("(Entrez n'importe quelle touche pour continuer."
                 " Ecrivez ''passer'' pour passer le tutoriel)")
                        os.system('cls')

def aidecombat():
    print("Vous êtes au milieu d'un combat, pour gagner, vous devez faire baisser les points de vie de votre adversaire jusqu'a 0")
    passer=input("(Entrez n'importe quelle touche pour continuer."
                 " Ecrivez ''passer'' pour passer le tutoriel)")
    os.system('cls')
    if passer!="passer" and passer!="Passer" :
        print("Pour combattre, vous devrez choisir une des actions qui vous sont proposées : vous pouvez tenter d'attaquer votre adversaire un entrant ''attaquer'', vous défendre en entrant ''défendre'', recuperer des points d'endurance en entrant ''repos'' ou utiliser une carte de banissement ou une potion si vous en possedez une en entrant ''utiliser'' ou tenter de fuir le combat en entrant ''fuir'' ")
        passer=input("(Entrez n'importe quelle touche pour continuer."
                 " Ecrivez ''passer'' pour passer le tutoriel)")
        os.system('cls')
        if passer!="passer" and passer!="Passer" :
            print("Vos chances de réussir une action dépendant de vos caractéristiques : l'attaque influence la chance de réussir une attaque et le nombre de points de vie que vous retirerez à votre adversdaire en cas de réussite et la défense influence la chance de réussir une défense et de paralyser votre ennemi pendant un tour de jeu.")
            passer=input("(Entrez n'importe quelle touche pour continuer."
                 " Ecrivez ''passer'' pour passer le tutoriel)")
            os.system('cls')
            if passer!="passer" and passer!="Passer" :
                print("Vous avez 1 chance sur 5 de réussir à fuir, vous recupererez forcément un point d'endurance en vous reposant")
                passer=input("(Entrez n'importe quelle touche pour continuer."
                 " Ecrivez ''passer'' pour passer le tutoriel)")
                os.system('cls')
                if passer!="passer" and passer!="Passer" :
                    print("Attention ! Si vous attaquez un adversaire et qu'il réussit se défend, vous serez paralysé au tour suivant ! Mais une défense (réussie ou non) vous coûtera un point d'endurance.")
                    passer=input("Entrez n'importe quelle touche pour continuer")
                    os.system('cls')
                    
def aideexploration():
    print("Vous êtes dans une des salles du manoir, votre but en tant que joueur est de réussir à quitter le manoir ! Plusieurs actions vous sont possibles : vous pouvez tenter d'observer les objets avec lesquels vous pouvez agir (écrits en MAJUSCULES) en entrant ''regarder'', utiliser un des objets que vous possedez ou un objet que vous avez remarqué dans la pièce en entrant ''utiliser'', récuperér un objet que vous avez vu (comme une potion ou un objet de quête) en entrant ''prendre'', vous pouvez également changer de salle en entrant ''bouger'', pour les actions utiliser et prendre, il vous sera demandé de préciser ensuite ce que vous voulez utiliser ou prendre, pour cela lisez bien les descriptions qui vous sont faites quand vous observez une salle et reperez les objets avec lesquels vous pouvez interragir(écrits en MAJUSCULES). Vous pouvez entrer ''inventaire'' pour voir les notes que vous possedez ainsi que les objets utilisables tels que des potions de soin.")
    passer=input("Entrez n'importe quelle touche pour continuer")
    os.system('cls')
                        
from random import*
def dé_n(n):
    global résultatdé
    résultatdé=randrange(1,n+1)
    return résultatdé

def combat(attaque, vie, defense, vieennemi, attaqueennemi, defenseennemi, potion, carte):
    endurance=4
    fincombat=0
    n=0
    fuite=0
    etat=0
    etatennemi=0
    global potion1
    global carte1
    global vie1
    global issue
    carte1=carte
    potion1=potion
    issue=0
    vie1=vie
    while (fincombat<1):
        print ("  ")
        print ("Vos caractéristiques :  Attaque :", attaque, "      Vie : ", vie1, "        Défense : ", defense,"       Endurance : ", endurance)
        print ("  ")
        print ("Caractéristiques de votre adversaire :   Attaque :", attaqueennemi, "      Vie : ", vieennemi, "        Défense : ", defenseennemi)
        print ("  ")
        dé_n(10)
        if résultatdé<=6:
            actionennemi=1
        else :
            actionennemi=2
        if etat>0:
            actionennemi=1
        if etatennemi>=1:
            print("Votre adversaire est destabilisé et ne peux ni attaquer ni se défendre")
        if etatennemi==0:
            if actionennemi==1:
                print ("Votre adversaire se prépare à vous attaquer !")
                dé_n(100)
                if résultatdé>=60+attaqueennemi*5:
                    actionennemi=4
            if actionennemi==2:
                print ("Votre adversaire se prépare à défendre")
                dé_n(100)
                if résultatdé>=60+attaqueennemi*5:
                    actionennemi=5                
        if etat==0:
            if n>0:
                print ("Veuillez choisir une action valide")
            action=input("Voulez vous attaquer, défendre, fuir, vous reposer ou utiliser un objet de votre inventaire ?")
            os.system('cls')
            if action=="utiliser" or action=="Utiliser":
                print("Vous possedez ", potion1," potions de soin, ")
                if carte1==1:
                    print("Vous possedez une carte de bannissement") 
                action=input("Que voulez vous utiliser ?")
                if action=="potion" or action=="Potion":
                    if potion1>0:
                        vie1=viemax
                        potion1=potion1-1
                    else : print("Vous n'avez pas de potion à utiliser")
                if action=="carte" or action=="Carte":
                    if carte1>0:
                        vieennemi=0
                        carte1=carte1-1
                    else : print("Vous n'avez pas de carte à utiliser")
            if action=="aide" or action=="Aide":
                aidecombat()
            if action!="attaquer" and action!="Attaquer" and action!="defendre" and action!="défendre" and action!="Défendre" and action!="Defendre" and action!="fuir" and action!="Fuir" and action!="Repos" and action!="repos":
                actionennemi=3
                n=1
            if action=="attaquer" or action=="Attaquer":
                dé_n(100)
                if résultatdé<=55+attaque*5:
                    if actionennemi==1:
                        vieennemi=vieennemi-2*attaque
                        print ("Vous portez un coup à votre adversaire et lui infligez ", 2*attaque," points de dégat !")
                    if actionennemi==2 :
                        if etatennemi==0:
                            print ("Vous portez un coup à votre adversaire ... Mais il pare le coup et vous déstabilise !")
                            etat=2
                        else :
                            vieennemi=vieennemi-2*attaque
                            print ("Vous portez un coup à votre adversaire et lui infligez ", 2*attaque," points de dégat !")
                else : print ("Vous manquez de toucher votre adversaire et êtes vulnérable")
                n=0
                
            if action=="defendre" or action=="défendre" or action=="Défendre" or action=="Defendre":
                if endurance>0:
                    dé_n(100)
                    endurance=endurance-1
                    if résultatdé<=45+defense*8:
                        if actionennemi==1:
                            dé_n(100)
                            if résultatdé<=10+defense*8:
                                print ("Vous parrez le coup de votre adversaire et le destabilisez !")
                                etatennemi=2
                            else: print ("Vous parrez le coup de votre adversaire")
                        if actionennemi==2:
                            print ("Vous et votre adversaire vous jaugez ...  ")
                    else :
                        if actionennemi==1:
                            print ("Vous tentez de parrer le coup de votre adversaire ... mais flechissez sous le coup : il vous inflige ", attaqueennemi-2," points de dégat")
                            vie1=vie1-attaqueennemi+2
                        if actionennemi==2:
                            print ("Vous et votre adversaire vous jaugez ...  ")
                    n=0
                else:
                    print("Vous n'avez pas assez d'endurance")
                    actionennemi=3
                    
            if action=="fuir" or action=="Fuir":
                dé_n(10)
                if résultatdé<=2:
                    fuite=1
                n=0
                
            if action=="repos" or action=="Repos":
                if endurance<4:
                    print ("Vous reprennez des forces")
                    endurance=endurance+1
                else:
                    print ("Votre endurance est déjà maximale !")
                    actionennemi=3
                    
        if etatennemi==0:
            if actionennemi==1:
                if action!="defendre" and  action!="défendre" and action!="Défendre" and action!="Defendre":
                    vie1=vie1-attaqueennemi
                    print ("Votre adversaire vous attaque et vous inflige ", attaqueennemi," points de dégat !")
        if actionennemi==4:
            print ("Votre adversaire ne parvient pas à vous attaquer")
        if actionennemi==5:
            print ("Votre adversaire échoue dans sa défense")
            
        if etat>0:
            etat=etat-1
        if etatennemi>0:
            etatennemi=etatennemi-1
        if vie1*vieennemi<=0 or fuite==1:
            fincombat=1
        if vieennemi<=0 :
            issue=1
        if fuite==1 :
            issue=2
        if vie1<=0 :
            issue=3
    return vie1, issue, potion1, carte1
issue=0
vie1=0
def creationpersonnage():
    ok=0
    while (ok!=1):
        global nom
        nom=input("Quel est votre nom, aventurier ? Votre nom : ")  
        os.system('cls')
        xp=-1
        n=0
        global attaquemax
        global defensemax
        global viemax
        attaquemax=1
        defensemax=1
        viemax=10
        while (xp<0):
            os.system('cls')
            print ("Bienvenue",nom)
            if n>0:
                os.system('cls')
                print ("Veuillez entrer une valeur entre 0 et 10")
            xp=10
            print ("Vous avez 10 points à répartir. Quels sont vos talents ?")
            print ("Attaque :", attaquemax, "      Vie : ", viemax, "        Défense : ", defensemax)
            attaque1=int(input("Points à ajouter en attaque :"))
            xp=xp-attaque1
            n=n+1
        n=0
        xp1=xp
        attaquemax=attaque1+attaquemax
        os.system('cls')
        if xp!=0:
            xp=-1
            while (xp<0):
                if n>0:
                    os.system('cls')
                    print ("Veuillez entrer une valeur entre 0 et ",10-attaque1)
                print ("Vous avez ", xp1, " points à répartir. Quels sont vos talents ?")
                print ("Attaque :", attaquemax, "      Vie : ", viemax, "        Défense : ", defensemax)
                xp=xp1
                defense1=int(input("Points à ajouter en défense :"))
                xp=xp-defense1
                n=n+1
            defensemax=defense1+defensemax        
            xp1=xp

            viemax=xp*10+viemax
        os.system('cls')
        print ("Vous êtes ",nom,"l'aventurier, vos caractéristiques sont :")
        print ("Attaque :", attaquemax, "      Vie : ", viemax, "        Défense : ", defensemax)
        accord=input("Cela vous convient-il ? Oui/Non")
        if accord=="Oui":
            ok=1
        else :
            if accord=="oui":
                ok=1
        os.system('cls')
    return viemax, attaquemax, defensemax, nom

#montée de niveau
def niveauup(attaque,defense,viemax):
    ok=0
    while (ok!=1):  
        n=0
        global attaque1
        global defense1
        global vie1
        attaque1=attaque
        defense1=defense
        vie1=viemax
        xp=1
        oui=input("Entrez n'importe quelle touche pour continuer")
        while (xp>0):
            os.system('cls')
            print ("Félicitations ",nom1," ! Vous venez de monter en niveau et pouvez ajouter un point de compétence à vos caractéristiques :")
            if n>0:
                os.system('cls')
                print ("Veuillez choisir une réponse valide : Attaque, Défense ou Vie")
            print ("Attaque :", attaque1, "      Vie : ", vie1, "        Défense : ", defense1)
            action=input("Vous avez 1 point à ajouter à l'une de vos compétences, à quelle compétence voulez vous l'appliquer ?")
            if action!="attaque" and action!="Attaque" and action!="defense" and action!="défense" and action!="Défense" and action!="Defense" and action!="Vie" and action!="vie":
                n=1
            if action=="attaque" or action=="Attaque":
                n=0
                xp=0
                attaque1=attaque1+1
            if action=="defense" or action=="défense" or action=="Défense" or action=="Defense" :
                n=0
                xp=0
                defense1=defense1+1
            if action=="vie" or action=="Vie":
                n=0
                xp=0
                vie1=vie1+10
        os.system('cls')
        print ("Vos caractéristiques sont :")
        print ("Attaque :", attaque1, "      Vie : ", vie1, "        Défense : ", defense1)
        accord=input("Cela vous convient-il ? Oui/Non")
        if accord=="Oui":
            ok=1
        else :
            if accord=="oui":
                ok=1
        os.system('cls')
    return vie1, attaque1, defense1

#initialisation des variables

statue=0
score=0
potion=0
findujeu=0
clef=0
objets=0
coffre1=0
coffre2=0
gant=0
porte11=0
osalle12=0
osalle13=0
osalle14=0
osalle15=0
osalle16=0
osalle17=0
osalle18=0
clefrdc=0
potion=0
carte=0
blocage1=0
tableau=0
findujeu=0
salle=11
objet=0
enigme1=0
score=0
gant=0
vampire=0
rideau=0
tutoriel()
creationpersonnage()
nom1=nom
attaque=attaquemax
vie=viemax
vie1=viemax
defense=defensemax
gain=0
grosmonstre=1
issue=0
coffre18=0
potion11=0
#notes
note=0
note1=0
note2=0
note3=0
note4=0
note5=0

textenote1="La note dit : 'Le manoir est un désordre sans nom ... Où aie-je bien pu mettre le gant de la statue du rez de chaussée ? La dernière fois que je l'ai vu c'était à l'étage, mais impossible de remettre la main dessus ...'"
textenote2="La note dans le carnet ensanglanté disait''Je n'en peux plus ... Ce n'est pas moi ... Je ne peux plus supproter ce que je leur fait endurer ... J'aurais aimé ne jamais arriver ici...''"  
textenote3="L'inscription mystérieuse derrière le tableau disait : ''Tout commence au PONANT et finit à l'ORIENT, celui du SUD précède celui de l'EST''"
textenote4=("''Jouer au bord de la ligne est un jeu dangereux,"
"Docteur Palmers, de son patient devrait être méfiant,"
"Même si ce n'est qu'un pauvre malheureux,"
"Le loup pourrait un jour montrer les dents ...''")
textenote5="''Les riches en manquent, les pauvres en ont et si tu en manges tu meurs...Que suis-je ? ''"
#début de l'aventure

while findujeu==0:

#SALLE 11 ; Début de l'aventure.---------------------------------------------------------------------------------------------------------------------------------------------------------------------    
    
    if salle==11:
        changersalle=0
        if osalle12==0:
            print ("Vous ouvrez les yeux et vous vous levez péniblement, vous vous rendez compte que vous êtes dans une petite pièce sombre, sans fenêtre.")
        if osalle12==1:
            print("Vous êtes dans la salle dans laquelle vous vous êtes réveillé.")

              
    while changersalle==0:   
        action=input("Que voulez vous faire ? ")
        if action!="bouger" and action!="Bouger" and action!="regarder" and action!="Regarder" and action!="utiliser" and action!="Utiliser" and action!="prendre" and action!="Prendre" and action!="Inventaire" and action!="inventaire":
            print("Veuillez entrer une action valide. (Rappel: 'Regarder', 'Bouger', 'Utiliser','Prendre')")

        if action=="aide" or action=="Aide":
                aideexploration()
                    
  #bouger Est, porte dévérouiller ou pas
        if porte11==0:
            if action=="bouger" or action=="Bouger":
                action=input("Une seule porte mène à l'Est du Manoir, où souhaitez vous aller ? ('Nord', 'Sud', 'Est', 'Ouest') ")
                if action!="Est" and action!="est":
                    print("Vous ne pouvez aller qu'à l'Est")
                else:
                    if clef==0:
                        print("La porte est verrouillée , vous devriez chercher une clef dans la salle.")
                    else:
                        print("La porte est toujours verrouillée...")
                      
        if osalle12==1:
                porte11=1

        if porte11==1:
            if action=="bouger" or action=="Bouger":
                action=input("Une seule porte mène à l'Est du Manoir, où souhaitez vous aller ? ('Nord', 'Sud', 'Est', 'Ouest') ")
                if action!="Est" and action!="est":
                    print("Vous ne pouvez aller qu'à l'Est")
                if action=="Est" or "est":
                    print("La porte est déjà dévérouillée, vous changez de salle")
                    osalle12=1
                    changersalle=1
                    salle=12
                    os.system('cls')
            
           
  #regarder
                                  
        if action=="regarder" or action=="Regarder":
            if clef==1 and potion==0:
                print("Le COFFRE est derrière vous, mais il semble qu'il reste toujours quelque chose dedans, cela ressemblait à une POTION.")
                
            if clef==0 and potion==1:
                print("Le COFFRE est derrière, mais quelque brille toujours au fond, c'est une CLEF!")

            if coffre1==1:
                print("Le coffre est toujours derrière vous.")
            if clef==0 and potion==0:
                print("Vous remarquez la présence d'un COFFRE derrière vous. Vous trouvez dans le coffre quelques débris, mais quelque chose brille au fond...C'est une CLEF !Il y a également une POTION de vie.")

   #utiliser des objets
                        
        if 1==1:
            if action=="utiliser" or action=="Utiliser":
                action=input("Que souhaitez-vous utiliser ? ")
                if action=="clef" or action=="clé" or action=="cle":
                    if osalle12==0:
                        if clef==1:
                            print ("Vous avez dévérouillé la porte !")
                            porte11=1
                        else:
                            print("Vous n'avez pas cet objet en votre possession.")
                    else:
                        print("La porte est déjà dévérouillée.")
                        changersalle=1
                        salle=12
                        porte11=1

                        
                if action=="potion" or action=="Potion":
                    if potion>=1:
                        potion=potion-1
                        vie=viemax
                        print("Vous avez utilisé une potion de vie")
                    else:
                        print("Vous n'avez pas cet objet dans votre inventaire")
            
            
    #prendre des objets
                        
        if action=="prendre" or action=="Prendre":
            action=input("Que souhaitez vous prendre ? ")
            
            if action=="clef" or action=="cle" or action=="clé" or action=="Clef" or action=="Cle" or action=="Clé":
                if clef==0:
                    print("Vous avez pris la clef de la salle se situant dans un coffre !")
                    clef=clef+1
                    objets=objets+1
                else:
                    print("Vous avez déjà pris la clef ici")
                    
            if action=="potion" or action=="Potion":
                if potion11==0:
                    potion11=1
                    print("Vous avez pris une potion.")
                    potion=potion+1
                    objets=objets+1
                else:
                    print("Vous avez déjà pris la potion ici")

                    
            if clef==1 and potion11==1:
                coffre1=1
                
        if action=="Prendre" or action=="prendre":
            if coffre==1:
                print("Il n'y a rien à prendre par içi")


                
 #Inventaire
                        
        if action=="inventaire" or action=="Inventaire":
            print("Vous posséder les objets suivants :")
            if potion>=1:
                print(potion, "potion(s) de soin")
            if carte>=1:
                print(carte, "Cartes de bannissement")
            if note1==1:
                print("Note1 (la note sur l'état du manoir)")
            if note2==1:
                print("Note2 (la note du carnet ensanglanté)")
            if tableau==1:
                print("Note3 (la note écrite dérière le tableau)")
            if note4==1:
                print("Note4")
            if note5==1:
                print("Note5")
            if clefrdc==1:
                print("La clef du rez de chaussée")
            if gant==1:
                print("Un gant")
                    
            action=input("Que souhaitez-vous utiliser ? ")
                
            if action=="potion" or action=="Potion":
                if potion>0:
                    vie=viemax
                    potion=potion-1
                else : print("Vous n'avez pas de potion à utiliser")
            if action=="note1" or action=="Note1":
                if note1==1:
                    print(textenote1)
            if action=="note2" or action=="Note2":
                if note2==1:
                    print(textenote2)
            if action=="note3" or action=="Note3":
                if note3==1:
                    print(textenote3)
            if action=="note4" or action=="Note4":
                if note4==1:
                    print(textenote4)
            if action=="note5" or action=="Note5":
                if note5==1:
                    print(textenote5)
            if action!="note1" and action!="Note1" and action!="note2" and action!="Note2" and action!="note3" and action!="Note3" and action!="note4" and action!="Note4" and action!="note5" and action!="Note5" and action!="potion" and action!="Potion":
                print("Vous ne pouvez pas utiliser cet objet ici")
                                                                   
        
#SALLE 12 --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
            
    if salle==12:
        changersalle=0
        osalle12=1
        porte11=1
        print ("Vous arrivez dans une petite salle mal rangée, qui semble vide. Deux portes sont présentes, celle dont vous venez, à l'Ouest, et une autre au Sud.")
        dé_n(10)
        if résultatdé<=6:
            dé_n(10)
            if résultatdé<=3:
                print("Vous entendez des claquements d'os dans la pièce...")
                print("Un squelette animé par une sorte d'aura maléfique se jette sur vous ! Vous sortez votre épée et vous appretez à vous battre")
                combat(attaque, vie, defense, 20, 3, 4, potion, carte)
            else :
                print("Des bruits de métal vous parviennent...")
                print("Une armure s'anime et commence à s'approcher de vous ! Vous sortez votre épée et vous appretez à vous battre")
                combat(attaque, vie, defense, 30, 4, 6, potion, carte)
            vie=vie1
            potion=potion1
            carte=carte1
            if issue==1:
                print ("Vous venez à bout de votre adversdaire")
                gain=gain+1
                if gain>1:
                    niveauup(attaque,defense,viemax)
                    gain=0
            if issue==2:
                print ("Vous fuyez le combat")
            if issue==3:
                print ("Vous tombez au combat ... Vous vous reveillez un peu plus tard en piteux état, votre ennemi a disparu...")
                score=score-1
                vie1=viemax/2
            vie=vie1
            
 #Bouger         

        while changersalle==0:
            
            action=input("Que voulez vous faire ? ")
            if action!="bouger" and action!="Bouger" and action!="regarder" and action!="Regarder" and action!="utiliser" and action!="Utiliser" and action!="prendre" and action!="Prendre" and action!="Inventaire" and action!="inventaire":
                print("Veuillez entrer une action valide. (Rappel: 'Regarder', 'Bouger', 'Utiliser','Prendre')")   
            if action=="aide" or action=="Aide":
                aideexploration()
            if action=="bouger":
                action=input("Où souhaitez vous aller ? ")
                if action!="Sud" and action!="sud" and action!="Ouest" and action!="ouest":
                    print("Vous ne pouvez aller qu'à l'Ouest ou au Sud")
                if action=="Sud" or action=="sud":
                    changersalle=1
                    salle=13
                    os.system('cls')
                if action=="Ouest" or action=="ouest":
                    changersalle=1                    
                    salle=11
                    os.system('cls')
     #prendre
                        
            if action=="Prendre" or action=="prendre":
                print("Il n'y a rien à prendre par içi")
     #Regarder
                        
            
            if action=="Regarder" or action=="regarder":
                if note==0:
                    print("Vous remarquez sur une étagère la présence d'une NOTE, vous décidez de vous en approchez et de la lire : 'Cher journal, les travaux du manoir ont enfin été terminés, il ne manque plus qu'à ranger toutes les affaires et meubles que j'ai apporté.Cependant pendant le déménagement, j'ai perdu le gant de la main de ma statue.Il me semble que quelqu'un l'a rangé à l'armurerie, à l'étage'. Vous décidez de garder la note sur vous, cela pourra surement vous être utile plus tard.")
                    objets=objets+1
                    note=note+1
                    note1=1
                    score=score+1
                else:
                    print("Il n'y plus rien à regarder içi, la NOTE est dans votre poche")
                        
     #Utiliser

            if action=="utiliser" or action=="Utiliser":
                print("Vous possedez ", potion," potions de soin, ")
                if tableau==1:
                      print("Vous avez noté l'inscription derière le tableau") 
                action=input("Que voulez vous utiliser ?")
                if action=="potion" or action=="Potion":
                    if potion>0:
                        vie=viemax
                        potion=potion-1
                    else : print("Vous n'avez pas de potion à utiliser")
                if action=="tableau" or action=="Tableau":
                    if tableau==1:
                        print("L'inscription mystérieuse derrière le tableau disait : ''Tout commence au PONANT et finit à l'ORIENT, celui du SUD précède celui de l'EST''")  
            

#Inventaire
                        
            if action=="inventaire" or action=="Inventaire":
                print("Vous posséder les objets suivants :")
                if potion>=1:
                    print(potion, "potion(s) de soin")
                if carte>=1:
                    print(carte, "Cartes de bannissement")
                if note1==1:
                    print("Note1 (la note sur l'état du manoir)")
                if note2==1:
                    print("Note2 (la note du carnet ensanglanté)")
                if tableau==1:
                    print("Note3 (la note écrite dérière le tableau)")
                if note4==1:
                    print("Note4")
                if note5==1:
                    print("Note5")
                if clefrdc==1:
                    print("La clef du rez de chaussée")
                if gant==1:
                    print("Un gant")
                    
                action=input("Que souhaitez-vous utiliser ? ")
                
                if action=="potion" or action=="Potion":
                    if potion>0:
                        vie=viemax
                        potion=potion-1
                    else : print("Vous n'avez pas de potion à utiliser")
                if action=="note1" or action=="Note1":
                    if note1==1:
                        print(textenote1)
                if action=="note2" or action=="Note2":
                    if note2==1:
                        print(textenote2)
                if action=="note3" or action=="Note3":
                    if note3==1:
                        print(textenote3)
                if action=="note4" or action=="Note4":
                    if note4==1:
                        print(textenote4)
                if action=="note5" or action=="Note5":
                    if note5==1:
                        print(textenote5)
                if action!="note1" and action!="Note1" and action!="note2" and action!="Note2" and action!="note3" and action!="Note3" and action!="note4" and action!="Note4" and action!="note5" and action!="Note5" and action!="potion" and action!="Potion":
                    print("Vous ne pouvez pas utiliser cet objet ici")


                   
#SALLE 13----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------            

    if salle==13:
        changersalle=0
        osalle13=1
        print ("Vous arrivez dans la salle principale du Rez de Chaussé. C'est un ancien salon délabré, et un escalier mène à l'étage. Il y a 4 portes pour chaques points cardinaux.")
        dé_n(10)
        if résultatdé<=6:
            dé_n(10)
            if résultatdé<=3:
                print("Vous entendez des claquements d'os dans la pièce...")
                print("Un squelette animé par une sorte d'aura maléfique se jette sur vous ! Vous sortez votre épée et vous appretez à vous battre")
                combat(attaque, vie, defense, 20, 3, 4, potion, carte)
            else :
                print("Des bruits de métal vous parviennent...")
                print("Une armure s'anime et commence à s'approcher de vous ! Vous sortez votre épée et vous appretez à vous battre")
                combat(attaque, vie, defense, 30, 4, 6, potion, carte)
            vie=vie1
            potion=potion1
            carte=carte1
            if issue==1:
                print ("Vous venez à bout de votre adversdaire")
                gain=gain+1
                if gain>1:
                    niveauup(attaque,defense,viemax)
                    gain=0
            if issue==2:
                print ("Vous fuyez le combat")
            if issue==3:
                print ("Vous tombez au combat ... Vous vous reveillez un peu plus tard, votre ennemi a disparu...")
                score=score-1
                vie1=viemax/2
            vie=vie1

        
 #Bouger         

        while changersalle==0:

            action=input("Que voulez vous faire ? ")
            if action!="bouger" and action!="Bouger" and action!="regarder" and action!="Regarder" and action!="utiliser" and action!="Utiliser" and action!="prendre" and action!="Prendre" and action!="Inventaire" and action!="inventaire":
                print("Veuillez entrer une action valide. (Rappel: 'Regarder', 'Bouger', 'Utiliser','Prendre')")   
            if action=="aide" or action=="Aide":
                aideexploration()
            if action=="bouger" or action=="Bouger" :
                action=input("Où souhaitez vous aller ?")            
                if action=="Ouest" or action=="ouest":
                    changersalle=1                    
                    salle=14
                    os.system('cls')
                
                if action=="Est" or action=="est":
                    changersalle=1                    
                    salle=15
                    os.system('cls')
                    
                if action=="Sud" or action=="sud":
                    changersalle=1                    
                    salle=17
                    os.system('cls')
                    
                if action=="Nord" or action=="nord":
                    changersalle=1                    
                    salle=12
                    os.system('cls')
                    
                if action=="monter" or action=="Monter":
                    changersalle=1                    
                    salle=21
                    os.system('cls')

    #regarder
            if action=="regarder":
                print("Vous voyez une grande table de banquet qui occupe une bonne partie de la pièce. Tout en haut d'une étagère vous remarquez un OBJET légèrement brillant, sans parvenir à definir sa nature ...")

    #Utiliser

            if action=="utiliser" or action=="Utiliser":
                print("Vous possedez ", potion," potions de soin, ")
                if tableau==1:
                      print("Vous avez noté l'inscription derière le tableau") 
                action=input("Que voulez vous utiliser ?")
                if action=="potion" or action=="Potion":
                    if potion>0:
                        vie=viemax
                        potion=potion-1
                    else : print("Vous n'avez pas de potion à utiliser")
                if action=="tableau" or action=="Tableau":
                    if tableau==1:
                        print("L'inscription mystérieuse derrière le tableau disait : ''Tout commence au PONANT et finit à l'ORIENT, celui du SUD précède celui de l'EST''")  
            
                if action=="objet" or action=="Objet" or action=="objet brillant" or action=="Objet brillant" or action=="étagère" or action=="Etagère" or action=="Etagere" or action=="étagere":
                    if vie>=2:
                        vie=vie-1
                    score=score-1
                    print ("Vous passez votre main sur l'étagère pour récupérer l'objet brillant, vous sentez une vive douleur et voyez un filet de sang couler le long de votre bras, l'objet en question était une lame de dague. Vous perdez un point de vie et vous sentez un peu honteux ...")

    #Inventaire
                        
            if action=="inventaire" or action=="Inventaire":
                print("Vous posséder les objets suivants :")
                if potion>=1:
                    print(potion, "potion(s) de soin")
                if carte>=1:
                    print(carte, "Cartes de bannissement")
                if note1==1:
                    print("Note1 (la note sur l'état du manoir)")
                if note2==1:
                    print("Note2 (la note du carnet ensanglanté)")
                if tableau==1:
                    print("Note3 (la note écrite dérière le tableau)")
                if note4==1:
                    print("Note4")
                if note5==1:
                    print("Note5")
                if clefrdc==1:
                    print("La clef du rez de chaussée")
                if gant==1:
                    print("Un gant")
                    
                action=input("Que souhaitez-vous utiliser ? ")
                
                if action=="potion" or action=="Potion":
                    if potion>0:
                        vie=viemax
                        potion=potion-1
                    else : print("Vous n'avez pas de potion à utiliser")
                if action=="note1" or action=="Note1":
                    if note1==1:
                        print(textenote1)
                if action=="note2" or action=="Note2":
                    if note2==1:
                        print(textenote2)
                if action=="note3" or action=="Note3":
                    if note3==1:
                        print(textenote3)
                if action=="note4" or action=="Note4":
                    if note4==1:
                        print(textenote4)
                if action=="note5" or action=="Note5":
                    if note5==1:
                        print(textenote5)
                if action!="note1" and action!="Note1" and action!="note2" and action!="Note2" and action!="note3" and action!="Note3" and action!="note4" and action!="Note4" and action!="note5" and action!="Note5" and action!="potion" and action!="Potion":
                    print("Vous ne pouvez pas utiliser cet objet ici")


#SALLE 15----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

    if salle==15:
        if osalle15==0:
            changersalle=0
            osalle15=1
            print("Vous arrivez dans une salle comportant 2 statues gardant une porte donnant vers le Nord.")
        if osalle15==1:
            changersalle=0
            if statue==1:
                print("Vous êtes dans la salle avec les 2 statues, la porte donnant vers le Nord est toujours ouverte")
        dé_n(10)
        if résultatdé<=6:
            dé_n(10)
            if résultatdé<=3:
                print("Vous entendez des claquements d'os dans la pièce...")
                print("Un squelette animé par une sorte d'aura maléfique se jette sur vous ! Vous sortez votre épée et vous appretez à vous battre")
                combat(attaque, vie, defense, 20, 3, 4, potion, carte)
            else :
                print("Des bruits de métal vous parviennent...")
                print("Une armure s'anime et commence à s'approcher de vous ! Vous sortez votre épée et vous appretez à vous battre")
                combat(attaque, vie, defense, 30, 4, 6, potion, carte)
            vie=vie1
            potion=potion1
            carte=carte1
            if issue==1:
                print ("Vous venez à bout de votre adversdaire")
                gain=gain+1
                if gain>1:
                    niveauup(attaque,defense,viemax)
                    gain=0
            if issue==2:
                print ("Vous fuyez le combat")
            if issue==3:
                print ("Vous tombez au combat ... Vous vous reveillez un peu plus tard, votre ennemi a disparu...")
                score=score-1
                vie1=viemax/2
            vie=vie1      
#Bouger

        while changersalle==0:
            action=input("Que voulez vous faire ? ")
            if action=="aide" or action=="Aide":
                aideexploration()
            if action=="bouger" or action=="Bouger" :
                action=input("Où souhaitez vous aller ? ")            
                if action=="Ouest" or action=="ouest":
                    changersalle=1                    
                    salle=13
                    os.system('cls')
                
                if action=="Est" or action=="est":
                    print("Il n'y a rien à l'Est")
                    
                if action=="Sud" or action=="sud":
                    print("Il n'y a rien au Sud")
                    
                if action=="Nord" or action=="nord":
                    if statue==0:
                        print("La porte est bloquée.")
                    if statue==1:
                        salle=19
                        changersalle=1
                        os.system('cls')
                   
                
#regarder
            if action=="regarder":
                print("Les deux statues ont l'air symétriques. Pourtant, vous remarquez que quelque chose ne va pas, une des statues présente un défaut à LA MAIN, comme si il manquait une partie..")

#utiliser
    
            if action=="utiliser" or action=="Utiliser":
                print("Vous possedez ", potion," potions de soin, ")
                if tableau==1:
                    print("Vous avez noté l'inscription derière le tableau") 

                action=input("Que souhaitez vous utiliser ? ")
                if action!="gant":
                    print("Vous n'avez pas cet objet ou l'objet ne va pas sur la statue")
                if action=="gant" or action=="Gant" or action=="Gant de mailles" or action=="gant de mailles" or action=="Gant de maille" or action=="gant de maille":
                    if gant==0:
                        print("Vous n'avez pas cet objet")
                    if gant==1:
                        print("Vous posez le gant sur la main de la statue, la porte qu'elles gardaient s'ouvre pour vous laissez l'accès à la salle suivant")
                        statue=1
                        gant=gant-1
                        score=score+1
                if action=="potion" or action=="Potion":
                    if potion>0:
                        vie=viemax
                        potion=potion-1
                    else : print("Vous n'avez pas de potion à utiliser")
                        
                if action=="tableau" or action=="Tableau":
                    if tableau==1:
                        print("L'inscription mystérieuse derrière le tableau disait : ''Tout commence au PONANT et finit à l'ORIENT, celui du SUD précède celui de l'EST''")  
            
#Inventaire
                        
            if action=="inventaire" or action=="Inventaire":
                print("Vous posséder les objets suivants :")
                if potion>=1:
                    print(potion, "potion(s) de soin")
                if carte>=1:
                    print(carte, "Cartes de bannissement")
                if note1==1:
                    print("Note1 (la note sur l'état du manoir)")
                if note2==1:
                    print("Note2 (la note du carnet ensanglanté)")
                if tableau==1:
                    print("Note3 (la note écrite dérière le tableau)")
                if note4==1:
                    print("Note4")
                if note5==1:
                    print("Note5")
                if clefrdc==1:
                    print("La clef du rez de chaussée")
                if gant==1:
                    print("Un gant")
                    
                action=input("Que souhaitez-vous utiliser ? ")
                
                if action=="potion" or action=="Potion":
                    if potion>0:
                        vie=viemax
                        potion=potion-1
                    else : print("Vous n'avez pas de potion à utiliser")
                if action=="note1" or action=="Note1":
                    if note1==1:
                        print(textenote1)
                if action=="note2" or action=="Note2":
                    if note2==1:
                        print(textenote2)
                if action=="note3" or action=="Note3":
                    if note3==1:
                        print(textenote3)
                if action=="note4" or action=="Note4":
                    if note4==1:
                        print(textenote4)
                if action=="note5" or action=="Note5":
                    if note5==1:
                        print(textenote5)
                if action!="note1" and action!="Note1" and action!="note2" and action!="Note2" and action!="note3" and action!="Note3" and action!="note4" and action!="Note4" and action!="note5" and action!="Note5" and action!="potion" and action!="Potion":
                    print("Vous ne pouvez pas utiliser cet objet ici")



#SALLE 19----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

            if salle==19:
                if 1==1:
                    changersalle=0
                    print("Vous arrivez dans une salle plutôt vide, mais un escalier semble mener vers le sous-sol")

                    dé_n(10)
                    if résultatdé<=6:
                        dé_n(10)
                        if résultatdé<=3:
                            print("Vous entendez des claquements d'os dans la pièce...")
                            print("Un squelette animé par une sorte d'aura maléfique se jette sur vous ! Vous sortez votre épée et vous appretez à vous battre")
                            combat(attaque, vie, defense, 20, 3, 4, potion, carte)
                        else :
                            print("Des bruits de métal vous parviennent...")
                            print("Une armure s'anime et commence à s'approcher de vous ! Vous sortez votre épée et vous appretez à vous battre")
                            combat(attaque, vie, defense, 30, 4, 6, potion, carte)
                        vie=vie1
                        potion=potion1
                        carte=carte1
                        if issue==1:
                            print ("Vous venez à bout de votre adversdaire")
                            gain=gain+1
                            if gain>1:
                                niveauup(attaque,defense,viemax)
                                gain=0
                        if issue==2:
                            print ("Vous fuyez le combat")
                        if issue==3:
                            print ("Vous tombez au combat ... Vous vous reveillez un peu plus tard, votre ennemi a disparu...")
                            score=score-1
                            vie1=viemax/2
                        vie=vie1 

#Bouger

                while changersalle==0:
                    action=input("Que voulez vous faire ? ")
                    if action=="aide" or action=="Aide":
                        aideexploration()
                    if action=="bouger" or action=="Bouger" :
                        action=input("Où souhaitez vous aller ?")
                        
                        if action=="Ouest" or action=="ouest":
                            print("Il n'y a rien à l'Ouest")                           
                        
                        if action=="Est" or action=="est":
                            print("Il n'y a rien à l'Est")
                            
                        if action=="Sud" or action=="sud":
                            print("Vous retournez dans la salle avec les 2 statues.")
                            changersalle=1
                            salle=15
                            os.system('cls')
                          
                        if action=="Nord" or action=="nord":
                            print("Il n'y a rien au Nord. ")


                        if action=="Descendre" or action=="descendre":
                            print("Vous descendez l'escalier, mais les marches n'ont pas l'air très stables...")
                            changersalle=1
                            salle=1
                            os.system('cls')

#Utiliser

                    if action=="utiliser" or action=="Utiliser":
                        print("Vous possedez ", potion," potions de soin, ")
                        if tableau==1:
                            print("Vous avez noté l'inscription derière le tableau") 
                        action=input("Que voulez vous utiliser ?")
                        if action=="potion" or action=="Potion":
                            if potion>0:
                                vie=viemax
                                potion=potion-1
                            else : print("Vous n'avez pas de potion à utiliser")
                        if action=="tableau" or action=="Tableau":
                            if tableau==1:
                                print("L'inscription mystérieuse derrière le tableau disait : ''Tout commence au PONANT et finit à l'ORIENT, celui du SUD précède celui de l'EST''")  
                        if action=="calepin" or action=="Calepin" or action=="calepin ensanglanté" or action=="Calepin ensanglanté":
                            if note2==0:
                                print ("En feuilletant les premières pages vous pouvez lire : ''Je n'en peux plus ... Ce n'est pas moi ... Je ne peux plus supproter ce que je leur fait endurer ... J'aurais aimé ne jamais arriver ici...'' Les pages suivantes sont ensanglantées et indéchiffrables")
                                score=score+1
                                note2=1
                            else : print("Vous avez déjà relevé la note du calepin")
#prendre
                    if action=="prendre" or action=="Prendre":
                        if action=="calepin" or action=="Calepin" or action=="calepin ensanglanté" or action=="Calepin ensanglanté":
                            if note2==0:
                                print ("En feuilletant les premières pages vous pouvez lire : ''Je n'en peux plus ... Ce n'est pas moi ... Je ne peux plus supproter ce que je leur fait endurer ... J'aurais aimé ne jamais arriver ici...'' Les pages suivantes sont ensanglantées et indéchiffrables")
                                score=score+1
                                note2=1
                            else : print("Vous avez déjà relevé la note du calepin")
                            
#regarder
                    if action=="regarder":
                        print("Dans la pièce où vous vous trouvez se trouve un escalier menant vers le sous sol, ce dernier semble usé par le temps... Vous remarquez également un CALEPIN légèrement ensanglanté sur le sol ...")

#Inventaire
                        
                    if action=="inventaire" or action=="Inventaire":
                        print("Vous posséder les objets suivants :")
                        if potion>=1:
                            print(potion, "potion(s) de soin")
                        if carte>=1:
                            print(carte, "Cartes de bannissement")
                        if note1==1:
                            print("Note1 (la note sur l'état du manoir)")
                        if note2==1:
                            print("Note2 (la note du carnet ensanglanté)")
                        if tableau==1:
                            print("Note3 (la note écrite dérière le tableau)")
                        if note4==1:
                            print("Note4")
                        if note5==1:
                            print("Note5")
                        if clefrdc==1:
                            print("La clef du rez de chaussée")
                        if gant==1:
                            print("Un gant")
                            
                        action=input("Que souhaitez-vous utiliser ? ")
                        
                        if action=="potion" or action=="Potion":
                            if potion>0:
                                vie=viemax
                                potion=potion-1
                            else : print("Vous n'avez pas de potion à utiliser")
                        if action=="note1" or action=="Note1":
                            if note1==1:
                                print(textenote1)
                        if action=="note2" or action=="Note2":
                            if note2==1:
                                print(textenote2)
                        if action=="note3" or action=="Note3":
                            if note3==1:
                                print(textenote3)
                        if action=="note4" or action=="Note4":
                            if note4==1:
                                print(textenote4)
                        if action=="note5" or action=="Note5":
                            if note5==1:
                                print(textenote5)
                        if action!="note1" and action!="Note1" and action!="note2" and action!="Note2" and action!="note3" and action!="Note3" and action!="note4" and action!="Note4" and action!="note5" and action!="Note5" and action!="potion" and action!="Potion":
                            print("Vous ne pouvez pas utiliser cet objet ici")


            
#Arrivée a l'étage, SALLE 21
    if salle==21:
        changersalle=0
        print ("Vous vous trouvez maintenant dans un petit couloir étroit, en haut d'un grand escalier de bois usé par le temps.")
        dé_n(10)
        if résultatdé<=6:
            dé_n(10)
            if résultatdé<=3:
                print("Vous entendez un cri rauque en entrant dans la pièce...")
                print("Soudain, une immense gargouille se jette sur vous ! Vous sortez votre épée et vous appretez à vous battre")
                combat(attaque, vie, defense, 50, 6, 4, potion, carte)
            else :
                print("Vous sentez une odeur âcre en arrivant dans la pièce...")
                print("Un cadavre se lève et commence à s'approcher de vous ! Vous sortez votre épée et vous appretez à vous battre")
                combat(attaque, vie, defense, 40, 4, 6, potion, carte)
            vie=vie1
            potion=potion1
            carte=carte1
            if issue==1:
                print ("Vous venez à bout de votre adversdaire")
                gain=gain+1
                if gain>1:
                    niveauup(attaque,defense,viemax)
                    gain=0
            if issue==2:
                print ("Vous fuyez le combat")
            if issue==3:
                print ("Vous tombez au combat ... Vous vous reveillez un peu plus tard, votre ennemi a disparu...")
                score=score-1
                vie1=viemax/2
            vie=vie1
            
        while changersalle==0:
            action=input("Que voulez vous faire ? ")
            if action!="bouger" and action!="Bouger" and action!="regarder" and action!="Regarder" and action!="utiliser" and action!="Utiliser" and action!="prendre" and action!="Prendre":
                print("Veuillez entrer une action valide. (Rappel: 'Regarder', 'Bouger', 'Utiliser','Prendre')")
            if action=="aide" or action=="Aide":
                aideexploration()
    #bouger
            if action=="bouger" or action=="Bouger":
                action=input("La pièce comporte 3 portes : une menant à l'Est, une au Nord et une à l'Ouest. Il y a également ungrand escalier qui mène vers le rez de chaussée, où souhaitez vous aller ? ('Nord', 'Sud', 'Est', 'Ouest' ou 'Descendre')")
                if action!="Est" and action!="est" and action!="Ouest" and action!="ouest" and action!="Nord" and action!="nord" and action!="Descendre" and action!="descendre" and action!="Bas" and action!="bas":
                    print("Vous ne pouvez aller qu'à l'Est, à l'Ouest, au Nord ou descendre les escaliers")
                if action=="Est" or action=="est":
                    if blocage1==0:
                        print("La porte semble bloquée de l'autre côté ...")
                    else :
                        changersalle=1
                        salle=26
                        os.system('cls')
                        
                if action=="Ouest" or action=="ouest":
                    changersalle=1
                    salle=23
                    os.system('cls')
                    
                if action=="Nord" or action=="nord":
                    changersalle=1
                    salle=22
                    os.system('cls')
                    
                if action=="Descendre" or action=="descendre" or action=="Bas" or action=="bas":
                    changersalle=1
                    salle=13
                    os.system('cls')

    #regarder
            if action=="regarder" or action=="Regarder":
                print("Rien n'attire votre attention dans ce couloir ... mis à part l'odeur désagréable de la moisissure qui envahit les murs...")


    #utiliser
            if action=="utiliser" or action=="Utiliser":
                print("Vous possedez ", potion," potions de soin, ")
                if tableau==1:
                    print("Vous avez noté l'inscription derière le tableau") 
                action=input("Que voulez vous utiliser ?")
                if action=="potion" or action=="Potion":
                    if potion>0:
                        vie=viemax
                        potion=potion-1
                    else : print("Vous n'avez pas de potion à utiliser")
                if action=="tableau" or action=="Tableau":
                    if tableau==1:
                        print("L'inscription mystérieuse derrière le tableau disait : ''Tout commence au PONANT et finit à l'ORIENT, celui du SUD précède celui de l'EST''")

    #prendre
            if action=="prendre" or action=="Prendre":
                print("Il n'y a rien à ramasser dans la pièce.")

    #Inventaire
                        
            if action=="inventaire" or action=="Inventaire":
                print("Vous posséder les objets suivants :")
                if potion>=1:
                    print(potion, "potion(s) de soin")
                if carte>=1:
                    print(carte, "Cartes de bannissement")
                if note1==1:
                    print("Note1 (la note sur l'état du manoir)")
                if note2==1:
                    print("Note2 (la note du carnet ensanglanté)")
                if tableau==1:
                    print("Note3 (la note écrite dérière le tableau)")
                if note4==1:
                    print("Note4")
                if note5==1:
                    print("Note5")
                if clefrdc==1:
                    print("La clef du rez de chaussée")
                if gant==1:
                    print("Un gant")
                    
                action=input("Que souhaitez-vous utiliser ? ")
                
                if action=="potion" or action=="Potion":
                    if potion>0:
                        vie=viemax
                        potion=potion-1
                    else : print("Vous n'avez pas de potion à utiliser")
                if action=="note1" or action=="Note1":
                    if note1==1:
                        print(textenote1)
                if action=="note2" or action=="Note2":
                    if note2==1:
                        print(textenote2)
                if action=="note3" or action=="Note3":
                    if note3==1:
                        print(textenote3)
                if action=="note4" or action=="Note4":
                    if note4==1:
                        print(textenote4)
                if action=="note5" or action=="Note5":
                    if note5==1:
                        print(textenote5)
                if action!="note1" and action!="Note1" and action!="note2" and action!="Note2" and action!="note3" and action!="Note3" and action!="note4" and action!="Note4" and action!="note5" and action!="Note5" and action!="potion" and action!="Potion":
                    print("Vous ne pouvez pas utiliser cet objet ici")

    
#SALLE 22
    if salle==22:
        changersalle=0
        print ("Vous arrivez dans une sorte de remise.")
        dé_n(10)
        if résultatdé<=6:
            dé_n(10)
            if résultatdé<=3:
                print("Vous entendez un cri rauque en entrant dans la pièce...")
                print("Soudain, une immense gargouille se jette sur vous ! Vous sortez votre épée et vous appretez à vous battre")
                combat(attaque, vie, defense, 50, 6, 4, potion, carte)
            else :
                print("Vous sentez une odeur âcre en arrivant dans la pièce...")
                print("Un cadavre se lève et commence à s'approcher de vous ! Vous sortez votre épée et vous appretez à vous battre")
                combat(attaque, vie, defense, 40, 4, 6, potion, carte)
            vie=vie1
            potion=potion1
            carte=carte1
            if issue==1:
                print ("Vous venez à bout de votre adversaire")
                gain=gain+1
                if gain>1:
                    niveauup(attaque,defense,viemax)
                    gain=0
            if issue==2:
                print ("Vous fuyez le combat")
            if issue==3:
                print ("Vous tombez au combat ... Vous vous reveillez un peu plus tard, votre ennemi a disparu...")
                score=score-1
                vie1=viemax/2
            vie=vie1
    
        while changersalle==0:
            action=input("Que voulez vous faire ? ")
            if action!="bouger" and action!="Bouger" and action!="regarder" and action!="Regarder" and action!="utiliser" and action!="Utiliser" and action!="prendre" and action!="Prendre":
                print("Veuillez entrer une action valide. (Rappel: 'Regarder', 'Bouger', 'Utiliser','Prendre')")
            if action=="aide" or action=="Aide":
                aideexploration()
    #bouger
            if action=="bouger" or action=="Bouger":
                action=input("Il y a deux sorties possibles : une menant à l'Est et une au Sud. Où souhaitez vous aller ? ('Nord', 'Sud', 'Est', 'Ouest')")
                if action!="Est" and action!="est" and action!="sud" and action!="Sud":
                    print("Vous ne pouvez aller qu'à l'Est ou au Sud")
                    
                if action=="Est" or action=="est":
                    changersalle=1
                    salle=25
                    os.system('cls')
                    
                if action=="Sud" or action=="sud":
                    changersalle=1
                    salle=21
                    os.system('cls')
                                    
    #regarder
            if action=="regarder" or action=="Regarder":
                print("La remise est sale et en grand désordre. En observant attentivement un TABLEAU accroché au mur, vous remarquez qu'il semble avoir été déplacé il y a peu ...")

    #utiliser

            if action=="utiliser" or action=="Utiliser":
                action=input("Que voulez vous utiliser ?")
                if action=="tableau" or action=="Tableau":
                    if tableau==0:
                        print("En déplaçant le tableau, vous pouvez voir une inscription asssez mystérieuse ... presque prophétique : ''Tout commence au PONANT et finit à l'ORIENT, celui du SUD précède celui de l'EST'' Vous vous empressez de marquer cela dans votre journal, cela peut toujours être utile ...")
                        tableau=1
                        objet=objet+1
                        score=score+1
                        note3=1
                    if tableau==1:
                        print("L'inscription mystérieuse derrière le tableau disait : ''Tout commence au PONANT et finit à l'ORIENT, celui du SUD précède celui de l'EST''")
                if action=="potion" or action=="Potion":
                    if potion>0:
                        vie=viemax
                        potion=potion-1
                    else : print("Vous n'avez pas de potion à utiliser")
                    
    #prendre
            if action=="prendre" or action=="Prendre":
                print("Il n'y a rien à ramasser dans la pièce.")

    #Inventaire
                        
            if action=="inventaire" or action=="Inventaire":
                print("Vous posséder les objets suivants :")
                if potion>=1:
                    print(potion, "potion(s) de soin")
                if carte>=1:
                    print(carte, "Cartes de bannissement")
                if note1==1:
                    print("Note1 (la note sur l'état du manoir)")
                if note2==1:
                    print("Note2 (la note du carnet ensanglanté)")
                if tableau==1:
                    print("Note3 (la note écrite dérière le tableau)")
                if note4==1:
                    print("Note4")
                if note5==1:
                    print("Note5")
                if clefrdc==1:
                    print("La clef du rez de chaussée")
                if gant==1:
                    print("Un gant")
                    
                action=input("Que souhaitez-vous utiliser ? ")
                
                if action=="potion" or action=="Potion":
                    if potion>0:
                        vie=viemax
                        potion=potion-1
                    else : print("Vous n'avez pas de potion à utiliser")
                if action=="note1" or action=="Note1":
                    if note1==1:
                        print(textenote1)
                if action=="note2" or action=="Note2":
                    if note2==1:
                        print(textenote2)
                if action=="note3" or action=="Note3":
                    if note3==1:
                        print(textenote3)
                if action=="note4" or action=="Note4":
                    if note4==1:
                        print(textenote4)
                if action=="note5" or action=="Note5":
                    if note5==1:
                        print(textenote5)
                if action!="note1" and action!="Note1" and action!="note2" and action!="Note2" and action!="note3" and action!="Note3" and action!="note4" and action!="Note4" and action!="note5" and action!="Note5" and action!="potion" and action!="Potion":
                    print("Vous ne pouvez pas utiliser cet objet ici")



#SALLE 25
    if salle==25:
        changersalle=0
        print ("Vous arrivez dans un atelier rempli de mécanismes et de rouages.")
        dé_n(10)
        if résultatdé<=6:
            dé_n(10)
            if résultatdé<=3:
                print("Vous entendez un cri rauque en entrant dans la pièce...")
                print("Soudain, une immense gargouille se jette sur vous ! Vous sortez votre épée et vous appretez à vous battre")
                combat(attaque, vie, defense, 50, 6, 4, potion, carte)
            else :
                print("Vous sentez une odeur âcre en arrivant dans la pièce...")
                print("Un cadavre se lève et commence à s'approcher de vous ! Vous sortez votre épée et vous appretez à vous battre")
                combat(attaque, vie, defense, 40, 4, 6, potion, carte)
            vie=vie1
            potion=potion1
            carte=carte1
            if issue==1:
                print ("Vous venez à bout de votre adversaire")
                gain=gain+1
                if gain>1:
                    niveauup(attaque,defense,viemax)
                    gain=0
            if issue==2:
                print ("Vous fuyez le combat")
            if issue==3:
                print ("Vous tombez au combat ... Vous vous reveillez un peu plus tard, votre ennemi a disparu...")
                score=score-1
        vie=vie1
        while changersalle==0:
            action=input("Que voulez vous faire ? ")
            if action!="bouger" and action!="Bouger" and action!="regarder" and action!="Regarder" and action!="utiliser" and action!="Utiliser" and action!="prendre" and action!="Prendre":
                print("Veuillez entrer une action valide. (Rappel: 'Regarder', 'Bouger', 'Utiliser','Prendre')")
            if action=="aide" or action=="Aide":
                aideexploration()
    #bouger
            if action=="bouger" or action=="Bouger":
                action=input("Il y a deux sorties possibles : une menant à l'Ouest et une au Sud. Où souhaitez vous aller ? ('Nord', 'Sud', 'Est', 'Ouest')")
                if action!="Ouest" and action!="ouest" and action!="sud" and action!="Sud":
                    print("Vous ne pouvez aller qu'à l'Ouest ou au Sud")
                if action=="Ouest" or action=="ouest":
                    changersalle=1
                    salle=22
                    os.system('cls')
                if action=="Sud" or action=="sud":
                    if enigme1==0:
                        print("La lourde porte menant vers le Sud est bloquée par une sorte de mécanisme ...")
                    else:
                        changersalle=1
                        salle=26
                        os.system('cls')
                                    
    #regarder
            if action=="regarder" or action=="Regarder":
                print("Vous voyez des mécanismes partout autours de vous, cependant aucun n'est en mouvement. Vous remarquez que sur chacun des quatre murs de la pièce se trouve un LEVIER")

    #utiliser
            if action=="utiliser" or action=="Utiliser":
                action=input("Que voulez vous utiliser ?")
                if action=="tableau" or action=="Tableau":
                    if tableau==1:
                        print("L'inscription mystérieuse derrière le tableau disait : ''Tout commence au PONANT et finit à l'ORIENT, celui du SUD précède celui de l'EST''")
                if action=="potion" or action=="Potion":
                    if potion>0:
                        vie=viemax
                        potion=potion-1
                    else : print("Vous n'avez pas de potion à utiliser")
                if action=="Levier" or action=="levier" or action=="Leviers" or action=="leviers":
                    if enigme1==0:
                        action=input("Dans quel ordre voulez vous activer les leviers ? (Il y a 4 leviers : un au Sud, un au Nord, un a l'Est et un à l'Ouest, écrivez le bon ordre des directions en minuscule avec un espace entre chaque) ")
                        if action=="ouest nord sud est":
                            print ("Les mécanismes de la pièce se mettent en marche et la porte menant vers le Sud s'ouvre ...")
                            enigme1=1
                            score=score+1
                        else : print("Rien ne se passe ...")
                            
    #prendre
            if action=="prendre" or action=="Prendre":
                print("Il n'y a rien à ramasser dans la pièce.")

    #Inventaire
                        
            if action=="inventaire" or action=="Inventaire":
                print("Vous posséder les objets suivants :")
                if potion>=1:
                    print(potion, "potion(s) de soin")
                if carte>=1:
                    print(carte, "Cartes de bannissement")
                if note1==1:
                    print("Note1 (la note sur l'état du manoir)")
                if note2==1:
                    print("Note2 (la note du carnet ensanglanté)")
                if tableau==1:
                    print("Note3 (la note écrite dérière le tableau)")
                if note4==1:
                    print("Note4")
                if note5==1:
                    print("Note5")
                if clefrdc==1:
                    print("La clef du rez de chaussée")
                if gant==1:
                    print("Un gant")
                    
                action=input("Que souhaitez-vous utiliser ? ")
                
                if action=="potion" or action=="Potion":
                    if potion>0:
                        vie=viemax
                        potion=potion-1
                    else : print("Vous n'avez pas de potion à utiliser")
                if action=="note1" or action=="Note1":
                    if note1==1:
                        print(textenote1)
                if action=="note2" or action=="Note2":
                    if note2==1:
                        print(textenote2)
                if action=="note3" or action=="Note3":
                    if note3==1:
                        print(textenote3)
                if action=="note4" or action=="Note4":
                    if note4==1:
                        print(textenote4)
                if action=="note5" or action=="Note5":
                    if note5==1:
                        print(textenote5)
                if action!="note1" and action!="Note1" and action!="note2" and action!="Note2" and action!="note3" and action!="Note3" and action!="note4" and action!="Note4" and action!="note5" and action!="Note5" and action!="potion" and action!="Potion":
                    print("Vous ne pouvez pas utiliser cet objet ici")



#SALLE 26
    if salle==26:
        changersalle=0
        print ("Vous arrivez dans une grande  armurerie.")
        dé_n(10)
        if résultatdé<=6:
            dé_n(10)
            if résultatdé<=3:
                print("Vous entendez un cri rauque en entrant dans la pièce...")
                print("Soudain, une immense gargouille se jette sur vous ! Vous sortez votre épée et vous appretez à vous battre")
                combat(attaque, vie, defense, 50, 6, 4, potion, carte)
            else :
                print("Vous sentez une odeur âcre en arrivant dans la pièce...")
                print("Un cadavre se lève et commence à s'approcher de vous ! Vous sortez votre épée et vous appretez à vous battre")
                combat(attaque, vie, defense, 40, 4, 6, potion, carte)
            vie=vie1
            potion=potion1
            carte=carte1
            if issue==1:
                print ("Vous venez à bout de votre adversaire")
                gain=gain+1
                if gain>1:
                    niveauup(attaque,defense,viemax)
                    gain=0
            if issue==2:
                print ("Vous fuyez le combat")
            if issue==3:
                print ("Vous tombez au combat ... Vous vous reveillez un peu plus tard, votre ennemi a disparu...")
                score=score-1
            
        vie=vie1
        while changersalle==0:
            action=input("Que voulez vous faire ? ")
            if action!="bouger" and action!="Bouger" and action!="regarder" and action!="Regarder" and action!="utiliser" and action!="Utiliser" and action!="prendre" and action!="Prendre":
                print("Veuillez entrer une action valide. (Rappel: 'Regarder', 'Bouger', 'Utiliser','Prendre')")
            if action=="aide" or action=="Aide":
                aideexploration()
    #bouger
            if action=="bouger" or action=="Bouger":
                action=input("Il y a deux sorties possibles : une menant à l'Ouest et une au Nord. Où souhaitez vous aller ? ('Nord', 'Sud', 'ouest', 'Ouest')")
                if action!="Ouest" and action!="ouest" and action!="nord" and action!="Nord":
                    print("Vous ne pouvez aller qu'à l'Ouest ou au Nord")
                if action=="Ouest" or action=="ouest":
                    if blocage1==0:
                        print("La porte menant vèrs l'Ouest est bloquée par une baricade en bois, vous pouvez l'enlever pour libérer la porte")
                    else:
                        changersalle=1
                        salle=21
                        os.system('cls')
                if action=="Nord" or action=="nord":
                    changersalle=1
                    salle=25
                    os.system('cls')
                                    
    #regarder
            if action=="regarder" or action=="Regarder":
                print("Il y a de nombreux porte-armures dans cette pièce, sur l'une d'entre elles un GANT de mailles attire votre attention... Vous remarquez également que la porte menant à l'Ouest est bloqué par une BARRICADE en bois, visiblement assez légère pour être retirée")

    #utiliser
            if action=="utiliser" or action=="Utiliser":
                action=input("Que voulez vous utiliser ?")
                if action=="tableau" or action=="Tableau":
                    if tableau==1:
                        print("L'inscription mystérieuse derrière le tableau disait : ''Tout commence au PONANT et finit à l'ORIENT, celui du SUD précède celui de l'EST''")
                if action=="potion" or action=="Potion":
                    if potion>0:
                        vie=viemax
                        potion=potion-1
                    else : print("Vous n'avez pas de potion à utiliser")
                if action=="barricade" or action=="Barricade" or action=="barricade en bois" or action=="Barricade en bois":
                    blocage1=1
                    print("Vous retirez la barricade et liberez le passage vers l'ouest")
    #prendre
            if action=="prendre" or action=="Prendre":
                action=input("Que voulez vous prendre ?")
                if gant==0:
                    if action=="gant" or action=="Gant" or action=="Gant de mailles" or action=="gant de mailles" or action=="Gant de maille" or action=="gant de maille":
                        print("Vous prenez le gant sur le porte armures, il peut peut être vous être utile ...")
                        score=score+1
                        gant=1
                else:
                    print("Il n'y a plus rien à ramasser dans la pièce.")

    #Inventaire
                        
            if action=="inventaire" or action=="Inventaire":
                print("Vous posséder les objets suivants :")
                if potion>=1:
                    print(potion, "potion(s) de soin")
                if carte>=1:
                    print(carte, "Cartes de bannissement")
                if note1==1:
                    print("Note1 (la note sur l'état du manoir)")
                if note2==1:
                    print("Note2 (la note du carnet ensanglanté)")
                if tableau==1:
                    print("Note3 (la note écrite dérière le tableau)")
                if note4==1:
                    print("Note4")
                if note5==1:
                    print("Note5")
                if clefrdc==1:
                    print("La clef du rez de chaussée")
                if gant==1:
                    print("Un gant")
                    
                action=input("Que souhaitez-vous utiliser ? ")
                
                if action=="potion" or action=="Potion":
                    if potion>0:
                        vie=viemax
                        potion=potion-1
                    else : print("Vous n'avez pas de potion à utiliser")
                if action=="note1" or action=="Note1":
                    if note1==1:
                        print(textenote1)
                if action=="note2" or action=="Note2":
                    if note2==1:
                        print(textenote2)
                if action=="note3" or action=="Note3":
                    if note3==1:
                        print(textenote3)
                if action=="note4" or action=="Note4":
                    if note4==1:
                        print(textenote4)
                if action=="note5" or action=="Note5":
                    if note5==1:
                        print(textenote5)
                if action!="note1" and action!="Note1" and action!="note2" and action!="Note2" and action!="note3" and action!="Note3" and action!="note4" and action!="Note4" and action!="note5" and action!="Note5" and action!="potion" and action!="Potion":
                    print("Vous ne pouvez pas utiliser cet objet ici")



#SALLE 23
    if salle==23:
        changersalle=0
        print ("Vous êtes dans un couloir sombre et inquiétant.")
        if vampire==0:
            print("Vous sentez un soufle glacé dans votre nuque ...")
            print("Vous faites volte-face et vous trouvez nez à nez avec un être humanoïde aux canines acérées ...")
            combat(attaque, vie, defense, 80, 8, 4, potion, carte)
            vie=vie1
            potion=potion1
            carte=carte1
            if issue==1:
                print ("Vous venez à bout de votre adversaire")
                gain=gain+1
                if gain>1:
                    niveauup(attaque,defense,viemax)
                    gain=0
                vampire=1
                score=score+5
            if issue==2:
                print ("Vous fuyez le combat")
            if issue==3:
                print ("Vous tombez au combat ... Vous vous reveillez un peu plus tard, votre ennemi a disparu...")
                score=score-1
                vie1=viemax/2
            vie=vie1
        else :
            dé_n(10)
            if résultatdé<=6:
                dé_n(10)
                if résultatdé<=3:
                    print("Vous entendez un cri rauque en entrant dans la pièce...")
                    print("Soudain, une immense gargouille se jette sur vous ! Vous sortez votre épée et vous appretez à vous battre")
                    combat(attaque, vie, defense, 50, 6, 4, potion, carte)
                else :
                    print("Vous sentez une odeur âcre en arrivant dans la pièce...")
                    print("Un cadavre se lève et commence à s'approcher de vous ! Vous sortez votre épée et vous appretez à vous battre")
                    combat(attaque, vie, defense, 40, 4, 6, potion, carte)
            vie=vie1
            potion=potion1
            carte=carte1
            if issue==1:
                print ("Vous venez à bout de votre adversaire")
                gain=gain+1
                if gain>1:
                    niveauup(attaque,defense,viemax)
                    gain=0
            if issue==2:
                print ("Vous fuyez le combat")
            if issue==3:
                print ("Vous tombez au combat ... Vous vous reveillez un peu plus tard, votre ennemi a disparu...")
                score=score-1
                vie1=viemax/2
            vie=vie1     
    
        while changersalle==0:
            action=input("Que voulez vous faire ? ")
            if action!="bouger" and action!="Bouger" and action!="regarder" and action!="Regarder" and action!="utiliser" and action!="Utiliser" and action!="prendre" and action!="Prendre":
                print("Veuillez entrer une action valide. (Rappel: 'Regarder', 'Bouger', 'Utiliser','Prendre')")
            if action=="aide" or action=="Aide":
                aideexploration()
    #bouger
            if action=="bouger" or action=="Bouger":
                action=input("Il y a deux sorties possibles : une menant à l'Est et une au Nord. Où souhaitez vous aller ? ('Nord', 'Sud', 'ouest', 'Ouest')")
                if action!="Est" and action!="est" and action!="nord" and action!="Nord":
                    print("Vous ne pouvez aller qu'à l'Est ou au Nord")
                if action=="Est" or action=="est":
                    changersalle=1
                    salle=21
                    os.system('cls')
                if action=="Nord" or action=="nord":
                    changersalle=1
                    salle=24
                    os.system('cls')
                                    
    #regarder
            if action=="regarder" or action=="Regarder":
                if rideau==0:
                    print("Le couloir est sombre, vous ne pouvez pas distinguer les détails de la pièce mis à part une petite fenêtre couverte par un épais RIDEAU.")
                else:
                    print("Un tableau accroché au mur attire votre attention : c'est un portrait dont les traits vous sont étrangement familiers ... Cependant il arbore un sourrire carnassier et dérangeant ...")
                    score=score+1

    #utiliser
            if action=="utiliser" or action=="Utiliser":
                action=input("Que voulez vous utiliser ?")
                if action=="tableau" or action=="Tableau":
                    if tableau==1:
                        print("L'inscription mystérieuse derrière le tableau disait : ''Tout commence au PONANT et finit à l'ORIENT, celui du SUD précède celui de l'EST''")
                if action=="potion" or action=="Potion":
                    if potion>0:
                        vie=viemax
                        potion=potion-1
                    else : print("Vous n'avez pas de potion à utiliser")
                            
    #prendre
            if action=="prendre" or action=="Prendre":
                print("Il n'y a rien à ramasser dans la pièce.")

    #Inventaire
                        
            if action=="inventaire" or action=="Inventaire":
                print("Vous posséder les objets suivants :")
                if potion>=1:
                    print(potion, "potion(s) de soin")
                if carte>=1:
                    print(carte, "Cartes de bannissement")
                if note1==1:
                    print("Note1 (la note sur l'état du manoir)")
                if note2==1:
                    print("Note2 (la note du carnet ensanglanté)")
                if tableau==1:
                    print("Note3 (la note écrite dérière le tableau)")
                if note4==1:
                    print("Note4")
                if note5==1:
                    print("Note5")
                if clefrdc==1:
                    print("La clef du rez de chaussée")
                if gant==1:
                    print("Un gant")
                    
                action=input("Que souhaitez-vous utiliser ? ")
                
                if action=="potion" or action=="Potion":
                    if potion>0:
                        vie=viemax
                        potion=potion-1
                    else : print("Vous n'avez pas de potion à utiliser")
                if action=="note1" or action=="Note1":
                    if note1==1:
                        print(textenote1)
                if action=="note2" or action=="Note2":
                    if note2==1:
                        print(textenote2)
                if action=="note3" or action=="Note3":
                    if note3==1:
                        print(textenote3)
                if action=="note4" or action=="Note4":
                    if note4==1:
                        print(textenote4)
                if action=="note5" or action=="Note5":
                    if note5==1:
                        print(textenote5)
                if action!="note1" and action!="Note1" and action!="note2" and action!="Note2" and action!="note3" and action!="Note3" and action!="note4" and action!="Note4" and action!="note5" and action!="Note5" and action!="potion" and action!="Potion":
                    print("Vous ne pouvez pas utiliser cet objet ici")


#SALLE 24
    if salle==24:
        changersalle=0
        print ("Vous arrivez dans une petite chambre éclairée à la seule lueur d'une bougie.")
        dé_n(10)
        if résultatdé<=6:
            dé_n(10)
            if résultatdé<=3:
                print("Vous entendez un cri rauque en entrant dans la pièce...")
                print("Soudain, une immense gargouille se jette sur vous ! Vous sortez votre épée et vous appretez à vous battre")
                combat(attaque, vie, defense, 50, 6, 4, potion, carte)
            else :
                print("Vous sentez une odeur âcre en arrivant dans la pièce...")
                print("Un cadavre se lève et commence à s'approcher de vous ! Vous sortez votre épée et vous appretez à vous battre")
                combat(attaque, vie, defense, 40, 4, 6, potion, carte)
            vie=vie1
            potion=potion1
            carte=carte1
            if issue==1:
                print ("Vous venez à bout de votre adversaire")
                gain=gain+1
                if gain>1:
                    niveauup(attaque,defense,viemax)
                    gain=0
            if issue==2:
                print ("Vous fuyez le combat")
            if issue==3:
                print ("Vous tombez au combat ... Vous vous reveillez un peu plus tard, votre ennemi a disparu...")
                score=score-1
                vie1=viemax/2
            vie=vie1
            
        while changersalle==0:
            action=input("Que voulez vous faire ? ")
            if action!="bouger" and action!="Bouger" and action!="regarder" and action!="Regarder" and action!="utiliser" and action!="Utiliser" and action!="prendre" and action!="Prendre":
                print("Veuillez entrer une action valide. (Rappel: 'Regarder', 'Bouger', 'Utiliser','Prendre')")
            if action=="aide" or action=="Aide":
                aideexploration()
    #bouger
            if action=="bouger" or action=="Bouger":
                action=input("Il y a deux sorties possibles : une menant à l'Est et une au Nord. Où souhaitez vous aller ? ('Nord', 'Sud', 'ouest', 'Ouest')")
                if action!="Est" and action!="est" and action!="nord" and action!="Nord":
                    print("Vous ne pouvez aller qu'à l'Est ou au Nord")
                if action=="Est" or action=="est":
                    changersalle=1
                    salle=21
                    os.system('cls')
                if action=="Nord" or action=="nord":
                    changersalle=1
                    os.system('cls')
                    salle=24
                                    
    #regarder
            if action=="regarder" or action=="Regarder":
                if rideau==0:
                    print("Le couloir est sombre, vous ne pouvez pas distinguer les détails de la pièce mis à part une petite fenêtre couverte par un épais RIDEAU.")
                else:
                    print("Un tableau accroché au mur attire votre attention : c'est un portrait dont les traits vous sont étrangement familiers, il vous rappelle un peu les votres ... Cependant le sourire de l'homme est carnassier et vicieux")
                    score=score+1

    #utiliser
            if action=="utiliser" or action=="Utiliser":
                print("Vous possedez ", potion," potions de soin, ")
                if tableau==1:
                    print("Vous avez noté l'inscription derière le tableau") 
                action=input("Que voulez vous utiliser ?")
                if action=="potion" or action=="Potion":
                    if potion>0:
                        vie=viemax
                        potion=potion-1
                    else : print("Vous n'avez pas de potion à utiliser")
                if action=="tableau" or action=="Tableau":
                    if tableau==1:
                        print("L'inscription mystérieuse derrière le tableau disait : ''Tout commence au PONANT et finit à l'ORIENT, celui du SUD précède celui de l'EST''")
                if action=="rideau" or action=="Rideau":
                    if rideau==0:
                        print("Vous tirez le rideau et pourrez maintenant REGARDER les détails de la salle si vous y portez votre attention ...")
                        rideau=1
                        score=score+1
                    else:print("Vous avez déjà tiré le rideau, vous pourrez maintenant REGARDER les détails de la salle si vous y portez votre attention ...")
    #prendre
            if action=="prendre" or action=="Prendre":
                print("Il n'y a rien à ramasser dans la pièce.")

            #Inventaire
                        
            if action=="inventaire" or action=="Inventaire":
                print("Vous posséder les objets suivants :")
                if potion>=1:
                    print(potion, "potion(s) de soin")
                if carte>=1:
                    print(carte, "Cartes de bannissement")
                if note1==1:
                    print("Note1 (la note sur l'état du manoir)")
                if note2==1:
                    print("Note2 (la note du carnet ensanglanté)")
                if tableau==1:
                    print("Note3 (la note écrite dérière le tableau)")
                if note4==1:
                    print("Note4")
                if note5==1:
                    print("Note5")
                if clefrdc==1:
                    print("La clef du rez de chaussée")
                if gant==1:
                    print("Un gant")
                    
                action=input("Que souhaitez-vous utiliser ? ")
                
                if action=="potion" or action=="Potion":
                    if potion>0:
                        vie=viemax
                        potion=potion-1
                    else : print("Vous n'avez pas de potion à utiliser")
                if action=="note1" or action=="Note1":
                    if note1==1:
                        print(textenote1)
                if action=="note2" or action=="Note2":
                    if note2==1:
                        print(textenote2)
                if action=="note3" or action=="Note3":
                    if note3==1:
                        print(textenote3)
                if action=="note4" or action=="Note4":
                    if note4==1:
                        print(textenote4)
                if action=="note5" or action=="Note5":
                    if note5==1:
                        print(textenote5)
                if action!="note1" and action!="Note1" and action!="note2" and action!="Note2" and action!="note3" and action!="Note3" and action!="note4" and action!="Note4" and action!="note5" and action!="Note5" and action!="potion" and action!="Potion":
                    print("Vous ne pouvez pas utiliser cet objet ici")



#Sous-sol

#salle1------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

    if salle==1:
        changersalle=0
        print ("Vous arrivez dans une salle dépourvue de lumière, un grand bruit vous surprend ! L'escalier vient de s'affaisser, il vous faudra trouver un autre moyen de remonter!")

        dé_n(10)
        if résultatdé<=6:
            dé_n(10)
            if résultatdé<=3:
                print("Vous entendez un cri rauque en entrant dans la pièce...")
                print("Soudain, une immense gargouille se jette sur vous ! Vous sortez votre épée et vous appretez à vous battre")
                combat(attaque, vie, defense, 50, 6, 4, potion, carte)
            else :
                print("Vous sentez une odeur âcre en arrivant dans la pièce...")
                print("Un cadavre se lève et commence à s'approcher de vous ! Vous sortez votre épée et vous appretez à vous battre")
                combat(attaque, vie, defense, 40, 4, 6, potion, carte)
            vie=vie1
            potion=potion1
            carte=carte1
            if issue==1:
                print ("Vous venez à bout de votre adversdaire")
                gain=gain+1
                if gain>1:
                    niveauup(attaque,defense,viemax)
                    gain=0
            if issue==2:
                print ("Vous fuyez le combat")
            if issue==3:
                print ("Vous tombez au combat ... Vous vous reveillez un peu plus tard, votre ennemi a disparu...")
                score=score-1
                vie1=viemax/2
            vie=vie1

        while changersalle==0:
            action=input("Que voulez vous faire ? ")

#les différentes actions :

#Les actions non valides.....................
            
            if action!="bouger" and action!="Bouger" and action!="regarder" and action!="Regarder" and action!="utiliser" and action!="Utiliser" and action!="prendre" and action!="Prendre": #rappels en cas d'erreurs
                print("Veuillez entrer une action valide. (Rappel: 'Regarder', 'Bouger', 'Utiliser','Prendre')")

#action regarder et utiliser.....................
                
            if action=="regarder":                                          
                print ("Il n'y a rien dans cette salle sauf le vieil escalier qui s'est écroulé")

#Déplacement................................

            if action=="bouger" or action=="Bouger":
                action=input("il n'y a qu'une seule porte qui mène à l'ouest du manoir dans cette pièce, où  voulez-vous aller ? ('Nord', 'Sud', 'Est', 'Ouest')")
                if action!="Ouest" and action!="ouest":
                    print("Vous ne pouvez aller qu'à l'Ouest")
                if action=="Ouest" or action=="ouest":
                    print("vous empruntez la porte situé à l'ouest")
                    salle=2
                    changersalle=1
                    os.system('cls')

            #Inventaire
                        
            if action=="inventaire" or action=="Inventaire":
                print("Vous posséder les objets suivants :")
                if potion>=1:
                    print(potion, "potion(s) de soin")
                if carte>=1:
                    print(carte, "Cartes de bannissement")
                if note1==1:
                    print("Note1 (la note sur l'état du manoir)")
                if note2==1:
                    print("Note2 (la note du carnet ensanglanté)")
                if tableau==1:
                    print("Note3 (la note écrite dérière le tableau)")
                if note4==1:
                    print("Note4")
                if note5==1:
                    print("Note5")
                if clefrdc==1:
                    print("La clef du rez de chaussée")
                if gant==1:
                    print("Un gant")
                    
                action=input("Que souhaitez-vous utiliser ? ")
                
                if action=="potion" or action=="Potion":
                    if potion>0:
                        vie=viemax
                        potion=potion-1
                    else : print("Vous n'avez pas de potion à utiliser")
                if action=="note1" or action=="Note1":
                    if note1==1:
                        print(textenote1)
                if action=="note2" or action=="Note2":
                    if note2==1:
                        print(textenote2)
                if action=="note3" or action=="Note3":
                    if note3==1:
                        print(textenote3)
                if action=="note4" or action=="Note4":
                    if note4==1:
                        print(textenote4)
                if action=="note5" or action=="Note5":
                    if note5==1:
                        print(textenote5)
                if action!="note1" and action!="Note1" and action!="note2" and action!="Note2" and action!="note3" and action!="Note3" and action!="note4" and action!="Note4" and action!="note5" and action!="Note5" and action!="potion" and action!="Potion":
                    print("Vous ne pouvez pas utiliser cet objet ici")



                    
#salle2---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

    if salle==2 : 

        changersalle=0
        print ("vous venez d'entrer dans la deuxiéme pièce du sous-sol. Toujours aucune lumière...")

        dé_n(10)
        if résultatdé<=6:
            dé_n(10)
            if résultatdé<=3:
                print("Vous entendez un cri rauque en entrant dans la pièce...")
                print("Soudain, une immense gargouille se jette sur vous ! Vous sortez votre épée et vous appretez à vous battre")
                combat(attaque, vie, defense, 50, 6, 4, potion, carte)
            else :
                print("Vous sentez une odeur âcre en arrivant dans la pièce...")
                print("Un cadavre se lève et commence à s'approcher de vous ! Vous sortez votre épée et vous appretez à vous battre")
                combat(attaque, vie, defense, 40, 4, 6, potion, carte)
            vie=vie1
            potion=potion1
            carte=carte1
            if issue==1:
                print ("Vous venez à bout de votre adversdaire")
                gain=gain+1
                if gain>1:
                    niveauup(attaque,defense,viemax)
                    gain=0
            if issue==2:
                print ("Vous fuyez le combat")
            if issue==3:
                print ("Vous tombez au combat ... Vous vous reveillez un peu plus tard, votre ennemi a disparu...")
                score=score-1
                vie1=viemax/2
            vie=vie1

        while changersalle==0:
            action=input("Que voulez vous faire ? ")

#les différentes actions :

#Les actions non valides.....................
            
            if action!="bouger" and action!="Bouger" and action!="regarder" and action!="Regarder" and action!="utiliser" and action!="Utiliser" and action!="prendre" and action!="Prendre":
                print("Veuillez entrer une action valide. (Rappel: 'Regarder', 'Bouger', 'Utiliser','Prendre')")

#action regarder et utiliser.....................
                
            if action=="regarder":
                print ("Il n'y a rien dans cette salle, seules trois portes sont présentes dans cette pièce.")

            #Inventaire
                        
            if action=="inventaire" or action=="Inventaire":
                print("Vous posséder les objets suivants :")
                if potion>=1:
                    print(potion, "potion(s) de soin")
                if carte>=1:
                    print(carte, "Cartes de bannissement")
                if note1==1:
                    print("Note1 (la note sur l'état du manoir)")
                if note2==1:
                    print("Note2 (la note du carnet ensanglanté)")
                if tableau==1:
                    print("Note3 (la note écrite dérière le tableau)")
                if note4==1:
                    print("Note4")
                if note5==1:
                    print("Note5")
                if clefrdc==1:
                    print("La clef du rez de chaussée")
                if gant==1:
                    print("Un gant")
                    
                action=input("Que souhaitez-vous utiliser ? ")
                
                if action=="potion" or action=="Potion":
                    if potion>0:
                        vie=viemax
                        potion=potion-1
                    else : print("Vous n'avez pas de potion à utiliser")
                if action=="note1" or action=="Note1":
                    if note1==1:
                        print(textenote1)
                if action=="note2" or action=="Note2":
                    if note2==1:
                        print(textenote2)
                if action=="note3" or action=="Note3":
                    if note3==1:
                        print(textenote3)
                if action=="note4" or action=="Note4":
                    if note4==1:
                        print(textenote4)
                if action=="note5" or action=="Note5":
                    if note5==1:
                        print(textenote5)
                if action!="note1" and action!="Note1" and action!="note2" and action!="Note2" and action!="note3" and action!="Note3" and action!="note4" and action!="Note4" and action!="note5" and action!="Note5" and action!="potion" and action!="Potion":
                    print("Vous ne pouvez pas utiliser cet objet ici")



#Déplacement................................

            if action=="bouger" or action=="Bouger":
                action=input("il y a trois portes qui mène à l'Est, au sud et à l'ouest du manoir dans cette pièce, où  voulez-vous aller ? ('Nord', 'Sud', 'Est', 'Ouest')")
                if action=="est" or action=="Est":
                    print("Vous empruntez la porte qui mène à l'est du manoir")
                    salle=1
                    os.system('cls')
                if action=="Ouest" or action=="ouest":
                    print("vous empruntez la porte situé à l'ouest")
                    changersalle=1
                    salle=5
                    os.system('cls')
                if action=="Sud" or action=="sud":
                    print("vous empruntez la porte situé au sud")
                    changersalle=1
                    salle=3
                    os.system('cls')
                if action!="nord" and action!="Nord":
                    print("vous ne pouvez pas aller au Nord")
            

#salle5----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
                    
    if salle==5:
        changersalle=0
        print ("Vous entrez dans la pièce du coffre...")

        dé_n(10)
        if résultatdé<=6:
            dé_n(10)
            if résultatdé<=3:
                print("Vous entendez un cri rauque en entrant dans la pièce...")
                print("Soudain, une immense gargouille se jette sur vous ! Vous sortez votre épée et vous appretez à vous battre")
                combat(attaque, vie, defense, 50, 6, 4, potion, carte)
            else :
                print("Vous sentez une odeur âcre en arrivant dans la pièce...")
                print("Un cadavre se lève et commence à s'approcher de vous ! Vous sortez votre épée et vous appretez à vous battre")
                combat(attaque, vie, defense, 40, 4, 6, potion, carte)
            vie=vie1
            potion=potion1
            carte=carte1
            if issue==1:
                print ("Vous venez à bout de votre adversdaire")
                gain=gain+1
                if gain>1:
                    niveauup(attaque,defense,viemax)
                    gain=0
            if issue==2:
                print ("Vous fuyez le combat")
            if issue==3:
                print ("Vous tombez au combat ... Vous vous reveillez un peu plus tard, votre ennemi a disparu...")
                score=score-1
                vie1=viemax/2
            vie=vie1

        while changersalle==0:
            
            action=input("Que voulez vous faire ? ")

#les différentes actions :

#Les actions non valides.....................
            
            if action!="bouger" and action!="Bouger" and action!="regarder" and action!="Regarder" and action!="utiliser" and action!="Utiliser" and action!="prendre" and action!="Prendre":
                print("Veuillez entrer une action valide. (Rappel: 'Regarder', 'Bouger', 'Utiliser','Prendre')")

#action regarder et utiliser.....................
                
            if action=="regarder":
                print("Vous appercevez un COFFRE dans un coin sombre de la pièce")
            if action!="bouger" and action!="Bouger" and action!="regarder" and action!="Regarder" and action!="utiliser" and action!="Utiliser" and action!="prendre" and action!="Prendre":
                print("Veuillez entrer une action valide. (Rappel: 'Regarder', 'Bouger', 'Utiliser','Prendre')")

            if action=="utiliser" or action=="Utiliser":
                action=input("Que souhaitez-vous utiliser ? ")
                if action=="coffre":
                    print("Vous ouvrez le coffre et trouvez un bout de papier sur lequel vous arrivez à lire : ''Les riches en manquent, les pauvres en ont et si tu en manges tu meurs...Que suis-je ? '' ")
                    note5=1
            #Inventaire
                        
            if action=="inventaire" or action=="Inventaire":
                print("Vous posséder les objets suivants :")
                if potion>=1:
                    print(potion, "potion(s) de soin")
                if carte>=1:
                    print(carte, "Cartes de bannissement")
                if note1==1:
                    print("Note1 (la note sur l'état du manoir)")
                if note2==1:
                    print("Note2 (la note du carnet ensanglanté)")
                if tableau==1:
                    print("Note3 (la note écrite dérière le tableau)")
                if note4==1:
                    print("Note4")
                if note5==1:
                    print("Note5")
                if clefrdc==1:
                    print("La clef du rez de chaussée")
                if gant==1:
                    print("Un gant")
                    
                action=input("Que souhaitez-vous utiliser ? ")
                
                if action=="potion" or action=="Potion":
                    if potion>0:
                        vie=viemax
                        potion=potion-1
                    else : print("Vous n'avez pas de potion à utiliser")
                if action=="note1" or action=="Note1":
                    if note1==1:
                        print(textenote1)
                if action=="note2" or action=="Note2":
                    if note2==1:
                        print(textenote2)
                if action=="note3" or action=="Note3":
                    if note3==1:
                        print(textenote3)
                if action=="note4" or action=="Note4":
                    if note4==1:
                        print(textenote4)
                if action=="note5" or action=="Note5":
                    if note5==1:
                        print(textenote5)
                if action!="note1" and action!="Note1" and action!="note2" and action!="Note2" and action!="note3" and action!="Note3" and action!="note4" and action!="Note4" and action!="note5" and action!="Note5" and action!="potion" and action!="Potion":
                    print("Vous ne pouvez pas utiliser cet objet ici")


            
#Déplacement................................
                                 
            if action=="bouger" or action=="Bouger":
                action=input("il n'y a qu'une seule porte qui mène à l'Est dans la pièce précédente du manoir, où  voulez-vous aller ? ('Nord', 'Sud', 'Est', 'Ouest')")
                if action!="Est" and action!="est":
                    print("Vous ne pouvez aller qu'à l'Est")
                if action=="Est" or action=="est":
                    print("vous empruntez la porte situé à l'Est")
                    changersalle=1
                    salle=2
                    os.system('cls')





#Salle 3--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

    if salle==3:
        changersalle=0
        print ("Vous entrez dans une grande pièce qui semble étre au centre du manoir...")

        dé_n(10)
        if résultatdé<=6:
            dé_n(10)
            if résultatdé<=3:
                print("Vous entendez un cri rauque en entrant dans la pièce...")
                print("Soudain, une immense gargouille se jette sur vous ! Vous sortez votre épée et vous appretez à vous battre")
                combat(attaque, vie, defense, 50, 6, 4, potion, carte)
            else :
                print("Vous sentez une odeur âcre en arrivant dans la pièce...")
                print("Un cadavre se lève et commence à s'approcher de vous ! Vous sortez votre épée et vous appretez à vous battre")
                combat(attaque, vie, defense, 40, 4, 6, potion, carte)
            vie=vie1
            potion=potion1
            carte=carte1
            if issue==1:
                print ("Vous venez à bout de votre adversdaire")
                gain=gain+1
                if gain>1:
                    niveauup(attaque,defense,viemax)
                    gain=0
            if issue==2:
                print ("Vous fuyez le combat")
            if issue==3:
                print ("Vous tombez au combat ... Vous vous reveillez un peu plus tard, votre ennemi a disparu...")
                score=score-1
                vie1=viemax/2
            vie=vie1

        while changersalle==0:
            action=input("Que voulez vous faire ? ")

#les différentes actions :

#Les actions non valides.....................

            if action!="bouger" and action!="Bouger" and action!="regarder" and action!="Regarder" and action!="utiliser" and action!="Utiliser" and action!="prendre" and action!="Prendre": #rappels en cas d'erreurs
                print("Veuillez entrer une action valide. (Rappel: 'Regarder', 'Bouger', 'Utiliser','Prendre')")

#action regarder et utiliser.....................
                    
            if action=="regarder":
                print ("Il n'y a rien dans cette salle en dehors de ces deux portes")

            #Inventaire
                        
            if action=="inventaire" or action=="Inventaire":
                print("Vous posséder les objets suivants :")
                if potion>=1:
                    print(potion, "potion(s) de soin")
                if carte>=1:
                    print(carte, "Cartes de bannissement")
                if note1==1:
                    print("Note1 (la note sur l'état du manoir)")
                if note2==1:
                    print("Note2 (la note du carnet ensanglanté)")
                if tableau==1:
                    print("Note3 (la note écrite dérière le tableau)")
                if note4==1:
                    print("Note4")
                if note5==1:
                    print("Note5")
                if clefrdc==1:
                    print("La clef du rez de chaussée")
                if gant==1:
                    print("Un gant")
                    
                action=input("Que souhaitez-vous utiliser ? ")
                
                if action=="potion" or action=="Potion":
                    if potion>0:
                        vie=viemax
                        potion=potion-1
                    else : print("Vous n'avez pas de potion à utiliser")
                if action=="note1" or action=="Note1":
                    if note1==1:
                        print(textenote1)
                if action=="note2" or action=="Note2":
                    if note2==1:
                        print(textenote2)
                if action=="note3" or action=="Note3":
                    if note3==1:
                        print(textenote3)
                if action=="note4" or action=="Note4":
                    if note4==1:
                        print(textenote4)
                if action=="note5" or action=="Note5":
                    if note5==1:
                        print(textenote5)
                if action!="note1" and action!="Note1" and action!="note2" and action!="Note2" and action!="note3" and action!="Note3" and action!="note4" and action!="Note4" and action!="note5" and action!="Note5" and action!="potion" and action!="Potion":
                    print("Vous ne pouvez pas utiliser cet objet ici")



#Déplacement................................

            if action=="bouger" or action=="Bouger":
                action=input("il n'y a deux portes, une qui mène au sud et une autre qui mène dans une pèce au nord du manoir. Où voulez-vous aller ? ('Nord', 'Sud', 'Est', 'Ouest')")
                if action=="Ouest" or action=="ouest":
                    print("Vous ne pouvez pas aller à l'Ouest")

                if action=="Est" or action=="est":
                    print("Vous ne pouvez pas aller à l'Est")

                if action=="Nord" or action=="nord":
                    print("vous empruntez la porte situé au Nord")
                    changersalle=1
                    salle=2
                    os.system('cls')
                if action=="Sud" or action=="sud":
                    print("vous empruntez la porte situé au Sud")
                    changersalle=1
                    salle=4
                    os.system('cls')



#Salle4------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

                                 
    if salle==4:
        changersalle=0
        print ("Cette pièce semble sans interet...")

        dé_n(10)
        if résultatdé<=6:
            dé_n(10)
            if résultatdé<=3:
                print("Vous entendez un cri rauque en entrant dans la pièce...")
                print("Soudain, une immense gargouille se jette sur vous ! Vous sortez votre épée et vous appretez à vous battre")
                combat(attaque, vie, defense, 50, 6, 4, potion, carte)
            else :
                print("Vous sentez une odeur âcre en arrivant dans la pièce...")
                print("Un cadavre se lève et commence à s'approcher de vous ! Vous sortez votre épée et vous appretez à vous battre")
                combat(attaque, vie, defense, 40, 4, 6, potion, carte)
            vie=vie1
            potion=potion1
            carte=carte1
            if issue==1:
                print ("Vous venez à bout de votre adversdaire")
                gain=gain+1
                if gain>1:
                    niveauup(attaque,defense,viemax)
                    gain=0
            if issue==2:
                print ("Vous fuyez le combat")
            if issue==3:
                print ("Vous tombez au combat ... Vous vous reveillez un peu plus tard, votre ennemi a disparu...")
                score=score-1
                vie1=viemax/2
            vie=vie1

        while changersalle==0:
            action=input("Que voulez vous faire ? ")

#les différentes actions :

#Les actions non valides.....................
            
            if action!="bouger" and action!="Bouger" and action!="regarder" and action!="Regarder" and action!="utiliser" and action!="Utiliser" and action!="prendre" and action!="Prendre":
                print("Veuillez entrer une action valide. (Rappel: 'Regarder', 'Bouger', 'Utiliser','Prendre')")

#action regarder et utiliser.....................
                
            if action=="regarder":
                print("Un VISAGE de pière gravé dans la porte semble animé ...")

            #Inventaire
                        
            if action=="inventaire" or action=="Inventaire":
                print("Vous posséder les objets suivants :")
                if potion>=1:
                    print(potion, "potion(s) de soin")
                if carte>=1:
                    print(carte, "Cartes de bannissement")
                if note1==1:
                    print("Note1 (la note sur l'état du manoir)")
                if note2==1:
                    print("Note2 (la note du carnet ensanglanté)")
                if tableau==1:
                    print("Note3 (la note écrite dérière le tableau)")
                if note4==1:
                    print("Note4")
                if note5==1:
                    print("Note5")
                if clefrdc==1:
                    print("La clef du rez de chaussée")
                if gant==1:
                    print("Un gant")
                    
                action=input("Que souhaitez-vous utiliser ? ")
                
                if action=="potion" or action=="Potion":
                    if potion>0:
                        vie=viemax
                        potion=potion-1
                    else : print("Vous n'avez pas de potion à utiliser")
                if action=="note1" or action=="Note1":
                    if note1==1:
                        print(textenote1)
                if action=="note2" or action=="Note2":
                    if note2==1:
                        print(textenote2)
                if action=="note3" or action=="Note3":
                    if note3==1:
                        print(textenote3)
                if action=="note4" or action=="Note4":
                    if note4==1:
                        print(textenote4)
                if action=="note5" or action=="Note5":
                    if note5==1:
                        print(textenote5)
                if action!="note1" and action!="Note1" and action!="note2" and action!="Note2" and action!="note3" and action!="Note3" and action!="note4" and action!="Note4" and action!="note5" and action!="Note5" and action!="potion" and action!="Potion":
                    print("Vous ne pouvez pas utiliser cet objet ici")


                
#Déplacement................................
                
            if action=="bouger" or action=="Bouger":
                action=input("il y a deux porte qui mène à l'Est et au Nord, où  voulez-vous aller ? ('Nord', 'Sud', 'Est', 'Ouest')")
                if action=="Est" or action=="est":
                    print("La porte est bloquée. Tout a coup le visage se met à vous parler...")
                    question=input("Cherches la question cachée dans ce sous sol et réponds y pour pouvoir passer ! Réponse:")
                    if question=="rien" or question=="Rien":
                        print("vous avez bien répondu ce n'était pas simple pourtant")
                        changersalle=1
                        salle=6
                        os.system('cls')
                    else:
                        print("Ce n'est pas la bonne réponse, il vous faut surement plus de temps la question n'est pas facile")
                                     
                if action=="Nord" or action=="nord":
                    print("Vous empruntez la porte qui mène au Nord")
                    changersalle=1
                    salle=3
                    os.system('cls')
                if action=="Ouest" or action=="ouest":
                    print("Vous ne pouvez pas aller à l'Ouest.")

                if action=="Sud" or action=="sud":
                    print("Vous ne pouvez pas aller au Sud.")




    #Salle6---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------     

    if salle==6:
        changersalle=0
        print ("Vous regagnez espoir en entrant dans cette pièce doté d'un escalier ! Pourvu que celui là ne s'écroule pas...")

        dé_n(10)
        if résultatdé<=6:
            dé_n(10)
            if résultatdé<=3:
                print("Vous entendez un cri rauque en entrant dans la pièce...")
                print("Soudain, une immense gargouille se jette sur vous ! Vous sortez votre épée et vous appretez à vous battre")
                combat(attaque, vie, defense, 50, 6, 4, potion, carte)
            else :
                print("Vous sentez une odeur âcre en arrivant dans la pièce...")
                print("Un cadavre se lève et commence à s'approcher de vous ! Vous sortez votre épée et vous appretez à vous battre")
                combat(attaque, vie, defense, 40, 4, 6, potion, carte)
            vie=vie1
            potion=potion1
            carte=carte1
            if issue==1:
                print ("Vous venez à bout de votre adversdaire")
                gain=gain+1
                if gain>1:
                    niveauup(attaque,defense,viemax)
                    gain=0
            if issue==2:
                print ("Vous fuyez le combat")
            if issue==3:
                print ("Vous tombez au combat ... Vous vous reveillez un peu plus tard, votre ennemi a disparu...")
                score=score-1
                vie1=viemax/2
            vie=vie1

        while changersalle==0:
            action=input("Que voulez vous faire ? ")

#les différentes actions :

#Les actions non valides.....................
            
            if action!="bouger" and action!="Bouger" and action!="regarder" and action!="Regarder" and action!="utiliser" and action!="Utiliser" and action!="prendre" and action!="Prendre":
                
                print("Veuillez entrer une action valide. (Rappel: 'Regarder', 'Bouger', 'Utiliser','Prendre')")

#action regarder et utiliser.....................
            if action=="regarder":
                print("Il y a un escalier au dessus d'une table d'architecte, vous remarquez également un petit COFFRE au milieu des instruments de dessin")
                
            if action!="bouger" and action!="Bouger" and action!="regarder" and action!="Regarder" and action!="utiliser" and action!="Utiliser" and action!="prendre" and action!="Prendre":
                print("Veuillez entrer une action valide. (Rappel: 'Regarder', 'Bouger', 'Utiliser','Prendre')")
                                 
            if action=="utiliser":
                action=input("Que voulez vous utiliser ?")
                if action=="coffre" or action=="Coffre":
                    print("Vous ouvrez le coffre et récuperez son contenu : la clef de la grande porte du rez de chaussée")
                    clefrdc=1
                    
            #Inventaire
                        
            if action=="inventaire" or action=="Inventaire":
                print("Vous posséder les objets suivants :")
                if potion>=1:
                    print(potion, "potion(s) de soin")
                if carte>=1:
                    print(carte, "Cartes de bannissement")
                if note1==1:
                    print("Note1 (la note sur l'état du manoir)")
                if note2==1:
                    print("Note2 (la note du carnet ensanglanté)")
                if tableau==1:
                    print("Note3 (la note écrite dérière le tableau)")
                if note4==1:
                    print("Note4")
                if note5==1:
                    print("Note5")
                if clefrdc==1:
                    print("La clef du rez de chaussée")
                if gant==1:
                    print("Un gant")
                    
                action=input("Que souhaitez-vous utiliser ? ")
                
                if action=="potion" or action=="Potion":
                    if potion>0:
                        vie=viemax
                        potion=potion-1
                    else : print("Vous n'avez pas de potion à utiliser")
                if action=="note1" or action=="Note1":
                    if note1==1:
                        print(textenote1)
                if action=="note2" or action=="Note2":
                    if note2==1:
                        print(textenote2)
                if action=="note3" or action=="Note3":
                    if note3==1:
                        print(textenote3)
                if action=="note4" or action=="Note4":
                    if note4==1:
                        print(textenote4)
                if action=="note5" or action=="Note5":
                    if note5==1:
                        print(textenote5)
                if action!="note1" and action!="Note1" and action!="note2" and action!="Note2" and action!="note3" and action!="Note3" and action!="note4" and action!="Note4" and action!="note5" and action!="Note5" and action!="potion" and action!="Potion":
                    print("Vous ne pouvez pas utiliser cet objet ici")


            
#Déplacement................................
                                 
            if action=="bouger" or action=="Bouger":
                action=input("il y a cet escalier qui mène au rez-de-chaussé du manoir et la porte qui mène à l'Ouest du manoir, où  voulez-vous aller ? ('Nord', 'Sud', 'Est', 'Ouest','Monter')")
                if action=="Est" or action=="est":
                    print("Vous ne pouvez pas aller à l'Est")
                if action=="Sud" or action=="sud":
                    print("Vous ne pouvez pas aller au Sud")
                if action=="Ouest" or action=="ouest":
                    print("Vous empruntez la porte qui mène à l'Ouest")
                    changersalle=1
                    salle=4
                    os.system('cls')
                if action=="monter" or action=="Monter":
                    print("Vous empruntez l'escalier qui mène à l'étage supérieur")
                    changersalle=1
                    salle=16
                    os.system('cls')
                if action=="nord" or action=="Nord":
                    print("Vous ne pouvez pas aller au Nord")





#SALLE 14---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

    if salle==14:
        changersalle=0
                
        if grosmonstre==0:
            print("Vous êtes dans la salle dans laquelle vous avez réalisé un combat avec un monstre puissant")
            dé_n(10)
            if résultatdé<=6:
                dé_n(10)
                if résultatdé<=3:
                    print("Vous entendez des claquements d'os dans la pièce...")
                    print("Un squelette animé par une sorte d'aura maléfique se jette sur vous ! Vous sortez votre épée et vous appretez à vous battre")
                    combat(attaque, vie, defense, 20, 3, 4, potion, carte)
                else :
                    print("Des bruits de métal vous parviennent...")
                    print("Une armure s'anime et commence à s'approcher de vous ! Vous sortez votre épée et vous appretez à vous battre")
                    combat(attaque, vie, defense, 30, 4, 6, potion, carte)
                vie=vie1
                potion=potion1
                carte=carte1
                if issue==1:
                    print ("Vous venez à bout de votre adversdaire")
                    gain=gain+1
                    if gain>1:
                        niveauup(attaque,defense,viemax)
                        gain=0
                if issue==2:
                    print ("Vous fuyez le combat")
                if issue==3:
                    print ("Vous tombez au combat ... Vous vous reveillez un peu plus tard, votre ennemi a disparu...")
                    score=score-1
                    vie1=viemax/2
                vie=vie1
                
        if grosmonstre==1:
            if grosmonstre==1:
                print("Vous arrivez dans une salle relativement grande.")
                print("Vous entendez le souffle fort d'une bête...")
                print("Un immense minotaure se jette sur vous ! Vous sortez votre épée et vous appretez à vous battre")
                combat(attaque, vie, defense, 50, 6, 5, potion, carte)
                vie=vie1
                potion=potion1
                carte=carte1
                if issue==1:
                    print ("Vous venez à bout de votre adversdaire")
                    gain=gain+1
                    if gain>1:
                        niveauup(attaque,defense,viemax)
                        gain=0
                    grosmonstre=0
                    score=score+5
                if issue==2:
                    print ("Vous fuyez le combat")
                if issue==3:
                    print ("Vous tombez au combat ... Vous vous reveillez un peu plus tard, votre ennemi a disparu...")
                    score=score-1
                    vie1=viemax/2
                vie=vie1


        while changersalle==0:
            action=input("Que voulez vous faire ? ")

            #Inventaire
                        
            if action=="inventaire" or action=="Inventaire":
                print("Vous posséder les objets suivants :")
                if potion>=1:
                    print(potion, "potion(s) de soin")
                if carte>=1:
                    print(carte, "Cartes de bannissement")
                if note1==1:
                    print("Note1 (la note sur l'état du manoir)")
                if note2==1:
                    print("Note2 (la note du carnet ensanglanté)")
                if tableau==1:
                    print("Note3 (la note écrite dérière le tableau)")
                if note4==1:
                    print("Note4")
                if note5==1:
                    print("Note5")
                if clefrdc==1:
                    print("La clef du rez de chaussée")
                if gant==1:
                    print("Un gant")
                    
                action=input("Que souhaitez-vous utiliser ? ")
                
                if action=="potion" or action=="Potion":
                    if potion>0:
                        vie=viemax
                        potion=potion-1
                    else : print("Vous n'avez pas de potion à utiliser")
                if action=="note1" or action=="Note1":
                    if note1==1:
                        print(textenote1)
                if action=="note2" or action=="Note2":
                    if note2==1:
                        print(textenote2)
                if action=="note3" or action=="Note3":
                    if note3==1:
                        print(textenote3)
                if action=="note4" or action=="Note4":
                    if note4==1:
                        print(textenote4)
                if action=="note5" or action=="Note5":
                    if note5==1:
                        print(textenote5)
                if action!="note1" and action!="Note1" and action!="note2" and action!="Note2" and action!="note3" and action!="Note3" and action!="note4" and action!="Note4" and action!="note5" and action!="Note5" and action!="potion" and action!="Potion":
                    print("Vous ne pouvez pas utiliser cet objet ici")

#Bouger

            if action=="bouger" or action=="Bouger" :
                action=input("Où souhaitez vous aller ?")
                        
                if action=="Ouest" or action=="ouest":
                    print("Il n'y a rien à l'Ouest")                           
                        
                if action=="Est" or action=="est":
                    changersalle=1
                    salle=13
                    os.system('cls')
                            
                if action=="Sud" or action=="sud":
                    print("Vous arrivez dans une sorte de réserve.")
                    changersalle=1
                    salle=18
                    os.system('cls')
                          
                if action=="Nord" or action=="nord":
                    print("Il n'y a rien au Nord. ")

        #regarder
                    
            if action=="regarder" or action=="Regarder":
                print("Vous vous trouvez dans une sorte d'écurie. Au milieu de la paille, un COFFRET attire votre attention ...")

        #utiliser
                
            if action=="utiliser" or action=="Utiliser":
                print("Vous possedez ", potion," potions de soin, ")
                if tableau==1:
                    print("Vous avez noté l'inscription derière le tableau") 
                action=input("Que voulez vous utiliser ?")
                if action=="potion" or action=="Potion":
                    if potion>0:
                        vie=viemax
                        potion=potion-1
                    else : print("Vous n'avez pas de potion à utiliser")
                if action=="tableau" or action=="Tableau":
                    if tableau==1:
                        print("L'inscription mystérieuse derrière le tableau disait : ''Tout commence au PONANT et finit à l'ORIENT, celui du SUD précède celui de l'EST''")
                if action=="coffret" or action=="Coffret":
                    print("A l'intérieur du coffret se trouve un petit parchemin enroulé sur lequel vous pouvez lire"
                          "''Jouer au bord de la ligne est un jeu dangereux,"
                          "Docteur Palmers, de son patient devrait être méfiant,"
                          "Même si ce n'est qu'un pauvre malheureux,"
                          "Le loup pourrait un jour montrer les dents ...''")
                    print("Ce poème vous donne des frissons sans que vous ne parveniez à savoir pourquoi ...")
                    note4=1
#SALLE 18------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

    if salle==18:
        if osalle18==0:
            changersalle=0
            osalle18=1
            print("Vous arrivez dans une sorte de réserve")

        dé_n(10)
        if résultatdé<=6:
            dé_n(10)
            if résultatdé<=3:
                print("Vous entendez des claquements d'os dans la pièce...")
                print("Un squelette animé par une sorte d'aura maléfique se jette sur vous ! Vous sortez votre épée et vous appretez à vous battre")
                combat(attaque, vie, defense, 20, 3, 4, potion, carte)
            else :
                print("Des bruits de métal vous parviennent...")
                print("Une armure s'anime et commence à s'approcher de vous ! Vous sortez votre épée et vous appretez à vous battre")
                combat(attaque, vie, defense, 30, 4, 6, potion, carte)
            vie=vie1
            potion=potion1
            carte=carte1
            if issue==1:
                print ("Vous venez à bout de votre adversdaire")
                gain=gain+1
                if gain>1:
                    niveauup(attaque,defense,viemax)
                    gain=0
            if issue==2:
                print ("Vous fuyez le combat")
            if issue==3:
                print ("Vous tombez au combat ... Vous vous reveillez un peu plus tard, votre ennemi a disparu...")
                score=score-1
                vie1=viemax/2
            vie=vie1
#Bouger
            
        while changersalle==0:
            action=input("Que voulez vous faire ? ")
            if action=="bouger" or action=="Bouger" :
                action=input("Où souhaitez vous aller ?")
                        
                if action=="Ouest" or action=="ouest":
                    print("Il n'y a rien à l'Ouest")                           
                        
                if action=="Est" or action=="est":
                    if barriere18==1:
                        print("Vous essayez d'ouvrir cette porte, mais une barrière de bois bloque la porte, vous pouvez sans doute l'enlever.")
                    else :
                        changersalle=1
                        salle=17
                        os.system('cls')
                            
                if action=="Sud" or action=="sud":
                    print("Il n'y a rien au Sud.")
                    
                          
                if action=="Nord" or action=="nord":
                    changersalle=1
                    salle=14
                    os.system('cls')
                
 #Regarder

            if action=="Regarder" or action=="regarder":
                if coffre2==0:
                    print("Vous cherchez dans les différents rangements si vous ne trouvez pas quelque chose d'intéressant. Vous remarquez au fond de la salle un petit COFFRE brillant.")
                    coffre2=1
                if coffre2==1:
                    if action=="Regarder" or action=="regarder":
                        print("Le COFFRE brillant se trouve toujours au fond de la salle")
                            

 #Utiliser
            if action=="Utiliser" or action=="utiliser":
                action=input("Que souhaitez vous utiliser ? ")
                if action=="coffre":
                    if coffre18==1:
                        print("Il n'y a plus rien dans le coffre")
                    else:print("Vous ouvrez le coffre et vous trouvez une CARTE reluisante, sur le dos de la carte est inscrit : 'CARTE DE BANISSEMENT'")
                if action=="barrière" or action=="Barrière" or action=="barriere" or action=="Barriere":
                    print("Vous retirez la barrière et libérez le passage vers l'est.")
                    barriere18=0

#prendre
            if action=="prendre" or action=="Prendre":
                action=input("Que souhaitez vous prendre ? ")
                if action=="carte" or action=="Carte" or action=="carte de banissement" or action=="Carte de banissement":
                    if coffre18==0:
                        print("Vous avez pris la 'Carte de Banissement' Elle vous permet de tuer instantanément un ennemi, attention, elle est à usage unique !")
                        carte=carte+1
                        coffre18=1
                    if coffre18==1:
                        print("Il n'y a plus rien dans le coffre")

            #Inventaire
                        
            if action=="inventaire" or action=="Inventaire":
                print("Vous posséder les objets suivants :")
                if potion>=1:
                    print(potion, "potion(s) de soin")
                if carte>=1:
                    print(carte, "Cartes de bannissement")
                if note1==1:
                    print("Note1 (la note sur l'état du manoir)")
                if note2==1:
                    print("Note2 (la note du carnet ensanglanté)")
                if tableau==1:
                    print("Note3 (la note écrite dérière le tableau)")
                if note4==1:
                    print("Note4")
                if note5==1:
                    print("Note5")
                if clefrdc==1:
                    print("La clef du rez de chaussée")
                if gant==1:
                    print("Un gant")
                    
                action=input("Que souhaitez-vous utiliser ? ")
                
                if action=="potion" or action=="Potion":
                    if potion>0:
                        vie=viemax
                        potion=potion-1
                    else : print("Vous n'avez pas de potion à utiliser")
                if action=="note1" or action=="Note1":
                    if note1==1:
                        print(textenote1)
                if action=="note2" or action=="Note2":
                    if note2==1:
                        print(textenote2)
                if action=="note3" or action=="Note3":
                    if note3==1:
                        print(textenote3)
                if action=="note4" or action=="Note4":
                    if note4==1:
                        print(textenote4)
                if action=="note5" or action=="Note5":
                    if note5==1:
                        print(textenote5)
                if action!="note1" and action!="Note1" and action!="note2" and action!="Note2" and action!="note3" and action!="Note3" and action!="note4" and action!="Note4" and action!="note5" and action!="Note5" and action!="potion" and action!="Potion":
                    print("Vous ne pouvez pas utiliser cet objet ici")



#SALLE 17----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

    if salle==17:
        if osalle17==0:
            changersalle=0
            osalle17=1
            print("Vous vous trouvez devant la porte d'entrée principale du Manoir, donnant sur l'extérieur")

        dé_n(10)
        if résultatdé<=6:
            dé_n(10)
            if résultatdé<=3:
                print("Vous entendez des claquements d'os dans la pièce...")
                print("Un squelette animé par une sorte d'aura maléfique se jette sur vous ! Vous sortez votre épée et vous appretez à vous battre")
                combat(attaque, vie, defense, 20, 3, 4, potion, carte)
            else :
                print("Des bruits de métal vous parviennent...")
                print("Une armure s'anime et commence à s'approcher de vous ! Vous sortez votre épée et vous appretez à vous battre")
                combat(attaque, vie, defense, 30, 4, 6, potion, carte)
            vie=vie1
            potion=potion1
            carte=carte1
            if issue==1:
                print ("Vous venez à bout de votre adversdaire")
                gain=gain+1
                if gain>1:
                    niveauup(attaque,defense,viemax)
                    gain=0
            if issue==2:
                print ("Vous fuyez le combat")
            if issue==3:
                print ("Vous tombez au combat ... Vous vous reveillez un peu plus tard, votre ennemi a disparu...")
                score=score-1
                vie1=viemax/2
            vie=vie1
            
#Bouger
            
        while changersalle==0:
            action=input("Que voulez vous faire ? ")
            if action=="bouger" or action=="Bouger" :
                action=input("Où souhaitez vous aller ?")
                        
                if action=="Ouest" or action=="ouest":
                    if barriere18==1:
                        print("Vous essayer d'ouvrir cette porte, mais elle semble bloquée de l'autre côté")
                    else :
                        changersalle=1
                        salle=18
                        os.system('cls')
                        
                if action=="Est" or action=="est":
                    if barriere16==1:
                        print("Vous essayer d'ouvrir cette porte, mais elle semble bloquée de l'autre côté")
                    else :
                        changersalle=1
                        salle=16
                        os.system('cls')
                            
                if action=="Sud" or action=="sud":
                    print("C'est la sortie, mais la porte ne bouge pas. Vous remarquez une grande serrure. Vous aurez sans doute besoin de trouver la clef pour vous échapper !")           
                          
                if action=="Nord" or action=="nord":
                    changersalle=1
                    salle=13
                    os.system('cls')
                    
#utiliser
            if action=="utiliser" or action=="Utiliser":
                print("Vous possedez ", potion," potions de soin, ")
                if tableau==1:
                    print("Vous avez noté l'inscription derière le tableau") 
                action=input("Que voulez vous utiliser ?")
                if action=="potion" or action=="Potion":
                    if potion>0:
                        vie=viemax
                        potion=potion-1
                    else : print("Vous n'avez pas de potion à utiliser")
                if action=="tableau" or action=="Tableau":
                    if tableau==1:
                        print("L'inscription mystérieuse derrière le tableau disait : ''Tout commence au PONANT et finit à l'ORIENT, celui du SUD précède celui de l'EST''")
               
                if action=="porte" or action=="Porte" or action=="clef" or action=="Clef" or action=="clé" or action=="Clé":
                    if clefrdc==1:
                        print ("Vous décrochez la clef de votre ceinture, l'approchez de la serrure de cette grande porte qui devrait mener à votre liberté ...")
                        passer=input("(Entrez n'importe quelle touche pour continuer.")
                        os.system('cls')
                        print ("Mais au moment ou vous entrez la clef dans la serrure, un bruit monstrueux résonne dans tout le manoir, le sol et les murs tremblent alors que vous reculez jusqu'au centre de la pièce, arme au clair, regardant dans toutes les directions...")
                        passer=input("(Entrez n'importe quelle touche pour continuer.")
                        os.system('cls')
                        print ("C'est alors que vous voyez un homme arme au clair s'approcher de vous ... Sa démarche est lente et familière et il est entouré d'une sorte d'aura maléfique ...")
                        passer=input("(Entrez n'importe quelle touche pour continuer.")
                        os.system('cls')
                        print ("Il s'arrête à quelques mètres de vous et enlève son casque pour découvrir des traits étrangement familiers et un sourire carnassier. Il vous lance : ''Tu comprends maintenant ?''")
                        passer=input("Oui/Non")
                        if passer=="Oui" or passer=="oui":
                            print("Tu sais donc qui je suis ...")
                            passer=input("Oui ... Tu es ")
                            if passer=="Moi" or passer=="moi" or passer=="Moi même" or passer=="moi même" or passer=="Ma folie" or passer=="ma folie" or passer=="fou" or passer=="Fou" or passer=="ma maladie" or passer=="Ma maladie" or passer=="malade" or passer=="Malade" :
                                print ("Exactement ... et il ne peut exister qu'un seul de nous deux ... Alors, en garde !")
                                score=score+10
                            else : print("Mhhhh ... Ce n'est pas grave ... Quoi qu'il en soit il ne peut exister qu'un seul de nous deux ... Alors, en garde !")
                        else : print("Mhhhh ... Ce n'est pas grave ... Quoi qu'il en soit il ne peut exister qu'un seul de nous deux ... Alors, en garde !")
                        passer=input("(Entrez n'importe quelle touche pour continuer.")             
                        os.system('cls')
                        issue=0
                        k=0
                        while (issue!=1):
                            if k==0:    
                                print("Votre adversaire se jette sur vous alors qu'une sorte de bulle maléfique vous englobe, empechant toute fuite")
                                combat(attaque, vie, defense, viemax, attaque, defense, potion, carte)
                                vie=vie1
                                potion=potion1
                                carte=carte1
                            if k==1:
                                print("Le combat continue alors que vous et votre adversdaire êtes toujours dans la bulle maléfique empechant toute fuite")
                                combat(attaque, vie, defense, vie, attaque, defense, potion, carte)
                                vie=vie1
                                potion=potion1
                                carte=carte1
                            if issue==3:
                                vie=viemax
                                score=score-1
                                print("Vous tombez sous les coups de votre adversaire ... Soudain, une lueur vient vous rechauffer et vous revigorer, vous vous levez et continuez à vous battre")
                                k=1
                            if issue==2:
                                print ("Vous tentez de fuir mais ne voyez aucune issue ...")
                                k=1
                        print ("''Comment ... Tu ne peux pas ... Je fais partie de toi !''")
                        print ("Votre adversaire s'affalle sur le sol et son aura maléfique se dissipe")
                        score=score+5
                        passer=input("Entrez n'importe quelle touche pour continuer")
                        os.system('cls')
                        print ("Vous vous ressaisissez et regardez en direction de la porte, elle s'ouvre lentement, laissant entrer dans la pièce une lumière aveuglante.") 
                        passer=input("Entrez n'importe quelle touche pour continuer")
                        os.system('cls')
                        print ("En passant le pas de la porte, vous êtes totalement aveuglé, en ouvrant les yeux à nouveau, vous voyez un homme en habits d'un blanc immaculé, assis en face de vous.")
                        passer=input("Entrez n'importe quelle touche pour continuer")
                        print ("Il se lève, vous reconnaissez les détails autours de vous, vous vous trouvez dans le bureau du docteur Palmers. ''Reprenons je vous prie Monsieur ", nom, "...''")
                        passer=input("Entrez n'importe quelle touche pour continuer")
                        print ("FELICITATIONS ! Vous venez de terminer le jeu ''Un voyage au Bord de la Ligne'' ! Votre score est de ",score," points ! Nous vous remercions d'avoir joué et espérons que vous avez apprécié le jeu !")
                        passer=input("Entrez n'importe quelle touche pour quitter le jeu.")
                        changersalle=1
                        salle=0
                        findujeu=1

            #Inventaire
                        
            if action=="inventaire" or action=="Inventaire":
                print("Vous posséder les objets suivants :")
                if potion>=1:
                    print(potion, "potion(s) de soin")
                if carte>=1:
                    print(carte, "Cartes de bannissement")
                if note1==1:
                    print("Note1 (la note sur l'état du manoir)")
                if note2==1:
                    print("Note2 (la note du carnet ensanglanté)")
                if tableau==1:
                    print("Note3 (la note écrite dérière le tableau)")
                if note4==1:
                    print("Note4")
                if note5==1:
                    print("Note5")
                if clefrdc==1:
                    print("La clef du rez de chaussée")
                if gant==1:
                    print("Un gant")
                    
                action=input("Que souhaitez-vous utiliser ? ")
                
                if action=="potion" or action=="Potion":
                    if potion>0:
                        vie=viemax
                        potion=potion-1
                    else : print("Vous n'avez pas de potion à utiliser")
                if action=="note1" or action=="Note1":
                    if note1==1:
                        print(textenote1)
                if action=="note2" or action=="Note2":
                    if note2==1:
                        print(textenote2)
                if action=="note3" or action=="Note3":
                    if note3==1:
                        print(textenote3)
                if action=="note4" or action=="Note4":
                    if note4==1:
                        print(textenote4)
                if action=="note5" or action=="Note5":
                    if note5==1:
                        print(textenote5)
                if action!="note1" and action!="Note1" and action!="note2" and action!="Note2" and action!="note3" and action!="Note3" and action!="note4" and action!="Note4" and action!="note5" and action!="Note5" and action!="potion" and action!="Potion":
                    print("Vous ne pouvez pas utiliser cet objet ici")



#SALLE 16-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


    if salle==16:
        if osalle16==0:
            changersalle=0
            osalle16=1
            print("Vous vous trouvez devant la porte barricadé. De l'autre côté se trouve la salle donnant sur la sortie.")

        dé_n(10)
        if résultatdé<=6:
            dé_n(10)
            if résultatdé<=3:
                print("Vous entendez des claquements d'os dans la pièce...")
                print("Un squelette animé par une sorte d'aura maléfique se jette sur vous ! Vous sortez votre épée et vous appretez à vous battre")
                combat(attaque, vie, defense, 20, 3, 4, potion, carte)
            else :
                print("Des bruits de métal vous parviennent...")
                print("Une armure s'anime et commence à s'approcher de vous ! Vous sortez votre épée et vous appretez à vous battre")
                combat(attaque, vie, defense, 30, 4, 6, potion, carte)
            vie=vie1
            potion=potion1
            carte=carte1
            if issue==1:
                print ("Vous venez à bout de votre adversdaire")
                gain=gain+1
                if gain>1:
                    niveauup(attaque,defense,viemax)
                    gain=0
            if issue==2:
                print ("Vous fuyez le combat")
            if issue==3:
                print ("Vous tombez au combat ... Vous vous reveillez un peu plus tard, votre ennemi a disparu...")
                score=score-1
                vie1=viemax/2
            vie=vie1
                                 
#Bouger
            
        while changersalle==0:
            action=input("Que voulez vous faire ? ")
            if action=="bouger" or action=="Bouger" :
                action=input("Où souhaitez vous aller ?")
                        
                if action=="Ouest" or action=="ouest":
                    print("Vous enlevez la barre bloquant la porte pour accèder à la salle donnant sur la sortie")
                    changersalle=1
                    salle=17
                    os.system('cls')
                        
                if action=="Est" or action=="est":
                    print("Il n'y a rien à l'Est")
                            
                if action=="Sud" or action=="sud":
                    print("Il n'y a rien au Sud")
                    
                          
                if action=="Nord" or action=="nord":
                    ("Il n'y a rien au Nord")
                    
                if action=="descendre" or action=="Descendre":
                    changersalle=1
                    salle=6
                    os.system('cls')


#utiliser
            if action=="utiliser" or action=="Utiliser":
                print("Vous possedez ", potion," potions de soin, ")
                if tableau==1:
                    print("Vous avez noté l'inscription derière le tableau") 
                action=input("Que voulez vous utiliser ?")
                if action=="potion" or action=="Potion":
                    if potion>0:
                        vie=viemax
                        potion=potion-1
                    else : print("Vous n'avez pas de potion à utiliser")
                if action=="tableau" or action=="Tableau":
                    if tableau==1:
                        print("L'inscription mystérieuse derrière le tableau disait : ''Tout commence au PONANT et finit à l'ORIENT, celui du SUD précède celui de l'EST''")
                if action=="barrière" or action=="Barrière" or action=="barriere" or action=="Barriere":
                    print("Vous retirez la barrière et libérez le passage vers l'ouest.")
                    barriere16=0


            #Inventaire
                        
            if action=="inventaire" or action=="Inventaire":
                print("Vous posséder les objets suivants :")
                if potion>=1:
                    print(potion, "potion(s) de soin")
                if carte>=1:
                    print(carte, "Cartes de bannissement")
                if note1==1:
                    print("Note1 (la note sur l'état du manoir)")
                if note2==1:
                    print("Note2 (la note du carnet ensanglanté)")
                if tableau==1:
                    print("Note3 (la note écrite dérière le tableau)")
                if note4==1:
                    print("Note4")
                if note5==1:
                    print("Note5")
                if clefrdc==1:
                    print("La clef du rez de chaussée")
                if gant==1:
                    print("Un gant")
                    
                action=input("Que souhaitez-vous utiliser ? ")
                
                if action=="potion" or action=="Potion":
                    if potion>0:
                        vie=viemax
                        potion=potion-1
                    else : print("Vous n'avez pas de potion à utiliser")
                if action=="note1" or action=="Note1":
                    if note1==1:
                        print(textenote1)
                if action=="note2" or action=="Note2":
                    if note2==1:
                        print(textenote2)
                if action=="note3" or action=="Note3":
                    if note3==1:
                        print(textenote3)
                if action=="note4" or action=="Note4":
                    if note4==1:
                        print(textenote4)
                if action=="note5" or action=="Note5":
                    if note5==1:
                        print(textenote5)
                if action!="note1" and action!="Note1" and action!="note2" and action!="Note2" and action!="note3" and action!="Note3" and action!="note4" and action!="Note4" and action!="note5" and action!="Note5" and action!="potion" and action!="Potion":
                    print("Vous ne pouvez pas utiliser cet objet ici")


#Regarder

            if action=="Regarder" or action=="regarder":
                if barrière16==0:
                    print("Vous cherchez dans les différents rangements si vous ne trouvez pas quelque chose d'intéressant. Vous remarquez au fond de la salle un petit COFFRE brillant.")
                    coffre2=1
                if coffre2==1:
                    if action=="Regarder" or action=="regarder":
                        print("Le COFFRE brillant se trouve toujours au fond de la salle")  
