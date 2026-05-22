import os
import google.generativeai as genai

def generate():
    # Конфигурација
    genai.configure(api_key=os.environ.get("GEMINI_API_KEY"))
    model = genai.GenerativeModel('gemini-1.5-flash')

    # Генерирање на содржина
    try:
        response = model.generate_content("Give a short, professional status update for LATIVM AI 2.0. Under 30 words.")
        ai_text = response.text
    except Exception:
        ai_text = "LATIVM AI 2.0: Системот е во подготвеност."

    # Запишување во HTML
    html_content = f"""
    <!DOCTYPE html>
    <html lang="mk">
    <head>
        <meta charset="UTF-8">
        <style>
            body {{ background: #0f172a; color: #fff; font-family: sans-serif; text-align: center; padding: 50px; }}
            .card {{ background: #1e293b; padding: 30px; border-radius: 15px; display: inline-block; }}
        </style>
    </head>
    <body>
        <div class="card">
            <h1>LATIVM AI 2.0</h1>
            <p>{ai_text}</p>
        </div>
    </body>
    </html>
    """
    with open("index.html", "w", encoding="utf-8") as f:
        f.write(html_content)

if __name__ == "__main__":
    generate()