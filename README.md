# REI_Defis

## Défis 1:
À l'aide de python, vous devrez développer une fonction qui pourra calculer les 2000 premières décimales de pi. Voici vos critères:
- Vous devrez calculer les 2000 premières décimales de pi;
- Vous devrez utiliser python;
- Votre code doit être contenus dans un seul fichier;
- Votre code doit être exécutable à partir de la fonction `main()`;
- La fonction `main()` doit renvoyer un string qui contient pi et ses 2000 premières décimales et dont tous les caractères sont des chiffres (excepté la virgule);
- Votre code doit être le plus rapide possible.
- Les résultas **ne peuvent pas** être pré-calculés. Le cas échéant, la soumission sera exclue.

Notez que python ne supporte pas les chiffres au-delà d'une précision d'autour de 18 décimales. Vous devrez donc inventer votre propre système de calcul.

## Défis 2:
À l'aide de python, vous devrez développer une fonction qui compte le nombre le plus grand possible. Voici vos critères :
- Vous devrez calculer le nombre le plus grand possible;
- Vous devrez utiliser python;
- Votre code doit être contenus dans un seul fichier;
- Ledit fichier devra faire moins de 4Ko;
- Votre code devra exécuter en moins de 10 secondes. **Notez que votre machine exécutera votre programme à une vitesse différente de celle qui sera utilisé pour évaluer votre soumission. Donnez-vous donc une marge de manoeuvre de 2-3 secondes.**;
- Votre code doit être exécutable à partir de la fonction `main()`;
- La fonction `main()` doit renvoyer un int.

## Défis 3:
À l'aide de python, vous devrez lire un fichier .txt qui contient un livre `Décider quel livre`. Vous devrez analyser ce fichier .txt afin d'extraire les informations suivantes:
- La fréquence de chaque lettre dans le fichier;
- La fréquence de chaque lettre comme première lettre d'un mot;
- La fréquence de chaque lettre comme dernière lettre d'un mot;
- La fréquence de chaque mot dans le fichier;
Voici vos critères:
- Vous devrez utiliser python;
- Votre code doit être contenu dans un seul fichier;
- Votre code doit accéder au fichier localement, dans le même dossier. *( Utilisez la fonction python* `open("fichier.txt")` *)*
- Votre code doit être exécutabla à partir de la fonction `main()`;
- La fonction `main()` doit renvoyer une liste bi-dimensionnelle sous la forme suivante :
  ```
  liste = [
  ["""Fréquence de chaque lettre""" (a : 0.15), (b : 0.56), ...],
  ["""Fréquence de chaque lettre au début du mot""" (a : 0.15), (b : 0.56), ...],
  ["""Fréquence de chaque lettre à la fin du mot""" (a : 0.15), (b : 0.56), ...],
  ["""Fréquence de chaque mot""" ("le" : 0.15), ("ma" : 0.56), ...]
  ]
  ```
- Le code doit être le plus rapide possible;
- Les résultas **ne peuvent pas** être pré-calculés. Le cas échéant, la soumission sera exclue.

## Défis 4:
À l'aide de python, vous devrez effectuer la multiplication de matrices de transformations 4x4 et d'un vecteur à 4 dimensions, le plus rapidement possible. Voici les détails de la tâche:

Le calcul à effectuer sera le suivant : P * V * T * p, où P est une matrice de projection 4x4, V est une matrice de transformation de caméra 4x4, T une matrice de transformation de 
modèle 4x4 et p un vecteur de position de sommet à 4 dimensions.
Les objets possèdent la structure suivante :
```
# x indique une valeur variable
P            V            T            p
[            [            [            [
[1,0,0,0],   [x,x,x,0],   [x,x,x,0],   x,
[0,x,0,0],   [x,x,x,0],   [x,x,x,0],   x,
[0,0,x,x],   [x,x,x,0],   [x,x,x,0],   x,
[0,0,x,1]    [x,x,x,1],   [x,x,x,1],   1
]            ]            ]            ]

La matrice est organisée comme suit :
Représentation     
classique          Représentation
mathématique       dans le code
|-       -|        [
| a b c d |        [a,e,i,m],
| e f g h |   =>   [b,f,j,n],
| i j k l |        [c,g,k,o],
| m n o p |        [d,h,l,p],
|-       -|        ]
```
Voici vos critères:
- Votre code devra multiplier trois matrices de dimensions 4x4 et un vecteur de dimensions 4 ensemble;
- Vous devrez utiliser python;
- Votre code doit être contenu dans un seul fichier;
- Votre code doit être exécutable depuis la fonction `main()`;
- La fonction `main` doit avoir la signature suivante : `def main(P : list[list[float]], V : list[list[float]], T : list[list[float]], p : list[float]) -> list[float]`;
- La fonction `main` doit renvoyer un vecteur à 4 dimensions sous la forme d'une `list[float]`;
- Votre code doit exécuter le plus rapidement possible;
- **L'utilisation de bibliothèques de calcul vectoriel est interdite**. *Le cas échant, la soumission sera rejetée.*
