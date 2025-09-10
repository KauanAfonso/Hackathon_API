from flask import Flask, jsonify, request
 
app = Flask(__name__)
 
 
data = [
    {
        "name": "Kauan Afonso",
        "EDV": "12345678",
        "companyEmailAddress": "Kauan@company.com",
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
    },
    {
        "name": "Laura Mendes",
        "EDV": "11223344",
        "companyEmailAddress": "LauraM@company.com",
        "CPF": "123.456.789-00",
        "Passport_n": "BB022307",
        "CVV": "221",
        "displayCreditN": "4532 8901 2345 6789",
        "validity": "07/27"
    },
    {
        "name": "Pedro Almeida",
        "EDV": "55667788",
        "companyEmailAddress": "PedroA@company.com",
        "CPF": "987.654.321-00",
        "Passport_n": "CC033408",
        "CVV": "890",
        "displayCreditN": "4716 8902 1346 7890",
        "validity": "09/28"
    },
    {
        "name": "Mariana Silva",
        "EDV": "10293847",
        "companyEmailAddress": "MarianaS@company.com",
        "CPF": "321.654.987-00",
        "Passport_n": "DD044509",
        "CVV": "678",
        "displayCreditN": "4929 2345 6789 1234",
        "validity": "05/30"
    },
    {
        "name": "Carlos Souza",
        "EDV": "01928374",
        "companyEmailAddress": "CarlosSouza@company.com",
        "CPF": "213.546.879-33",
        "Passport_n": "EE055610",
        "CVV": "456",
        "displayCreditN": "4556 2345 1234 7890",
        "validity": "11/26"
    },
    {
        "name": "Ana Clara",
        "EDV": "83746592",
        "companyEmailAddress": "AnaClara@company.com",
        "CPF": "987.321.654-11",
        "Passport_n": "FF066711",
        "CVV": "912",
        "displayCreditN": "4024 1234 5678 9123",
        "validity": "03/31"
    },
    {
        "name": "Bruno Castro",
        "EDV": "74638291",
        "companyEmailAddress": "BrunoCastro@company.com",
        "CPF": "654.987.321-44",
        "Passport_n": "GG077812",
        "CVV": "101",
        "displayCreditN": "4539 8765 4321 0987",
        "validity": "12/32"
    },
    {
        "name": "Juliana Costa",
        "EDV": "92837465",
        "companyEmailAddress": "JulianaCosta@company.com",
        "CPF": "456.789.123-55",
        "Passport_n": "HH088913",
        "CVV": "741",
        "displayCreditN": "4343 2121 3434 5656",
        "validity": "08/29"
    },
    {
        "name": "Felipe Ramos",
        "EDV": "19283746",
        "companyEmailAddress": "FelipeR@company.com",
        "CPF": "159.753.486-00",
        "Passport_n": "II099014",
        "CVV": "369",
        "displayCreditN": "4111 5678 1234 8765",
        "validity": "04/33"
    }
]

 
 

 
@app.route("/", methods=["GET"])
def get_users_or_single_user():

    email = request.args.get('email')
    name = request.args.get('name')
    user_found = None

    if email:
        # Se um e-mail for fornecido, procura um usuário específico
        for user in data:
            if user["companyEmailAddress"] == email:
                user_found = user
                break  # Interrompe a busca após encontrar o usuário
        if user_found:
            return jsonify({"data": user_found}), 200
        else:
            return jsonify({"error": "Usuário não encontrado"}), 404
    elif name:
        for user in data:
            if user["name"] == name:
                user_found = user
                break  # Interrompe a busca após encontrar o usuário
        if user_found:
            return jsonify({"data": user_found}), 200
        else:
            return jsonify({"error": "Usuário não encontrado"}), 404
    else:
       
        return jsonify({"data": data}), 200

@app.route("/post", methods=["POST"])
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
 