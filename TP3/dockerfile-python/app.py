from flask import Flask, jsonify, request  # type: ignore

app = Flask(__name__)

students = [
    {"id": 1, "prenom": "riham", "age": 21},
    {"id": 2, "prenom": "safa", "age": 22},
]

@app.route('/')
def home():
    return """
    <h1>Bienvenue !</h1>
    <p>Ceci est la page d'accueil.</p>
    <a href="/message">Aller à /message</a><br>
    <a href="/students">Voir les étudiants</a>
    """

@app.route('/message')
def message():
    return """
    <h1>Page de message</h1>
    <p>Ceci est une page HTML simple.</p>
    <a href="/">Retour à l'accueil</a>
    """

@app.route('/students', methods=['GET'])
def get_students():
    html = "<h1>Liste des étudiants</h1><ul>"
    for s in students:
        html += f"<li>ID : {s['id']} — {s['prenom']} (âge : {s['age']})</li>"
    html += "</ul>"
    html += '<a href="/">Retour à l’accueil</a>'
    return html

@app.route('/students', methods=['POST'])
def add_student():
    new_student = request.get_json()
    new_student['id'] = len(students) + 1
    students.append(new_student)
    return jsonify(new_student), 201

@app.route('/students/<int:id>',methods=['GET'])
def get_student(id):
    student = next ((s for s in students if  s['id']==id),None)
    if student : 
        return jsonify(student)
    return jsonify({"erreur" : " stduent  not found"}),404

@app.route('/students/<int:id>',methods=['PUT'])
def update_student(id):
    student = next ((s for s in students if  s['id']==id),None)
    if not student: 
        return jsonify({"erreur" :"not exist"}) ,404
    
    data = request.get_json()
    student.update(data)
    return jsonify(student)
@app.route('/students/<int:id>',methods=['DELETE'])
def delete_student(id):
    global students
    students=[ s for s in students if  s['id']!=id]
    return jsonify({"message" :"ok"}),200

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
