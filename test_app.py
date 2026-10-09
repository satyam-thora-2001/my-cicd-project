from app import app

def test_home_page():
    response = app.test_client().get("/")
    
    assert response.status_code == 200
    assert b"CI/CD Pipeline is Working Successfully" in response.data