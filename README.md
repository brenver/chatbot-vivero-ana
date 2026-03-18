# Chatbot Vivero Ana 🌿

Asistente virtual para el Vivero Ana, desarrollado con Python, Flask y la API de Claude (Anthropic). Responde consultas sobre plantas, cuidados, disponibilidad y datos del vivero.

## Vivero Ana
- 📍 La Reja, Moreno
- 🕐 Lunes a domingo de 10 a 17hs
- 📸 Instagram: @vivero_ana_plantas

## Tecnologías

![Python](https://img.shields.io/badge/Python-3.14-blue?logo=python)
![Flask](https://img.shields.io/badge/Flask-3.1-black?logo=flask)
![Claude](https://img.shields.io/badge/Claude-Anthropic-orange)

## Funcionalidades

- Responde preguntas sobre las plantas disponibles
- Da consejos de cuidado, riego y luz
- Recomienda plantas según las necesidades del cliente
- Informa sobre horarios, ubicación y contacto del vivero
- Historial de conversación en la misma sesión

## Instalación y uso local

1. Cloná el repositorio
```
git clone https://github.com/brenver/chatbot-vivero-ana.git
```

2. Instalá las dependencias
```
pip install flask anthropic python-dotenv
```

3. Creá un archivo `.env` con tu API key
```
ANTHROPIC_API_KEY=tu_api_key_aqui
```

4. Corré la aplicación
```
python app.py
```

5. Abrí el navegador en `http://127.0.0.1:5000`

## Próximos pasos

- [ ] Deploy en la nube
- [ ] Integración con WhatsApp Business API
- [ ] Panel de administración para actualizar el catálogo
