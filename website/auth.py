from flask import Blueprint, render_template, request, redirect
import os
import numpy as np
import cv2
import pytesseract 

pytesseract.pytesseract.tesseract_cmd = "tesseract"
os.environ["TESSDATA_PREFIX"] = "/home/runner/.apt/usr/share/tesseract-ocr/4.00/tessdata/"

auth = Blueprint('auth', __name__)

@auth.route('/', methods=['GET', 'POST'])
def land():
    restrictionGroups = {
        "lactose": ["milk", "cheese", "butter", "cream", "butter"], 
        "vegetarian": ["pork", "beef", "chicken", "lamb", "fish", "shellfish"], 
        "vegan": ["pork", "beef", "chicken", "lamb", "shellfish", "fish", "egg", "milk"], 
        "gluten": ["wheat", "barley", "rye"], "pascetarian": ["pork", "beef", "chicken", "lamb"]
    }
    
    if request.method == 'POST':
        restriction = request.form.get('restriction')
        restrictions = restriction.isalnum() and restriction.split()

        if 'image' in request.files:
            image = request.files['image']

            # read in grey scale
            textImage = cv2.imread(image, 0)
            text = pytesseract.image_to_string(textImage)

            # Continue with your processing
            text = pytesseract.image_to_string(textImage)
            text = text.lower()

            for restriction in restrictions:
                for item in restrictionGroups[restriction]:
                    if item in text:
                        print("Redirecting to badresult.html")
                        return redirect("badresult.html")

            print("Redirecting to goodresult.html")
            return redirect("goodresult.html")

    return render_template('index.html')
