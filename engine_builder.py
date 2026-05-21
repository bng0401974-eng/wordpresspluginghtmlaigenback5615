# engine_builder.py
def generate():
    html_content = """
    <!DOCTYPE html>
    <html lang="mk">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>LATIVM AI 2.0 | Dashboard</title>
        <style>
            body { font-family: 'Segoe UI', sans-serif; background: #0f172a; color: #f8fafc; text-align: center; padding: 50px; }
            .container { background: #1e293b; padding: 30px; border-radius: 15px; display: inline-block; box-shadow: 0 4px 15px rgba(0,0,0,0.3); }
            h1 { color: #38bdf8; }
            p { color: #94a3b8; }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>LATIVM AI 2.0</h1>
            <p>Статус: Системот е целосно функционален.</p>
            <p>Последно ажурирање: 2026-05-22</p>
        </div>
    </body>
    </html>
    """
    with open("index.html", "w", encoding="utf-8") as f:
        f.write(html_content)

if __name__ == "__main__":
    generate()