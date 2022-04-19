from flask import request, render_template
from flask import Flask
import skimage.io
from PIL import Image
from predictor_api import make_prediction
import numpy as np
import io
import base64
import colour


app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template("home.html")

@app.route('/predict', methods=['GET','POST'])
def predict():
    img = request.files['img']
    img.save('img.jpg')
    image = skimage.io.imread('img.jpg')[:,:,:3]/255
    
    
    k = colour.LUT3D(size=10)
    og_shape = k.linear_table(size=10).shape
    LUT = k.linear_table(size=10).reshape(-1,3)
    
    reshape = LUT.shape

    
    
    
    inputWB = float(request.form['Input White Balance'])
    outputWB = float(request.form["Output White Balance"])
    inputWB_arr = np.tile(inputWB,(reshape[0],1))
    outputWB_arr = np.tile(outputWB,(reshape[0],1))
    
    
    data = np.concatenate((inputWB_arr,LUT,outputWB_arr), axis=1)
    LUT_out = make_prediction(data)

    APPLY = colour.LUT3D(table= LUT_out.reshape(og_shape))
    newimage = APPLY.apply(image)
    
    
    
#    output = (rgb_out.reshape(shape)*255).astype(np.uint8)
    dat = io.BytesIO()
    Image.fromarray((newimage*255).astype(np.uint8)).save(dat, "JPEG")
    dat2 = io.BytesIO()
    Image.fromarray((image*255).astype(np.uint8)).save(dat2, "JPEG")
    
    encoded_img_data = base64.b64encode(dat.getvalue())
    encoded_img_data2 = base64.b64encode(dat2.getvalue())
    return render_template("prediction.html", img_data=encoded_img_data.decode('utf-8'),
        img_data2=encoded_img_data2.decode('utf-8'),
        )


   
    


if __name__ == "__main__":
    app.run(debug=True)
    
