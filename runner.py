import easyocr
import cv2

iranian_plate_char = ['ش'    ,'س'   ,'الف'   ,'ا'   , 'ب'   ,'پ'   ,'ت'   ,'ث'   ,'ج'   ,'چ'    ,'ح'    ,'خ'    ,'د'   ,'ذ'     ,'ر'   ,'ز'   ,'ژ'    ,'ص'    ,'ض'    ,'ط'    ,'ظ'    ,'ع'    ,'غ'   ,'ف'   ,'ق'    ,'ک'    ,'گ'    ,'ل'    ,'م'    ,'ن'    ,'و'    ,'ه'    ,'ی'    ,'سیاسی'     ,'ولیچر'     ,'دیپلمات'     ,'ویلچر'     ,'هـ'    ,'ي'     ,'ويلچر'     ,'252']
			
char_plate = [
    'A',
    's',
    'a',
    'a',
    'b',
    'p',
    't',
    'B',
    'j',
    'C',
    'D',
    'E',
    'd',
    'F',
    'r',
    'G',
    'H',
    'I',
    'J',
    'K',
    'L',
    'M',
    'N',
    'f',
    'O',
    'k',
    'g',
    'l',
    'm',
    'n',
    'v',
    'h',
    'y',
    'P',
    'Q',
    'R',
    'Q',
    'h',
    'y',
    'Q',
    '252',
    ]

en_int = [
    '1',
    '2',
    '3',
    '4',
    '5',
    '6',
    '7',
    '8',
    '9',
    '0',
    ]

eng_plate_char = [
    'sh',
    's',
    'alf',
    'a',
    'b',
    'p',
    't',
    'th',
    'jim',
    'ch',
    'he',
    'kh',
    'd',
    'zal',
    'r',
    'z',
    'zh',
    'sad',
    'zad',
    'ta',
    'za',
    'eyn',
    'qayn',
    'f',
    'ghaf',
    'k',
    'g',
    'l',
    'm',
    'n',
    'v',
    'h',
    'ye',
    'sis',
    'vil',
    'dip',
    'vil',
    'h',
    'ye',
    'vil',
    '252',
    ]

def convert_ch(reader):

    str_plate = ""
    possibility = []
    for item in reader:
        possibility.append(item[2])
    str_plate = reader[possibility.index(max(possibility))][1]

    plate = ""
    for ch in str_plate:
        if ch in en_int:
            plate = plate + ch
        else:
            ch = eng_plate_char[char_plate.index(ch)]
            plate = plate = plate + ch
    
    return plate

def run_ocr(img):
    reader = easyocr.Reader(['en'], recog_network='custom_plate')
    reader = reader.readtext(img)
    return convert_ch(reader)


# originalImage = cv2.imread('/Users/error/Desktop/esm.jpg')
# reader = easyocr.Reader(['en'], recog_network='custom_plate')
# reader = reader.readtext(originalImage)

# print(reader)
