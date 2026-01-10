import streamlit as st
import streamlit.components.v1 as components


st.title("📚 Gerador de Assinaturas")


st.markdown("Insira os dados solicitados para gerar a assitura:")


nome_usuario = st.text_input("🔍 Nome do usuário:")
gerencia = st.text_input("🔍 Digite a Gerência:")
cargo = st.text_input("💼 Digite o Cargo do usuário:")
ramal_str = st.text_input("📞 Digite o Ramal:")




st.markdown("""
<style>
.checkbox-container {
    display: flex;
    align-items: center;
    gap: 8px;
}
</style>


<label class="checkbox-container">
    📌 Funcionário do compras
    <input type="checkbox">
</label>
""", unsafe_allow_html=True)



if ramal_str:
    ramal_numeros = ''.join(filter(str.isdigit, ramal_str))
    
    if ramal_numeros.isdigit() and len(ramal_numeros) >= 4:
        ramal_int = int(ramal_numeros)
        st.success(f"✅ Ramal limpo: {ramal_int}")
    else:
        st.error("❌ Só números, mínimo 8 dígitos!")



col3, col4, col5 = st.columns([2, 2, 2])


with col4:
    if 'clicked' not in st.session_state:
        st.session_state.clicked = False
    
    def click_button():
        st.session_state.clicked = True

    button = st.button("Gerar Assinatura", use_container_width=100, on_click=click_button)

# AQUI FORA DO IF - defina html_content
if st.session_state.clicked:
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
                        (37)3229-7555 | {ramal_str}<br><br>
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
    
    components.html(html_content, height=300)
    
