#https://auto.ru/cars/lamborghini/all/
import requests
#DOC: https://requests.readthedocs.io/en/latest/

# POST(изменить) vs GET(получение)

# Задание: написать функцию fetch
def fetch(url, params): # params = {method, headers, body}
    headers = params["headers"]
    body = params["body"]
    method = params["method"]

    if method == "POST":
        return requests.post(url, headers=headers, data=body)
    
    if method == "GET":
        return requests.get(url, headers=headers)
        
# HTTP header, HTTP Method, HTTP Body
# НЕ КОПИРОВАТЬ, ВЗЯТЬ ИЗ Web-Inspector!
lambo = fetch("https://auto.ru/-/ajax/desktop/listing/", {
  "headers": {
    "accept": "*/*",
    "accept-language": "en,ru;q=0.9",
    "cache-control": "no-cache",
    "content-type": "application/json",
    "pragma": "no-cache",
    "sec-ch-ua": "\".Not/A)Brand\";v=\"99\", \"Google Chrome\";v=\"103\", \"Chromium\";v=\"103\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "same-origin",
    "sec-fetch-site": "same-origin",
    "x-client-app-version": "87.0.9727341",
    "x-client-date": "1657909708631",
    "x-csrf-token": "9fbf73a9e0920f1257c10d02b30351ca8674e7f6ee98ff56",
    "x-page-request-id": "677734079aba2781134c11ddac8469aa",
    "x-requested-with": "XMLHttpRequest",
    "x-retpath-y": "https://auto.ru/cars/lamborghini/all/?price_from=40000000",
    "x-yafp": "{\"a1\":\"BWTAeg==;0\",\"a2\":\"z7yj+GuiWLgPU451MVVY1a60HdNsQA==;1\",\"a3\":\"kgtBhouNTvIJ+ryjlnxYSw==;2\",\"a4\":\"ggEQMrqrplyyIA==;3\",\"a5\":\"gUaYVrG+LXwA6A==;4\",\"a6\":\"HMI=;5\",\"a7\":\"/NJtCtXB9kcXyg==;6\",\"a8\":\"GLwrF06i+98=;7\",\"a9\":\"VrI9cpuj39oJCg==;8\",\"b1\":\"gs870S3ivaA=;9\",\"b2\":\"8NPEjuDkV5N1Lw==;10\",\"b3\":\"YykhNhKbyOpCGg==;11\",\"b4\":\"XnlcHVbMTQ8=;12\",\"b5\":\"0Hmw+HEQ7ZCaAg==;13\",\"b6\":\"cbHpWSBFNgX5Ug==;14\",\"b7\":\"bsg68KCr+XLtrA==;15\",\"b8\":\"9JNX5ZC2KGs7MA==;16\",\"b9\":\"uCOFIzdezoHhjw==;17\",\"c1\":\"Q6QFTQ==;18\",\"c2\":\"KsF0fD3URndnk3lzE5jKfg==;19\",\"c3\":\"9tzBfhsgXRyySRIZ8YqWfQ==;20\",\"c4\":\"v39RYnBHJOs=;21\",\"c5\":\"aG1dAg+EJww=;22\",\"c6\":\"41QZqA==;23\",\"c7\":\"4smjSu0AlgU=;24\",\"c8\":\"kIQ=;25\",\"c9\":\"BICXooyDljg=;26\",\"d1\":\"KFi6n51Pqzg=;27\",\"d2\":\"xf4=;28\",\"d3\":\"S9Bjpc/iWJ4TUQ==;29\",\"d4\":\"jUKQkDiyeGs=;30\",\"d5\":\"gX3kHdVUyJc=;31\",\"d7\":\"UyE=;32\",\"d8\":\"p4KeXJ9X1jgy3eLxra0md/KbzVYPEqiCkTU=;33\",\"d9\":\"lmIz4Ypq7Pk=;34\",\"e1\":\"R7IN9KgyVYKFXw==;35\",\"e2\":\"FUAhTqf4jq4=;36\",\"e3\":\"w3ifOql6vrs=;37\",\"e4\":\"umzODUs/Y5c=;38\",\"e5\":\"i/NmzL9vS8NdBg==;39\",\"e6\":\"rByl9hS+kP0=;40\",\"e7\":\"XO5wKWhGRwvaeA==;41\",\"e8\":\"fpkDQaFPeWU=;42\",\"e9\":\"j45DJyslbvo=;43\",\"f1\":\"pawG+i2f2JVmzg==;44\",\"f2\":\"4RY/HGzUkqI=;45\",\"f3\":\"IbhTrTWnSiliGg==;46\",\"f4\":\"xY1U0V7EYjI=;47\",\"f5\":\"dEW/Vooer9CRdg==;48\",\"f6\":\"BIacpe0WeF/SUw==;49\",\"f7\":\"l3zb2u2hIbL+SQ==;50\",\"f8\":\"J9OhFFqYltZ6sQ==;51\",\"f9\":\"O1w0VyrOz8E=;52\",\"g1\":\"Ta11NwHFePzp/A==;53\",\"g2\":\"XnIO2mhbfBUZFw==;54\",\"g3\":\"pVSjfnF64e0=;55\",\"g4\":\"RcGrMapUye43vQ==;56\",\"g5\":\"yO9SWmYu0q0=;57\",\"g6\":\"KJsf/lzrkFY=;58\",\"g7\":\"ndCz94Cp1z8=;59\",\"g8\":\"ms/xWEwn8CM=;60\",\"g9\":\"Se7jhWp9Ygo=;61\",\"h1\":\"k0pC0D1TENtfkA==;62\",\"h2\":\"dv2y3PgnENaRag==;63\",\"h3\":\"ZQlxs5lA3UHyGw==;64\",\"h4\":\"fFtwqlMxJGAe6w==;65\",\"h5\":\"gUoifbzPV88=;66\",\"h6\":\"2isolFJW0bA13w==;67\",\"h7\":\"4RB3ZXPZgiDWO7PkeBr122aXeKowLarN57isLU+AZ9zkX+pQ;68\",\"h8\":\"lnZGmsN4Xj1N9w==;69\",\"h9\":\"eznnGNUuhT60bw==;70\",\"i1\":\"v5zihEkb5fc=;71\",\"i2\":\"RXVRbDMvMyLtHA==;72\",\"i3\":\"6xqXbxWdoCb+TQ==;73\",\"i4\":\"LiaosEuFWi98PQ==;74\",\"i5\":\"ClG54HlfK7muVw==;75\",\"z1\":\"OLFSx8A9dsNVzb3Yy395KzbTNJt2uOWPi/LFe8xdTNb9bErveGZ4DhjSerjhiHiCL8WN2w0OaKg7ZV9NYobwkg==;76\",\"z2\":\"3lFj8W4RLYFyOrd5HbNECPpSKimcwEDqELDKHbpgYMt3b60Glo3MuQQNdBvY8iDIh+g4Ky7PHNGHaZjnPW8VKg==;77\",\"y2\":\"AZfc5WpijPk6fg==;78\",\"y3\":\"Ih1NPq+OJh3qBA==;79\",\"y6\":\"1t97VPlrQnyyNQ==;80\",\"y8\":\"xGS66293FyCsrQ==;81\",\"x4\":\"dAKVGttZbG6Qog==;82\",\"z5\":\"kOyyhOzrdOQ=;83\",\"z4\":\"DkjGC91Onzhm5A==;84\",\"z6\":\"QoAYc7tZ0YtNZcbC;85\",\"z7\":\"4MA+6uJTvVGmJ+vH;86\",\"z8\":\"aRQQxZW5XPjkm9Z3H58=;87\",\"z9\":\"CIqMqtquEU0p5276;88\",\"y1\":\"eU9qrx4HSNCoJtW/;89\",\"y4\":\"nnYpgpc1VPr5M+Yv;90\",\"y5\":\"yzQeYnmp7Tj56z+VsUI=;91\",\"y7\":\"nSui6NpZ9fGQD2At;92\",\"y9\":\"kYez6uZhM98vO2zPX68=;93\",\"y10\":\"dfxV7LC0giTxP8ERfKk=;94\",\"x1\":\"Xrx41mP3shzIIHGp;95\",\"x2\":\"6BTHPH7+UuK0Fk6kNCY=;96\",\"x3\":\"6nmVVNqwgQANPudw;97\",\"x5\":\"ObaOnVh9v41wx/zN;98\",\"z3\":\"7zAbuMT2Zl8c6scxgLytHksreAIfCx6nmVeFZq0p+KA=;99\",\"v\":\"6.3.1\",\"pgrdt\":\"gJBqcXB6czpSLWaT8sJyRbKSc6Q=;100\",\"pgrd\":\"uZOXsy4pL/KFNQK8c0ESreU1eZPbDVHOJOWaOIZofh4jDxXF4wSYWjOuWbZ0jjLK5P/luC9QzgrvNrvQVvf76b5BApJDXKMivpmfxBehY5cglVsRk8KVcMIATEc6YM9QQvuu4Gi0VDnhr9/IMf5wDyMzdywCKu3h4xAEqbpL+tn0+EGqEVtpwK4hDoz0EPqDaOXbZtfpXW9aOqTGn2HUrTbz/FY=\"}",
    "cookie": "_csrf_token=9fbf73a9e0920f1257c10d02b30351ca8674e7f6ee98ff56; autoru_gdpr=1; suid=85f19f0b88f068335ba14eba3f5e3435.14c9674db7da17f1988676e377b9dc01; from=direct; yandex_login=mike.ovc; i=+ig900XxUD2KPyhZzxvB/AFtdEDBcDv6Kf44NuFBzlrHrCuBC/BTn3fXGOOzP49fQFvqkB4u6RmiiWR85nul08TIOtU=; gdpr=0; _ym_uid=1645564389770852331; Session_id=3:1651602110.5.0.1610028951543:Y0DWUY4Md_wArzqJAEsBKg:32.1.2:1|348690723.-1.2.0:3.1:63090147|61:4179.734334.JzGSZR4l7-5nnNkhXjOkFWnxYqw; mda2_beacon=1651602110184; _ym_isad=1; _ym_visorc=b; spravka=dD0xNjU3OTA5MzQ4O2k9MmEwMTo0YjAwOmE4NWY6ODgwMDpkNGYxOjYyMGI6Zjg4ZTpjMjMwO0Q9QjI0RDQ5MjIwMzMxMkExOTkyRjAwQkYxQkM5OThGNjZFQTVDRDU5Q0Y5RDFBMzZERDI4M0M4ODhBQUQ5RDJEOEI2MTk2NkQ2O3U9MTY1NzkwOTM0ODE4NjEzMjYzMztoPTUzNWY1NzI3ODlmNjRkODFiM2Y1MTJhMGRhYjdmNjc2; autoru_sid=a%3Ag62d1b0642oij9uajfsqurf1all33va3.eb258a4ad54bdcb7d157dd9e5cdfab1e%7C1657909348310.604800.LOsoXEObCG6BKMMum7_ugQ.-oO98SH-ImySD_l1Mu4AcXnz0lDGQ_HD90UZsqrlhTY; autoruuid=g62d1b0642oij9uajfsqurf1all33va3.eb258a4ad54bdcb7d157dd9e5cdfab1e; yuidlt=1; yandexuid=6280271851523913546; my=YwA%3D; ys=udn.cDrQnNC40YXQsNC40Lsg0J7QstGH0LjQvdC90LjQutC%2B0LI%3D%23wprid.1657203178471267-16304609657449765454-sas3-0712-43f-sas-l7-balancer-8080-BAL-5426%23c_chck.111146787; crookie=67GvBm5Ta3+xP+OTII84t7iy5lZ6IkubzZjJXxaGgcXCWwmWncXb2v/ORkCGMBhWVm0OMj2Az3W+KeuFcIBr+YZRCYM=; cmtchd=MTY1NzkwOTM1MDAzNw==; _yasc=HUNstrd4V5cnLFetxc2epO3RSAN3qHD5+KXjH/MAF4HZ3epz; sso_status=sso.passport.yandex.ru:blocked; los=1; bltsr=1; from_lifetime=1657909687643; _ym_d=1657909689",
    "Referer": "https://auto.ru/cars/lamborghini/all/?price_from=40000000",
    "Referrer-Policy": "no-referrer-when-downgrade"
  },
  "body": "{\"price_from\":40000000,\"catalog_filter\":[{\"mark\":\"ROLLS_ROYCE\"}],\"section\":\"all\",\"category\":\"cars\",\"output_type\":\"list\"}",
  "method": "POST"
});

lambo.headers["Content-Type"] # Что за формат данных у нас

lambo_data = lambo.json()
len(lambo_data["offers"])
for offer in lambo_data["offers"]:
    print(f'LAMBO {offer["vehicle_info"]["tech_param"]["human_name"]} Mileage: {offer["state"]["mileage"]}, Price: {offer["price_info"]["EUR"]}')