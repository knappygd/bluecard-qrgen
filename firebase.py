import firebase_admin
from firebase_admin import firestore
from qrgen import code

cred_obj = firebase_admin.credentials.Certificate('sak.json')
default_app = firebase_admin.initialize_app(cred_obj)

db = firestore.client()
data = {
    'redeemed': False,
    }
db.collection('codes').document(code).set(data)