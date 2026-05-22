import os
from google import genai
from google.genai import types


def generate():
    api_key = os.environ.get("GEMINI_API_KEY")
    # Директно иницијализирање со API клучот
    client = genai.Client(api_key=api_key)

    try:
        # Повик кон моделот без префикс 'models/'
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
    <body>
        <h1>LATIVM AI 2.0</h1>
        <p>{ai_text}</p>
    </body>
    </html>
    """
    with open("index.html", "w", encoding="utf-8") as f:
        f.write(html_content)


if __name__ == "__main__":
    generate()