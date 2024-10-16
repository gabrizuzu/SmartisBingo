import os
import random
from PIL import Image, ImageDraw



# Percorso della cartella che contiene le 70 foto numerate
folder_path = "/Users/gabrieleshu/Desktop/Bingo/foto"  # Modifica con il tuo percorso
template_path = "/Users/gabrieleshu/Desktop/Bingo/Template.png"  # Modifica con il percorso del template

# Percorso della cartella di output per le Bingo Cards
output_folder = "BingoCard"
if not os.path.exists(output_folder):
    os.makedirs(output_folder)  # Crea la cartella se non esiste

# Carichiamo tutte le immagini numerate dalla cartella
images = [Image.open(os.path.join(folder_path, f)) for f in sorted(os.listdir(folder_path)) if f.endswith(('.png', '.jpg', '.jpeg', '.JPG', '.JPEG', '.PNG'))]

# Carica il template di bingo
template = Image.open(template_path)

# Dimensioni della griglia (3x4 caselle)
grid_size = (3, 4)

cell_width, cell_height = 1550, 1150, 

margin = 20  # Margine tra le caselle
# Genera 20 cartelle
for bingo_card_num in range(1):
    # Seleziona 12 immagini casuali (senza ripetizione) dalle 70 immagini
    selected_images = random.sample(images, 12)
    
    # Crea una copia del template per modificare
    bingo_card = template.copy()
    
    # Posiziona le immagini selezionate nelle caselle del template
    for i, img in enumerate(selected_images):
        # Ridimensiona l'immagine per adattarla alla casella
        img = img.resize((cell_width, cell_height))
        
        # Prendi la posizione corrispondente per la casella
        x = (i % grid_size[1]) * (cell_width + margin) + 740
        y = (i // grid_size[1]) * (cell_height + margin)
        
        # Incolla l'immagine nel template alla posizione corretta
        bingo_card.paste(img, (x, y))
            # Disegna un rettangolo vuoto intorno alla casella per creare un bordo

    # Salva l'immagine della cartella bingo generata nella cartella BingoCard
    bingo_card.save(os.path.join(output_folder, f"bingo_card_{bingo_card_num + 1}.png"))


