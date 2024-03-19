# Outil_traitement_corpus

## La tâche à réaliser
J'ai décider que travailler sur de la classification pourrait être intéressant, puisque cela suppose de définir des caractéristiques bien distinctes pour chaque catégorie, ce qui peut mener à débat parfois.

En l'occurence, j'ai choisi de travailler sur les sujets abordés sur internet par des internautes en les classant en fonction de leur caractéristiques.

## Le corpus
J'ai trouvé plusieurs corpus qui pouvaient répondre à cette têhce, notamment issus de Twitter ou Reddit, mais j'ai finalement choisi de partir avec le corpus <a href="https://huggingface.co/datasets/blog_authorship_corpus">"blog_authorship_corpus"</a>. 

Il s'agit d'un corpus qui regroupe evniron 35 posts venant de 19 320 profils du site blogger.com, pour un total de 681 288 posts.
Ce qui rend ce corpus d'autant plus intéressant, c'est le fait que chaque post représente un fichier et qu'il soit associé à sa date de publication, le genre de l'auteur, son age, son signe astrologique et son emploi. De plus, chaque post contient au moins 200 occurences d'utilisation d'un mot commun du vocabulaire anglais, ce qui permet de donner des posts de taille assez conséquente et donc de rendre l'analyse plus intéressante. 
Ce corpus peut donc favilement donner à imaginer un modèle qui prédirait les mots utilisés/sujets abordés en fonction du profil de l'utilisateur, ou à l'inveerse essayer de se donner une idée de l'auteur grâce au contenu de son post.

## Modèles qui l'ont utilisé
 Ce corpus à servi à entrainer et ajuster les modèles DeBERTa-v3-large-tasksource-nli et DeBERTa-v3-base-tasksource-nli, qui sont des modèles de classification à choix multiples.

## Infos suplémentaires 
* Les ages sont regroupés par ranches : 13-17 ans (8 240 blogs), 23-27 ans (8086 blogs) et 33-47 ans (2 994 blogs). Cela pourrait permettre de créer un algorithme de classification plutôt que de régression?
