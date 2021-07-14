import bloodbath
import requests
from bloodbath.error import ApiKeyError

class Event:
  def find(id):
    url = f'{bloodbath.api_url}/events/{id}'
    response = requests.get(url, headers = Event.__headers())
    result = response.json()
    if 'data' in result.keys(): return result['data']
    return result

  @staticmethod
  def __headers():
    if bloodbath.api_key is None:
      raise ApiKeyError("No API key transmitted. Please set it up.")

    return {
      "authorization": f'Bearer {bloodbath.api_key}'
    }
