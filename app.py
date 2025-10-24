from flask import Flask, jsonify, abort, render_template_string
import math

app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False

@app.route("/", methods=["GET"])
def index():
    html = """
    <h1>Microservicio de Cálculo de Factorial</h1>
    <p>Bienvenido al microservicio Flask que calcula el factorial de un número.</p>

    <h2>Instrucciones de uso:</h2>
    <ul>
        <li>Endpoint principal: <code>/factorial/&lt;n&gt;</code></li>
        <li>Ejemplo: <code>/factorial/5</code></li>
        <li>Respuesta JSON:</li>
    </ul>

    <pre>{
  "numero": 5,
  "factorial": 120,
  "etiqueta": "impar"
}</pre>
    """
    return render_template_string(html)

def etiqueta_paridad(n: int) -> str:
    return "par" if n % 2 == 0 else "impar"

@app.route("/health", methods=["GET"])
def health():
    return jsonify({"status": "ok"}), 200

@app.route("/factorial/<int:n>", methods=["GET"])
def calcular_factorial(n: int):
    if n < 0:
        return jsonify({"error": "El número debe ser entero no negativo"}), 400

    try:
        fact = math.factorial(n)
    except (ValueError, OverflowError):
        return jsonify({"error": "No se pudo calcular el factorial para este número"}), 500

    resultado = {
        "numero": n,
        "factorial": fact,
        "etiqueta": etiqueta_paridad(n)
    }

    return jsonify(resultado), 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
