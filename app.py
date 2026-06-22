import streamlit as st
from search_algorithms import naive_search, kmp_search, rabin_karp

st.title("String Search Algorithm Visualizer")

text = st.text_area(
    "Enter Text",
    "AABAACAADAABAABA"
)

pattern = st.text_input(
    "Enter Pattern",
    "AABA"
)

if st.button("Run Search"):
    m1, c1 = naive_search(text, pattern)
    m2, c2 = kmp_search(text, pattern)
    m3, c3 = rabin_karp(text, pattern)

    st.subheader("Results")

    st.write(f"**Naive Search:** Matches = {m1}, Comparisons = {c1}")
    st.write(f"**KMP Search:** Matches = {m2}, Comparisons = {c2}")
    st.write(f"**Rabin-Karp:** Matches = {m3}, Comparisons = {c3}")
