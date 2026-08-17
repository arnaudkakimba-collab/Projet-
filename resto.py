import  flet as ft
import os

def main(page:ft.Page):
    
    page.title="Getion des personnes"
    page.padding=30
    page.scroll="auto"
    page.vertical_alignment="start"
    page.horizontal_alignment="center"
    page.spacing=20
    page.window_width=500
    page.window_height=700
    page.bgcolor = "lightgrey"
    # Appliquer le mode système
    #page.theme_mode = ft.ThemeMode.SYSTEM
    
    # Définir explicitement les deux thèmes si vous les personnalisez
    #page.theme = ft.Theme(color_scheme_seed="blue")
    #page.dark_theme = ft.Theme(color_scheme_seed="blue")
    
    titre=ft.Text(
        "Bienvenu!",
        weight="bold",
        size=24,
        color="black"
      )
    conteneur=ft.Container(
        content=titre,
        padding=25,
        border_radius=15,
        bgcolor="white",
        alignment=ft.Alignment.CENTER
      )
    stitre=ft.Text(
        "Gérez vos contacts",
        #color="black"
      )
    textl=ft.Text(
        "Statut :",
        #color="black"
      )
    textv=ft.Text(
        "En ligne",
        #color="black"
      )
    statusl=ft.Row(
        controls=[
            textl,
            textv
          ],
        spacing=10
      )
    nom=ft.Text(
      "Nom :",
      #color="black"
    )
    chnom=ft.TextField(
        label="Nom",
        width=250,
        height=45,
        hint_text="Entrez votre nom",
        #color="black"
      )
    rown=ft.Row(
        controls=[
            nom,
            chnom
          ]
      )
    
    menug=ft.Dropdown(
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
    casef=ft.Checkbox(
        label="Favori",
        value=False
      )
    statutch=ft.RadioGroup(
        content=ft.Row(
            controls=[
                ft.Radio(
                    label="Actif",
                    value="Actif"
                  ),
                ft.Radio(
                    label="Inactif",
                    value="Inactif"
                  )
              ]
          )
      )
      
    def save(e):
    # 1. Définir le composant SnackBar sur la page
    page.snack_bar = ft.SnackBar(
        content=ft.Text("Ajouté!"),
        bgcolor="blue",
        duration=3000,
    )
    # 2. Forcer l'ouverture explicite de la SnackBar
    page.snack_bar.open = True
    
    # 3. Mettre à jour l'interface
    page.update()

    
    boutona=ft.Button(
      "Ajouter",
      icon=ft.Icons.ADD,
      on_click=save
      )

    def delete(e):
        
        print("deleted")
        
    colone=ft.Column(
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
    #,reload=True
)