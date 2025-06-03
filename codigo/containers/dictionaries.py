# como los mapas en java, o sea acepta duplicados solo en los values pero no en los keys.

months = {
    "Jan":"January",
    "Feb":"February",
    "Mar":"March"
}

print(months["Jan"])

months["Apr"] = "April"
print(months)

months.update({"May":"May","Jun":"June"})
print(months)

for month in months:
    print(month, months[month])

for month in months.keys():
    print(month, months[month])

for month in months.values():
    print(month)

for key,value in months.items():
    print(key,value)