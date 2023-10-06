from pprint import pprint
import os


# %%
posts = os.listdir("/Users/nico/Sites/ouilogique.com/_posts/blog/")
posts = [post.split(".")[0] for post in posts]
# posts


# %%
files = os.listdir("/Users/nico/Sites/ouilogique.com/files/")
files = [file for file in files if file not in [".DS_Store"]]
# files


ensemble1 = set(posts)
ensemble2 = set(files)

# Trouver les éléments manquants dans chaque liste
manquants_liste1 = sorted(list(ensemble2 - ensemble1))
manquants_liste2 = sorted(list(ensemble1 - ensemble2))

# Afficher les éléments manquants
print(f"{len(manquants_liste1)} éléments manquants dans posts :")
pprint(manquants_liste1)
print(f"{len(manquants_liste2)} éléments manquants dans files :")
pprint(manquants_liste2)
