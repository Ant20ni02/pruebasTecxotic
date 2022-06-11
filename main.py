import os
import sys
from flask import Flask, render_template, send_file, redirect, url_for, request
import cv2
import Photomosaic
import Floatgrid

currPhoto = 0
cap = cv2.VideoCapture(0)
mainDir = os.getcwd()
photosDir = mainDir + "\photos" #windows
#photosDir = mainDir + "/photos" #macos

# Configuration of Flask_Socketio
app = Flask(__name__)

@app.route('/photomosaicPhoto')#Take photo one by one
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


@app.route('/photomosaicChange',methods=['POST'])#take and change a photo with the number of the photo
def photomosaic_change():
    json_dict = request.get_json()
    currentPhoto = json_dict["currentPhoto"]
    os.chdir(photosDir)
    Photomosaic.takePhoto(currentPhoto, cap)
    os.chdir(mainDir)
    return send_file("photos\photo" + str(currentPhoto) + ".jpg", mimetype='image/jpg')



@app.route('/floatgrid',methods = ['POST'])
def floatgrid():
    json_dict = request.get_json()
    speed = float(json_dict["grid_speed"])
    angle =  float(json_dict["grid_angle"])
    time =  float(json_dict["grid_time"])
    x = int(json_dict["grid_x"])
    y = int(json_dict["grid_y"])
    Floatgrid.main(speed, angle, time,x,y)
    return send_file('floatgrid.jpg', mimetype='image/jpg') 



if __name__ == '__main__':
    try:
        print("Running...")
        app.run(debug = True, host='0.0.0.0', port="8080")
    except KeyboardInterrupt:
        for f in os.listdir(photosDir):
            os.remove(os.path.join(photosDir, f))
        print('kiti')
    except Exception as e:
        for f in os.listdir(photosDir):
            os.remove(os.path.join(photosDir, f))
        print(e)

        
