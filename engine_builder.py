import os
from google import genai


def generate():
    api_key = os.environ.get("GEMINI_API_KEY")
    client = genai.Client(api_key=api_key)

    try:
        response = client.models.generate_content(
            model='gemini-1.5-flash',
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
        f.write(html_content)


if __name__ == "__main__":
    generate()