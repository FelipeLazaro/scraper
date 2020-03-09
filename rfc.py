import requests

if __name__ == '__main__':
    API_KEY = '85212010e6392d4540db44bb197adb2f'
    URL_TO_SCRAPE = 'https://www.gob.mx/v1/renapoCURP/consulta'
payload = {'api_key': API_KEY, 'url': URL_TO_SCRAPE}
cookies = {"_ga":"GA1.1.1742668824.1574871635", "_gid":"GA1.1.104301455.1583259337", "_gat":"1", "RT":"z=1&dm=www.gob.mx&si=9d8929bb-7d8f-45ef-8ab6-fcf89d801d0d&ss=k7f1fclf&sl=1&tt=2qq&ld=2qx"}
r = requests.post('http://api.scraperapi.com', params=payload, data={"formMain": "formMain","valRFC": "LASF871119E89","consulta":'',"javax.faces.ViewState": "5554873812774818944:6735907153824116487"})
#json_response = r.json()
#json_response['data']

print(r.text)  