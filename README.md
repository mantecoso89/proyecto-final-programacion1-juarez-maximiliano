# Esquiva Bloques - Proyecto Final de Programación 1

Este proyecto es un videojuego simple desarrollado en Python con la biblioteca Pygame. Fue creado como parte del trabajo final para la materia "Programación 1".

## Descripción

"Esquiva Bloques" es un juego de arcade de tipo "dodger". El jugador controla un cuadrado verde en la parte inferior de la pantalla y debe moverse de izquierda a derecha para esquivar los bloques rojos que caen desde la parte superior. El objetivo es sobrevivir el mayor tiempo posible para acumular la puntuación más alta.

## Requisitos e Instalación

Para ejecutar este juego, necesitarás tener instalado Python 3 en tu sistema. El proyecto utiliza un entorno virtual para gestionar sus dependencias, asegurando una instalación limpia y sin conflictos.

Sigue estos pasos para instalar y ejecutar el proyecto localmente:

1. **Clonar el repositorio:**
```bash
git clone https://github.com/tu_usuario/tu_repositorio.git
cd tu_repositorio
```

2. **Crear y activar el entorno virtual:**
   * En **Linux/macOS**:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

   * En **Windows**:
   ```bash
   python -m venv venv
   venv\Scripts\activate
   ```

3. **Instalar las dependencias:** Con el entorno virtual activado, instala `pygame` usando el archivo `requirements.txt`:
```bash
pip install -r requirements.txt
```

4. **Ejecutar el juego:**
```bash
python main.py
```

## Cómo Jugar

* Usa las teclas **A y D** del teclado para mover tu personaje.
* Esquiva los bloques rojos que caen.
* Si un bloque te golpea, el juego termina.
* En la pantalla de "Game Over", presiona cualquier tecla para reiniciar el juego o la tecla `ESC` para **salir**.
