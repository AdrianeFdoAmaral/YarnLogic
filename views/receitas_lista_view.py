import flet as ft


def receitas_lista_view(mudar_tela, page: ft.Page):
  COR_TERRACOTA = "#C8623E"
  COR_FUNDO = "#FAFAF8"
  COR_CARD = "#FFFFFF"
  COR_TEXTO = "#2E2522"
  COR_SUBTEXTO = "#7B7571"

  # Função auxiliar para criar cada card de amigurumi
  def card_receita(nome, nivel, progresso_texto, progresso_barra):
    return ft.Container(
        bgcolor=COR_CARD,
        border_radius=15,
        padding=15,
        border=ft.border.all(1, "#EAE5DE"),
        content=ft.Column(
            controls=[
                ft.Row(
                    controls=[
                        ft.Icon(
                            ft.icons.AUTO_AWESOME,
                            color=COR_TERRACOTA,
                            size=28,
                        ),
                        ft.Column(
                            controls=[
                                ft.Text(
                                    nome,
                                    size=16,
                                    weight=ft.FontWeight.BOLD,
                                    color=COR_TEXTO,
                                ),
                                ft.Text(
                                    f"Dificuldade: {nivel}",
                                    size=12,
                                    color=COR_SUBTEXTO,
                                ),
                            ],
                            spacing=2,
                        ),
                    ],
                    alignment=ft.MainAxisAlignment.START,
                ),
                ft.Divider(height=10, color=ft.colors.TRANSPARENT),
                ft.Row(
                    controls=[
                        ft.Text(
                            progresso_texto, size=12, weight=ft.FontWeight.W_500
                        ),
                        ft.Text(
                            f"{int(progresso_barra * 100)}%",
                            size=12,
                            color=COR_SUBTEXTO,
                        ),
                    ],
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                ),
                ft.ProgressBar(
                    value=progresso_barra, color=COR_TERRACOTA, bgcolor="#EAE5DE"
                ),
                ft.ElevatedButton(
                    "Continuar Crochetando",
                    bgcolor=COR_TERRACOTA,
                    color=ft.colors.WHITE,
                    width=280,
                    on_click=lambda _: mudar_tela("scanner"),
                ),
            ],
            spacing=8,
        ),
    )

  return ft.Container(
      bgcolor=COR_FUNDO,
      padding=20,
      expand=True,
      content=ft.Column(
          controls=[
              ft.Row(
                  controls=[
                      ft.Text(
                          "Minhas Receitas",
                          size=22,
                          weight=ft.FontWeight.BOLD,
                          color=COR_TEXTO,
                      ),
                      ft.IconButton(
                          icon=ft.icons.LOGOUT,
                          icon_color=COR_TERRACOTA,
                          on_click=lambda _: mudar_tela("cadastro"),
                      ),
                  ],
                  alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
              ),
              ft.Text(
                  "Acompanhe o progresso das suas peças",
                  size=13,
                  color=COR_SUBTEXTO,
              ),
              ft.Divider(height=15, color=ft.colors.TRANSPARENT),
              # Cards dos projetos do YarnLogic
              card_receita("Gnomo Amigurumi", "Intermediário", "Carreira 3/18", 0.17),
              card_receita("Lagarta Colorida", "Iniciante", "Carreira 1/12", 0.08),
          ],
          scroll=ft.ScrollMode.ADAPTIVE,
          spacing=15,
      ),
  )