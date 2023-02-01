import time
import vk

TOKEN='vk1.a.oS-dO8TVFcTn1d9uESjpv4IKRUht9nAC1iOu-w6FCwkbPUEquAaDpLM1wQb5jvgm3yFgIp6AdwxZUrfrPu5O3XRMbYao8glI-mr8YFwxtStxbUongUwPcSpjAunoBH8Lyd2Gv24p_F4szyJ6k84Vhp5Zzitg6C0PoDhDotpLvwp2QWK_or3HvcxYsNPhiYUFXiBp9QUHGL--MhmSAFu6KQ',
VERSION='5.81'

api = vk.API(access_token=TOKEN,v=VERSION)

first_group = "perm_musevents"
second_group = "permm_museum"

def count_by_place(group:list, param:str):
    di = {}
    counter = 0
    for person in group:
        try:
            x = person[param]
            if x["title"] not in di:
                di[x["title"]] = 1
            else:
                di[x["title"]] += 1
        except Exception:
            counter+=1
    print(f"Подсчет по параметру: {param} не прошли {counter} пользователей")
    return di


def grab_all_members(group_id):
    members = []
    count = api.groups.getMembers(group_id=group_id)['count']
    i = 0
    while True:
        m = api.groups.getMembers(group_id=group_id, offset=i, count=200, fields=['sex', 'bdate', 'city', 'country', 'has_mobile'])["items"]
        members += m
        i += len(m)
        time.sleep(0.3)
        if len(m) == 0:
            break
    print(f"Считано {len(members)} пользователей!")
    return members


def analize_age(members:list):
    di = {}
    counter = 0
    for person in members:
        try:
            x = person['bdate']
            x = x.split('.')[2]
            age = 2022 - int(x)
            if age not in di:
                di[age] = 1
            else:
                di[age] += 1
        except Exception:
            counter += 1
    users = 0
    ages = 0
    for k,v in di.items():
        ages += k*v
        users += v
    ages /= users
    print(f"Подсчет по параметру age не прошли {counter} пользователей")
    return di, ages

def analize_by_sex(members):
    di = {}
    counter = 0
    for person in members:
        try:
            x = person['sex']
            if x not in di:
                di[x] = 1
            else:
                di[x] += 1
        except Exception:
            counter += 1
    print(f"Подсчет по параметру sex не прошли {counter} пользователей")
    return di

def analize_by_place(places_d, name):
    places = list(places_d.values())
    maxes = max(places)
    count = sum(places)
    print(f'Самый популярный(ая) {name} для группы:')
    for k, v in places_d.items():
        if v == maxes:
            print(f"{k} - {round(v/count, 4)*100}%")
            break

def compare_by_user_intersection(first, second):
    f_id = set([person['id'] for person in first])
    s_id = set([person['id'] for person in second])
    ids = f_id.intersection(s_id)
    print(f'Количество пересекающихся пользователей = {len(ids)}\n'
          f'Для {first_group} = {round(len(ids)/(len(f_id)), 4)*100}%\n'
          f'Для {second_group} = {round(len(ids)/(len(s_id)), 4)*100}%')


def compare_by_sex(first, second):
    print(f'Процент мужчин в {first_group} = {round(first[2]/len(first_members), 4) * 100}%'
          f' Процент женщин в {first_group} =  {round(first[1]/len(first_members), 4) * 100}% \n'
          f'Процент мужчин в {second_group} = {round(second[2]/len(second_members), 4) * 100}%'
          f' Процент женщин в {second_group} =  {round(second[1]/len(second_members), 4) * 100}%')

#1-w, 2-m

#members_f = api.groups.getMembers(group_id=first_group, fields=['sex', 'bdate', 'city', 'country', 'has_mobile'])
#members_s = api.groups.getMembers(group_id=second_group, fields=['sex', 'bdate', 'city', 'country', 'has_mobile'])


print(f'-----------------Анализ {first_group}----------------------')
first_members = grab_all_members(first_group)
f_city = count_by_place(first_members, 'city')
f_country = count_by_place(first_members, 'country')
analize_by_place(f_country, "страна")
analize_by_place(f_city, 'город')
f_age = analize_age(first_members)
f_s = analize_by_sex(first_members)



print(f'-----------------Анализ {second_group}----------------------')
second_members = grab_all_members(second_group)
s_city = count_by_place(second_members, 'city')
s_country = count_by_place(second_members, 'country')
analize_by_place(s_country, "страна")
analize_by_place(s_city, 'город')
s_age = analize_age(second_members)
s_s = analize_by_sex(second_members)

print('-----------------------------Сравнение---------------------------------------')
compare_by_user_intersection(first_members, second_members)
compare_by_sex(f_s, s_s)








