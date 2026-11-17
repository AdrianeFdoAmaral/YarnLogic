import flet as ft


def cadastro_view(mudar_tela, page: ft.Page):
  # Cores com base do  protótipo do figma.
  COR_BOTAO = "#C8623E"  # mostarda
  COR_FUNDO_CAMPO = "#F6F1EA"  # creme suave
  COR_BORDA_CAMPO = "#EDE5DA"
  COR_TITULO = "#2E2522"  # marrom escuro
  COR_SUBTITULO = "#7B7571"  # cinza quente

  # Campos de entrada
  nome_input = ft.TextField(
      hint_text="Seu Nome",
      bgcolor=COR_FUNDO_CAMPO,
      border_color=COR_BORDA_CAMPO,
      border_radius=25,
      content_padding=ft.padding.symmetric(horizontal=20, vertical=14),
      width=310,
  )

  email_input = ft.TextField(
      hint_text="exemplo@email.com",
      prefix_icon=ft.icons.EMAIL_OUTLINED,
      bgcolor=COR_FUNDO_CAMPO,
      border_color=COR_BORDA_CAMPO,
      border_radius=25,
      content_padding=ft.padding.symmetric(horizontal=20, vertical=14),
      width=310,
  )

  senha_input = ft.TextField(
      hint_text="Senha",
      password=True,
      can_reveal_password=True,
      prefix_icon=ft.icons.LOCK_OUTLINED,
      bgcolor=COR_FUNDO_CAMPO,
      border_color=COR_BORDA_CAMPO,
      border_radius=25,
      content_padding=ft.padding.symmetric(horizontal=20, vertical=14),
      width=310,
  )

  confirmar_senha_input = ft.TextField(
      hint_text="Digite sua senha novamente",
      password=True,
      can_reveal_password=True,
      prefix_icon=ft.icons.LOCK_OUTLINED,
      bgcolor=COR_FUNDO_CAMPO,
      border_color=COR_BORDA_CAMPO,
      border_radius=25,
      content_padding=ft.padding.symmetric(horizontal=20, vertical=14),
      width=310,
  )

  msg_erro = ft.Text("", size=12, color=ft.colors.RED_600, visible=False)

  # botão Cadastrar
  def cadastrar_usuario(e):
    if not nome_input.value or not email_input.value or not senha_input.value:
      msg_erro.value = "Por favor, preencha todos os campos."
      msg_erro.visible = True
      page.update()
      return

    if senha_input.value != confirmar_senha_input.value:
      msg_erro.value = "As senhas não coincidem!"
      msg_erro.visible = True
      page.update()
      return

    # se der tudo certo, vai para a pagina de login
    mudar_tela("login")

  # botão Cadastrar
  btn_cadastrar = ft.ElevatedButton(
      "Cadastrar",
      bgcolor=COR_BOTAO,
      color=ft.colors.WHITE,
      width=280,
      height=50,
      style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=25)),
      on_click=cadastrar_usuario,
  )

  # botão do x para sair da pagina
  btn_fechar = ft.Container(
      content=ft.IconButton(
          icon=ft.icons.CLOSE,
          icon_color=COR_BOTAO,
          on_click=lambda _: mudar_tela("login"),
      ),
      width=50,
      height=50,
      bgcolor="#FBF2EB",
      border_radius=25,
      border=ft.border.all(1, "#E8D5C8"),
      alignment=ft.alignment.center,
  )

  return ft.Container(
      bgcolor=ft.colors.WHITE,
      padding=ft.padding.only(left=25, right=25, top=20, bottom=30),
      expand=True,
      content=ft.Column(
          controls=[
              btn_fechar,
              ft.Text(
                  "YarnLogic",
                  size=30,
                  weight=ft.FontWeight.BOLD,
                  color=COR_TITULO,
              ),
              ft.Text(
                  "Seu assistente de crochê",
                  size=14,
                  color=COR_SUBTITULO,
              ),
              ft.Divider(height=10, color=ft.colors.TRANSPARENT),
              ft.Column(
                  [
                      ft.Text(
                          "Nome",
                          size=13,
                          weight=ft.FontWeight.W_500,
                          color=COR_TITULO,
                      ),
                      nome_input,
                  ],
                  spacing=4,
              ),
              ft.Column(
                  [
                      ft.Text(
                          "E-mail",
                          size=13,
                          weight=ft.FontWeight.W_500,
                          color=COR_TITULO,
                      ),
                      email_input,
                  ],
                  spacing=4,
              ),
              ft.Column(
                  [
                      ft.Text(
                          "Senha",
                          size=13,
                          weight=ft.FontWeight.W_500,
                          color=COR_TITULO,
                      ),
                      senha_input,
                  ],
                  spacing=4,
              ),
              ft.Column(
                  [
                      ft.Text(
                          "Confirmar senha",
                          size=13,
                          weight=ft.FontWeight.W_500,
                          color=COR_TITULO,
                      ),
                      confirmar_senha_input,
                  ],
                  spacing=4,
              ),
              msg_erro,
              ft.Divider(height=10, color=ft.colors.TRANSPARENT),
               #botao de cadastro
              btn_cadastrar,
              ft.TextButton(
                  "Já tem uma conta? Entrar",
                  on_click=lambda _: mudar_tela("login"),
                  style=ft.ButtonStyle(color=COR_SUBTITULO),
              ),
          ],
          horizontal_alignment=ft.CrossAxisAlignment.CENTER,
          scroll=ft.ScrollMode.ADAPTIVE,
          spacing=10,
      ),
  )