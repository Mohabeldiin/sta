from flask import Flask, request
from packages.websec import WebSec
from packages.speed import SpeedApi
from packages.seo import SEORanking
from packages.testsuites.all_test_cases import get_result

app = Flask(__name__)


@app.route('/test', methods=['POST'])
def process_json():
    content_type = request.headers['Content-Type']
    if content_type == 'application/json':
        data = request.get_json()
        if data['name'] == "speed":
            speed = SpeedApi(data)
            result = speed.get()
        elif data['name'] == "seo":
            seo = SEORanking(data)
            result = seo.get_result()
        elif data['name'] == "security":
            security = WebSec(data)
            result = security()
        elif data['name'] == "selenium":
            result = get_result()
        elif data['name'] == "all":
            speed = SpeedApi(data)
            result_speed = speed.get()
            seo = SEORanking(data)
            result_seo = seo.get_result()
            security = WebSec(data)
            result_sec = security()
            result_selenium = get_result()
            result = {'speed': result_speed,
                      'seo': result_seo, 'security': result_sec,
                      'selenium': result_selenium}
        return {'message': 200, 'data': result}
    else:
        return '415 Unsupported Media Type'


if __name__ == '__main__':
    app.run()
