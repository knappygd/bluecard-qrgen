import qrcode
from qrcode.image.styledpil import StyledPilImage
from datetime import datetime
import string    
import random
import firebase_admin
from firebase_admin import firestore

cred_obj = firebase_admin.credentials.Certificate('sak.json')
default_app = firebase_admin.initialize_app(cred_obj)

current_time = datetime.today().strftime('%Y%m%d%H%M%S')
random = ''.join(random.choices(string.ascii_uppercase + string.ascii_lowercase + string.digits, k = 6))
code = random + current_time + "p=" + "500"

def pushToFirestore():
    db = firestore.client()
    data = {
        'redeemed': False,
        'dateGen': current_time}
    db.collection('codes').document(code).set(data)
    
def generateQR():
    qr = qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_H, border=2)
    qr.add_data(code)

    img = qr.make_image(image_factory=StyledPilImage, embeded_image_path="assets/test.png")
    img.save(f'codes/{code}.png')
    
pushToFirestore()
generateQR()