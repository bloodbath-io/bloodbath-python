import bloodbath

def test_find():
    bloodbath.api_key = 'zStM_aXwrs1Arp43IYPbRLvH2dy9OkiLWSYOrshRQKjtpfjjzaxREFVfiVWKRK4aDs7qUfOSUjnE1Ix9zQZhMw=='
    response = bloodbath.Event.find('bc42d831-fd17-41ab-9d42-41e45b2fc3a2')
    assert ('id' in response.keys()) == True
