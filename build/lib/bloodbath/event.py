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

  def cancel(id):
    url = f'{bloodbath.api_url}/events/{id}'
    response = requests.delete(url, headers = Event.__headers())
    return Event.__serializer(
      response.json()
    )

  def list():
    url = f'{bloodbath.api_url}/events'
    response = requests.get(url, headers = Event.__headers())
    return Event.__serializer(
      response.json()
    )

  def schedule(**arguments):
    url = f'{bloodbath.api_url}/events'
    response = requests.post(url, headers = Event.__headers(), json = arguments)
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
    if 'data' in response.keys():
      if response['data'] is None:
        return {}
      return response['data']
    return response
