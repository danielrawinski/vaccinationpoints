import streamlit as st
import streamlit.components.v1 as components

st.header("Mapa punktów szczepień w Polsce")

selection = st.selectbox("Wybierz województwo:", ["Dolnośląskie",
                                                  "Kujawsko-pomorskie",
                                                  "Lubelskie",
                                                  "Lubuskie",
                                                  "Łódzkie",
                                                  "Małopolskie",
                                                  "Mazowieckie",
                                                  "Opolskie",
                                                  "Podkarpackie",
                                                  "Podlaskie",
                                                  "Pomorskie",
                                                  "Śląskie",
                                                  "Świętokrzyskie",
                                                  "Warmińsko-mazurskie",
                                                  "Wielkopolskie",
                                                  "Zachodniopomorskie"])
                                                  
HtmlFile = open(fr"{selection}.html", 'r', encoding='utf-8')
source_code = HtmlFile.read() 
components.html(source_code, width=700, height=700)

st.write("""Mapa została stworzona w oparciu o dane z gov.pl z dnia 5 stycznia.
          Dołożyłem wszelkich starań, by dane były jak najbardziej poprawne, ale proszę o
          zgłaszanie ewentualnych błędów na daniel.rawinski@gmail.com""")
