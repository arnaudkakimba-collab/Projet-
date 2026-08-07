import flet as ft

def main(page:ft.Page):
    
    page.title="My WebApp"
    page.padding=30
    page.scroll="auto"
    page.vertical_alignment="start"
    page.bgcolor="#f0f0f0"
    
    titre=ft.Text(
        "Welcom!"
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
          ]
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
        bgcolor="black"
      )
    colone=ft.Column(
        controls=[
            conteneur,
            stitre,
            statusl,
            rown
          ]
      )
      
    page.add(colone)
    
ft.app(
    target=main,
    view=ft.AppView.WEB_BROWSER,
    port=int(os.environ.get("PORT", 5000))
)