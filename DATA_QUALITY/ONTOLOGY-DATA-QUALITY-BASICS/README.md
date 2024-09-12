# Notions de base d'ontologie et qualité des données 

## 1. Ontologie :

### 1.1. Définition d'une Ontologie :

L'`ontologie` est une représentation formelle et explicite des concepts et de leurs interrelations dans un domaine particulier. Par exemple, dans le domaine médical, une ontologie pourrait définir des concepts tels que `Maladie`, `Traitement`, et `Symptôme`, ainsi que les relations entre eux.

### 1.2. Langages d'Ontologie :

#### RDF (Resource Description Framework) :

Exemple : Considérons une déclaration RDF : <Personne> a <Âge> de <30 ans>. Cela indique qu'une instance de la classe `Personne` a une propriété `Âge` égale à `30 ans`.

Exemple de vocabulaire RDF : https://github.com/InseeFr/Ontologies

#### OWL (Web Ontology Language) :

Exemple : En utilisant OWL, nous pourrions définir que toute instance de la classe "Personne" a exactement un âge de type entier : Personne `SubClassOf` a une Âge exactly 1 xsd:integer.

### 1.3. Classes, Instances, Propriétés :

- Classes : Dans une `ontologie médicale`, la classe `Maladie` pourrait avoir des sous-classes telles que `Cancer` et `Diabète`.
  
- Instances : Une instance de la classe `Cancer` pourrait être une entité spécifique appelée `Cancer du sein`.
  
- Propriétés : Une propriété `A pour Symptôme` pourrait relier une instance de `Maladie` à une instance de `Symptôme`.

### 1.4. Alignement d'Ontologies :

Exemple : Supposons que vous ayez deux `ontologies différentes`, l'une décrivant les propriétés des `voitures` et l'autre décrivant les propriétés des `véhicules` en général. L'alignement pourrait établir que le concept `Roue` dans la première `ontologie` est équivalent au concept `Roue` dans la seconde `ontologie`.

### 1.5. Applications d'Ontologies :

Exemple : Dans le domaine de la finance, une `ontologie` peut être utilisée pour représenter les relations entre les entités financières telles que `Banque`, `Client` et `Transaction`, facilitant ainsi l'analyse des données financières.

## 2. Qualité des Données :

### 2.1. Dimensions de la Qualité des Données :

#### Précision :

Exemple : La valeur `35,6 degrés Celsius` enregistrée comme température corporelle doit être précise et exacte.

#### Complétude :

Exemple : Un enregistrement de patient avec tous les champs obligatoires (`nom, date de naissance, adresse`) est complet.

#### Cohérence :

Exemple : Si un système a des enregistrements contradictoires sur l'âge d'une personne, il y a une incohérence à résoudre.

### 2.2. Évaluation de la Qualité des Données :

#### Profiling des données :

Exemple : L'analyse statistique des données de vente peut révéler des valeurs aberrantes qui nécessitent une attention particulière.

#### Cleansing des données :
Exemple : Un processus de nettoyage peut corriger les `erreurs typographiques` dans les noms de produits.

### 2.3. Gestion de la Qualité des Données :

#### Politiques et normes :

Exemple : Une politique pourrait spécifier que toutes les `adresses e-mail` doivent être valides et suivre un format spécifique.

#### Responsabilités :

Exemple : Un responsable de la qualité des données pourrait être chargé de superviser les activités de gestion de la qualité.

#### Outils de qualité des données :

Exemple : L'utilisation d'`outils automatisés` pour détecter et corriger les erreurs de données, comme les doublons ou les valeurs aberrantes.

#### Intégration Ontologie et Qualité des Données :

Exemple : En utilisant une `ontologie` pour définir la structure et les relations des données, on peut garantir une meilleure qualité en évitant les ambigüités et en normalisant la représentation des informations.
