import streamlit as st
from search_algorithms import naive_search, kmp_search, rabin_karp

st.set_page_config(page_title="String Search Comparison", layout="wide")

st.title("String Search Algorithm Comparison")

text = st.text_area(
    "Enter Text",
    value="AABAACAADAABAABA",
    height=150
)

pattern = st.text_input(
    "Enter Pattern",
    value="AABA"
)

if st.button("Search"):
    naive_matches, naive_comp = naive_search(text, pattern)
    kmp_matches, kmp_comp = kmp_search(text, pattern)
    rk_matches, rk_comp = rabin_karp(text, pattern)

    st.subheader("Results")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("Naive Comparisons", naive_comp)
        st.write("Matches:", naive_matches)

    with col2:
        st.metric("KMP Comparisons", kmp_comp)
        st.write("Matches:", kmp_matches)

    with col3:
        st.metric("Rabin-Karp Comparisons", rk_comp)
        st.write("Matches:", rk_matches)

    st.subheader("Performance Comparison")

    st.bar_chart({
        "Naive": naive_comp,
        "KMP": kmp_comp,
        "Rabin-Karp": rk_comp
    })
