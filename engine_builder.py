# engine_builder.py
def generate():
    content = "<h1>LATIVM AI 2.0</h1><p>Системот е успешно ажуриран во 2026!</p>"
    with open("lativm_output.html", "w") as f:
        f.write(content)

if __name__ == "__main__":
    generate()
