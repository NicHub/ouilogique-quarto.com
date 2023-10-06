import markdown_it
from urllib.parse import urlparse
from pprint import pprint


def extract_links_from_md_file(file_path):
    # Créez un analyseur Markdown
    md = markdown_it.MarkdownIt()

    # Ouvrez le fichier Markdown
    with open(file_path, "r", encoding="utf-8") as md_file:
        markdown_content = md_file.read()

    # Analysez le contenu Markdown
    tokens = md.parse(markdown_content)

    pprint(tokens)

    # Initialisation des listes pour les trois catégories de liens
    image_links = []
    local_links = []
    remote_links = []

    # Parcourez les jetons Markdown pour extraire les liens
    for token in tokens:
        print(type(token))
        print(token)

        if


        continue
        if "lin" in token.type:
            print(token.type)
        if token.type == "link_open":
            # Obtenez l'URL du lien
            link_url = token["attrs"][0][1]
            # Vérifiez si c'est une URL d'image
            if link_url.lower().endswith((".png", ".jpg", ".jpeg", ".gif", ".svg")):
                image_links.append(link_url)
            else:
                parsed_url = urlparse(link_url)
                # Vérifiez si c'est une URL locale ou distante
                if parsed_url.netloc == "":
                    local_links.append(link_url)
                else:
                    remote_links.append(link_url)

    return image_links, local_links, remote_links


# Utilisez la fonction pour extraire les liens du fichier Markdown
file_path = "/Users/nico/Desktop/ouilogique.com/posts/2019-03-27-plateforme-de-stewart-esp32/index.qmd"
image_links, local_links, remote_links = extract_links_from_md_file(file_path)

# Affichez les résultats
print("Liens vers des images:")
for link in image_links:
    print(link)

print("\nURL locaux:")
for link in local_links:
    print(link)

print("\nURL distants:")
for link in remote_links:
    print(link)


import markdown_link_extractor
string = open(file_path).read()
markdown_link_extractor.getlinks(string)