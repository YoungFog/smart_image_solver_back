from flask import Flask
from flask import request
from flask_cors import CORS
import os
import base64
app = Flask(__name__)

@app.route('/encode', methods = ['POST'])
def encode():
    os.system('touch upload/upload.png')
    img = request.values.get('img')
    txt = request.values.get('txt')
    img_ori = base64.b64decode(img)
    with open('./upload/upload.png', 'wb') as f:
        f.write(img_ori)
    str_secret = txt
    cmd = ['python','--secret']
    pth_ecd_function = 'StegaStamp/encode_image.py'
    cmd_run = cmd[0] + ' ' + pth_ecd_function + ' ' + cmd[1] + ' ' + str_secret
    os.system(cmd_run) # launch image watermark model
    # to this step, encoded image is saved in ./save/decoded.png
	
    pth_encoded_img = 'save/decoded.png'
    with open(pth_encoded_img, 'rb') as f:
        img_ecd = f.read()
        img_ecd_base64 = base64.b64encode(img_ecd)
    os.system('rm upload/upload.png')
    os.system('rm save/decoded.png')

    return img_ecd_base64

@app.route('/decode', methods = ['POST'])
def deccode():
    os.system('touch upload/upload.png')
    # img_ori = request.values.get('img')
    img = request.values.get('img')
    img_ori = base64.b64decode(img)
    with open('upload/upload.png', 'wb') as f:
        f.write(img_ori)
    cmd = ['python', '--image']
    pth_dcd_function = 'StegaStamp/decode_image.py'
    cmd_run = cmd[0] + ' ' + pth_dcd_function
    os.system(cmd_run)
    pth_code = 'save/code.txt'
    with open(pth_code, 'r') as f:
        str_code = f.read()
    os.system('rm upload/upload.png')
    os.system('rm save/code.txt')
    return str_code
    
@app.route('/lock',methods=['POST'])
def lock():
    os.system('touch upload/input.pdf')
    pdf_ori = request.values.get('ori_pdf')
    pwd = request.values.get('password')
    new_name = request.values.get('new_pdf')
    pdf_ori = base64.b64decode(pdf_ori)
    with open("./upload/input.pdf",'wb') as f:
        f.write(pdf_ori)
    cmd = "python StegaStamp/pdf_lock_unlock.py upload/input.pdf -a encrypt -l 1 -p " + pwd + " -o save/" + new_name 
    os.system(cmd)
    new_pdf_base64 = None
    with open('save/'+new_name,'rb') as f:
        new_pdf = f.read()
        new_pdf_base64 = base64.b64encode(new_pdf)

    # os.system("rm ./save/"+new_name)
    os.system("rm ./upload/input.pdf")
    return '/'+new_name
    # return new_pdf_base64

@app.route('/unlock',methods=['POST'])
def unlock():
    os.system('touch upload/locked.pdf')
    pdf_locked = request.values.get('pdf_locked')
    unlock_pwd = request.values.get('password')
    new_name = request.values.get('new_pdf')
    pdf_locked = base64.b64decode(pdf_locked)
    with open("./upload/locked.pdf",'wb') as f:
        f.write(pdf_locked)
    cmd = "python StegaStamp/pdf_lock_unlock.py upload/locked.pdf -a decrypt -l 1 -p " + unlock_pwd + " -o save/" + new_name 
    os.system(cmd)
    new_pdf_base64 = None
    with open('save/'+new_name,'rb') as f:
        new_pdf = f.read()
        new_pdf_base64 = base64.b64encode(new_pdf)

    # os.system("rm ./save/"+new_name)
    os.system("rm ./upload/locked.pdf")
    return '/'+new_name
    # return new_pdf_base64

@app.route('/add_water',methods=['POST'])
def add_water():
    os.system('touch upload/input.pdf')
    os.system('touch upload/water.pdf')
    pdf_ori = request.values.get('ori_pdf')
    pdf_water = request.values.get('water_pdf')
    new_name = request.values.get('new_pdf')
    pdf_ori = base64.b64decode(pdf_ori)
    pdf_water = base64.b64decode(pdf_water)
    with open("./upload/input.pdf",'wb') as f:
        f.write(pdf_ori)
    with open("./upload/water.pdf",'wb') as f:
        f.write(pdf_water)
    cmd = "python StegaStamp/pdf_addwater.py --input_file=./upload/input.pdf --water_file=./upload/water.pdf --new_file=./save/" + new_name 
    os.system(cmd)
    new_pdf_base64 = None
    with open('save/'+new_name,'rb') as f:
        new_pdf = f.read()
        new_pdf_base64 = base64.b64encode(new_pdf)

    # os.system("rm ./save/"+new_name)
    os.system("rm ./upload/input.pdf")
    os.system('rm ./upload/water.pdf')
    return '/'+new_name
    # return new_pdf_base64

@app.route('/test', methods=['GET'])
def test():
    text = request.values.get("text")
    return text

if __name__ == '__main__':
    CORS(app, supports_credentials=True)
    app.run(
            host = '127.0.0.1',
            port = 5000,  
            debug = True 
            )
