import datetime
import bloodbath

# Setup
bloodbath.api_key = 'zStM_aXwrs1Arp43IYPbRLvH2dy9OkiLWSYOrshRQKjtpfjjzaxREFVfiVWKRK4aDs7qUfOSUjnE1Ix9zQZhMw=='

def test_find():
    response = bloodbath.Event.find('bc42d831-fd17-41ab-9d42-41e45b2fc3a2')
    assert ('id' in response.keys()) == True

# def test_cancel():
#     response = bloodbath.Event.cancel('bc42d831-fd17-41ab-9d42-41e45b2fc3a2')
#     assert ('errors' in response.keys() == False

def test_list():
    response = bloodbath.Event.list()
    assert ('id' in response[0].keys()) == True

def test_schedule():
    response = bloodbath.Event.schedule(
        # TODO: internal server crash with strftime('%Y-%m-%dT%H:%M:%S') we should investigate why
        scheduled_for=(datetime.datetime.now() + datetime.timedelta(hours=1)).isoformat(), # "2022-07-14T19:54:06Z" <- this one works
        headers="{}",
        method="post",
        body="some body content",
        endpoint='https://api.acme.com/path'
    )
    assert ('id' in response.keys()) == True
