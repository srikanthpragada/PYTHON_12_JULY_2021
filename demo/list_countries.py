import requests

resp = requests.get("https://restcountries.eu/rest/v2/all")
countries = resp.json()

print("10 Largest by Population")
print("=" * 50)
for country in sorted(countries, key=lambda d: d['population'], reverse=True)[:10]:
    print(f"{country['name']:30}  {country['capital']:30} {country['population']:10}")

print("10 Largest by Area")
print("=" * 50)
for country in sorted(countries,
                      key=lambda d: 0 if d['area'] is None else d['area'],
                      reverse=True)[:10]:
    print(f"{country['name']:30}  {country['capital']:30} {country['area']:10}")
