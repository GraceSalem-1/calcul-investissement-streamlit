import streamlit as st
st.title("💰Calculateur de rentabilité d'un investissement")

# Les champs utilisateur
capital = st.number_input("💶 Capital initial (€)", min_value=0.0, step=100.0, format="%.2f")
taux = st.number_input("Taux d'intérêt annuel (%)", min_value=0.0, max_value=100.0, step=0.1, format="%.2f")
duree = st.number_input("📅 Durée en années", min_value=1, step=1)

# Calcul du capital futur
if st.button("Calculer"):
    valeur_future = capital * (1 + taux/100) ** duree
    st.success(f"🎯Après {duree} ans, votre investissement vaudra {valeur_future:.2f} € 🔥")

# Graphique de croissance
import pandas as pd
import matplotlib.pyplot as plt

# Calcul de la valeur année par année
annees = list(range(1, int(duree)+1))
valeurs = [capital * (1 + taux/100)**i for i in annees]

# Creation d'un DataFrame pour faciliter le graphique
df = pd.DataFrame({"Année": annees, "Valeur": valeurs})

# Creation du graphique
fig, ax = plt.subplots()
ax.plot(df["Année"], df["Valeur"], marker='o', color='green')
ax.set_title("Evolution du capital année par année")
ax.set_xlabel("Année")
ax.set_ylabel("Valeur (€)")
st.pyplot(fig)

