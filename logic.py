#testForAllergens(allergy, file):
  import os
  import cv2
  import pytesseract  
  #intitialize tesseract
  pytesseract.pytesseract.tesseract_cmd = "tesseract"
  os.environ["TESSDATA_PREFIX"] = "/home/runner/.apt/usr/share/tesseract-ocr/4.00/tessdata/"
  
  restrictionGroups = {"lactose": ["milk", "cheese", "butter", "cream", "butter"], "vegetarian": ["pork", "beef", "chicken", "lamb", "fish","shellfish"], "vegan": ["pork", "beef", "chicken", "lamb","shellfish", "fish","egg","milk"], "gluten": ["wheat", "barley", "rye"], "pascetarian": ["pork", "beef", "chicken", "lamb"]}
  #make it a list
  restrictionlist = allergy.split(",")
  
  #read the inputed label
  img = cv2.imread('ingredients.jpg',0)
  text = pytesseract.image_to_string(img)
  text.lower()
  
  #check if any of the restrictions are on the ingredients list
  restrictionsPresent = []
  for element in restrictionlist:
    if str(element).lower() in restrictionGroups.keys():
      restrictionlist.extend(restrictionGroups[element.lower()])
  for element in restrictionlist:
    if element.lower() in text:
      restrictionsPresent.append(element)
  
  #print the restrictions or lack thereof
  if len(restrictionsPresent) == 0:
    print("This food is safe to eat!")
  else:
    print(f"This food is unsafe to eat and contains the following allergens: {', '.join(restrictionsPresent)}")
