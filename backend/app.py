{\rtf1\ansi\ansicpg1251\cocoartf2822
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\paperw11900\paperh16840\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\pard\tx720\tx1440\tx2160\tx2880\tx3600\tx4320\tx5040\tx5760\tx6480\tx7200\tx7920\tx8640\pardirnatural\partightenfactor0

\f0\fs24 \cf0 from flask import Flask, jsonify\
from flask_cors import CORS\
import os\
\
app = Flask(__name__)\
CORS(app)\
\
USER = os.environ.get("STUDENT_ID", "XX")\
\
@app.route("/api/hello", methods=["GET"])\
def hello():\
    return jsonify(\{\
        "message": f"Hello from student red\{USER\}!",\
        "student": f"red\{USER\}",\
        "status": "ok"\
    \})\
\
@app.route("/api/health", methods=["GET"])\
def health():\
    return jsonify(\{"status": "healthy"\})\
\
@app.route('/api/health', methods=['GET'])\
def health_check():\
    # \uc0\u1051 \u1077 \u1075 \u1082 \u1086 \u1074 \u1077 \u1089 \u1085 \u1099 \u1081  \u1101 \u1085 \u1076 \u1087 \u1086 \u1080 \u1085 \u1090  \u1076 \u1083 \u1103  \u1087 \u1088 \u1086 \u1074 \u1077 \u1088 \u1082 \u1080  \u1089 \u1090 \u1072 \u1090 \u1091 \u1089 \u1072  \u1089 \u1072 \u1084 \u1086 \u1075 \u1086  Flask-\u1087 \u1088 \u1080 \u1083 \u1086 \u1078 \u1077 \u1085 \u1080 \u1103 \
    return jsonify(\{"status": "healthy"\}), 200\
\
if __name__ == "__main__":\
    app.run(host="0.0.0.0", port=5000)}