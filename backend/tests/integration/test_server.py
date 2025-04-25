import unittest
   import os
   import sys
   
   # 상위 디렉토리를 모듈 검색 경로에 추가
   sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))
   
   from app import app

   class ServerIntegrationTests(unittest.TestCase):
       def setUp(self):
           self.app = app.test_client()
           self.app.testing = True

       def test_server_running(self):
           response = self.app.get('/')
           self.assertEqual(response.status_code, 200)
       
       def test_static_files(self):
           # 정적 파일 제공 테스트 (실제 빌드 후 테스트 필요)
           # 이 테스트는 프론트엔드가 빌드되어 backend/www에 복사된 후 실행해야 함
           pass