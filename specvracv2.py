import streamlit as st

st.title("Bienvenue sur l'application de chat IA de Le Spéc:rainbow['IA']liste du Vrac")

def login_user(username):
    # Simule une vérification de l'identifiant utilisateur
    return username == "admin"

def main():
    st.title("Login")

    if 'logged_in' not in st.session_state:
        st.session_state['logged_in'] = False

    if st.session_state['logged_in']:
        st.success(f"Vous êtes connecté en tant que {st.session_state['username']}!")
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

if __name__ == "__main__":
    main()

