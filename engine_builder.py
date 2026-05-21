from huggingface_hub import InferenceClient
import os


def get_ai_text():
    # Го земаме токенот од GitHub Secrets
    token = os.getenv("HF_TOKEN")
    client = InferenceClient(model="gpt2", token=token)

    try:
        response = client.text_generation("LATIVM AI 2.0 system status:", max_new_tokens=50)
        return response
    except Exception as e:
        return f"AI Status: Error - {str(e)}"


def generate():
    ai_text = get_ai_text()
    html_content = f"""
    <!DOCTYPE html>
    <html lang="en">
    <body style="font-family: sans-serif; background: #0f172a; color: #f8fafc; padding: 50px; text-align: center;">
        <div style="background: #1e293b; padding: 20px; border-radius: 10px; display: inline-block;">
            <h1>LATIVM AI 2.0</h1>
            <p style="font-style: italic; color: #94a3b8;">{ai_text}</p>
        </div>
    </body>
    </html>
    """
    with open("index.html", "w", encoding="utf-8") as f:
        f.write(html_content)


if __name__ == "__main__":
    generate()