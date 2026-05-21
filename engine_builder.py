# engine_builder.py
def generate():
    html_content = """
    <!DOCTYPE html>
    <html lang="mk">
    <head>
        <meta charset="UTF-8">
        <title>TEST TEST TEST</title>
        <style>
            body { font-family: sans-serif; background: #ea580c; color: white; text-align: center; padding: 100px; }
            h1 { font-size: 50px; }
        </style>
    </head>
    <body>
        <h1>ТЕСТ ПОМИНА УСПЕШНО!</h1>
        <p>Автоматизацијата работи совршено на: 2026-05-22</p>
    </body>
    </html>
    """
    with open("index.html", "w", encoding="utf-8") as f:
        f.write(html_content)

if __name__ == "__main__":
    generate()