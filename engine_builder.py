import os
import requests
import random


def get_ai_text():
    # Наша интерна база на фрази ако AI API не е достапно
    backup_phrases = [
        "LATIVM AI 2.0: Системот е во режим на подготвеност.",
        "LATIVM AI 2.0: Анализата на податоците е во тек...",
        "LATIVM AI 2.0: Инфраструктурата е стабилна и брза.",
        "LATIVM AI 2.0: Подготвуваме нови функции за вас."
    ]

    token = os.getenv("HF_TOKEN")
    api_url = "https://api-inference.huggingface.co/models/google/flan-t5-small"
    headers = {"Authorization": f"Bearer {token}"}

    try:
        response = requests.post(api_url, headers=headers,
                                 json={"inputs": "Write a short status update for LATIVM AI."})
        data = response.json()
        if isinstance(data, dict) and 'generated_text' in data:
            return data['generated_text']
        return random.choice(backup_phrases)
    except Exception:
        return random.choice(backup_phrases)


def generate():
    ai_text = get_ai_text()
    html_content = f"""
    <!DOCTYPE html>
    <html lang="en">
    <body style="font-family: sans-serif; background: #0f172a; color: #f8fafc; padding: 50px; text-align: center;">
        <div style="background: #1e293b; padding: 30px; border-radius: 15px; border: 1px solid #38bdf8;">
            <h1 style="color: #38bdf8;">LATIVM AI 2.0</h1>
            <p style="font-size: 1.2em;">{ai_text}</p>
            <p style="font-size: 0.8em; color: #64748b;">System status: Live | {2026}</p>
        </div>
    </body>
    </html>
    """
    with open("index.html", "w", encoding="utf-8") as f:
        f.write(html_content)


if __name__ == "__main__":
    generate()