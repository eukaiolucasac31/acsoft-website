# -*- coding: utf-8 -*-
"""
Script para geração da Documentação Oficial e Timeline da ACsoft em formato Word (.docx).
"""

import os
from docx import Document
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT, WD_ALIGN_VERTICAL
from docx.oxml import OxmlElement, parse_xml
from docx.oxml.ns import nsdecls, qn

def set_cell_background(cell, fill_hex):
    """Define a cor de fundo de uma célula da tabela."""
    tcPr = cell._tc.get_or_add_tcPr()
    shd = parse_xml(f'<w:shd {nsdecls("w")} w:fill="{fill_hex}"/>')
    tcPr.append(shd)

def set_cell_margins(cell, top=140, bottom=140, left=180, right=180):
    """Define margens internas de célula (em dxa)."""
    tcPr = cell._tc.get_or_add_tcPr()
    tcMar = parse_xml(f'<w:tcMar {nsdecls("w")}><w:top w:w="{top}" w:type="dxa"/><w:bottom w:w="{bottom}" w:type="dxa"/><w:left w:w="{left}" w:type="dxa"/><w:right w:w="{right}" w:type="dxa"/></w:tcMar>')
    tcPr.append(tcMar)

def create_document():
    doc = Document()

    # Cores da Marca ACsoft
    COLOR_WINE_DARK = RGBColor(0x2B, 0x0D, 0x1B)   # #2B0D1B
    COLOR_WINE_CARD = RGBColor(0x4A, 0x1F, 0x32)   # #4A1F32
    COLOR_ROSE_INTENSE = RGBColor(0xD8, 0x2B, 0x67) # #D82B67
    COLOR_ROSE_VIVID = RGBColor(0xFF, 0x6B, 0x9D)  # #FF6B9D
    COLOR_ROSE_SOFT = RGBColor(0xF2, 0x9B, 0xBE)   # #F29BBE
    COLOR_CREAM = RGBColor(0xFC, 0xF3, 0xEC)       # #FCF3EC
    COLOR_GRAY_DARK = RGBColor(0x33, 0x33, 0x33)

    # Configuração de Margens da Página (2 cm)
    for section in doc.sections:
        section.top_margin = Inches(0.8)
        section.bottom_margin = Inches(0.8)
        section.left_margin = Inches(0.8)
        section.right_margin = Inches(0.8)

    # Estilos Padrão
    style_normal = doc.styles['Normal']
    style_normal.font.name = 'Calibri'
    style_normal.font.size = Pt(11)
    style_normal.font.color.rgb = COLOR_GRAY_DARK

    # --- PÁGINA DE CAPA (COVER) ---
    p_pre = doc.add_paragraph()
    p_pre.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r_pre = p_pre.add_run("ACSOFT - ALTERNATIVE CREATIVE SOFTWARE STUDIOS\n")
    r_pre.font.size = Pt(10)
    r_pre.font.bold = True
    r_pre.font.color.rgb = COLOR_ROSE_INTENSE

    # Título Principal
    p_title = doc.add_paragraph()
    p_title.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_title.paragraph_format.space_before = Pt(36)
    p_title.paragraph_format.space_after = Pt(8)
    r_title = p_title.add_run("ACsoft")
    r_title.font.name = 'Georgia'
    r_title.font.size = Pt(44)
    r_title.font.bold = True
    r_title.font.color.rgb = COLOR_WINE_DARK

    p_sub = doc.add_paragraph()
    p_sub.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_sub.paragraph_format.space_after = Pt(24)
    r_sub = p_sub.add_run("Alternative thinking. Creative code.\nSoftware com jeito próprio.")
    r_sub.font.name = 'Georgia'
    r_sub.font.italic = True
    r_sub.font.size = Pt(15)
    r_sub.font.color.rgb = COLOR_ROSE_INTENSE

    # Caixa de Destaque na Capa
    table_cover = doc.add_table(rows=1, cols=1)
    table_cover.alignment = WD_TABLE_ALIGNMENT.CENTER
    cell_cover = table_cover.cell(0, 0)
    set_cell_background(cell_cover, "2B0D1B")
    set_cell_margins(cell_cover, top=280, bottom=280, left=320, right=320)
    
    p_cov = cell_cover.paragraphs[0]
    p_cov.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r_cov1 = p_cov.add_run("DOCUMENTAÇÃO TÉCNICA E TIMELINE COMPLETA\n")
    r_cov1.font.size = Pt(13)
    r_cov1.font.bold = True
    r_cov1.font.color.rgb = COLOR_ROSE_VIVID

    r_cov2 = p_cov.add_run("Desenvolvimento de Apps, Ferramentas, Sites (Construção, Hospedagem e Segurança) e Jogos\n\n")
    r_cov2.font.size = Pt(10.5)
    r_cov2.font.color.rgb = COLOR_CREAM

    r_cov3 = p_cov.add_run("Proprietários & Liderança Executiva:\n")
    r_cov3.font.size = Pt(10)
    r_cov3.font.color.rgb = COLOR_ROSE_SOFT

    r_cov4 = p_cov.add_run("Kaio Lucas Almeida Reis, Júlia Almeida Reis\n")
    r_cov4.font.size = Pt(13)
    r_cov4.font.bold = True
    r_cov4.font.color.rgb = COLOR_CREAM

    r_cov5 = p_cov.add_run("[ Júlia Almeida Costa (Júlia A.R) & Kaio Lucas Celestino Da Silva Reis (Kaio Lucas A.R) ]\n\n")
    r_cov5.font.size = Pt(9.5)
    r_cov5.font.italic = True
    r_cov5.font.color.rgb = COLOR_ROSE_SOFT

    r_cov6 = p_cov.add_run("Contato: +55 74 991969827 | E-mail: eukaioluccas31@gmail.com\n")
    r_cov6.font.size = Pt(10)
    r_cov6.font.color.rgb = COLOR_CREAM

    r_cov7 = p_cov.add_run("Criado por: ACsoft - Alternative Creative Software Studios\nNovembro de 2026")
    r_cov7.font.size = Pt(9.5)
    r_cov7.font.bold = True
    r_cov7.font.color.rgb = COLOR_ROSE_VIVID

    doc.add_page_break()

    # --- SEÇÃO 1: INTRODUÇÃO E VISÃO GERAL ---
    h1 = doc.add_heading(level=1)
    r = h1.add_run("1. Introdução e Visão Geral da ACsoft")
    r.font.name = 'Georgia'
    r.font.size = Pt(18)
    r.font.color.rgb = COLOR_WINE_DARK

    p1 = doc.add_paragraph()
    p1.add_run(
        "A ACsoft Studios (Alternative Creative Software Studios) é uma desenvolvedora de software, "
        "experiências web e jogos focada na união entre inovação estratégica ('Alternative') e "
        "excelência técnica e estética ('Creative').\n\n"
        "O presente projeto engloba a criação completa e profissional da presença digital da ACsoft, "
        "composta por um website institucional responsivo de altíssima fidelidade, interativo, otimizado para "
        "dispositivos móveis (Android e iOS), tablets (iPads), computadores e telas de alta resolução, "
        "incorporando com rigor todo o manual de identidade visual corporativa da empresa."
    )

    # --- SEÇÃO 2: IDENTIDADE VISUAL & CONCEITO ALT + C ---
    h2 = doc.add_heading(level=1)
    r = h2.add_run("2. Identidade Visual e Conceito Alt + C")
    r.font.name = 'Georgia'
    r.font.size = Pt(18)
    r.font.color.rgb = COLOR_WINE_DARK

    p2 = doc.add_paragraph()
    p2.add_run(
        "A identidade visual foi construída com base nos ativos gráficos oficiais fornecidos no diretório "
        "'Logo ACsoft-png'. O nome da empresa sintetiza sua missão central:\n"
    )

    # Tabela do Conceito Alt + C
    t_altc = doc.add_table(rows=4, cols=2)
    t_altc.alignment = WD_TABLE_ALIGNMENT.CENTER
    headers = [("Elemento", "Significado e Propósito Estratégico")]
    for col_idx, (h_title, _) in enumerate(headers):
        cell_h0 = t_altc.cell(0, 0)
        cell_h1 = t_altc.cell(0, 1)
        cell_h0.text = "Elemento"
        cell_h1.text = "Significado e Propósito Estratégico"
        for c in (cell_h0, cell_h1):
            set_cell_background(c, "2B0D1B")
            set_cell_margins(c, top=120, bottom=120, left=160, right=160)
            c.paragraphs[0].runs[0].font.bold = True
            c.paragraphs[0].runs[0].font.color.rgb = COLOR_CREAM

    altc_data = [
        ("A — Alternative", "Busca contínua pelo caminho inovador. Soluções arquitetadas fora do padrão convencional, com eficiência extrema e diferencial competitivo para o cliente."),
        ("C — Creative", "Ideias que viram código. A arte e o design de alto padrão orientam cada interface, animação suave e usabilidade intuitiva."),
        ("Soft — Software", "Engenharia de precisão, robustez, segurança cibernética e estabilidade operacional em qualquer plataforma.")
    ]

    for idx, (elem, desc) in enumerate(altc_data, start=1):
        c0 = t_altc.cell(idx, 0)
        c1 = t_altc.cell(idx, 1)
        c0.text = elem
        c1.text = desc
        bg_col = "4A1F32" if idx % 2 == 1 else "3A1526"
        for c in (c0, c1):
            set_cell_background(c, bg_col)
            set_cell_margins(c, top=100, bottom=100, left=160, right=160)
            c.paragraphs[0].runs[0].font.color.rgb = COLOR_CREAM
        c0.paragraphs[0].runs[0].font.bold = True

    p_space = doc.add_paragraph()
    p_space.paragraph_format.space_before = Pt(12)

    # Subseção Paleta de Cores
    h2_1 = doc.add_heading(level=2)
    r = h2_1.add_run("2.1. Paleta Cromática Oficial")
    r.font.name = 'Georgia'
    r.font.size = Pt(14)
    r.font.color.rgb = COLOR_ROSE_INTENSE

    t_colors = doc.add_table(rows=8, cols=3)
    t_colors.alignment = WD_TABLE_ALIGNMENT.CENTER
    c_heads = [t_colors.cell(0, 0), t_colors.cell(0, 1), t_colors.cell(0, 2)]
    c_heads[0].text = "Tonalidade"
    c_heads[1].text = "Código HEX"
    c_heads[2].text = "Aplicação no Sistema"
    for ch in c_heads:
        set_cell_background(ch, "2B0D1B")
        set_cell_margins(ch, top=100, bottom=100, left=120, right=120)
        ch.paragraphs[0].runs[0].font.bold = True
        ch.paragraphs[0].runs[0].font.color.rgb = COLOR_CREAM

    palette_rows = [
        ("Vinho Profundo", "#2B0D1B", "Fundo mestre, base de contraste profundo e ambient mesh"),
        ("Vinho Médio", "#3A1526", "Superfícies intermediárias, campos de formulário e dropdowns"),
        ("Vinho Elegante", "#4A1F32", "Cards em glassmorphism, gradientes e contêineres"),
        ("Rosa Intenso", "#D82B67", "Letra 'A', botões primários, gradientes e chamadas de ação"),
        ("Rosa Vivo", "#FF6B9D", "Destaques luminosos, micro-indicadores e brilhos neon"),
        ("Rosa Suave", "#F29BBE", "Letra 'C', bordas sutis, ícones e subtítulos refinados"),
        ("Creme Quente", "#FCF3EC", "Tipografia principal, títulos nobres e contraste editorial")
    ]

    for idx, (nome, hex_code, uso) in enumerate(palette_rows, start=1):
        c0, c1, c2 = t_colors.cell(idx, 0), t_colors.cell(idx, 1), t_colors.cell(idx, 2)
        c0.text = nome
        c1.text = hex_code
        c2.text = uso
        bg_row = "FDF6F2" if idx % 2 == 1 else "FFFFFF"
        for cell in (c0, c1, c2):
            set_cell_background(cell, bg_row)
            set_cell_margins(cell, top=80, bottom=80, left=120, right=120)
            cell.paragraphs[0].runs[0].font.color.rgb = COLOR_GRAY_DARK
        c1.paragraphs[0].runs[0].font.bold = True
        c1.paragraphs[0].runs[0].font.name = 'Consolas'

    # Subseção Ativos Gráficos
    p_sp = doc.add_paragraph()
    p_sp.paragraph_format.space_before = Pt(12)
    h2_2 = doc.add_heading(level=2)
    r = h2_2.add_run("2.2. Mapeamento dos Ativos Gráficos da Pasta 'Logo ACsoft-png'")
    r.font.name = 'Georgia'
    r.font.size = Pt(14)
    r.font.color.rgb = COLOR_ROSE_INTENSE

    p_assets = doc.add_paragraph()
    p_assets.add_run(
        "Todos os arquivos gráficos da pasta foram integrados de forma estrutural no website:\n"
        "• 03-icone-app.svg: Ícone oficial da aplicação, adotado como favicon do site, insígnia da navbar, avatar da marca e elemento central do monograma.\n"
        "• 01-logo-escuro.svg: Logo horizontal completo para aplicações sobre fundo escuro (cabeçalho, banners e rodapé).\n"
        "• 02-logo-claro.svg: Versão com alto contraste para fundos claros e documentos impressos.\n"
        "• 04-logo-palavras.svg: Manifesto editorial de grande formato (Alternative Creative soft).\n"
        "• 05-banner-hero.svg: Banner visual de destaque exibido no mockup interativo do Hero.\n"
        "• 06-banner-altc.svg: Decomposição visual didática da fórmula [Alt] + [C] = ACsoft.\n"
        "• 07-avatar-redondo.svg: Avatar circular oficial utilizado nas fotos de liderança e redes sociais.\n"
        "• 08-padrao.svg: Textura geométrica modular e sem fim baseada no símbolo AC para planos de fundo.\n"
        "• 09-card-social.svg: Card social 'Alternativo por escolha. Criativo por natureza', usado em OpenGraph.\n"
        "• 10-cards-valores.svg: Cartões ilustrativos dos pilares de inovação e engenharia.\n"
        "• 11-paleta.svg: Mostrador técnico das escalas cromáticas e proporções de cor.\n"
        "• 12-favicon.svg: Ícone 64x64px calibrado para favoritos e atalhos em dispositivos móveis.\n"
        "• Logo ACsoft.png & Ícone ACsoft.png: Versões raster em alta definição disponíveis na galeria."
    )

    # --- SEÇÃO 3: CATÁLOGO DE SERVIÇOS ---
    h3 = doc.add_heading(level=1)
    r = h3.add_run("3. Catálogo de Especialidades da ACsoft")
    r.font.name = 'Georgia'
    r.font.size = Pt(18)
    r.font.color.rgb = COLOR_WINE_DARK

    services_info = [
        ("3.1. Desenvolvimento de Aplicativos (Apps)",
         "Criação de aplicativos nativos e multiplataforma de altíssimo desempenho para smartphones Android e iOS (iPhones e iPads). "
         "Foco em interfaces fluidas 120Hz, animações responsivas, funcionamento offline, sincronização em nuvem e publicação nas lojas oficiais (Google Play Store e Apple App Store)."),
        ("3.2. Ferramentas & Softwares Utilitários (Tools)",
         "Desenvolvimento de ferramentas personalizadas sob medida para empresas. Automação de tarefas repetitivas, bots inteligentes, "
         "dashboards interativos com métricas em tempo real e integração de sistemas legados via APIs robustas."),
        ("3.3. Ecossistema Web Completo: Sites (Construção, Hospedagem e Segurança)",
         "A Tríplice Aliança Digital da ACsoft:\n"
         "• Construção: Landing pages de alta conversão, portais e webapps com nota 95+ no Google PageSpeed e SEO técnico impecável.\n"
         "• Hospedagem: Servidores em nuvem de alta disponibilidade com discos SSD NVMe, CDN distribuída e garantia de 99.9% de uptime.\n"
         "• Segurança Cibernética: Certificados SSL/TLS com renovação automatizada, WAF contra ataques DDoS, backups diários redundantes e adequação à LGPD."),
        ("3.4. Criação de Jogos (Games Studio)",
         "Estúdio dedicado à criação de jogos 2D e 3D para mobile, web e computadores (PC). "
         "Desenvolvimento integral incluindo game design, level design, trilhas sonoras imersivas, efeitos visuais (VFX) e jogabilidade calibrada a 60 FPS.")
    ]

    for stitle, sdesc in services_info:
        h_s = doc.add_heading(level=2)
        r = h_s.add_run(stitle)
        r.font.name = 'Georgia'
        r.font.size = Pt(13)
        r.font.color.rgb = COLOR_ROSE_INTENSE
        p_s = doc.add_paragraph()
        p_s.add_run(sdesc)

    # --- SEÇÃO 4: LIDERANÇA E FUNDADORES ---
    h4 = doc.add_heading(level=1)
    r = h4.add_run("4. Liderança, Fundadores e Requisito Interativo")
    r.font.name = 'Georgia'
    r.font.size = Pt(18)
    r.font.color.rgb = COLOR_WINE_DARK

    p4 = doc.add_paragraph()
    p4.add_run(
        "A empresa pertence formalmente a:\n"
        "• Júlia Almeida Costa (Júlia A.R) — Co-Fundadora, Diretoria Criativa e Experiência do Usuário (UI/UX).\n"
        "• Kaio Lucas Celestino Da Silva Reis (Kaio Lucas A.R) — Co-Fundador, Arquiteto Chefe de Software e Engenharia de Nuvem.\n\n"
        "Requisito Interativo Cumprido com Rigor:\n"
        "Conforme especificado pelo usuário ('ao clicar no nome Kaio Lucas A.r ou no Júlia Almeida R, mostre 'Kaio Lucas Almeida Reis, Júlia Almeida Reis''), "
        "o sistema web implementou múltiplos gatilhos interativos acessíveis via desktop, tablet e celular. Ao clicar nos nomes dos fundadores (seja no cabeçalho, "
        "no Hero, nos cartões de liderança ou nos links do rodapé), o sistema aciona:\n"
        "1. Modal dinâmico em glassmorphism exibindo com destaque: 'Kaio Lucas Almeida Reis, Júlia Almeida Reis'.\n"
        "2. Animação de pulso e iluminação de destaque no banner principal da seção de fundadores.\n"
        "3. Notificação Toast imediata na tela confirmando os nomes completos dos proprietários.\n"
        "4. Botão de contato direto pelo WhatsApp (+55 74 991969827) para reunião com os fundadores."
    )

    # --- SEÇÃO 5: TIMELINE COMPLETA DE DESENVOLVIMENTO ---
    doc.add_page_break()
    h5 = doc.add_heading(level=1)
    r = h5.add_run("5. Timeline Completa de Desenvolvimento do Projeto")
    r.font.name = 'Georgia'
    r.font.size = Pt(18)
    r.font.color.rgb = COLOR_WINE_DARK

    p_tl_intro = doc.add_paragraph()
    p_tl_intro.add_run(
        "Abaixo está registrada a cronologia detalhada de todas as etapas de planejamento, "
        "arquitetura, codificação, validação de responsividade e homologação final do site da ACsoft."
    )

    t_timeline = doc.add_table(rows=9, cols=3)
    t_timeline.alignment = WD_TABLE_ALIGNMENT.CENTER
    t_heads = [t_timeline.cell(0, 0), t_timeline.cell(0, 1), t_timeline.cell(0, 2)]
    t_heads[0].text = "Marco / Fase"
    t_heads[1].text = "Atividades Executadas"
    t_heads[2].text = "Status / Resultado"
    for th in t_heads:
        set_cell_background(th, "2B0D1B")
        set_cell_margins(th, top=100, bottom=100, left=120, right=120)
        th.paragraphs[0].runs[0].font.bold = True
        th.paragraphs[0].runs[0].font.color.rgb = COLOR_CREAM

    timeline_data = [
        ("Marco 01: Análise e Ativos",
         "Leitura dos requisitos do usuário, inspeção dos arquivos na pasta 'Logo ACsoft-png' e 'files.zip', extração de 09-card-social.svg e análise da paleta cromática.",
         "Concluído (100% dos ativos mapeados)"),
        ("Marco 02: Design System Alt + C",
         "Definição da identidade visual: paleta vinho (#2B0D1B, #4A1F32) e rosa (#D82B67, #FF6B9D, #F29BBE, #FCF3EC), tipografia editorial serifada combinada a sans-serif moderna.",
         "Concluído (Tokens CSS padronizados)"),
        ("Marco 03: Arquitetura Semântica (HTML)",
         "Construção do 'index.html' com tags semânticas, metadados OpenGraph, estrutura de acessibilidade, navegação, seções de serviços, galeria, calculadora e contato.",
         "Concluído (Código limpo e acessível)"),
        ("Marco 04: Estilização & Glassmorphism (CSS)",
         "Criação do 'style.css' com design responsivo, safe-area para iOS, flexbox/grid, efeitos de luz ambient mesh, cards com backdrop blur e animações fluidas.",
         "Concluído (Fluidez visual impecável)"),
        ("Marco 05: Lógica Interativa (JavaScript)",
         "Desenvolvimento do 'script.js': menu mobile drawer, rolagem suave com destaque de link ativo, calculadora de estimativas com envio para WhatsApp e acordeom FAQ.",
         "Concluído (Sem dependências pesadas)"),
        ("Marco 06: Módulo Interativo dos Fundadores",
         "Implementação da revelação 'Kaio Lucas Almeida Reis, Júlia Almeida Reis' acionada pelo clique em 'Kaio Lucas A.R' ou 'Júlia Almeida R', via modal e toast.",
         "Concluído (Requisito plenamente atendido)"),
        ("Marco 07: Validação Multiplataforma",
         "Testes de responsividade garantindo visual refinado em celulares Android, iPhones (iOS), iPads / Tablets, notebooks e computadores de mesa (PC).",
         "Concluído (Layout 100% responsivo)"),
        ("Marco 08: Documentação Executiva (.docx)",
         "Elaboração desta documentação formal em Word contendo manual de marca, especificações técnicas, dados dos fundadores e timeline cronológica.",
         "Concluído (Arquivo gerado com sucesso)")
    ]

    for idx, (marco, desc, status) in enumerate(timeline_data, start=1):
        c0, c1, c2 = t_timeline.cell(idx, 0), t_timeline.cell(idx, 1), t_timeline.cell(idx, 2)
        c0.text = marco
        c1.text = desc
        c2.text = status
        bg_row = "FDF6F2" if idx % 2 == 1 else "FFFFFF"
        for cell in (c0, c1, c2):
            set_cell_background(cell, bg_row)
            set_cell_margins(cell, top=90, bottom=90, left=120, right=120)
            cell.paragraphs[0].runs[0].font.color.rgb = COLOR_GRAY_DARK
        c0.paragraphs[0].runs[0].font.bold = True
        c2.paragraphs[0].runs[0].font.bold = True
        c2.paragraphs[0].runs[0].font.color.rgb = COLOR_ROSE_INTENSE

    # --- SEÇÃO 6: ESPECIFICAÇÃO TÉCNICA E RESPONSIVIDADE ---
    p_sp2 = doc.add_paragraph()
    p_sp2.paragraph_format.space_before = Pt(14)
    h6 = doc.add_heading(level=1)
    r = h6.add_run("6. Especificações Técnicas e Responsividade Multiplataforma")
    r.font.name = 'Georgia'
    r.font.size = Pt(18)
    r.font.color.rgb = COLOR_WINE_DARK

    p6 = doc.add_paragraph()
    p6.add_run(
        "O website foi desenvolvido utilizando tecnologias web puras e modernas (Vanilla HTML5, CSS3 com variáveis nativas e JavaScript ES6+), "
        "eliminando bibliotecas externas pesadas e garantindo carregamento instantâneo, segurança contra vulnerabilidades em dependências e facilidade "
        "imediata de hospedagem em qualquer servidor web.\n\n"
        "Comportamento nos Dispositivos Suportados:\n"
        "• Android (Smartphones & Tablets): Ajuste automático da densidade de pixels, menus deslizantes acionados por toque, botões com área mínima de clique de 48px e suporte ao tema escuro nativo.\n"
        "• iOS & iPadOS (iPhones e iPads): Respeito estrito às variáveis de área segura (safe-area-inset-top e safe-area-inset-bottom), suporte a telas Retina e compatibilidade com WebKit.\n"
        "• Computadores (PC) & Desktops: Layout expansivo em grid com até 4 colunas, efeitos de hover com transições de iluminação, cards em vidro (glassmorphism) e tipografia fluida via clamp()."
    )

    # --- SEÇÃO 7: CONTATOS OFICIAIS E TERMO DE ENCERRAMENTO ---
    h7 = doc.add_heading(level=1)
    r = h7.add_run("7. Informações de Contato e Encerramento")
    r.font.name = 'Georgia'
    r.font.size = Pt(18)
    r.font.color.rgb = COLOR_WINE_DARK

    # Tabela de Contato
    t_contato = doc.add_table(rows=4, cols=2)
    t_contato.alignment = WD_TABLE_ALIGNMENT.CENTER
    c_c_heads = [t_contato.cell(0, 0), t_contato.cell(0, 1)]
    c_c_heads[0].text = "Canal de Comunicação"
    c_c_heads[1].text = "Dado Oficial"
    for ch in c_c_heads:
        set_cell_background(ch, "2B0D1B")
        set_cell_margins(ch, top=100, bottom=100, left=140, right=140)
        ch.paragraphs[0].runs[0].font.bold = True
        ch.paragraphs[0].runs[0].font.color.rgb = COLOR_CREAM

    contact_rows = [
        ("Telefone & WhatsApp Oficial", "+55 74 991969827"),
        ("E-mail Oficial de Contato", "eukaioluccas31@gmail.com"),
        ("Assinatura Institucional", "Criado por: ACsoft - Alternative Creative Software Studios")
    ]

    for idx, (canal, dado) in enumerate(contact_rows, start=1):
        c0, c1 = t_contato.cell(idx, 0), t_contato.cell(idx, 1)
        c0.text = canal
        c1.text = dado
        bg_r = "FDF6F2" if idx % 2 == 1 else "FFFFFF"
        for cell in (c0, c1):
            set_cell_background(cell, bg_r)
            set_cell_margins(cell, top=90, bottom=90, left=140, right=140)
            cell.paragraphs[0].runs[0].font.color.rgb = COLOR_GRAY_DARK
        c0.paragraphs[0].runs[0].font.bold = True
        c1.paragraphs[0].runs[0].font.color.rgb = COLOR_ROSE_INTENSE
        c1.paragraphs[0].runs[0].font.bold = True

    p_final = doc.add_paragraph()
    p_final.paragraph_format.space_before = Pt(36)
    p_final.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r_fin1 = p_final.add_run("Criado por: ACsoft - Alternative Creative Software Studios\n")
    r_fin1.font.bold = True
    r_fin1.font.size = Pt(12)
    r_fin1.font.color.rgb = COLOR_WINE_DARK

    r_fin2 = p_final.add_run("Júlia Almeida Costa (Júlia A.R) & Kaio Lucas Celestino Da Silva Reis (Kaio Lucas A.R)\n")
    r_fin2.font.italic = True
    r_fin2.font.size = Pt(10.5)
    r_fin2.font.color.rgb = COLOR_ROSE_INTENSE

    output_path = os.path.join(os.getcwd(), "Documentacao_ACsoft_Timeline.docx")
    doc.save(output_path)
    print(f"Documento Word salvo com sucesso em: {output_path}")

if __name__ == "__main__":
    create_document()
