import os
import requests
import random


def get_ai_text():
    # ... (твојот постоечки код)
    # Кога добиваш одговор:
    text = data.get('generated_text', "Sistemska optimizacija...")
    return text.encode('utf-8').decode('utf-8')


def generate():
    ai_text = get_ai_text()

    # СЕКОГАШ користи charset="UTF-8" во HTML-от
    html_content = f"""
    <!DOCTYPE html>
    <html lang="mk">
    <head>
        <meta charset="UTF-8">
    </head>
    <body style="font-family: sans-serif; background: #0f172a; color: #f8fafc; padding: 50px; text-align: center;">
        <div style="background: #1e293b; padding: 30px; border-radius: 15px;">
            <h1>LATIVM AI 2.0</h1>
            <p>{ai_text}</p>
        </div>
    </body>
    </html>
    """
    # Зачувување на фајлот со utf-8
    with open("index.html", "w", encoding="utf-8") as f:
        f.write(html_content)