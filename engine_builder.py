import os
from huggingface_hub import InferenceClient

def generate():
    try:
        # Користиме 'gpt2' преку библиотеката, таа сама управува со конекцијата
        client = InferenceClient(model="gpt2")
        ai_text = client.text_generation("LATIVM AI 2.0 system is active.", max_new_tokens=30)
    except Exception as e:
        ai_text = "AI konekcijata privremeno ne e dostapna (downtime)."

    html_content = f"""
    <!DOCTYPE html>
    <html lang="en">
    <body style="font-family: sans-serif; background: #0f172a; color: #f8fafc; padding: 50px; text-align: center;">
        <div style="background: #1e293b; padding: 20px; border-radius: 10px; display: inline-block;">
            <h1>LATIVM AI 2.0</h1>
            <p>AI Status: {ai_text}</p>
        </div>
    </body>
    </html>
    """
    with open("index.html", "w", encoding="utf-8") as f:
        f.write(html_content)

if __name__ == "__main__":
    generate()