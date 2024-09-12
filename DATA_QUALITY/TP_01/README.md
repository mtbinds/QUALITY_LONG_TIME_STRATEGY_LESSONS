# TP1 - Qualité de données

## Sujet du TP

Comparer deux jeux de données de climat pour déterminer la capitale européenne dont les données de température sont fournies dans le fichier `Climat.xlsx`.

On se servira du fichier `Savukoski kirkonkyla.xlsx` issu de l’`Open Data` pour servir de référence.

## Objectifs :

- Mettre en oeuvre un environnement de traitement graphique de données issues de sources plus ou moins fiables.

- Corriger un jeu de données mal formé.

- proposer un candidat potentiel pour l’origine des données.

## Déroulement :

- Pour l’échantillon `SI`, calculez :

    - moyenne par `mois`

    - écart type par `mois`

    - min /max par `mois` et par `année`

- Utilisez `Python Scipy` pour les parties mathématiques.

- Tracez les courbes de chaque mois avec une bibliothèque graphique python `Matplotlib`, `12 vues mensuelles`.

- Assemblez les courbes sur un seul graphique (`J1 -> J365`) : vue annuelle

- Présentez la valeur lue en parcourant la courbe à l'aide du pointeur,

- Présentez les valeurs précédentes par mois glissant de `30 jours` centré sur la valeur lue

- Recommencez avec le jeu `SI-erreur` après avoir corrigé les valeurs en erreur. Précisez vos méthodes.

- Les données corrigées sont elles proches des valeurs sans erreur ?

- A partir de données `opendata` du second fichier, retrouver le type de climat
    
    - Reprenez les données typiques de la localisation proche fournies en complément , comparer les écarts. 
    
    - Qu'en concluez vous ?
    
    - De quelle la capitale européenne avez vous eu les données.


## Outils : 

- Utilisez `Python + matplotlib, Jupyter` éventuellement pas de `R` ni d’autre langage :). 

-----------------

