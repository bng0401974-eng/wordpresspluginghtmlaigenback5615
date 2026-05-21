import os
import requests


def get_ai_text():
    token = os.getenv("HF_TOKEN")
    # Користиме модел кој е посигурен за API повици
    api_url = "https://api-inference.huggingface.co/models/gpt2"
    headers = {"Authorization": f"Bearer {token}"}

    try:
        response = requests.post(api_url, headers=headers,
                                 json={"inputs": "LATIVM AI 2.0 system is fully operational and"})
        data = response.json()

        # Проверка дали добивме валиден одговор
        if isinstance(data, list) and 'generated_text' in data[0]:
            return data[0]['generated_text']
        else:
            return "AI е во фаза на иницијализација..."
    except Exception as e:
        return f"System Status: Operational (AI Load Error: {str(e)})"


def generate():
    ai_text = get_ai_text()

    html_content = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>LATIVM AI 2.0</title>
        <style>
            body {{ font-family: sans-serif; background: #0f172a; color: #f8fafc; padding: 50px; text-align: center; }}
            .card {{ background: #1e293b; padding: 30px; border-radius: 15px; display: inline-block; max-width: 600px; }}
        </style>
    </head>
    <body>
        <div class="card">
            <h1>LATIVM AI 2.0</h1>
            <p style="color: #94a3b8;">AI Generiran tekst:</p>
            <p style="font-style: italic;">{ai_text}</p>
        </div>
    </body>
    </html>
    """
    with open("index.html", "w", encoding="utf-8") as f:
        f.write(html_content)


if __name__ == "__main__":
    generate()