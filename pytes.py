import cv2
import sys
import pytesseract

if __name__ == '__main__':


    # Read image path from command line
    imPath = 'C:\\Users\\girik\\Desktop\\handwritten\\2020_08_10 10_08 PM Office Lens.jpg'

    # Uncomment the line below to provide path to tesseract manually
    # pytesseract.pytesseract.tesseract_cmd = '/usr/bin/tesseract'

    # Define config parameters.
    # '-l eng'  for using the English language
    # '--oem 1' for using LSTM OCR Engine
    config = ('-l eng --oem 1 --psm 3')

    # Read image from disk
    im = cv2.imread(imPath, cv2.IMREAD_COLOR)

    # Run tesseract OCR on image
    text = pytesseract.image_to_string(im, config=config)

    # Print recognized text
    print("\033[1m" +"Recognised Text\n")
    print(text)
    cv2.imshow("img", im)
    cv2.waitKey()
    cv2.destroyAllWindows()