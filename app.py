import streamlit as st

# Função para calcular a pontuação total e classificar o usuário
def calculate_score(total_score):
    if 16 <= total_score <= 20:
        return "Você é um Inovador – Gosta de experimentar novas tecnologias e assumir riscos."
    elif 11 <= total_score <= 15:
        return "Você é um Adotante Inicial – É receptivo a novas tecnologias, mas busca valor agregado claro."
    elif 6 <= total_score <= 10:
        return "Você está na Primeira Maioria – Prefere adotar inovações que já foram testadas e aprovadas."
    else:
        return "Você está na Última Maioria ou é um Retardatário – Prefere estabilidade e minimiza riscos ao adotar novas tecnologias."

# Perguntas e opções com pontuação
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
    {
        "question": "Qual dos seguintes fatores é mais importante para você ao considerar um novo produto?",
        "options": [
            ("Necessidade e praticidade – adoto apenas se resolver um problema prático.", 1),
            ("Exclusividade e inovação – gosto de experimentar algo novo antes dos outros.", 4),
            ("Benefícios claros e comprovados – adoto se vejo valor agregado significativo.", 3),
            ("Aceitação social e popularidade – prefiro adotar quando outras pessoas já estão usando.", 2)
        ]
    },
    {
        "question": "Você participa de versões beta ou experimentais de produtos?",
        "options": [
            ("Raramente – prefiro produtos finalizados e estáveis.", 2),
            ("Às vezes, se estou muito interessado na novidade.", 3),
            ("Nunca – prefiro esperar até que o produto esteja consolidado.", 1),
            ("Sim, frequentemente – gosto de explorar novidades e dar feedback.", 4)
        ]
    },
    {
        "question": "Como você lida com o risco de adotar novas tecnologias?",
        "options": [
            ("Considero o risco, mas adoto se houver um bom custo-benefício.", 3),
            ("Evito riscos – prefiro esperar até que o produto esteja estável.", 2),
            ("Aceito o risco, pois vejo valor em ser um dos primeiros.", 4),
            ("Não gosto de riscos e evito inovações até que sejam necessárias.", 1)
        ]
    },
    {
        "question": "Ao adotar uma nova tecnologia, qual é sua abordagem para buscar informações?",
        "options": [
            ("Espero que pessoas próximas testem primeiro e compartilhem suas experiências.", 2),
            ("Pesquiso intensamente em comunidades e redes especializadas, para me manter na vanguarda.", 4),
            ("Acompanho as novidades, mas busco opiniões de usuários iniciais.", 3),
            ("Busco informações apenas quando não tenho outra escolha.", 1)
        ]
    }
]

# Título do aplicativo
st.title("Questionário de Identificação do Perfil de Adotante de Inovação")

# Variável para somar a pontuação
total_score = 0

# Exibir cada pergunta com suas opções de resposta
for i, q in enumerate(questions):
    st.write(f"{i + 1}. {q['question']}")
    options = [option[0] for option in q["options"]]
    selected_option = st.radio("Escolha uma opção:", options, key=i)
    # Adicionar a pontuação da resposta selecionada
    score = dict(q["options"])[selected_option]
    total_score += score

# Botão para calcular e exibir o resultado
if st.button("Ver Resultado"):
    result = calculate_score(total_score)
    st.write("Resultado:")
    st.write(result)
