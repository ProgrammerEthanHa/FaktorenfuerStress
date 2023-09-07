import streamlit as st
import pandas as pd
import altair as alt

st.header("Welche Faktoren würden bei Ihnen Stress auf der Arbeit fördern?")
st.subheader("")

source = pd.DataFrame({
        'Anteil (%)': [46, 45, 32, 31, 21, 21],
        'Faktoren': ['Zeitdruck', 'Arbeitsatmosphäre', 'Leistungsdruck', 'Große Aufgabenmenge', 'Angst um Arbeitsplatz', 'Dauerhafte Erreichbarkeit']
})
bar_chart = alt.Chart(source).mark_bar().encode(
        y='Anteil (%):Q',
        x='Faktoren:O',
    )
st.altair_chart(bar_chart, use_container_width=True)


txt = st.text_area('', '''
    Basis: 2027 Befragte; 2019
    ''')
st.text("Klicke an die Balken um die Daten genauer anzuschauen. Du kannst auch die Diagramm vergrößern und ein Bild davon machen")
st.text("Quelle: Swiss Life Deutschland und Yougov Deutschland")