import streamlit as st
import openai

client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

st.set_page_config(page_icon="./favicon.ico")
st.sidebar.title(":wrench:Configuration du Chatbot")
st.sidebar.image("./favicon.ico")
st.title("Bienvenue sur l'application de chat IA :robot:: de Le Spéc:rainbow['IA']liste du Vrac 🌱")

st.sidebar.write("inserrer votre cle API 🔑 de openAI et l'ID de votre assistant OpenAI ici ⬇️")
api_key = st.sidebar.text_input("Clé API de OpenAI")
st.sidebar.warning("(Assurez-vous d'inserrer la meme clé API lors de la création de l'assistant qui correspond a votre assistant)")
assistant_id = st.sidebar.text_input("ID de l'assistant")

def login_user(username):
    # Simule une vérification de l'identifiant utilisateur
    return username == "admin"

def main():
    st.title("Login")

    if 'logged_in' not in st.session_state:
        st.session_state['logged_in'] = False

    if st.session_state['logged_in']:
        st.success(f"Vous êtes connecté en tant que 🛻 {st.session_state['username']}!")
        st.button("Se déconnecter", on_click=lambda: st.session_state.update(logged_in=False, username=None))
    else:
        with st.form("login_form"):
            username = st.text_input("Nom d'utilisateur")
            password = st.text_input("Mot de passe", type='password')
            submit_button = st.form_submit_button("Se connecter")

            if submit_button and login_user(username):
                st.session_state['logged_in'] = True
                st.session_state['username'] = username
                st.experimental_rerun()
            elif submit_button:
                st.error("Échec de la connexion. Veuillez réessayer.")


    def ask_openai(question, api_key, assistant_id):
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": question}],
            api_key=api_key,
            system="assistant",
            assistant_id=assistant_id
    )

    return response.choices[0].message['content']
if __name__ == "__main__":
    main()

