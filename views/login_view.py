import flet as ft


def LoginView(mudar_tela):
  cor_primaria = "#C86D51"
  cor_fundo_campo = "#F5ECE5"
  cor_texto = "#2D211B"
  cor_subtexto = "#7D6E65"
  cor_rotulo = "#4A3E37"

  largura_padrao = 320

  campo_email = ft.TextField(
      hint_text="exemplo@email.com",
      border_radius=25,
      bgcolor=cor_fundo_campo,
      border_color="transparent",
      prefix_icon=ft.icons.EMAIL_OUTLINED,
      width=largura_padrao,
  )

  campo_senha = ft.TextField(
      hint_text="Sua senha secreta",
      password=True,
      can_reveal_password=True,
      border_radius=25,
      bgcolor=cor_fundo_campo,
      border_color="transparent",
      prefix_icon=ft.icons.LOCK_OUTLINED,
      width=largura_padrao,
  )

  return ft.Column(
      controls=[
          ft.Container(height=30),
          # botar de retorno
          ft.Container(
              content=ft.Icon(
                  ft.icons.CLOSE_ROUNDED, color=cor_primaria, size=20
              ),
              bgcolor=cor_fundo_campo,
              shape=ft.BoxShape.CIRCLE,
              padding=10,
              alignment=ft.alignment.center,
              on_click=lambda _: mudar_tela("cadastro"),
          ),
          ft.Container(height=10),
          ft.Text(
              "YarnLogic", size=32, weight=ft.FontWeight.BOLD, color=cor_texto
          ),
          ft.Text(
              "Seu assistente inteligente de croche",
              size=14,
              color=cor_subtexto,
          ),
          ft.Container(height=25),
          # campo do email
          ft.Container(
              width=largura_padrao,
              content=ft.Column(
                  controls=[
                      ft.Text(
                          "E-mail",
                          size=13,
                          weight=ft.FontWeight.W_600,
                          color=cor_rotulo,
                      ),
                      campo_email,
                  ],
                  spacing=4,
                  horizontal_alignment=ft.CrossAxisAlignment.START,
              ),
          ),
          # o campo da senha
          ft.Container(
              width=largura_padrao,
              content=ft.Column(
                  controls=[
                      ft.Text(
                          "Senha",
                          size=13,
                          weight=ft.FontWeight.W_600,
                          color=cor_rotulo,
                      ),
                      campo_senha,
                  ],
                  spacing=4,
                  horizontal_alignment=ft.CrossAxisAlignment.START,
              ),
          ),
          # recuperar a senha
          ft.Container(
              width=largura_padrao,
              content=ft.TextButton(
                  "Esqueceu a senha?",
                  style=ft.ButtonStyle(color=cor_primaria),
              ),
              alignment=ft.alignment.center_right,
          ),
          ft.Container(height=15),
          # o botao para entrar
          ft.ElevatedButton(
              "Entrar",
              width=largura_padrao,
              style=ft.ButtonStyle(
                  bgcolor=cor_primaria,
                  color="white",
                  shape=ft.RoundedRectangleBorder(radius=25),
                  padding=16,
              ),
              on_click=lambda _: mudar_tela("scanner"),
          ),
          # o botao para criar conta
          ft.OutlinedButton(
              "Criar Conta",
              width=largura_padrao,
              style=ft.ButtonStyle(
                  color=cor_texto,
                  side=ft.BorderSide(1, "#E0D7D0"),
                  shape=ft.RoundedRectangleBorder(radius=25),
                  padding=16,
              ),
              on_click=lambda _: mudar_tela("cadastro"),
          ),
      ],
      horizontal_alignment=ft.CrossAxisAlignment.CENTER,
      spacing=10,
  )