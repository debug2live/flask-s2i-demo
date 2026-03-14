from flask import Flask, jsonify
import os

app = Flask(__name__)

@app.route('/')
def hello_openshift():
    return jsonify({
        "message": "Hello OpenShift S2I!, This is V2",
        "status": "Success",
        "version": "v1.0"
    })

if __name__ == '__main__':
    # Lấy port từ biến môi trường, mặc định là 8080
    port = int(os.environ.get('PORT', 8080))
    app.run(host='0.0.0.0', port=port)
