import requests

#Задание 1

def inlellligent_hero():
    url = 'https://akabab.github.io/superhero-api/api/all.json'
    response = requests.get(url)
    heros = {}
    heros_dict = ['Captain America', 'Hulk', 'Thanos']
    if 200 <= response.status_code < 300:
        in_ = response.json()
        for id_ in in_:
            if id_['name'] in heros_dict:
                name_ = id_['name']
                intelligence = id_['powerstats']['intelligence']
                heros[name_] = intelligence
    print(f'Самый умный супергерой: {max(heros)}')
# inlellligent_hero()

#Задание 2

class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def upload(self, file_path: str):
        """Метод загружает файлы по списку file_list на яндекс диск"""
        url = 'https://cloud-api.yandex.net/v1/disk/resources/upload'
        name_file = file_path.split('/')[-1]
        params = {
            'path': name_file
        }
        headers = {
            'Authorization': token
        }
        #получили ссылку на загрузку
        response = requests.get(url, headers=headers, params=params)
        #проверка
        if 200 <= response.status_code < 300:
        #загружаем картинку
            url_for_upload = response.json().get('href', '')
            with open(file_path, 'rb') as file:
                response2 = requests.put(url_for_upload, files={'file': file})


if __name__ == '__main__':
    # Получить путь к загружаемому файлу и токен от пользователя
    path_to_file = ...
    token = ...
    uploader = YaUploader(token)
    result = uploader.upload(path_to_file)