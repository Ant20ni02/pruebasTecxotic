import os
import sys
from flask import Flask, render_template, send_file, redirect, url_for, request
import cv2
import Photomosaic

#from floatgrid import main "photo" + str(currPhoto+1) + ".jpg"
currPhoto = 0
cap = cv2.VideoCapture(0)
mainDir = os.getcwd()
photosDir = mainDir + "\photos" #windows
#photosDir = mainDir + "/photos" #macos

# Configuration of Flask_Socketio
app = Flask(__name__)

@app.route('/photomosaic_takePhoto')
def photomosaic_photo():
    global currPhoto
    currPhoto +=1
    if currPhoto > 8:
        currPhoto = 1
        for f in os.listdir(photosDir):
            os.remove(os.path.join(photosDir, f))
    os.chdir(photosDir)
    Photomosaic.takePhoto(currPhoto, cap)
    os.chdir(mainDir)
    return send_file("photos\photo" + str(currPhoto) + ".jpg", mimetype='image/jpg')


@app.route('/photomosaic_changePhoto',methods=['POST'])
def photomosaic_change():
    json_dict = request.get_json()
    currentPhoto = json_dict["currentPhoto"]
    os.chdir(photosDir)
    Photomosaic.takePhoto(currentPhoto, cap)
    os.chdir(mainDir)
    return send_file("photos\photo" + str(currentPhoto) + ".jpg", mimetype='image/jpg')


'''
@app.route('/floatgrid',methods = ['POST'])
def floatgrid():
    speed =  request.form['float_speed']
    angle =  request.form['float_angle']
    time =  request.form['float_time']
    float(speed)
    float(angle)
    float(time)
    #floatgrid.main(speed, angle, time)
    return send_file('floatgrid.jpg', mimetype='image/jpg') 
'''


if __name__ == '__main__':
    try:
        print("Running...")
        app.run(debug = True, host='0.0.0.0', port="3000")
    except KeyboardInterrupt:
        for f in os.listdir(photosDir):
            os.remove(os.path.join(photosDir, f))
        print('kiti')
    except Exception as e:
        for f in os.listdir(photosDir):
            os.remove(os.path.join(photosDir, f))
        print(e)

        
