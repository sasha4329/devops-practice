{\rtf1\ansi\ansicpg1251\cocoartf2822
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\paperw11900\paperh16840\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\pard\tx720\tx1440\tx2160\tx2880\tx3600\tx4320\tx5040\tx5760\tx6480\tx7200\tx7920\tx8640\pardirnatural\partightenfactor0

\f0\fs24 \cf0 import unittest\
from unittest.mock import patch, MagicMock\
import sys\
import os\
\
sys.path.append(os.path.dirname(__file__))\
from app import app\
\
class TestNotesApp(unittest.TestCase):\
    def setUp(self):\
        self.ctx = app.app_context()\
        self.ctx.push()\
        self.client = app.test_client()\
\
    def tearDown(self):\
        self.ctx.pop()\
\
    def test_health_endpoint(self):\
        """1. \uc0\u1055 \u1088 \u1086 \u1074 \u1077 \u1088 \u1082 \u1072  \u1088 \u1072 \u1073 \u1086 \u1090 \u1086 \u1089 \u1087 \u1086 \u1089 \u1086 \u1073 \u1085 \u1086 \u1089 \u1090 \u1080  \u1101 \u1085 \u1076 \u1087 \u1086 \u1080 \u1085 \u1090 \u1072  /api/health"""\
        response = self.client.get('/api/health')\
        self.assertEqual(response.status_code, 200)\
        self.assertEqual(response.json, \{"status": "healthy"\})\
\
    @patch('app.get_db_connection')\
    def test_get_notes_mocked(self, mock_get_db_connection):\
        """2. \uc0\u1058 \u1077 \u1089 \u1090 \u1080 \u1088 \u1086 \u1074 \u1072 \u1085 \u1080 \u1077  \u1073 \u1080 \u1079 \u1085 \u1077 \u1089 -\u1083 \u1086 \u1075 \u1080 \u1082 \u1080  \u1087 \u1086 \u1083 \u1091 \u1095 \u1077 \u1085 \u1080 \u1103  \u1079 \u1072 \u1084 \u1077 \u1090 \u1086 \u1082  \u1089  \u1079 \u1072 \u1075 \u1083 \u1091 \u1096 \u1082 \u1086 \u1081  \u1041 \u1044 """\
        mock_conn = MagicMock()\
        mock_cursor = MagicMock()\
\
        mock_cursor.fetchall.return_value = [(1, "\uc0\u1058 \u1077 \u1089 \u1090 \u1086 \u1074 \u1099 \u1081  \u1079 \u1072 \u1075 \u1086 \u1083 \u1086 \u1074 \u1086 \u1082 ", "\u1058 \u1077 \u1089 \u1090 \u1086 \u1074 \u1099 \u1081  \u1090 \u1077 \u1082 \u1089 \u1090 ")]\
        mock_conn.cursor.return_value = mock_cursor\
\
        mock_get_db_connection.return_value = mock_conn\
\
        response = self.client.get('/api/notes')\
\
        self.assertEqual(response.status_code, 200)\
        self.assertEqual(len(response.json), 1)\
        self.assertEqual(response.json[0]['title'], "\uc0\u1058 \u1077 \u1089 \u1090 \u1086 \u1074 \u1099 \u1081  \u1079 \u1072 \u1075 \u1086 \u1083 \u1086 \u1074 \u1086 \u1082 ")\
\
if __name__ == '__main__':\
    unittest.main()}