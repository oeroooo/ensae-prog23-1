

"""
    Ce document présente les réponses aux questions des TP 1 et 2
    Dans ce fichier, on trouvera uniquement les explications (notamment
    concernant les complexités), et l'endroit dans le code où se trouve
    les algorithmes et les tests que nous avons implémentés

    Au début de chaque fonction ou de chaque test, on trouvera un commentaire
    détaillé. Cette page est juste un résumé
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
    fonction parcours_en_profondeur qui a un sommet donne tous les sommets
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
    XX

    Nous passons avec succès les tests donnés dans test_s1q3_node_reachable
    Nous passons également nos propres tests dans
    le fichier Test get path with power

"""

"""
-------------------------
    Question 4

    Le code modifié est dans la fonction graph_from_file dans le fichier graph
    On implémente un test pour voir si on arrive à ouvrir correctement network04.
    On implémente ce test dans le fichier test_s1q4_graph_loading2

"""


"""
-------------------------
    Question 5

    XX

"""

"""
-------------------------
    Question 6

    On crée la fonction min_power dans le fichier graph.

    Nous passons bien le test donné test_s1q6_minimal_power
    Nous passons également le test que nous avons créé Test_min distance

    En ce qui concerne la complexité : XX

"""

"""
-------------------------
    Question 7

    Non traité

"""

"""
-------------------------
    Question 8

    Nous passons l'ensemble des tests donnés.
    Nous avons également créés des tests pour les algorithmes :
    - Test get path with power
    - Test graph_from_file
    - Test min_distance

    Les explications sur ces tests sont fournis dans les fichiers des tests

"""

"""
-------------------------
    Question 9

    Non traité

"""
