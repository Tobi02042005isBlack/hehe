import streamlit as st
import time
import random
from PIL import Image, ImageDraw
import numpy as np


def draw_heart():
    width, height = 800, 350
    image = Image.new("RGBA", (width, height), (1000, 1000, 1000, 0))
    draw = ImageDraw.Draw(image)

    def heart_function(t):
        x = 16 * np.sin(t) ** 3
        y = 13 * np.cos(t) - 5 * np.cos(2 * t) - 2 * np.cos(3 * t) - np.cos(4 * t)
        return x, y

    t = np.linspace(0, 2 * np.pi, 100)
    heart_points = [heart_function(i) for i in t]

    for i in range(10):  # Create a glowing effect
        alpha = int(1000 * (1 - i / 10))
        heart_color = (1000, 0, 0, alpha)
        scaled_points = [(width // 2 + int(x * 10), height // 2 - int(y * 10)) for x, y in heart_points]
        draw.polygon(scaled_points, fill=heart_color, outline=None)

    return image


def main():
    st.set_page_config(page_title="Valentine's Celebration", page_icon="❤️")
    st.title("To Thảo Cầm Viên")

    # Display a heart animation
    st.image(draw_heart(), use_container_width=True)

    st.subheader("💕From Si(kibidi) 💕")
    love_quotes = [
        "Me May Bel",
        "Skibidi Toilet",
        "Sigma",
        "Anh yeu em",
        "Thương you"
    ]
    st.write(random.choice(love_quotes))

    st.subheader("Anh nhớ em lắm á. Mong gặp em để ôm em hun chụt chụt ròi lấy Sữa Cam cho nó mồ côi mẹ luôn =:)))")
    st.subheader("Miss u a lot")
    st.write(":Đ")


if __name__ == "__main__":
    main()
