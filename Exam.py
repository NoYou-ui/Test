import requests
import csv

while True:
    RegionCode = input("Please enter a region code:\n")

    if RegionCode == "01" or RegionCode == "05" or RegionCode == "07" or RegionCode == "12" or RegionCode == "14"\
            or RegionCode == "18" or RegionCode == "21" or RegionCode == "23" or RegionCode == "26"\
            or RegionCode == "32" or RegionCode == "35" or RegionCode == "44" or RegionCode == "46"\
            or RegionCode == "08" or RegionCode == "51" or RegionCode == "53" or RegionCode == "56"\
            or RegionCode == "59" or RegionCode == "61" or RegionCode == "63" or RegionCode == "65"\
            or RegionCode == "68" or RegionCode == "71" or RegionCode == "73" or RegionCode == "74"\
            or RegionCode == "80" or RegionCode == "85":

        r = requests.get('https://registry.edbo.gov.ua/api/universities/?ut=1&lc=' + RegionCode + '&exp=json')

        universities: list = r.json()
        filtered_data = [{k: row[k] for k in ['university_id', 'post_index',
                                              'university_financing_type_name']} for row in universities]
        universities_names = [{k: row[k] for k in ['university_name', 'university_name_en']} for row in universities]

        with open('universities.csv', mode='w', encoding='UTF-8') as f:
            writer = csv.DictWriter(f, fieldnames=filtered_data[0].keys())
            writer.writeheader()
            writer.writerows(filtered_data)

        with open('universities_' + RegionCode + '.csv', mode='w', encoding='UTF-8') as f:
            writer = csv.DictWriter(f, fieldnames=filtered_data[0].keys())
            writer.writeheader()
            writer.writerows(filtered_data)

        with open('ua_en.csv', mode='w', encoding='UTF-8') as f:
            writer = csv.DictWriter(f, fieldnames=universities_names[0].keys())
            writer.writeheader()
            writer.writerows(universities_names)
            break
    else:
        print("Bad Region")