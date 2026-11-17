import flet as ft


def receitas_lista_view(mudar_tela):
  cor_terracota = "#C86D51"
  cor_fundo_claro = "#F5ECE5"
  cor_texto_escuro = "#2D211B"
  cor_subtexto = "#7D6E65"
  cor_badge_fundo = "#E8F5E9"
  cor_badge_texto = "#2E7D32"

  # Funcao auxiliar para construir cada card de receita
  def criar_card_receita(nome, nivel, carreiras_feitas, total_carreiras):
    progresso = carreiras_feitas / total_carreiras

    return ft.Container(
        width=160,
        bgcolor="white",
        border_radius=20,
        padding=12,
        border=ft.border.all(1, "#EAE5DE"),
        on_click=lambda _: mudar_tela("scanner"),
        content=ft.Column(
            controls=[
                # Placeholder para a imagem da peca
                ft.Container(
                    height=130,
                    bgcolor=cor_fundo_claro,
                    border_radius=15,
                    alignment=ft.alignment.center,
                    content=ft.Icon(
                        ft.icons.IMAGE_OUTLINED, color=cor_subtexto, size=32
                    ),
                ),
                # Tag de dificuldade
                ft.Container(
                    bgcolor=cor_badge_fundo,
                    padding=ft.padding.symmetric(horizontal=8, vertical=3),
                    border_radius=8,
                    content=ft.Text(
                        nivel,
                        size=11,
                        weight=ft.FontWeight.BOLD,
                        color=cor_badge_texto,
                    ),
                ),
                # Nome do amigurumi
                ft.Text(
                    nome,
                    size=16,
                    weight=ft.FontWeight.BOLD,
                    color=cor_texto_escuro,
                ),
                # Informacoes de progresso
                ft.Row(
                    controls=[
                        ft.Text("Carreiras", size=11, color=cor_subtexto),
                        ft.Text(
                            f"{carreiras_feitas}/{total_carreiras}",
                            size=11,
                            weight=ft.FontWeight.BOLD,
                            color=cor_texto_escuro,
                        ),
                    ],
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                ),
                # Barra indicadora de progresso
                ft.ProgressBar(
                    value=progresso,
                    color=cor_terracota,
                    bgcolor="#F0EAE4",
                    height=6,
                ),
            ],
            spacing=6,
            horizontal_alignment=ft.CrossAxisAlignment.START,
        ),
    )

  return ft.Container(
      bgcolor="#FAF8F5",
      padding=ft.padding.only(left=20, right=20, top=15, bottom=20),
      expand=True,
      content=ft.Column(
          controls=[
              # Cabecalho: Voltar, Titulo YarnLogic e Avatar
              ft.Row(
                  controls=[
                      ft.Container(
                          content=ft.Icon(
                              ft.icons.ARROW_BACK_IOS_NEW,
                              size=16,
                              color=cor_terracota,
                          ),
                          bgcolor=cor_fundo_claro,
                          shape=ft.BoxShape.CIRCLE,
                          padding=10,
                          on_click=lambda _: mudar_tela("login"),
                      ),
                      ft.Text(
                          "YarnLogic",
                          size=22,
                          weight=ft.FontWeight.BOLD,
                          color=cor_texto_escuro,
                      ),
                      ft.Container(
                          content=ft.Text(
                              "A",
                              size=14,
                              weight=ft.FontWeight.BOLD,
                              color="white",
                          ),
                          bgcolor=cor_terracota,
                          shape=ft.BoxShape.CIRCLE,
                          padding=10,
                          width=36,
                          height=36,
                          alignment=ft.alignment.center,
                      ),
                  ],
                  alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
              ),
              ft.Container(height=10),
              # Titulo e subtitulo da secao
              ft.Text(
                  "Minhas Receitas",
                  size=26,
                  weight=ft.FontWeight.BOLD,
                  color=cor_texto_escuro,
              ),
              ft.Text(
                  "Gerencie e acompanhe seus amigurumis ativos",
                  size=13,
                  color=cor_subtexto,
              ),
              ft.Container(height=8),
              # Filtros de status (Todas, Ativas, Concluidas)
              ft.Row(
                  controls=[
                      ft.Container(
                          content=ft.Text(
                              "Todas",
                              size=12,
                              weight=ft.FontWeight.W_500,
                              color="white",
                          ),
                          bgcolor=cor_terracota,
                          padding=ft.padding.symmetric(
                              horizontal=18, vertical=8
                          ),
                          border_radius=20,
                      ),
                      ft.Container(
                          content=ft.Text(
                              "Ativas",
                              size=12,
                              weight=ft.FontWeight.W_500,
                              color=cor_texto_escuro,
                          ),
                          bgcolor="white",
                          border=ft.border.all(1, "#E0D7D0"),
                          padding=ft.padding.symmetric(
                              horizontal=18, vertical=8
                          ),
                          border_radius=20,
                      ),
                      ft.Container(
                          content=ft.Text(
                              "Concluídas",
                              size=12,
                              weight=ft.FontWeight.W_500,
                              color=cor_texto_escuro,
                          ),
                          bgcolor="white",
                          border=ft.border.all(1, "#E0D7D0"),
                          padding=ft.padding.symmetric(
                              horizontal=18, vertical=8
                          ),
                          border_radius=20,
                      ),
                  ],
                  spacing=8,
              ),
              ft.Container(height=10),
              # Grade de cards dos amigurumis em andamento
              ft.Row(
                  controls=[
                      criar_card_receita("Gnomo", "Fácil", 12, 24),
                      criar_card_receita("Centopeia", "Fácil", 24, 32),
                  ],
                  alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
              ),
              ft.Container(height=25),
              # Botao de acao: Nova Receita
              ft.Container(
                  alignment=ft.alignment.center,
                  content=ft.ElevatedButton(
                      content=ft.Row(
                          controls=[
                              ft.Icon(ft.icons.ADD, color="white", size=18),
                              ft.Text(
                                  "Nova Receita",
                                  size=15,
                                  weight=ft.FontWeight.BOLD,
                              ),
                          ],
                          alignment=ft.MainAxisAlignment.CENTER,
                          tight=True,
                      ),
                      bgcolor=cor_terracota,
                      color="white",
                      width=260,
                      height=50,
                      style=ft.ButtonStyle(
                          shape=ft.RoundedRectangleBorder(radius=25)
                      ),
                      on_click=lambda _: print(
                          "[ROTA] Abrir cadastro de nova receita"
                      ),
                  ),
              ),
          ],
          scroll=ft.ScrollMode.ADAPTIVE,
          spacing=6,
      ),
  )