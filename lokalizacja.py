import requests
Key ="0d1356a0c37774b2f1b132913381d9b1"
def funkcja_szer_dlug(szerokosc):
    lista=[]
    url = "https://developers.zomato.com/api/v2.1/search?lat="+str(szerokosc)+"&lon=18&radius=2&sort=real_distance"
    r = requests.get(url, headers={'user-key': Key})
    data =r.json()
    miejsca = data['restaurants']
    for miejsce in miejsca:
        lista.append(str(miejsce['restaurant']['location']))
    return str(lista)

