def generate():
    content = "<h1>LATIVM AI 2.0</h1><p>Системот работи стабилно на: 2026-05-21</p>"
    with open("lativm_output.html", "w") as f:
        f.write(content)

if __name__ == "__main__":
    generate()