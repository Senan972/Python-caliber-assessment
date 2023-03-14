# import necessary modules
from datetime import datetime

# create a dictionary to map sub-category ID with sub-category name
subcat_dict = {
    1: 'Fishery',
    2: 'Meat',
    3: 'Medical Accessories',
    4: 'Fruits',
    5: 'Vegetables',
    6: 'Packed Fruits and Vegetables',
    7: 'Medical Consumables',
    8: 'Medical Ointments & Sprays',
    9: 'Chocolates',
    10: 'Biscuits',
    11: 'Croissant',
    12: 'Ice-Cream',
    13: 'Milk',
    14: 'Baby Diapers',
    15: 'Baby Milk Formula',
    16: 'Baby Feeding Accessories',
    17: 'Adult Pads',
    18: 'Sensual Care',
    19: 'Personal Care',
    20: 'Hygiene',
    21: 'Household Care',
    22: 'Fragrances',
    23: 'Perfumes',
    24: 'Air Fragrances',
    25: 'Surface Cleaners',
    26: 'Dish Washers',
    27: 'Laundry',
    28: 'Facial Care',
    29: 'Body Care',
    30: 'Oral Care',
    31: 'Baby Oral Care',
    32: 'Baby Body Care',
    33: 'Soap & Body Wash',
    34: 'Baby Bath supplies',
    35: 'Foodgrains',
    36: 'Rice',
    37: 'Pulses',
    38: 'Salt',
    39: 'Sugar',
    40: 'Chips and other snacks',
    41: 'Frozen Meat',
    42: 'Frozen Poultry',
    43: 'Fresh Poultry',
    44: 'Canned Poultry',
    45: 'Canned Meat',
    46: 'Canned Fish',
    47: 'Canned Fruits',
    48: 'Canned Veggies',
    49: 'Frozen Veggies',
    50: 'Frozen Fruits'
}

# create a dictionary to map product ID with sub-category ID
product_dict = {
    1: 4,
    2: 44,
    3: 24,
    4: 12,
    5: 27,
    6: 14,
    7: 9,
    8: 13,
    9: 28,
    10: 30
}

# create a dictionary to map sub-category ID with a list of interest points on each date
subcat_interest = {}
for subcat_id in subcat_dict:
    subcat_interest[subcat_id] = {}

# process the given data
data = [
 {
   "Date": "1/2/2023",
   "Time": "12:12:12",
   "User ID": 5,
   "Product ID": 1,
   "Interest Point": 30
 },
 {
   "Date": "1/2/2023",
   "Time": "12:12:12",
   "User ID": 3,
   "Product ID": 3,
   "Interest Point": 100
 },
 {
   "Date": "1/2/2023",
   "Time": "12:12:12",
   "User ID": 2,
   "Product ID": 7,
   "Interest Point": 40
 },
 {
   "Date": "1/2/2023",
   "Time": "12:12:12",
   "User ID": 1,
   "Product ID": 3,
   "Interest Point": 50
 },
 {
   "Date": "2/2/2023",
   "Time": "12:12:12",
   "User ID": 12,
   "Product ID": 9,
   "Interest Point": 60
 },
 {
   "Date": "2/2/2023",
   "Time": "12:12:12",
   "User ID": 4,
   "Product ID": 2,
   "Interest Point": 10
 },
 {
   "Date": "2/2/2023",
   "Time": "12:12:12",
   "User ID": 6,
   "Product ID": 7,
   "Interest Point": 40
 },
 {
   "Date": "3/3/2023",
   "Time": "12:12:12",
   "User ID": 2,
   "Product ID": 5,
   "Interest Point": 40
 },
 {
   "Date": "3/3/2023",
   "Time": "12:12:12",
   "User ID": 34,
   "Product ID": 3,
   "Interest Point": 30
 },
 {
   "Date": "3/3/2023",
   "Time": "12:12:12",
   "User ID": 78,
   "Product ID": 10,
   "Interest Point": 10
 },
 {
   "Date": "3/3/2023",
   "Time": "12:12:12",
   "User ID": 123,
   "Product ID": 1,
   "Interest Point": 10
 },
 {
   "Date": "4/3/2023",
   "Time": "12:12:12",
   "User ID": 1234,
   "Product ID": 6,
   "Interest Point": 60
 },
 {
   "Date": "4/3/2023",
   "Time": "12:12:12",
   "User ID": 45,
   "Product ID": 3,
   "Interest Point": 70
 },
 {
   "Date": "5/3/2023",
   "Time": "12:12:12",
   "User ID": 67,
   "Product ID": 7,
   "Interest Point": 20
 },
 {
   "Date": "5/3/2023",
   "Time": "12:12:12",
   "User ID": 89,
   "Product ID": 5,
   "Interest Point": 40
 },
 {
   "Date": "5/3/2023",
   "Time": "12:12:12",
   "User ID": 9,
   "Product ID": 9,
   "Interest Point": 60
 },
 {
   "Date": "5/3/2023",
   "Time": "12:12:12",
   "User ID": 65,
   "Product ID": 2,
   "Interest Point": 100
 },
 {
   "Date": "5/3/2023",
   "Time": "12:12:12",
   "User ID": 33,
   "Product ID": 5,
   "Interest Point": 30
 },
 {
   "Date": "6/3/2023",
   "Time": "12:12:12",
   "User ID": 223,
   "Product ID": 8,
   "Interest Point": 70
 },
 {
   "Date": "6/3/2023",
   "Time": "12:12:12",
   "User ID": 44,
   "Product ID": 6,
   "Interest Point": 80
 },
 {
   "Date": "7/3/2023",
   "Time": "12:12:12",
   "User ID": 553,
   "Product ID": 4,
   "Interest Point": 20
 },
 {
   "Date": "7/3/2023",
   "Time": "12:12:12",
   "User ID": 324,
   "Product ID": 3,
   "Interest Point": 40
 },
 {
   "Date": "7/3/2023",
   "Time": "12:12:12",
   "User ID": 23445,
   "Product ID": 2,
   "Interest Point": 50
 },
 {
   "Date": "7/3/2023",
   "Time": "12:12:12",
   "User ID": 2434,
   "Product ID": 7,
   "Interest Point": 50
 },
 {
   "Date": "7/3/2023",
   "Time": "12:12:12",
   "User ID": 25435,
   "Product ID": 4,
   "Interest Point": 100
 },
 {
   "Date": "7/3/2023",
   "Time": "12:12:12",
   "User ID": 246,
   "Product ID": 10,
   "Interest Point": 10
 },
 {
   "Date": "8/3/2023",
   "Time": "12:12:12",
   "User ID": 2342,
   "Product ID": 9,
   "Interest Point": 40
 },
 {
   "Date": "8/3/2023",
   "Time": "12:12:12",
   "User ID": 234,
   "Product ID": 8,
   "Interest Point": 50
 },
 {
   "Date": "8/3/2023",
   "Time": "12:12:12",
   "User ID": 45,
   "Product ID": 9,
   "Interest Point": 60
 },
 {
   "Date": "8/3/2023",
   "Time": "12:12:12",
   "User ID": 234,
   "Product ID": 1,
   "Interest Point": 70
 },
 {
   "Date": "8/3/2023",
   "Time": "12:12:12",
   "User ID": 343,
   "Product ID": 4,
   "Interest Point": 80
 },
 {
   "Date": "8/3/2023",
   "Time": "12:12:12",
   "User ID": 324,
   "Product ID": 6,
   "Interest Point": 10
 },
 {
   "Date": "8/3/2023",
   "Time": "12:12:12",
   "User ID": 346,
   "Product ID": 8,
   "Interest Point": 90
 },
 {
   "Date": "8/3/2023",
   "Time": "12:12:12",
   "User ID": 232,
   "Product ID": 5,
   "Interest Point": 80
 },
 {
   "Date": "8/3/2023",
   "Time": "12:12:12",
   "User ID": 4534,
   "Product ID": 3,
   "Interest Point": 70
 },
 {
   "Date": "8/3/2023",
   "Time": "12:12:12",
   "User ID": 234,
   "Product ID": 6,
   "Interest Point": 60
 },
 {
   "Date": "9/3/2023",
   "Time": "12:12:12",
   "User ID": 4564,
   "Product ID": 10,
   "Interest Point": 50
 },
 {
   "Date": "9/3/2023",
   "Time": "12:12:12",
   "User ID": 565,
   "Product ID": 1,
   "Interest Point": 10
 },
 {
   "Date": "9/3/2023",
   "Time": "12:12:12",
   "User ID": 786,
   "Product ID": 4,
   "Interest Point": 70
 },
 {
   "Date": "9/3/2023",
   "Time": "12:12:12",
   "User ID": 897,
   "Product ID": 3,
   "Interest Point": 40
 },
 {
   "Date": "9/3/2023",
   "Time": "12:12:12",
   "User ID": 867,
   "Product ID": 7,
   "Interest Point": 30
 },
 {
   "Date": "9/3/2023",
   "Time": "12:12:12",
   "User ID": 97,
   "Product ID": 4,
   "Interest Point": 20
 },
 {
   "Date": "9/3/2023",
   "Time": "12:12:12",
   "User ID": 6756,
   "Product ID": 8,
   "Interest Point": 60
 },
 {
   "Date": "9/3/2023",
   "Time": "12:12:12",
   "User ID": 786,
   "Product ID": 6,
   "Interest Point": 70
 },
 {
   "Date": "10/3/2023",
   "Time": "12:12:12",
   "User ID": 645,
   "Product ID": 4,
   "Interest Point": 90
 },
 {
   "Date": "10/3/2023",
   "Time": "12:12:12",
   "User ID": 34,
   "Product ID": 6,
   "Interest Point": 100
 },
 {
   "Date": "10/3/2023",
   "Time": "12:12:12",
   "User ID": 5675,
   "Product ID": 3,
   "Interest Point": 10
 },
 {
   "Date": "10/3/2023",
   "Time": "12:12:12",
   "User ID": 242,
   "Product ID": 8,
   "Interest Point": 40
 },
 {
   "Date": "10/3/2023",
   "Time": "12:12:12",
   "User ID": 5675,
   "Product ID": 3,
   "Interest Point": 20
 },
 {
   "Date": "10/3/2023",
   "Time": "12:12:12",
   "User ID": 234235,
   "Product ID": 5,
   "Interest Point": 40
 }]
 
# create the subcat_interest dictionary
subcat_interest = {}
for item in data:
    subcat_id = product_dict.get(item["Product ID"])
    date = datetime.strptime(item["Date"], "%d/%m/%Y").date()
    if subcat_id is not None:
        if subcat_id not in subcat_interest:
            subcat_interest[subcat_id] = {}
        if date not in subcat_interest[subcat_id]:
            subcat_interest[subcat_id][date] = []
        subcat_interest[subcat_id][date].append(item["Interest Point"])

# print the interest points for each sub-category for each date
for subcat_id in subcat_dict:
    print(f"Sub-category: {subcat_dict[subcat_id]}")
    if subcat_id in subcat_interest:
        for date in subcat_interest[subcat_id]:
            print(f"Date: {date.strftime('%d/%m/%Y')}, Interest Points: {subcat_interest[subcat_id][date]}")
    else:
        print("No interest points for this sub-category.")
    print()
