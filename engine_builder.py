import os
import requests


def get_ai_text():
    token = os.getenv("HF_TOKEN")
    # Користиме побрз и постабилен модел
    api_url = "https://api-inference.huggingface.co/models/google/flan-t5-small"
    headers = {"Authorization": f"Bearer {token}"}

    try:
        # flan-t5 очекува inputs во json
        response = requests.post(api_url, headers=headers,
                                 json={"inputs": "Write a short creative sentence about LATIVM AI."})
        data = response.json()
        if 'generated_text' in data:
            return data['generated_text']
        return "AI е подготвен за работа!"
    except Exception:
        return "Sistemska optimizacija: AI modelot se restartira..."


def generate():
    ai_text = get_ai_text()

    html_content = f"""
    <!DOCTYPE html>
    <html lang="en">
    <body style="font-family: sans-serif; background: #0f172a; color: #f8fafc; padding: 50px; text-align: center;">
        <div style="background: #1e293b; padding: 30px; border-radius: 15px; border: 1px solid #38bdf8;">
            <h1 style="color: #38bdf8;">LATIVM AI 2.0</h1>
            <p style="font-size: 1.2em;">{ai_text}</p>
            <p style="font-size: 0.8em; color: #64748b;">Automatsko generiranje: 2026-05-22</p>
        </div>
    </body>
    </html>
    """
    with open("index.html", "w", encoding="utf-8") as f:
        f.write(html_content)


if __name__ == "__main__":
    generate()