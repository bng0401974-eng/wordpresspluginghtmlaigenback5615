import os
import vertexai
from vertexai.generative_models import GenerativeModel


def generate():
    # Постави го проектот (ова обично го бара Vertex AI)
    # Замени 'tvoj-project-id' со ID-то од твојот Google Cloud проект
    project_id = "tvoj-project-id"
    location = "us-central1"

    vertexai.init(project=project_id, location=location)
    model = GenerativeModel("gemini-1.5-flash")

    try:
        response = model.generate_content("Write a short, professional status update for LATIVM AI 2.0 system.")
        ai_text = response.text
    except Exception as e:
        ai_text = f"Vertex Error: {str(e)}"

    html_content = f"""
    <!DOCTYPE html>
    <html>
    <body style="background:#0f172a; color:#fff; text-align:center; padding:50px;">
        <h1>LATIVM AI 2.0</h1>
        <p>{ai_text}</p>
    </body>
    </html>
    """
    with open("index.html", "w", encoding="utf-8") as f:
        f.write(html_content)


if __name__ == "__main__":
    generate()