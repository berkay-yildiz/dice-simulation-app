import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.title("Zar Atışı Simülasyonu")

n_rolls = st.slider(
    "Kaç kez zar atılsın?",
    min_value=10,
    max_value=1_000_000,
    value=100,
    step=10
)

rolls = np.random.randint(1, 7, n_rolls)

# Bar chart için dağılım
values, counts = np.unique(rolls, return_counts=True)
percentages = counts / n_rolls * 100

# Estetik grafik
fig, ax = plt.subplots(figsize=(7, 4))

bars = ax.bar(
    values,
    counts,
    width=0.6,
    color="#4c72b0",          # soft mavi ton
    edgecolor="black",
    linewidth=1
)

# Grid çizgileri
ax.grid(axis="y", linestyle="--", alpha=0.5)

ax.set_title(f"{n_rolls} Zar Atışı Sonucu", fontsize=14, fontweight="bold")
ax.set_xlabel("Zar Yüzü (1–6)")
ax.set_ylabel("Tekrarlanma Sayısı")
ax.set_xticks(values)

# Her barın üzerine yüzde yaz
for bar, pct in zip(bars, percentages):
    height = bar.get_height()
    ax.text(
        bar.get_x() + bar.get_width() / 2,
        height,
        f"%{pct:.1f}",
        ha="center",
        va="bottom",
        fontsize=10,
        fontweight="bold"
    )

st.pyplot(fig)
