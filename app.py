# from flask import Flask
# from flask_cors import CORS
# from routes import api_blueprint

# # Initialiseer Flask app
# app = Flask(__name__)

# # Enable CORS
# CORS(app, origins=["https://dashboardfrontend-4ak3.onrender.com"])

# # Registreer de blueprint voor API-routes
# app.register_blueprint(api_blueprint)

# # Hoofdentry point
# if __name__ == '__main__':
#     app.run(debug=True)



from flask import Flask
from flask_cors import CORS
from routes import api_blueprint


app = Flask(__name__)

# Sta CORS toe voor verzoeken afkomstig van je React frontend
CORS(app, origins=["http://localhost:3000", "https://dashboardfrontend-4ak3.onrender.com"])

# Voeg hier je routes en andere logica toe
app.register_blueprint(api_blueprint)


if __name__ == '__main__':
    app.run(debug=True)
