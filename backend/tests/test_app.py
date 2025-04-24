import pytest
from app import app
import io

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_health_check(client):
    """Test health check endpoint"""
    response = client.get('/api/health')
    assert response.status_code == 200
    json_data = response.get_json()
    assert json_data['status'] == 'healthy'
    assert 'message' in json_data

def test_transcribe_without_file(client):
    """Test transcribe endpoint without file"""
    response = client.post('/api/transcribe')
    assert response.status_code == 400
    json_data = response.get_json()
    assert json_data['error'] == 'No file provided'

def test_transcribe_with_file(client):
    """Test transcribe endpoint with file"""
    data = {}
    data['file'] = (io.BytesIO(b"dummy audio content"), 'test.wav')
    response = client.post('/api/transcribe', data=data)
    assert response.status_code == 200
    json_data = response.get_json()
    assert json_data['status'] == 'processing'
    assert json_data['message'] == 'Audio received'

def test_get_transcriptions(client):
    """Test get transcriptions endpoint"""
    response = client.get('/api/transcriptions')
    assert response.status_code == 200
    json_data = response.get_json()
    assert 'transcriptions' in json_data
    assert isinstance(json_data['transcriptions'], list)