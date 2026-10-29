
# Inicialização da Memória da Sessão
import streamlit as st

st.title(" Aprendendo Streamlit")

# 1. VERIFICAÇÃO E INICIALIZAÇÃO DA MEMÓRIA DE SESSÃO (SESSION STATE) - O Streamlit recarrega o script do zero a cada clique. Se não salvarmos a variável
# no 'st.session_state', ela seria resetada para 0 a cada interatividade na tela.
if "contador_doacoes" not in st.session_state:
    # Se a chave 'contador_doacoes' ainda não existir na memória da sessão atual do usuário, nós a criamos e a inicializamos com o valor 0.
    st.session_state.contador_doacoes = 0

# 2. LAYOUT EM COLUNAS - Cria 2 colunas lado a lado na interface gráfica para organizar visualmente os botões.
col1, col2 = st.columns(2)

# 3. LÓGICA E BOTÃO DA PRIMEIRA COLUNA (INCREMENTO) - O bloco 'with col1:' indica que tudo dentro dele será desenhado na primeira coluna (esquerda).
with col1:
    # 'st.button()' desenha o botão na tela e retorna True APENAS no momento em que é clicado.
    if st.button("Registrar Doação (+10 kg)"):
        # Se o usuário clicar neste botão, adicionamos +10 ao valor que já está guardado no session_state.
        st.session_state.contador_doacoes += 10

# 4. LÓGICA E BOTÃO DA SEGUNDA COLUNA (RESET) - O bloco 'with col2:' indica que tudo dentro dele será desenhado na segunda coluna (direita).
with col2:
    # Desenha o segundo botão na tela.
    if st.button("Zerar Painel"):
        # Se o usuário clicar neste botão, redefinimos o contador guardado diretamente para 0.
        st.session_state.contador_doacoes = 0

# 5. EXIBIÇÃO DINÂMICA DA MÉTRICA - Desenha um componente visual de cartão de destaque (KPI/Métrica) na interface.
# O parâmetro 'label' é o título do cartão e 'value' é o texto exibido em destaque.
# Usamos uma f-string para formatar dinamicamente o número atualizado do 'session_state' seguido de 'kg'.
st.metric(
    label="Total de Alimentos no Dia", 
    value=f"{st.session_state.contador_doacoes} kg"
)