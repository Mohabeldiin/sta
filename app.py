import requests
from flask import Flask, request
from flask_cors import CORS
from packages.websec import WebSec
from packages.speed import SpeedApi
from packages.seo import SEORanking
from packages.testsuites.all_test_cases import get_result

app = Flask(__name__)
CORS(app)


@app.route('/test', methods=['POST'])
def process_json():
    content_type = request.headers['Content-Type']
    if content_type == 'application/json':
        data = request.get_json()
        if data['name'] == "speed":
            speed = SpeedApi(data)
            result = speed.get()
            requests.post(url="http://localhost:4000/performance", json=result, headers={
            'Content-Type': 'application/json'})
        elif data['name'] == "seo":
            seo = SEORanking(data)
            result = seo.get_result()
            requests.post(url="http://localhost:4000/SEO", json=result, headers={
            'Content-Type': 'application/json'})
        elif data['name'] == "security":
            security = WebSec(data)
            result = security()
            requests.post(url="http://localhost:4000/Security", json=result, headers={
            'Content-Type': 'application/json'})
        elif data['name'] == "selenium":
            result = get_result(data['id'])
            requests.post(url="http://localhost:4000/selenium", json=result, headers={
            'Content-Type': 'application/json'})
        elif data['name'] == "all":
            speed = SpeedApi(data)
            result_speed = speed.get()
            seo = SEORanking(data)
            result_seo = seo.get_result()
            security = WebSec(data)
            result_sec = security()
            result_selenium = get_result(data['id'])
            result1 = {'speed': result_speed,
                       'seo': result_seo, 'security': result_sec,
                       'selenium': result_selenium}
            result = {
                "loadingExperince": result_speed['loadingExperince'],
                "OriginLoadingExperince": result_speed['OriginLoadingExperince'],
                "PR_Precentage": result_speed['PR_Precentage'],
                "total_traffic": result_seo['total_traffic'],
                "key_Word": result_seo['key_Word'],
                "total_traffic_cost": result_seo['total_traffic_cost'],
                "final_score": result_sec['final_score'],
                "software_found": result_sec['software_found'],
                "software_outdated": result_sec['software_outdated'],
                "software_vulnerabil": result_sec['software_vulnerabil'],
                "LinkOwner": data['id']}
            requests.post(url="http://localhost:4000/ALL", json=result, headers={
            'Content-Type': 'application/json'})
        return {'message': 200, 'data': result}
    else:
        return '415 Unsupported Media Type'


if __name__ == '__main__':
    app.run()
