import pyrebase

def conecta_db():
    firebaseConfig = {
        "apiKey": "AIzaSyAkVfrezK_tg6KRAm4YnRAdXe0Wu4w45tQ",
        "authDomain": "project-spje.firebaseapp.com",
        "databaseURL": "https://project-spje-default-rtdb.firebaseio.com",
        "projectId": "project-spje",
        "storageBucket": "project-spje.appspot.com",
        "messagingSenderId": "575112787589",
        "appId": "1:575112787589:web:83dd303429e328121f5bec",
        "measurementId": "G-YV0CSH7MH9"
    }

    firebase = pyrebase.initialize_app(firebaseConfig)

    db = firebase.database()

    return db
