import streamlit as st

st.title("📚 Gerador de Assinaturas")

st.markdown("Insira os dados solicitados para gerar a assitura:")

nome_usuario = st.text_input("🔍 Nome do usuário:")
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
    button = st.button("Gerar Assinatura", use_container_width=100)





