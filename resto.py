import flet as ft
import os

def main(page: ft.Page):
    
    page.title = "Gestion des personnes"
    page.padding = 30
    page.scroll = "auto"
    page.vertical_alignment = "start"
    page.horizontal_alignment = "center"
    page.spacing = 20
    page.window_width = 500
    page.window_height = 700
    page.bgcolor = "lightgrey"
    
    titre = ft.Text(
        "Bienvenu!",
        weight="bold",
        size=24,
        color="black"
    )
    conteneur = ft.Container(
        content=titre,
        padding=25,
        border_radius=15,
        bgcolor="white",
        alignment=ft.Alignment.CENTER
    )
    stitre = ft.Text("Gérez vos contacts")
    textl = ft.Text("Statut :")
    textv = ft.Text("En ligne")
    
    statusl = ft.Row(
        controls=[textl, textv],
        spacing=10
    )
    
    nom = ft.Text("Nom :")
    chnom = ft.TextField(
        label="Nom",
        width=250,
        height=45,
        hint_text="Entrez votre nom",
    )
    rown = ft.Row(
        controls=[nom, chnom]
    )
    
    menug = ft.Dropdown(
        label="Genre",
        hint_text="Choisissez un genre",
        width=250,
        height=45,
        options=[
            ft.dropdown.Option("Homme"),
            ft.dropdown.Option("Femme"),
            ft.dropdown.Option("Autre")
        ]
    )
    casef = ft.Checkbox(
        label="Favori",
        value=False
    )
    statutch = ft.RadioGroup(
        content=ft.Row(
            controls=[
                ft.Radio(label="Actif", value="Actif"),
                ft.Radio(label="Inactif", value="Inactif")
            ]
        )
    )

    # 1. Déclaration de la SnackBar
    snack = ft.SnackBar(
        content=ft.Text("Ajouté!"),
        bgcolor="blue",
        duration=3000,
    )

    # 2. Fonction de sauvegarde
    def save(e):
        page.snack_bar = snack
        snack.open = True
        page.update()

    def delete(e):
        print("deleted")
        
    # 3. Création du bouton (placé HORS de la fonction save)
    boutona = ft.Button(
        "Ajouter",
        icon=ft.Icons.ADD,
        on_click=save
    )

    colone = ft.Column(
        controls=[
            conteneur,
            stitre,
            statusl,
            rown,
            menug,
            casef,
            statutch,
            boutona
        ],
        spacing=15
    )
      
    page.add(colone)

ft.app(
    target=main,
    view=ft.AppView.WEB_BROWSER,
    host="0.0.0.0",
    port=int(os.environ.get("PORT", 10000))
)
