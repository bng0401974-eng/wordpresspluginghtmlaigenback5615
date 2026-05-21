from huggingface_hub import InferenceClient


def get_ai_text():
    # Користиме бесплатен модел
    client = InferenceClient(model="gpt2")
    # Генерираме текст со мала должина за брзина
    response = client.text_generation("LATIVM AI 2.0 system status report:", max_new_tokens=60)
    return response


def generate():
    ai_text = get_ai_text()

    html_content = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>LATIVM AI 2.0</title>
        <style>
            body {{ font-family: 'Segoe UI', sans-serif; background: #0f172a; color: #f8fafc; padding: 50px; text-align: center; }}
            .card {{ background: #1e293b; padding: 30px; border-radius: 15px; display: inline-block; max-width: 600px; box-shadow: 0 4px 15px rgba(0,0,0,0.5); }}
            h1 {{ color: #38bdf8; }}
        </style>
    </head>
    <body>
        <div class="card">
            <h1>LATIVM AI 2.0</h1>
            <p style="color: #94a3b8;">AI Report:</p>
            <p style="font-size: 1.2em; font-weight: bold;">{ai_text}</p>
        </div>
    </body>
    </html>
    """
    with open("index.html", "w", encoding="utf-8") as f:
        f.write(html_content)


if __name__ == "__main__":
    generate()