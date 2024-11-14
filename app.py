import streamlit as st

# Função para calcular o total da pontuação e classificar o usuário
def calculate_score(total_score):
    if 16 <= total_score <= 20:
        return "Você é um Inovador – Gosta de experimentar novas tecnologias e assumir riscos."
    elif 11 <= total_score <= 15:
        return "Você é um Adotante Inicial – É receptivo a novas tecnologias, mas busca valor agregado claro."
    elif 6 <= total_score <= 10:
        return "Você está na Primeira Maioria – Prefere adotar inovações que já foram testadas e aprovadas."
    else:
        return "Você está na Última Maioria ou é um Retardatário – Prefere estabilidade e minimiza riscos ao adotar novas tecnologias."

# Perguntas e opções
questions = [
    {
        "question": "Com que frequência você adota novas tecnologias ou produtos após o lançamento?",
        "options": [
            ("Prefiro esperar até que a tecnologia seja amplamente usada e considerada confiável.", 2),
            ("Sempre que possível, gosto de ser um dos primeiros a testar.", 4),
            ("Adoto apenas quando realmente necessário ou inevitável.", 1),
            ("Adoto cedo, mas espero ver algumas opiniões iniciais.", 3)
        ]
    },
    # ... (outras perguntas como no código anterior)
]

# Título do aplicativo
st.title("Questionário de Identificação do Perfil de Adotante de Inovação")

total_score = 0

# Exibição das perguntas
for q in questions:
    st.write(q["question"])
    options = [option[0] for option in q["options"]]
    answer = st.radio("", options)
    score = dict(q["options"])[answer]
    total_score += score

# Exibir resultado final
if st.button("Ver Resultado"):
    result = calculate_score(total_score)
    st.write("Resultado:")
    st.write(result)
