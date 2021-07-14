import bloodbath
import requests
from bloodbath.error import ApiKeyError

class Event:
  def find(id):
    url = f'{bloodbath.api_url}/events/{id}'
    response = requests.get(url, headers = Event.__headers())
    return Event.__serializer(
      response.json()
    )

  @staticmethod
  def __headers():
    if bloodbath.api_key is None:
      raise ApiKeyError("No API key transmitted. Please set it up.")

    return {
      "authorization": f'Bearer {bloodbath.api_key}'
    }

  def __serializer(response):
    if 'data' in response.keys(): return response['data']
    return response
