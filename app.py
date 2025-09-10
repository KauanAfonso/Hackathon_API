from flask import Flask, jsonify, request
 
app = Flask(__name__)
 
 
data = [
    {
        "name": "Kauan Afonso",
        "EDV": "12345678",
        "companyEmailAddress": "AfonsinhaKauan@company.com",
        "CPF": "543.543.675-16",
        "Passport_n": "AA011906",
        "CVV": "125",
        "displayCreditN": "5326 5368 1352 8844",
        "validity": "21/39"
    },
    {
        "name": "Caua Barbosa",
        "EDV": "98745612",
        "companyEmailAddress": "CauaOlive@company.com",
        "CPF": "543.666.643-12",
        "Passport_n": "AA011906",
        "CVV": "333",
        "displayCreditN": "5456 1532 4322 8795",
        "validity": "22/29"
    }
]
 
 
@app.route("/", methods=["GET"])
def get_users():
    return jsonify({"message": data})
 
 
@app.route("/p", methods=["POST"])
def add_user():
 
    new_user = request.get_json()
 
 
    required_fields = ["name", "EDV", "companyEmailAddress", "CPF", "displayCreditN", "validity"]
    for field in required_fields:
        if field not in new_user:
            return jsonify({"error": f"Campo '{field}' é obrigatório"}), 400
 
 
    data.append(new_user)
    return jsonify({"message": "Usuário adicionado com sucesso!", "user": new_user}), 201
 
if __name__ == "__main__":
    app.run(debug=True)
 