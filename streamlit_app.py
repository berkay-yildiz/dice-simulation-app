import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.title("Zar Atışı Simülasyonu")

# Max 1.000.000
n_rolls = st.slider(
    "Kaç kez zar atılsın?",
    min_value=10,
    max_value=1_000_000,
    value=100,
    step=10
)

rolls = np.random.randint(1, 7, n_rolls)

fig, ax = plt.subplots(figsize=(6, 4))
ax.hist(rolls, bins=np.arange(0.5, 7.5, 1), rwidth=0.8, edgecolor='black')
ax.set_title(f"{n_rolls} Zar Atışı Sonucu")
ax.set_xlabel("Zar Yüzü (1–6)")
ax.set_ylabel("Tekrarlanma Sayısı")
ax.set_xticks(range(1, 7))

st.pyplot(fig)
