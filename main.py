import requests
from pyfiglet import Figlet
import folium


def get_info_by_ip(ip='127.0.01'):
    try:
        response= requests.get(url=f'http://ip-api.com/json/{ip}').json()
        print(response)

        data={
            '[IP]':response.get("query"),
            '[Int prov]':response.get("isp"),
            '[Org]':response.get("org"),
            '[Country]':response.get("country"),
            '[Region Name]':response.get("regionName"),
            '[City]':response.get("city"),
            '[ZIP]':response.get("zip"),
            '[Lat]':response.get("lat"),
            '[Lon]':response.get("lon")
        }

        for k,v in data.items():
            print(f'{k}:{v}')

        area=folium.Map(location=[response.get('lat'), response.get("lon")])
        area.save(f'{response.get("query")}_{response.get("city")}.html')

    except requests.exceptions.ConnectionError:
        print("[!] Please check your connection!")


def main():
    preview=Figlet(font="slant")
    print(preview.renderText("IP INFO"))
    ip=input("Please enter a taget IP: ")

    get_info_by_ip(ip=ip)

# 185.41.120.41
if __name__ =='__main__':
    main()