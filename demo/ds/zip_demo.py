langs = ['Python', 'Java', 'C#', 'C', 'TypeScript']
years = [1991, 1995, 2000, 1972]

# for idx, value in enumerate(langs):
#     print(f"{value} - {years[idx]}")

for lang, year in zip(langs, years):
    print(f"{lang} - {year}")
