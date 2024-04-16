(English below)

# __Python-pour-la-Data-Science__

Vous trouverez dans ce répertoire le projet réalisé par Valentin Smague et Clément Gadeau, qui essaie de donner une réponse à la question suivante : *Peut-on à partir de données quantitatives sur un morceau, prédire le genre musical auquel il appartient ?*

  - follow_me.ipynb est le notebook qui présente l'intégralité de notre projet. Tout le contenu du projet est accessible depuis le notebook.

  - function.py est un fichier python qui répertorie toutes les fonctions utilisées au cours du projet. Le code de chaque fonction est retranscrit dans le notebook, à l'exception de get_features_labels. Ce fichier est un simple répertoire de fonctions et n'apporte pas plus d'informations que le notebook n'en contient.

  - df_init.csv est le data set initial assemblé de façon expérimental par notre première méthode.

  - Dataset_Genres.csv est le data set final sur lequel nous travaillerons.


Voici le plan de notre projet :
## __I. Récupérer et traiter les données__
  - Requêter l'API Spotify pour constituer un premier dataset
  - Nettoyer le dataset : identifier un genre unique pour chaque morceau
  - Constituer un dataset muri de nos réflexions

## __II. Visualiser pour comprendre les données__
  - Vérifier la bonne répartition des genres musicaux
  - Comprendre le lien entre les variables et les genres
  - Mettre en évidence ces relations

## __III. Modéliser la prédiction du genre__
  - Random Forest
  - XGBoost

### __Conclusion__


# Python-for-Data-Science

In this repository, you will find the project carried out by Valentin Smague and Clément Gadeau, which attempts to answer the following question: *Can we predict the musical genre of a piece based on quantitative data?*

- follow_me.ipynb is the notebook presenting the entirety of our project. All the project content is accessible from the notebook.

- function.py is a Python file listing all the functions used throughout the project. The code for each function is transcribed in the notebook, except for get_features_labels. This file is a simple directory of functions and does not provide more information than what the notebook contains.

- df_init.csv is the initial dataset assembled experimentally by our first method.

- Dataset_Genres.csv is the final dataset on which we will work.

Here is the outline of our project:
## I. Retrieve and process the data
- Query the Spotify API to build an initial dataset
- Clean the dataset: identify a unique genre for each track
- Assemble a mature dataset based on our reflections

## II. Visualize to understand the data
- Check the proper distribution of musical genres
- Understand the relationship between variables and genres
- Highlight these relationships

## III. Model the genre prediction
- Random Forest
- XGBoost

### Conclusion
