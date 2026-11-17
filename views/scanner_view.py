import flet as ft


def scanner_view(
        mudar_tela=None,
        page: ft.Page = None,
        nome_receita="Gnomo",
        carreira="Carreira 13",
        pontos_detectados=13,
        pontos_esperados=24,
        mensagem_alerta="Falta 1 ponto baixo nesta carreira! Atenção!",
        caminho_imagem=None,
):

    cor_terracota = "#C86D51"
    cor_fundo_pagina = "FAF8F5"
    cor_fundo_icone = "F5ECE5"
    cor_subtexto = "#7D6E65"
    cor_alerta_fundo = "#FDF2ED"

    largura_padrao = 320

    #a configuração do filepicker 
    def resultado_picker(e: ft.FilePickerResultEvent):
        if e.files and len(e.files) > 0:
            novo_caminho = e.files[0].path
            if on_imagem_selecionada:
                on_imagem_selecionada(novo_caminho)
                
    file_picker = ft.FilePicker(on_result=resultado_picker)

    if page and file_picker not in page.overlay:
        page.overlay.append(file_picker)

    def adicionar_camera(e):
        file_picker.pick_files(
            allow_multiple=False,
            file_type=ft.FilePickerFileType.IMAGE,
        )

      #1 Cabeçalho
    header = ft.Row(
        controls=[
            ft.IconButton(
                icon=ft.Icons.CHEVRON_LEFT,
                icon_color="#5F4B43",
                bgcolor="#F5ECE5",
                on_click=lambda _: mudar-tela("home") if mudar_tela else None,
              ),
              ft.Text("YarnLogic", size=20, weight=ft.FontWeight.BOLD),
              ft.CircleAvatar(
                  content=ft.Text("A", color=ft.Colors.WHITE),
                  bgcolor=cor_terracota,
                  radius=18,
              ),
          ],
          alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
          width=largura_padrao,
      )

    titulo_pagina = ft.Text(
        f"Validar {carreira}",
        size=18,
        weight=ft.FontWeight.BOLD,
    )
        
    if caminho_imagem:
        conteudo_imagem = ft.Container(
            content=ft.Image(
                src=caminho_imagem,
                fit=ft.ImageFit.COVER,
            ),
            height=260,
            widgth=largura_padrao,
            border_radius=15,
            clip_behavior=ft.ClipBehavior.ANTI_ALIAS,
            on_click=acionar_camera,
        )
    else:
        conteudo_imagem = ft.Container(
            content=ft.Icon(
                name=ft.Icons.CAMERA_ALT,
                size=50,
                color=cor_subtexto,
            ),
            alignment=ft.alignment.center,
            height=260,
            width=largura_padrao,
            bgcolor="#E0D7D0",
            border_radius=15,
            on_click=acionar_camera,
        )

    card_resultado = ft.Container(
        content=ft.Column(
            controls=[
                ft.Text(
                    f"PONTOS DETECTADOS: {pontos_detectados}/{pontos_esperados}",
                    size=16,
                    weight=ft.FontWeight.BOLD,
                    color=cor_terracota,
                ),
                ft.Container(
                    content=ft.Row(
                        controls=[
                            ft.Icon(ft.Icons.ERROR_OUTLINE, color=cor_terracota, size=20),
                            ft.Expanded(
                                ft.Text(
                                    mensagem_alerta,
                                    color="#5F4B43",
                                    size=13,
                                    weight=ft.FontWeight.W_500,
                                )
                            ),
                        ],
                        spacing=8,
                    ),
                    bgcolor=cor_alerta_fundo,
                    padding=12,
                    border_radius=10,       
                ),
            ],
            spacing=10,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        ),
        padding=16,
        bgcolor=ft.Colors.WHITE,
        border_radius=15,
        width=largura_padrao,
    )

    #botao 'tirar nova foto'
    bnt_tirar_foto = ft.ElevatedButton(
        content=ft.Row(
            controls=[
                ft.Icon(name=ft.Icons.CAMERA_ALT_OUTILINED, color=ft.Colors.WHITE, size=20),
                ft.Text("Tirar nova foto", color=ft.Colors.WHITE, size=15, weight=ft.FontWeight.BOLD),
            ],
            alignment=ft.MainAxisAlignmente.CENTER,
            spacing=8,
        ),
        bgcolor=cor_terracota,
        height=50,
        width=largura_padrao,
        style=ft.ButtonStyle(
            shape=ft.RoundedRectangleBorder(radius=25),
        ),
        on_click=adicionar_camera,
    )

    return ft.Container(
        content=ft.Clumn(
            controls=[
                header,
                ft.Container(height=5),
                titulo_pagina,
                conteudo_imagem,
                ft.Container(height=5),
                card_resultado,
                ft.Container(height=10),
                bnt_tirar_foto,
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=8,
        ),
        bgcolor=cor_fundo_pagina,
        padding=16,
        alifnment=ft.alignment.top_center,
        expand=True,
    )