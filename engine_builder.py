import os
from google import genai


def generate():
    # Го влече клучот директно од GitHub Secrets
    api_key = os.environ.get("GEMINI_API_KEY")

    if not api_key:
        raise ValueError("ГРЕШКА: GEMINI_API_KEY не е пронајден во системските променливи!")

    client = genai.Client(api_key=api_key)

    try:
        response = client.models.generate_content(
            model='gemini-1.5-flash',  # Сменивме од 2.0 на 1.5-flash
            contents="Write a short, professional status update for LATIVM AI 2.0 system."
        )
        ai_text = response.text
    except Exception as e:
        ai_text = f"Sistemska greska: {str(e)}"

    html_content = f"""
    <!DOCTYPE html>
    <html lang="mk">
    <head><meta charset="UTF-8"></head>
    <body style="background:#0f172a; color:#fff; font-family:sans-serif; text-align:center; padding:50px;">
        <div style="background:#1e293b; padding:30px; border-radius:15px; display:inline-block;">
            <h1>LATIVM AI 2.0</h1>
            <p>{ai_text}</p>
        </div>
    </body>
    </html>
    """
    with open("index.html", "w", encoding="utf-8") as f:
        f.write(html_content)  # Ова е правилниот начин, без 'wer='


if __name__ == "__main__":
    generate()