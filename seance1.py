from flask import Flask, jsonify, request


#  Création de l'application Flask

app = Flask(__name__)


#  Base de données simple en mémoire
#    (juste une liste d'étudiants)

students = [
    {"id": 1, "prenom": "samir", "age": 31},
    {"id": 2, "prenom": "safa", "age": 22},
]


#  Page d'accueil (retourne un peu d'HTML)

@app.route('/')
def home():
    return """
    <h1 style='color: purple; text-align:center;'>Bienvenue c'est cool rest ! </h1>
    
    <ul>
        <li><a href='/students'>Voir les étudiants</a></li>
        <li><a href='/message'>Voir le message</a></li>
    </ul>
    """


#  Petite page HTML avec un message

@app.route('/message')
def message():
    return """
    <div style='padding:20px; background:#f0f0f0; border-radius:10px; width:300px; margin:auto;'>
        <h1 style='color:black;'> Hello !</h1>
    </div>

    <ul>
        <li><a href='/'>Accueil</a></li>
    </ul>
    """


#  Récupérer tous les étudiants (GET)

@app.route('/students', methods=['GET'])
def get_students():
    return jsonify(students)


#  Ajouter un étudiant (POST)

@app.route('/students', methods=['POST'])
def add_student():
    # Récupérer l'objet JSON envoyé par le client
    new_student = request.get_json()
    
    # Générer un nouvel ID automatiquement
    new_student['id'] = len(students) + 1
    
    # Ajouter l'étudiant à la liste
    students.append(new_student)
    
    # Retourner l'étudiant créé + code 201 = CREATED
    return jsonify(new_student), 201


#  Récupérer un étudiant par ID (GET)

@app.route('/students/<int:id>', methods=['GET'])
def get_student(id):
    # Chercher l'étudiant dans la liste
    student = next((s for s in students if s['id'] == id), None)
    
    if student:
        return jsonify(student)
    
    # Si l'étudiant n'existe pas donc erreur 404
    return jsonify({"erreur": "l'etudiant n'est pas trouvé"}), 404


#  Mettre à jour un étudiant (PUT)

@app.route('/students/<int:id>', methods=['PUT'])
def update_student(id):
    # rechercher l'étudiant
    student = next((s for s in students if s['id'] == id), None)
    
    if not student:
        return jsonify({"erreur": "not exist"}), 404

    # Récupérer les nouvelles données JSON
    data = request.get_json()

    # Mettre à jour les champs existants
    student.update(data)

    return jsonify(student)


#  Supprimer un étudiant (DELETE)

@app.route('/students/<int:id>', methods=['DELETE'])
def delete_student(id):
    global students
    
    # Garder tous les étudiants sauf celui à supprimer
    students = [s for s in students if s['id'] != id]
    
    return jsonify({"message": "ok"}), 200


#  Lancer l'application Flask

if __name__ == '__main__':
    app.run(debug=True)
