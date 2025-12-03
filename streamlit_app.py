import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import time

st.title("Zar Atışı Simülasyonu")

n_rolls = st.slider(
    "Kaç kez zar atılsın?",
    min_value=10,
    max_value=1_000_000,
    value=100,
    step=10
)

start_button = st.button("Zarı At 🎲")

if start_button:

    # --- Animasyon Alanı ---
    anim = st.empty()

    dice_frames = [
        "⚀", "⚁", "⚂", "⚃", "⚄", "⚅",
    ]

    # 10 tekrar → 0.6 saniyelik animasyon
    for _ in range(10):
        anim.markdown(
            f"<h1 style='text-align:center;font-size:80px;'>{np.random.choice(dice_frames)}</h1>",
            unsafe_allow_html=True
        )
        time.sleep(0.06)

    # --- Sonuç Üret ---
    rolls = np.random.randint(1, 7, n_rolls)
    values, counts = np.unique(rolls, return_counts=True)
    percentages = counts / n_rolls * 100

    # --- Grafiği çiz ---
    fig, ax = plt.subplots(figsize=(7, 4))

    bars = ax.bar(
        values,
        counts,
        width=0.6,
        color="#4c72b0",
        edgecolor="black",
        linewidth=1
    )

    ax.grid(axis="y", linestyle="--", alpha=0.5)
    ax.set_title(f"{n_rolls} Zar Atışı Sonucu", fontsize=14, fontweight="bold")
    ax.set_xlabel("Zar Yüzü (1–6)")
    ax.set_ylabel("Tekrarlanma Sayısı")
    ax.set_xticks(values)

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

    # Animasyonu grafiğe çevir
    anim.pyplot(fig)
