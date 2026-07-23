# Gestion d'un magasin de fruits et légumes

Ce projet Python permet de simuler les ventes d'un magasin de fruits etlégumes.

## L'application doit permettre :

- d'afficher le catalogue des produits ;
- d'enregistrer plusieurs clients ;
- de sélectionner un produit et une quantité ;
- de vérifier si la quantité demandée est disponible ;
- de mettre à jour le stock après un achat ;
- de calculer le montant du ticket d'un client ;
- d'afficher le bilan total des ventes.

## Technologies utilisées

Python 3
Programmation orientée objet
Aucune bibliothèque externe n'est nécessaire.

## Structure du projet

.
├── main.py       # Logique principale et déroulement des ventes
├── product.py    # Classe Product représentant un produit
├── purchase.py   # Classe Achat représentant une ligne d'achat
├── client.py     # Classe Client et gestion de son ticket
├── display.py    # Fonctions d'affichage
└── test.py       # Catalogue de fruits et légumes utilisé pour les tests

## Modèle de données

### Produit

Un produit possède :
- un nom ;
- une catégorie (Fruit ou Légume) ;
- une quantité en stock ;
- un prix unitaire ;
- une unité (kg ou pièce).

#### Exemple :

Product("Clémentine", "Fruit", 6, 2.90, "kg")

#### Méthodes

Une méthode pour l'affichage des information du produit.
Et une autre pour la mise a jour des stock


### Achat

Un achat contient :
- un objet produit
- la quantité que le client souhaite acheter
 
Il y a une méthode pour afficher les informations du produit et la somme de l'achat du client.
La classe posséde une méthode qui calcule le prix : prix = produit.price * quantite.

### Client

Un client possède :
- un nom ;
- un prénom ;
- un ticket contenant ses achats ;
- le montant total de ses achats.

La classe possede une méthode pour afficher les information du client et une autre.
Une méthode pour gérer les achats et ajouter les informations sur le tikcet et
mettre à jour le montant à payer
