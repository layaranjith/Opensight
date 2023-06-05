from quickdraw import QuickDrawData
from flask import Flask, jsonify, send_file
from io import BytesIO
qd=QuickDrawData(recognized=True)
class InstructionGenerator:

    def __init__(self, object_name):
        try:
            self.obj = qd.get_drawing(object)
        except:
            self.obj=None

            

def serve_pil_image(pil_img):
    img_io = BytesIO()
    pil_img.save(img_io, 'JPEG', quality=70)
    img_io.seek(0)
    return send_file(img_io, mimetype='image/jpeg')

app=Flask(__name__)

@app.route("/drawing/<name>")
def drawing(name: str):
    try:
        obj = qd.get_drawing(name)
    except:
        return jsonify({"error":"Drawing for given name not found"})
    return serve_pil_image(obj.image)

@app.route("/points/<name>")
def points(name: str):
    try:
        obj = qd.get_drawing(name)
    except:
        return jsonify({"error":"Drawing for given name not found"})
    return jsonify(obj.image_data)
app.run()