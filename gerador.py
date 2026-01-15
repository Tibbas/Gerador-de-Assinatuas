

""" quando for rodar o codigo instala o streamlit usando na cmd:
            pip install streamlit
    
    e pra rodar usa esse comando, porque por algum motivo da forma tradicional nao estava rodando:

    forma normal: streamlit run gerador.py
    forma que da certo: python -m streamlit run gerador.py
``` [2][5]

Copia esses numeros tambem.

"""


import streamlit as st
import hashlib
from passlib.context import CryptContext
import streamlit.components.v1 as components


pwd_context = CryptContext(schemes=["argon2"], deprecated="auto")

USUARIO_HASH = "d4d17945af7692a0a59ac322039f6da6b160374ffb719c3714a57c906e0663b7"
HASH_SENHA = "$argon2id$v=19$m=65536,t=3,p=4$/T8n5BzD+F8rRcj5P4ewdg$btjvLhjcjoGP2Xa3SqAgSUvVa9u/fl6o6dXvyWzNtvg"


def hash_usuario(usuario: str) -> str:
    return hashlib.sha256(usuario.strip().lower().encode()).hexdigest()


if "pagina" not in st.session_state:
    st.session_state.pagina = "login"

if "clicked" not in st.session_state:
    st.session_state.clicked = False


st.markdown("""
<style>
.card {
    padding: 2rem;
    border-radius: 12px;
    max-width: 420px;
    margin: 80px auto;
}
.card h2 {
    text-align: center;
    margin-bottom: 1.5rem;
}
</style>
""", unsafe_allow_html=True)


def tela_login():
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.markdown("<h2>🔐 Login</h2>", unsafe_allow_html=True)

    user = st.text_input("Usuário")
    pwd = st.text_input("Senha", type="password")

    if st.button("Entrar", use_container_width=True):
        if (
            hash_usuario(user) == USUARIO_HASH
            and pwd_context.verify(pwd, HASH_SENHA)
        ):
            st.session_state.pagina = "gerador"
            st.rerun()
        else:
            st.error("Usuário ou senha inválidos")

    st.markdown('</div>', unsafe_allow_html=True)


def tela_gerador():
    st.title("📚 Gerador de Assinaturas")

    col1, col2 = st.columns([6, 1])
    with col2:
        if st.button("🚪 Sair"):
            st.session_state.pagina = "login"
            st.session_state.clicked = False
            st.rerun()

    st.markdown("Insira os dados solicitados para gerar a assinatura:")

    nome_usuario = st.text_input("🔍 Nome do usuário:")
    gerencia = st.text_input("📋 Digite o Setor:")
    cargo = st.text_input("💼 Digite o Cargo do usuário:")
    ramal_str = st.text_input("📞 Digite o Ramal:")

    col_texto, col_checkbox = st.columns([6, 1])

    with col_texto:
        st.markdown(
            "<div style='padding-top:6px;'>📌 Funcionário do Compras</div>",
            unsafe_allow_html=True
        )

    with col_checkbox:
        funcionario_compras = st.checkbox(
            "funcionario_compras_hidden",
            key="funcionario_compras",
            label_visibility="collapsed"
        )

    if ramal_str:
        ramal_numeros = ''.join(filter(str.isdigit, ramal_str))
        if ramal_numeros.isdigit() and len(ramal_numeros) >= 4:
            ramal_int = int(ramal_numeros)
            st.success(f"✅ Ramal limpo: {ramal_int}")
        else:
            st.error("❌ Só números, mínimo 4 dígitos!")

    def click_button():
        st.session_state.clicked = True

    st.button("Gerar Assinatura", use_container_width=True, on_click=click_button)

    if st.session_state.clicked:
        if funcionario_compras:
            html_content = f"""
                <!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Assinatura E-mail nova</title>
    <style>
        body{{
            background-color: white;
            color: black;
            width: 100%;
            min-height: 100vh;
        }}
        table{{
            font-family: verdana;
            width:620px; 
            height: 200px; 
            font-size: 14px; 
            border-collapse: collapse;
        }}
        .imageOnaCssjd{{
            margin-left: 10px; 
            width:250px;
        }}
        td{{
            padding: 5px;
        }}
        a{{
            text-decoration: none; 
            display: inline-block; 
        }}
    </style>
</head>
    <body>
        <table>
            <tbody>
                <tr>
                    <td rowspan="4"><img class="imageOnaCssjd" src="https://htmlsigs.s3.amazonaws.com/logos/files/001/360/346/landscape/zyro-image.png" alt=""></td>
                    <td class="tdNomeUsuario" style="font-size: 12px;">
                        <span style="font-weight: 600; font-size: 14px;">{nome_usuario}</span><br>
                        <span style="font-weight: 600;">Gerência de {gerencia} - {cargo}</span><br>
                        (37)3229-7700 | (37)3229-{ramal_str}<br><br>
                        <a href="https://www.instagram.com/cssjd_divinopolis/" target="_blank">
                            <img src="https://cssjd.org.br/imagens/assinaturas/v2/cssjd_07.gif" alt="Instagram" width="30" height="30">
                        </a>
                        <a href="https://www.facebook.com/cssjddivinopolis/" target="_blank">
                            <img src="https://cssjd.org.br/imagens/assinaturas/v2/cssjd_08.gif" alt="Facebook" width="30" height="30">
                        </a>
                        <a href="https://www.youtube.com/channel/UCpxoWYHt1gYIbR4G0QWTklA" target="_blank">
                            <img src="https://cssjd.org.br/imagens/assinaturas/v2/cssjd_09.gif" alt="Youtube" width="30" height="30">
                        </a>
                        <span style="display:inline-block;">&nbsp;&nbsp;Site: www.cssjd.org.br</span><br>
                        <span style="font-size: 11px;">Fundação Geraldo Corrêa - CNPJ 20.146.064/0001-2<br>Rua do Cobre - 800 - Bairro São João de Deus <br>35500-227 - Divinópolis - MG</span>
                    </td>
                </tr>
            </tbody>
        </table>
    </body>
</html>
"""
        else:
            html_content = f"""
                <!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Assinatura Email dafault</title>
    <style>
        *{{
            box-sizing: border-box;
            padding: 0;
            margin: 0;
        }}

        body{{
            margin: 10px;
            min-height: 80vh;
            font-family: Verdana, Geneva, Tahoma, sans-serif;
            font-size: 14px;
            line-height: 20px;
            background-color: white;
            color: black;
            width: 100%;
            min-height: 100vh;
        }}

        table{{
            text-align: left;
            min-width: 620px;
            height: 210px;
            border-collapse: unset;
        }}

        tbody{{
            padding: 10px;
        }}

        td{{
            vertical-align: middle;
        }}

        .imageOnaCssjd{{
            margin-left: 10px; 
            width:270px;
        }}

        .spanName{{
            font-size: 16px;
        }}

        #containerRamal{{
            margin-top: -10px;
        }}

        #containerLinksDiversos td a{{
            text-decoration: none;
            color: black;
        }}

        #containerLinksDiversos td a img{{
            width: 42px;
            height: 42px;
        }}

    </style>
</head>
<body>
    <table>
        <tbody>
            <tr>
                <td rowspan="4"><img class="imageOnaCssjd" src="https://htmlsigs.s3.amazonaws.com/logos/files/001/360/346/landscape/zyro-image.png"></td>
            </tr>
            
            <tr id="containerNameSetor">
                <td><strong><span class="spanName">{nome_usuario}</span><br>Gerência de {gerencia} - {cargo}</strong><br><span style="line-height: 28px;">(37)3229-7700 | (37)3229-{ramal_str}</span></td>
            </tr>

            <tr id="containerLinkhospital">
                <td>Site: www.cssjd.org.br</td>
            </tr>

            <tr id="containerLinksDiversos">
                <td>
                    <a href="https://www.facebook.com/cssjddivinopolis/" target="_blank">
                        <img src="https://cssjd.org.br/imagens/assinaturas/v2/cssjd_08.gif" alt="Facebook" width="30" height="30">
                    </a>
                    <a href="https://www.instagram.com/cssjd_divinopolis/" target="_blank">
                        <img src="https://cssjd.org.br/imagens/assinaturas/v2/cssjd_07.gif" alt="Instagram" width="30" height="30">
                    </a>
                    <a href="https://www.youtube.com/channel/UCpxoWYHt1gYIbR4G0QWTklA" target="_blank">
                        <img src="https://cssjd.org.br/imagens/assinaturas/v2/cssjd_09.gif" alt="Youtube" width="30" height="30">
                    </a>
                </td>
            </tr>
        </tbody>
    </table>
</body>
</html>
"""

        components.html(html_content, height=220)


if st.session_state.pagina == "login":
    tela_login()

elif st.session_state.pagina == "gerador":
    tela_gerador()
