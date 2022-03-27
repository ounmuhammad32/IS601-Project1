"""This is tests2 simple pages"""



def test_request_aaatesting(client):
    """This tests AAA page"""
    response = client.get("/AAAtesting")
    assert response.status_code == 200
    assert b"What is AAA testing?" in response.data


def test_request_oop(client):
    """This tests OOP page"""
    response = client.get("/OOPs")
    assert response.status_code == 200
    assert b"Encapsulation" in response.data


def test_request_pyliny(client):
    """This tests Pylint page"""
    response = client.get("/pylint")
    assert response.status_code == 200
    assert b"What is Pytest?" in response.data


def test_request_solid(client):
    """This tests SOLID page"""
    response = client.get("/SOLID")
    assert response.status_code == 200
    assert b"SOLIDbanner.png" in response.data

def test_request_page_not_found(client):
    """This tests page not found page"""
    response = client.get("/page5")
    assert response.status_code == 404