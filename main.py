import os
import sys
from flask import Flask, render_template, send_file, redirect, url_for, request
import pickle
from Photomosaic import photomosaic
#from floatgrid import main

currPhoto = 0


# Configuration of Flask_Socketio
app = Flask(__name__)


'''
@app.route('/photomosaic')
def get_photomosaic():
    global count
    if(count == 8):
        count = 0
        #photomosaic.main()
        if request.args.get('type') == '1':
            filename = 'photomosaic.jpg'
        else:
            filename = 'error.jpg'
        return send_file(filename, mimetype='image/jpg')
    else:
        count += 1
        #photomosaic.main()
        return 'Done!'
        'photomosaic.jpg'
'''

@app.route('/photomosaic')
def get_photomosaic():
    global currPhoto
    try:
        infile = open("currentPhoto.pk",'rb')
        currPhoto = pickle.load(infile)
        infile.close()
    except:
        currPhoto = 0
    if(currPhoto < 8):
        photomosaic()
        return send_file('loading.jpg', mimetype='image/jpg')
    else:
        photomosaic()
        return send_file('photomosaic.jpg', mimetype='image/jpg')
        

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
        dir =  os.getcwd() + '\photos'
        for f in os.listdir(dir):
            os.remove(os.path.join(dir, f))
        os.remove(os.getcwd() + '\currentPhoto.pk')
        print('kiti')
    except Exception as e:
        dir =  os.getcwd() + '\photos'
        for f in os.listdir(dir):
            os.remove(os.path.join(dir, f))
        os.remove(os.getcwd() + '\currentPhoto.pk')
        print(e)

        
