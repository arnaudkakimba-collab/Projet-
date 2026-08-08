import flet as ft
import os

def main(page:ft.Page):
    
    page.title="My WebApp"
    page.padding=30
    page.scroll="auto"
    page.vertical_alignment="start"
    page.horizontal_alignment="center"
    page.bgcolor="#f0f0f0"
    
    titre=ft.Text(
        "Welcom!",
        weight="bold",
        size=24
      )
    stitre=ft.Text(
        "Gérez vos contacts",
        color="black"
      )
    textl=ft.Text(
        "Statut",
        color="black"
      )
    textv=ft.Text(
        "En ligne",
        color="black"
      )
    statusl=ft.Row(
        controls=[
            textl,
            textv
          ],
        spacing=10
      )
    nom=ft.Text(
      "Name :",
      color="black"
    )
    chnom=ft.TextField(
        label="Name",
        width=250,
        height=45,
        hint_text="Put your name here",
        color="black"
      )
    rown=ft.Row(
        controls=[
            nom,
            chnom
          ]
      )
    conteneur=ft.Container(
        content=titre,
        padding=25,
        border_radius=15,
        bgcolor="black",
        alignment=ft.Alignment.CENTER
      )
      
    def addp(e):
      
      print("personne added")
    
    boutona=ft.Button(
      "Ajouter",
      icon=ft.Icon.ADD,
      on_click=addp
      )
    colone=ft.Column(
        controls=[
            conteneur,
            stitre,
            statusl,
            rown,
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