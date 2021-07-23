langs = ['Python', 'Java', 'C#', 'C', 'TypeScript' , 'Go']
years = [1991, 1995, 2000, 1972]

for idx, value in enumerate(langs):
    if idx < len(years):
        print(f"{value} - {years[idx]}")
    else:
        print(f"{value} - Unknown")

