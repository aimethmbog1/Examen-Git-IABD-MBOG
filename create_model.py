import os

# Nom du fichier
filename = "model_weights.pt"

# Taille souhaitée (en Mo)
size_mb = 20  # > 15 Mo exigé

# Conversion en bytes
size_bytes = size_mb * 1024 * 1024

# Création du fichier binaire
with open(filename, "wb") as f:
    f.write(os.urandom(size_bytes))

print(f"Fichier '{filename}' créé avec succès ({size_mb} Mo)")
