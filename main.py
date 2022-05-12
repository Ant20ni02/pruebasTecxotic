from flask import Flask, render_template, send_file, redirect, url_for, request
#from photomosaic import main
#from floatgrid import main

#count = 0


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
'''

@app.route('/photomosaic')
def get_photomosaic():
    filename = 'photomosaic.jpeg'
    return send_file(filename, mimetype='image/jpeg')


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
    except Exception as e:
        print(e)
