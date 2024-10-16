import os
from PIL import Image

# Percorso della cartella contenente le immagini
cartella_immagini = "/Users/gabrieleshu/Desktop/Bingo/BingoCard"

# Dimensioni di un foglio A4 in pixel
dimensioni_a4 = (3508, 2480)

# Scandisci tutte le immagini nella cartella
for nome_file in os.listdir(cartella_immagini):
    percorso_file = os.path.join(cartella_immagini, nome_file)
    
    # Verifica se il file è un'immagine
    if os.path.isfile(percorso_file) and nome_file.lower().endswith((".jpg", ".jpeg", ".png")):
        # Apri l'immagine
        immagine = Image.open(percorso_file)
        
        # Ridimensiona l'immagine alle dimensioni di un foglio A4
        immagine_ridimensionata = immagine.resize(dimensioni_a4)
        
        # Salva l'immagine ridimensionata nella stessa cartella con un nuovo nome
        nome_file_ridimensionato = f"ridimensionato_{nome_file}"
        percorso_file_ridimensionato = os.path.join(cartella_immagini, nome_file_ridimensionato)
        immagine_ridimensionata.save(percorso_file_ridimensionato)
        
        # Chiudi l'immagine
        immagine.close()

print("Ridimensionamento completato!")
