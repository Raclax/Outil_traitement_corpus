# Outil_traitement_corpus

## La tâche à réaliser
J'ai décider que travailler sur de la classification de texte pourrait être intéressant, puisque cela suppose de définir des caractéristiques bien distinctes pour chaque catégorie, ce qui peut mener à débat parfois.

En l'occurence, j'ai choisi de travailler sur des reviews laissées par des internautes sur internet et la gradation, sur un système d'étoiles, qu'ils ont associés à leur commentaire.

### Le corpus
J'ai trouvé plusieurs corpus qui pouvaient répondre à cette description, notamment issus de Yelp ou de Trivago, mais j'ai finalement choisi de partir avec le corpus <a href="https://huggingface.co/datasets/mteb/amazon_reviews_multi">"amazon_reviews_multi"</a>. 

Il a été publié sur HuggingFace en 2022 par Niklas Muennighoff, Loïck BOURDOIS  et Nouamane Tazi.

Il s'agit d'un corpus qui regroupe evniron 1 800 000 commentaires laissés sur le site Amazon, en anglais, allemand, français, espagnol, chinois ou japonais, associés à leur note /5. Chaque note (0, 1, 2, 3, 4) est associée à exactement 20% du corpus, sout environ 360 000 commentaires. Le dataset est réparti en train/dev/test : il contient 1 200 000 lignes destinées à l'entrainement, 30 000 pour la validation et 30 000 pour le test.

Il est structuré dans un format JSON, qui recence l''id' associé à l'identifiant du client, le 'text' associé au texte, puis 'label' pour la note laissée, et 'label_text' pour la note mais en type string cette fois.

La taille totale de ce corpus est de 918 MB.

Ce corpus, on l'imagine bien peut facilement être utilisé dans le cas de l'entrainement et du test d'un modèle qui tente de prédire la note en fonction du commentaire, ou même plus largement la polarité ou les sentiments d'un message.

### Modèles qui l'ont utilisé
Ce coprus à servi à entrainer et tester plus de 85 modèles, tels que <a href="https://huggingface.co/nixiesearch/nixie-querygen-v2">"nixie-querygen-v2"</a>, qui est un algorithme de classification, ou encore <a href="https://huggingface.co/arnabdhar/distilbert-base-amazon-multi">"bert-base-amazon-multi"</a>, la version entrainée avec ce corpus du modèle bert-base-multilingual-cased, pour la prédiction de phrases et de labels.

### Infos suplémentaires 
* La page HuggingFace de ce corpus ne contient par d'informations dans son README.md, mais il existe sur HuggingFace unautre modèle qui porte exactement le même nom, 'amazon_reviews_multi', qui pourrait être une autre version de ce dataset : il récupère des avis des mêmes langues et balance également son corpus sur la répartition des avis en fonction de sa note (20% pour chaque).


## Récupération des données  

### Le script de récupération
Le script de récupération est situé dans src/script/recuperation.py

J'ai d'abord fait un script pour trouver comment récupérer les informations que je voulais (note, commentaire, id de pa personne) qu'on peut retrouver dans src/tests/testmodele1.py

Mon dataset était à l'origine sur des données récupérées sur Yelp mais suite à des problèmes d'API sur ce site (je me suis fait ban), j'ai du changer pour un datset fait sur Amazon. Mon script fonctionnait très bien sur Yelp, bien que l'architecture était différente. Mais lorsque j'ai essayé de le faire confctionner sur Amazon, ce qui était récupéré de chaque page était incompréhensible. Le site doit prévenir du scrppping en provoquant des soucis d'encodages.
Ainsi donc, les codes de recuperation.py et testmodele1.py fonctionnent en théorie mais pas en partique. J'ai décidé de les laisser sur mon git mais d'utiliser le corpus d'HuggingFace directement pour les autres TP.

### Les autres TPs
J'ai crée un notebook pour réaliser le TP3 puis ai simplement continué à l'utiliser pour le reste des TPs.

On peut le retrouver dans scripts/process/traitement/données.ipynb

Il s'agit d'abor de le récupérer et le ocnvertir en dataframe.

Une des métriques qui pourrait être intéressantes pour ce corpus est d'évaluer la répartition du nombre de commentaires par langue et par notes.

Ensuite j'ai effectué le calcule de la corrélation et de la p value entre la longueur du commentaire et sa note : on peut émettre l'hypothèse que plus la note est mauvaise, plus l'acheteur est mécontent donc plus il aura de cohses à écrire dans ce commentaire. Cea a demandé d'abord de tokeniser les commentaires, mais puisqu'il s'agit d'un corpus multilingue je me suis dit que le plus simple était de couper les tokens aux espaces, même si c'est pas très précis. 

 Les résultats ne paraissent par très concluents donc on va essayer de voir cela directement par une représentation graphique (résultat à retrouver dans figures/label_taille_graph.png). Finalement notre hypothèse est fausse comme on le voit ensuite avec la moyenne de la longueur des commentaires par notes.

On élimine ensuite les valeurs abérantes, on augmente les données (cellule un peu longue à faire tourner vu que le corpus est déjà bien fourni) en utilisant des synonymes et en concaténant les nouveaus éléments aux anciens. ON arrive à un corpus à peu près deux fois plus long. On sépare ensuite en train et test (80/20).

Enfin, comme dernière mesure, on va essayer de comparer les entités nomées les plus récurentes en fonction du label.