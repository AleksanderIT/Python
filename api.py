from flask import Flask, jsonify, request
#from flask_restplus import Api

app = Flask (__name__)

class Server():
    def __int__(self, ):
        self.app = Flask(__name__)
        self.api = Api(self.app,
                       version='1.0',
                       title='API do Aleksander Pereira',
                       description='Primeira API em Python do Aleksander',
                       doc='/livros'
                       )
    def run(self, ):
        self.app.run(
            debug=True
        )

#server = Server()

livros = [
    {
        'id': 1,
        'titulo': 'titulo_teste1',
        'autor': 'autor_teste'
    },
    {
        'id': 2,
        'titulo': 'titulo_teste2',
        'autor': 'autor_teste'
    },
]

# Consultar
@app.route('/livros', methods=['GET'])
def obter_livros():
    return jsonify(livros)


# Consultar por ID
@app.route('/livros/<int:id>', methods=['GET'])
def obter_livros_id(id):
    for livros in livros:
        if livros.get('id') == id:
            return jsonify(livros)
        
# Editar   
@app.route('/livros/<int:id>', methods=['PUT'])     
def editar_livros(id):
    livro_alterado = request.get_json()
    for indice,livro in enumerate(livros):
        if livro.get('id') == id:
            livros[indice].update(livro_alterado)
            return jsonify(livros[indice])
        
# Criar
@app.route('/livros', methods=['POST'])
def incluir_novo_livro():
    novo_livro = request.get_json()
    livros.append(novo_livro)
    return jsonify(livros)
    


# Excluir
@app.route('/livros/<int:id>', methods=['DELETE'])
def excluir_livro(id):
    for indice, livro in enumerate(livros):
        if livro.get('id') == id:
            del livros[indice]
            return jsonify(livros)
    
app.run(port=5000,host='localhost',debug=True)