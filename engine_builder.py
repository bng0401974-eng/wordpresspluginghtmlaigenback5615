import os
import requests
import json


def generate():
    token = os.getenv("HF_TOKEN")
    api_url = "https://api-inference.huggingface.co/models/gpt2"
    headers = {"Authorization": f"Bearer {token}"}

    # Прво пробуваме со AI
    ai_text = "LATIVM AI 2.0: Систем во иницијализација..."
    try:
        response = requests.post(api_url, headers=headers, json={"inputs": "LATIVM AI 2.0 system status:"}, timeout=10)
        if response.status_code == 200:
            data = response.json()
            if isinstance(data, list) and len(data) > 0:
                ai_text = data[0].get('generated_text', "AI статус: Активен")
    except:
        ai_text = "AI статус: Режим на подготвеност"

    # Креирање на HTML-от со дефиниран UTF-8 енкодинг
    html_content = f"""<!DOCTYPE html>
<html lang="mk">
<head>
    <meta charset="UTF-8">
    <title>LATIVM AI 2.0</title>
</head>
<body style="background:#0f172a; color:#fff; font-family:sans-serif; text-align:center; padding:50px;">
    <div style="background:#1e293b; padding:30px; border-radius:15px; display:inline-block;">
        <h1>LATIVM AI 2.0</h1>
        <p>{ai_text}</p>
    </div>
</body>
</html>"""

    with open("index.html", "w", encoding="utf-8") as f:
        f.write(html_content)


if __name__ == "__main__":
    generate()