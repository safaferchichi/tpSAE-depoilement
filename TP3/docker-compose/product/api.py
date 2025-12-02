from flask import Flask
from flask_restful import Resource, Api

# Instanciation de l'application
app = Flask(__name__)
api = Api(app)

# Définition de la ressource
class Product(Resource):
    def get(self):
        return {'products': ['iPad Pro 14', 'MacBook Pro', 'Remarkable 2', 'Ordinateur de bureau']}

# Définition de la route
api.add_resource(Product, '/')

# Exécution de l'application
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80, debug=True)
