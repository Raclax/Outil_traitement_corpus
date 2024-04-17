# Outil_traitement_corpus

## La tâche à réaliser
J'ai décider que travailler sur de la classification pourrait être intéressant, puisque cela suppose de définir des caractéristiques bien distinctes pour chaque catégorie, ce qui peut mener à débat parfois.

En l'occurence, j'ai choisi de travailler sur des reviews laiss&es par des internautes sur internet et la gradation, sur un système d'étoiles, qu'ils ont associés à leur commentaire.

## Le corpus
J'ai trouvé plusieurs corpus qui pouvaient répondre à cette description, notamment issus d'Amazone ou de Trivago, mais j'ai finalement choisi de partir avec le corpus <a href="https://huggingface.co/datasets/yelp_review_full">"yels_review_full"</a>. 

Il s'agit d'un corpus qui regroupe evniron 700 000 commentaires laissés sur le site Yelp, en anglais, associés à leur note /5. Chaque note (1, 2, 3, 4, 5) est associée à 130 000 commentaires destinés à l'entrainement et 10 000 au test.
IL est structuré sous la forme d'un dictionnaire par commentaire avec en première clé 'label' associé à sa valeur, egt en seconde 'text' associé au texte.
Ce corpus, on l'imagine bien peut facilement être utilisé dans le cas de l'entrainement et du test d'un modèle qui tente de prédire la note en fonction du commentaire, ou même plus largement la polarité ou les sentiments d'un message.

## Modèles qui l'ont utilisé
Ce coprus à servi à entrainer et tester plus de 85 modèles, tels que <a href="https://huggingface.co/sileod/deberta-v3-base-tasksource-nli">"deberta-v3-tasksource-nli"</a>, qui est un algorithme de classification, ou encore bert-base-uncased-yelp-reviews, la version entrainée avec ce corpus du modèle bert-base-uncased.

## Infos suplémentaires 
* Ce corpus a été construit à partir des données reucueillies lors du Yelp Dataset Challenge de 2015, durant lequel les étudiants ont l'opportunité d'utiliséer les données de Yelp pour mener leurs propres recherches.