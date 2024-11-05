import qrcode
from PIL import Image
import tkinter as tk
from tkinter import filedialog, messagebox, colorchooser
from tkinter import ttk
import imageio


# Fonction pour générer un QR code animé
def generate_animated_qr():
    # Récupération des entrées utilisateur
    data_type = data_type_combobox.get()
    data_value = data_entry.get()
    if not data_value:
        messagebox.showerror("Erreur", "Veuillez entrer les données à encoder.")
        return

    # Récupération des options de personnalisation
    qr_color = colorchooser.askcolor()[1] or "black"
    bg_color = colorchooser.askcolor()[1] or "white"

    # Création de la liste pour stocker les images QR
    images = []

    # Création du QR code
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=4,
    )

    # Encodage des données dans le QR code
    if data_type == "URL":
        qr.add_data(data_value)
    elif data_type == "Texte":
        qr.add_data(data_value)
    elif data_type == "Numéro de téléphone":
        qr.add_data(f"tel:{data_value}")
    elif data_type == "E-mail":
        qr.add_data(f"mailto:{data_value}")

    qr.make(fit=True)

    # Chemin pour le logo (si sélectionné)
    logo_path = filedialog.askopenfilename(title="Sélectionner une image/logo",
                                           filetypes=[("Image files", "*.jpg;*.png")])

    # Création de plusieurs images pour l'animation en changeant la couleur progressivement
    for i in range(10):
        fill_color = f'#{hex(255 - i * 25)[2:].zfill(2)}00{hex(i * 25)[2:].zfill(2)}'  # Dégradé de rouge à vert

        img_qr = qr.make_image(fill_color=fill_color, back_color=bg_color).convert('RGB')

        # Ajout d'une image ou logo au centre du QR code
        if logo_path:
            logo = Image.open(logo_path)
            logo = logo.resize((50, 50))
            pos = ((img_qr.size[0] - logo.size[0]) // 2, (img_qr.size[1] - logo.size[1]) // 2)
            img_qr.paste(logo, pos)

        # Ajout de l'image dans la liste pour l'animation
        images.append(img_qr)

    # Sauvegarde de l'animation en tant que GIF
    save_path = filedialog.asksaveasfilename(defaultextension=".gif", filetypes=[("GIF files", "*.gif")])
    if save_path:
        imageio.mimsave(save_path, images, format='GIF', duration=0.5)  # Création d'un GIF
        messagebox.showinfo("Succès", "QR code animé sauvegardé avec succès !")

        # Fermer la fenêtre après la génération du QR code
        root.destroy()


# Création de la fenêtre tkinter
root = tk.Tk()
root.title("Générateur de QR Code Animé")

# Titre
title_label = ttk.Label(root, text="QR Code Generator", font=("Helvetica", 16))
title_label.pack(pady=10)

# Sélection du type de contenu
ttk.Label(root, text="Sélectionnez le type de contenu :").pack(pady=5)
data_type_combobox = ttk.Combobox(root, values=["URL", "Texte", "Numéro de téléphone", "E-mail"])
data_type_combobox.pack(pady=5)
data_type_combobox.current(0)

# Champ de saisie des données
ttk.Label(root, text="Entrez les données à encoder :").pack(pady=5)
data_entry = ttk.Entry(root, width=40)
data_entry.pack(pady=5)

# Bouton pour générer le QR code animé
generate_button = ttk.Button(root, text="Générer le QR Code Animé", command=generate_animated_qr)
generate_button.pack(pady=20)

# Démarrage de l'interface
root.mainloop()