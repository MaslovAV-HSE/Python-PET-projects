from urllib.request import urlretrieve
import  os, time, math, vk

vkapi = vk.API(access_token='vk1.a.oS-dO8TVFcTn1d9uESjpv4IKRUht9nAC1iOu-w6FCwkbPUEquAaDpLM1wQb5jvgm3yFgIp6AdwxZUrfrPu5O3XRMbYao8glI-mr8YFwxtStxbUongUwPcSpjAunoBH8Lyd2Gv24p_F4szyJ6k84Vhp5Zzitg6C0PoDhDotpLvwp2QWK_or3HvcxYsNPhiYUFXiBp9QUHGL--MhmSAFu6KQ',
               v='5.81')

url = "https://vk.com/albums-16955"
owner_id = url.split('/')[-1].replace('albums', '')
albums = vkapi.photos.getAlbums(owner_id=owner_id)

dir = 'saved_photos'
if not os.path.exists(dir):
    os.mkdir(dir)
sucsess = 0
breaked = 0

for album in albums['items']:
    photos = vkapi.photos.get(owner_id=owner_id, album_id=album["id"], count=1000, photo_sizes=0)
    photo_folder = ''
    try:
        if not os.path.exists(f'{dir}/{album["title"]}'):
            os.mkdir(f'{dir}/{album["title"]}')
        photo_folder = album["title"]
    except Exception:
        if not os.path.exists(f'{dir}/{album["id"]}'):
            os.mkdir(f'{dir}/{album["id"]}')
        photo_folder = album["id"]

    for photo in photos["items"]:
        url = photo["sizes"][0]["url"]
        try:
            urlretrieve(url, f'{dir}/{photo_folder}/{photo["id"]}.jpg')
            sucsess += 1
        except Exception:
            print('Произошла ошибка, файл пропущен.')
            breaked += 1
            continue

print(f'Фото скачано:{sucsess} \n Произошла ошибка при загрузке {breaked}')