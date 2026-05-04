from flask import Flask, request, jsonify
from flask_cors import CORS
import requests
import json

app = Flask(__name__)
# بفتح الباب لأي موقع يكلم السيرفر (حل الـ 403 النهائي)
CORS(app, resources={r"/*": {"origins": "*"}})

@app.route('/chat', methods=['POST', 'OPTIONS'])
def chat():
    # معالجة طلبات الـ Preflight اللي المتصفح بيبعتها
    if request.method == 'OPTIONS':
        return jsonify({"status": "ok"}), 200

    try:
        # استلام البيانات بأي صيغة (JSON أو غيرها)
        data = request.get_json(force=True) or {}
        user_msg = data.get('message', 'No message')

        # هنا "السيستم" بتاعك بيرد برد احترافي
        # الرد ده مصمم إنه ميعملش أي Error في Lovable
        return jsonify({
            "status": "success",
            "reply": f"PRO AI Global System: [ {user_msg} ] - Status: Online brothers",
            "rex_team_auth": True
        })

    except Exception as e:
        # نظام الإنقاذ الذاتي: لو حصلت كارثة السيرفر بيفضل صاحي
        return jsonify({
            "status": "self_heal",
            "reply": f"Emergency Mode: System is recovering from ({str(e)}) brothers"
        }), 200

# تشغيل السيرفر على Vercel
def handler(request):
    return app(request)
