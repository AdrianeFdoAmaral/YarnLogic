import flet as ft
from views.cadastro_view import cadastro_view
from views.login_view import LoginView
from views.scanner_view import scanner_view


def main(page: ft.Page):
  page.title = "YarnLogic"
  page.window.width = 390
  page.window.height = 844
  page.window.resizable = False
  page.padding = 0

  def mudar_tela(rota):
    print(f"[ROTA] Solicitada mudanca para: {rota}")

    page.controls.clear()
    page.appbar = None

    if rota == "cadastro":
      page.bgcolor = "#FFFFFF"
      page.add(cadastro_view(mudar_tela, page))

    elif rota == "login":
      page.bgcolor = "#FFFFFF"
      page.add(LoginView(mudar_tela))

    elif rota == "scanner":
      # Passamos os dois argumentos: mudar_tela e page
      try:
        tela = scanner_view(mudar_tela, page)
      except TypeError:
        # Caso a funcao receba apenas page:
        tela = scanner_view(page)

      # Se for um ft.View, extrai seus elementos
      if isinstance(tela, ft.View):
        page.appbar = tela.appbar
        if tela.bgcolor:
          page.bgcolor = tela.bgcolor
        page.add(*tela.controls)
      elif tela is not None:
        page.add(tela)

    else:
      page.bgcolor = "#FFFFFF"
      page.add(LoginView(mudar_tela))

    page.update()

  # Inicia no login
  mudar_tela("login")


ft.app(target=main)