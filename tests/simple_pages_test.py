"""This test the homepage"""


def test_request_main_menu_links(client):
    """This tests menu links"""
    response = client.get("/")
    assert response.status_code == 200
    assert b'<a class="nav-link" href="/about">About</a>' in response.data



def test_request_index(client):
    """This tests home page"""
    response = client.get("/")
    assert response.status_code == 200
    assert b"Home" in response.data


def test_request_about(client):
    """This tests about page"""
    response = client.get("/about")
    assert response.status_code == 200
    assert b"About" in response.data


def test_request_page1(client):
    """This tests page1 page"""
    response = client.get("/page1")
    assert response.status_code == 200
    assert b"Git" in response.data


def test_request_page2(client):
    """This tests page2 page"""
    response = client.get("/page2")
    assert response.status_code == 200
    assert b"Docker" in response.data


def test_request_page3(client):
    """This tests page3 page"""
    response = client.get("/page3")
    assert response.status_code == 200
    assert b"Python" in response.data


def test_request_page4(client):
    """This tests page4 page"""
    response = client.get("/page4")
    assert response.status_code == 200
    assert b"CI/CD" in response.data