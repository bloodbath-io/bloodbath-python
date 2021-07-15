import datetime
import pytest
import requests
import requests_mock
import bloodbath

# Setup
bloodbath.api_key = 'zStM_aXwrs1Arp43IYPbRLvH2dy9OkiLWSYOrshRQKjtpfjjzaxREFVfiVWKRK4aDs7qUfOSUjnE1Ix9zQZhMw=='

def test_find():
    with requests_mock.Mocker() as mock:
        id = 'bc42d831-fd17-41ab-9d42-41e45b2fc3a2'
        mock.get(f'https://api.bloodbath.io/rest/events/{id}', json={'data': {'id': id}})
        response = bloodbath.Event.find(id)
        assert ('id' in response.keys()) == True

def test_cancel():
    with requests_mock.Mocker() as mock:
        id = '54815f72-a720-4f3e-95ec-6efa13eb95b1'
        mock.delete(f'https://api.bloodbath.io/rest/events/{id}', json={'data': {}})
        response = bloodbath.Event.cancel(id)
        assert ('errors' in response.keys()) == False

def test_list():
   with requests_mock.Mocker() as mock:
        mock.get(f'https://api.bloodbath.io/rest/events', json={'data': [{'id': 'some-id'}]})
        response = bloodbath.Event.list()
        assert ('id' in response[0].keys()) == True

def test_schedule():
    with requests_mock.Mocker() as mock:
        mock.post('https://api.bloodbath.io/rest/events', json={'data': {'id': 'random-id'}})
        response = bloodbath.Event.schedule(
            scheduled_for=(datetime.datetime.now() + datetime.timedelta(hours=1)).isoformat(),
            headers="{}",
            method="post",
            body="some body content",
            endpoint='https://api.acme.com/path'
        )
        assert ('id' in response.keys()) == True
