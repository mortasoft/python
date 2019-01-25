from flask import Flask, request, jsonify
from werkzeug.utils import secure_filename

app = Flask(__name__)

@app.route('/analizador', methods=['POST'])
def buscarVerbos():
    try:
        verbos=open("diccionario.txt", encoding="utf-8")
        diccionario = verbos.read()
        adjetivos=open("diccionario_adjetivos.txt", encoding="utf-8")
        diccionario_adjetivos = adjetivos.read()
        libro=request.files['elLibro']
        libro.save(secure_filename(libro.filename))
        elArchivo = open(libro.filename, "r")
        elLibro = str(elArchivo.read())
        cont_verbos=0
        cont_adjetivos=0
        elLibroMaldito = elLibro.replace(u'\ufeff', '')
        palabras = elLibroMaldito.split()

        for palabra_clave in palabras:
            for verbo in diccionario.split():
                if palabra_clave == verbo:
                    cont_verbos = cont_verbos +1
            for adjetivo in diccionario_adjetivos.split():
                if palabra_clave == adjetivo:
                    cont_adjetivos = cont_adjetivos +1

        total = str(cont_verbos / len(palabras) * 100)
        total2 = str(cont_adjetivos / len(palabras) * 100)
        return jsonify('En el documento se encuentra un total de '+ str(cont_verbos) + ' verbos' + ' que representa el '+ total + '% del texto',
        	'En el documento se encuentra un total de '+ str(cont_adjetivos) + ' adjetivos' + ' que representa el '+ total2 + '% del texto')

    except Exception as e:
         return jsonify('error: ' + str(e))

if __name__ == '__main__':
    app.run('0.0.0.0')