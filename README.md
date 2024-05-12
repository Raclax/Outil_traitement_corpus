# Outil_traitement_corpus

## La tâche à réaliser
J'ai décider que travailler sur de la classification pourrait être intéressant, puisque cela suppose de définir des caractéristiques bien distinctes pour chaque catégorie, ce qui peut mener à débat parfois.

En l'occurence, j'ai choisi de travailler sur des reviews laissées par des internautes sur internet et la gradation, sur un système d'étoiles, qu'ils ont associés à leur commentaire.

## Le corpus
J'ai trouvé plusieurs corpus qui pouvaient répondre à cette description, notamment issus de Yelp ou de Trivago, mais j'ai finalement choisi de partir avec le corpus <a href="https://huggingface.co/datasets/mteb/amazon_reviews_multi">"amazon_reviews_multi"</a>. 

Il s'agit d'un corpus qui regroupe evniron 1 800 000 commentaires laissés sur le site Amazon, en anglais, allemand, français, espagnol, chinois ou japonais, associés à leur note /5. Chaque note (0, 1, 2, 3, 4) est associée à exactement 20% du corpus, sout environ 360 000 commentaires. Le dataset est réparti en train/dev/test : il contient 1 200 000 lignes destinées à l'entrainement, 30 000 pour la validation et 30 000 pour le test.

Il est structuré sous la forme d'un dictionnaire par commentaire avec en première clé 'id' associé à l'identifiant du client, en seconde 'text' associé au texte, puis 'label' pour la note laissée, et 'label_text' pour la note mais en type string cette fois.

La taille totale de ce corpus est de 918 MB.

Ce corpus, on l'imagine bien peut facilement être utilisé dans le cas de l'entrainement et du test d'un modèle qui tente de prédire la note en fonction du commentaire, ou même plus largement la polarité ou les sentiments d'un message.

## Modèles qui l'ont utilisé
Ce coprus à servi à entrainer et tester plus de 85 modèles, tels que <a href="https://huggingface.co/nixiesearch/nixie-querygen-v2">"nixie-querygen-v2"</a>, qui est un algorithme de classification, ou encore <a href="https://huggingface.co/arnabdhar/distilbert-base-amazon-multi">"bert-base-amazon-multi"</a>, la version entrainée avec ce corpus du modèle bert-base-multilingual-cased, pour la prédiction de phrases et de labels.

## Infos suplémentaires 
* La page HuggingFace de ce corpus ne contient par d'informations dans son README.md, mais il existe sur HuggingFace unautre modèle qui porte exactement le même nom, 'amazon_reviews_multi', qui pourrait être une autre version de ce dataset : il récupère des avis des mêmes langues et balance également son corpus sur la répartition des avis en fonction de sa note (20% pour chaque).