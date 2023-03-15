

from main import temps_routes
from main import temps_routes_opti
"""
-------------------------------------
    Ce document présente les réponses aux questions des TP 1 et 2
    Dans ce fichier, on trouvera uniquement les explications (notamment
    concernant les complexités), et l'endroit dans le code où se trouve
    les algorithmes et les tests que nous avons implémentés.

    Au début de chaque fonction ou de chaque test, dans les fichiers main,
    graph et les test on trouvera un commentaire détaillé. Cette page est
    juste un résumé

    La séance 3 n'a pas encore été traitée, malgré le fait que nous
    trouvions bien des temps de l'ordre de la minute pour tous les fichiers
    routes.
-------------------------------------
"""

"""
-------------------------
    Question 1
    On implémente add_edge et  graph_from_file dans le fichier graph
    On a réutilisé les fonctions données par l'enseignant

    Nous passons le test donné test_s1q1_graph_loading
"""

"""
-------------------------
    Question 2

    On répond en deux temps. Dans un premier on crée dans la classe graph la
    fonction parcours_en_profondeur qui à un sommet donne tous les sommets
    accessibles par un chemin.
    Cette fonction nous permet ensuite de trouver les différentes composantes
    connexes. En effet en partant d'un sommet, le parcours en profondeur
    nous donne tous les éléments de la composante connexe.

    Nous passons le test donné test_s1q2_connected_components

"""

"""
-------------------------
    Question 3

    On utilise le principe de la file pour parcourir le graph et trouver le
    chemin.
    On utilise pour cela les fonctions get_path_with_power et voisin_acc dans
    le fichier graph

    En ce qui concerne la complexité de l'algorithme :

    Si l'on considère que nous avons N nodes, alors il y'a N-1 voisins
    possibles pour un node dans le pire des cas, et l'opération la plus
    coûteuse dans la boucle while est celle réalisée par la fonction
    voisin_acc, la complexité de celle-ci étant le nombre de voisin d'un node
    (boucle for + coût unitaire dans la boucle) on a alors une compléxité pour
    voisin_acc en O(N), de plus la boucle while parcours toutes les nodes du
    graph, ainsi la compléxité est en O(N²) pour la fonction
    get_path_with_power


    Nous passons avec succès les tests donnés dans test_s1q3_node_reachable
    Nous passons également nos propres tests dans
    le fichier Test get path with power

"""

"""
-------------------------
    Question 4

    Le code modifié est dans la fonction graph_from_file dans le fichier graph
    On implémente un test pour voir si on arrive à ouvrir correctement
    network04. On implémente ce test dans le fichier test_s1q4_graph_loading2

    On passe avec succès le test

"""


"""
-------------------------
    Question 5

    On implémente l'algorithme de dijkstra

    Cet algorithme ayant été rajouté tardivement, nous ne l'avons
    pas encore commenté. Il consiste en 4 fonctions.
    Elles se trouve tout à la fin de la class graph sur le fichier graph
    (Des commentaires indiquent le début et la fin)

    Nous avons créé un test (Test dijkstra) que nous passons avec succès

"""

"""
-------------------------
    Question 6

    On crée la fonction min_power dans le fichier graph, en 
    utilisant get_path_with_power de la question 3

    En ce qui concerne la complexité :

    Notons P la valeur de la puissance maximale des arêtes, la recherche
    exponentielle sur P est en O(log(P)) tandis que à chaque itération,
    la fonction get_path_with_power dont la compléxité est en O(n²)
    est appelée, la boucle while qui effectue la recherche dichotomique a un
    coût en log(P) et à chaque itération, la fonction get_path_with_power est
    appelée, finalement la complexité de min_power est en O(n²*log(P))

    Nous passons bien le test donné test_s1q6_minimal_power
    Nous passons également le test que nous avons créé Test_min distance

"""

"""
-------------------------
    Question 7

    Bonus, non traité

"""

"""
-------------------------
    Question 8

    Nous passons l'ensemble des tests donnés.
    Nous avons également créés des tests pour les algorithmes :
    - Test get path with power
    - Test graph_from_file
    - Test min_distance
    - Test kruskal

    Les explications sur ces tests sont fournis dans les fichiers des tests

"""

"""
-------------------------
    Question 9

    Bonus, non traité

"""

"""
-------------------------
    Question 10

    Dans le fichier main, on implémente la fonction temps_routes qui calcule
    pour chaque fichier, le temps nécéssaire pour calculer les min_power
    de l'ensemble des trajets (on en calcule 10, et on ramène ça au nombre
    de trajets total).
    On trouve le temps avec les print ci-dessous.

    Pour routes1, on trouve 0.01 secondes
    Pour routes2, on trouve environ 8 500 heures 
    (on a laissé tourner, et on a trouvé exactement 31883861 secondes)

    Pour une raison inconnu ce temps était auparavant de 30h, mais
    depuis une modification de get_path_with_power, il est devenu beaucoup plus
    long.
    Faire tourner routes3, routes4, ..., serait bien trop long (même si avec
    des print dans les fonctions, on observe qu'on avance bien,
    juste très lentement)

    Ces temps sont beaucoup trop longs, mais on va améliorer cela par la suite
    avec succès.

"""
#print(temps_routes("input/routes.1.in", "input/network.1.in"))
# print(temps_routes("input/routes.2.in", "input/network.2.in"))
# etc.

"""
-------------------------
    Question 11

    Bonus, non traité

"""

"""
-------------------------
    Question 12

    On commence par implémenter Union-find qui nous servira pour la fonction 
    kruskal.
    Cela correspond aux fontions find et union dans la class graph du fichier
    graph

    On crée ensuite la fonction kruskal dans cette même class.

"""

"""
-------------------------
    Question 13

    On implémente un test de la fonction kruskal.
    Ce test se trouve dans le fichier Test kruskal.

    Vérifier que l'arbre est bien l'arbre couvrant minimal est assez
    dur. Par contre on peut vérifier qu'on a bien le bon nombre
    d'arêtes, c'est-à-dire le nombre de sommets - 1

    Avec cette méthode on peut vérifier pour des graph très grands comme
    network 3 !

    A propos de la complexité :

    La boucle sur toute les aretes est uniquement de complexité  o(V-1)
    avec V le nombre de noeuds. En effet on s'arretera dès qu'on aura
    fait V-1 itérations. Ce temps est liénaire

    Par contre le tri de la liste des aretes au début est de complexité
    o(Elog(E)) avec E le nombre d'arêtes dans le graph initial.
    et E >= V
    Donc la complexité totale de l'algorithme est bien o(Elog(E))

"""

"""
-------------------------
    Question 14

    Maintenant que l'on a un arbre couvrant minimal.
    Tout d'abord, on a moins d'aretes, et donc les parcours du graphe
    seront plus court.

    On cherche à améliorer la fonction min_power qui n'était pas
    satisfaisante.

    La première idée, naive, consiste à utiliser le fait que
    l'on sait qu'il est existe un seul chemin entre deux noeuds.
    On peut réécrire get_path sans avoir à chercher les voisins accessibles
    avec le power, ce qui réduit la complexité de l'algorithme.
    Ensuite on récupère le power max croisé sur ce chemin et ce
    sera notre min power.
    Nous avions ainsi créé dans un premier temps get_path_mst
    et min_power_mst dans le fichier graph

    Mais on peut faire bien mieux, car ici on parcourt
    encore beaucoup de branches inutiles de l'arbre

    On va plutôt chercher à utiliser la notion de profondeur. On va recréer
    un arbre avec un sommet et des noeuds plus ou moins profond.
    Trouver le chemin entre deux noeuds se fait en trouvant
    l'ancêtre commun le plus proche. Ainsi on ne fait que
    remonter l'arbre (qui est maintenant orienté en quelque sorte)
    vers le parent jusqu'à trouver l'ancêtre commun.
    Ainsi, on ne visite plus les branches inutiles !
    
    On crée ainsi la fonction min_power opti dans le fichier graph

"""


"""
-------------------------
    Question 15

    On implémente dans le fichier main une mesure du temps pour la
    fonction min_power_opti. Cette fonction se nomme temps_routes_opti.

    Routes1: 0.00 s
    Routes2: 2.13 s
    Routes3: 32.28 s
    Routes4: 31.19 s
    Routes5: 8.49 s
    Routes6: 40.06 s
    Routes7: 59.93 s
    Routes8: 39.83 s
    Routes9: 27.44 s

    Ces temps sont bien meilleurs !

    Ici on ne compte pas le temps de créer l'arbre à partir du graph,
    mais cela ne prend pas plus d'une dizaine de secondes ...

"""
#print(temps_routes_opti("input/routes.1.in", "input/network.1.in"))
#print(temps_routes_opti("input/routes.7.in", "input/network.7.in"))
#print(temps_routes_opti("input/routes.8.in", "input/network.8.in"))
#print(temps_routes_opti("input/routes.9.in", "input/network.9.in"))