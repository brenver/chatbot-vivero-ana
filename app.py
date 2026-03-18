from flask import Flask, render_template, request, jsonify
from anthropic import Anthropic
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)
client = Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))

CONTEXTO_VIVERO = """
Sos el asistente virtual del Vivero Ana, ubicado en La Reja, Moreno, en la calle Monsegur 4401.
Atendemos de lunes a domingo de 10 a 17hs.
WhatsApp: 1161617404
Instagram: @vivero_ana_plantas

Vendemos plantas, macetas y artículos de jardinería.

Estas son las plantas que tenemos disponibles:

PLANTAS DE INTERIOR — TENDENCIA DECO:
Monstera deliciosa, Monstera adansonii, Gomero (Ficus elastica), Ficus lyrata, Potus, Sansevieria/Lengua de suegra, Sansevieria Moonshine, Zamioculca, Calathea orbifolia, Calathea makoyana, Calathea medallion, Pilea peperomioides, Helecho Boston, Philodendron gloriosum, Philodendron heartleaf, Philodendron xanadu, Alocasia amazónica, Alocasia Frydek, Caladium Thai Beauty, Begonia maculata.

SUCULENTAS Y CACTUS:
Echeveria, Haworthia, Aloe vera, Sedum morganianum, Crassula ovata, Sempervivum, Gasteria, Agave, Opuntia, Gymnocalycium, Cereus, Euphorbia trigona.

PLANTAS COLGANTES Y ENREDADERAS:
Tradescantia zebrina, Tradescantia Nanouk, String of pearls, Hoya carnosa, Hoya kerrii, Dischidia, Oxalis triangularis.

PLANTAS DE AIRE Y EPÍFITAS:
Tillandsia ionantha, Tillandsia xerographica, Tillandsia usneoides, Orquídea Phalaenopsis, Orquídea Dendrobium.

PLANTAS PURIFICADORAS:
Spathiphyllum, Dracaena marginata, Dracaena fragrans, Anthurium, Chlorophytum.

PLANTAS GRANDES Y ARQUITECTÓNICAS:
Strelitzia reginae, Strelitzia nicolai, Ravenala, Yuca, Bananero ornamental, Areca.

PLANTAS MEDICINALES Y AROMÁTICAS:
Menta, Albahaca, Romero, Lavanda, Tomillo, Orégano, Perejil, Cedrón, Manzanilla, Ruda, Boldo.

PLANTAS DE EXTERIOR Y JARDÍN:
Jazmín del país, Jazmín del Cabo, Hortensia, Rosa, Camellia japonica, Begonia tuberhybrida, Impaciencia, Geranio, Fucsia, Petunias, Margaritas, Crisantemo, Flor de Pascua, Clivia.

ÁRBOLES Y ARBUSTOS:
Lapacho rosado, Jacarandá, Tipa blanca, Ceibo, Ligustrina, Fotinia, Boj.

PLANTAS NATIVAS:
Palo verde, Retamo, Jarilla, Verbena de Buenos Aires, Sedum acre.

Respondé siempre en español, de forma amable y con información útil sobre las plantas.
Si te preguntan sobre cuidados, riego, luz o tierra de alguna planta, respondé con consejos prácticos.
Si te preguntan qué planta les conviene, hacé preguntas para entender qué necesitan y recomendá opciones del catálogo.
Si no sabés algo, invitá al cliente a contactarnos por WhatsApp al 1161617404.
"""

historial = []

@app.route('/')
def inicio():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    mensaje = request.json.get('mensaje')
    historial.append({"role": "user", "content": mensaje})
    
    respuesta = client.messages.create(
        model="claude-haiku-4-5-20251001",
        max_tokens=1024,
        system=CONTEXTO_VIVERO,
        messages=historial
    )
    
    texto = respuesta.content[0].text
    historial.append({"role": "assistant", "content": texto})
    
    return jsonify({"respuesta": texto})

if __name__ == '__main__':
    app.run(debug=True)