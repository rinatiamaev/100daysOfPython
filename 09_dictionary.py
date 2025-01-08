

stud_score = {
    "Anna" : 98,
    "Boris" : 50,
    "Fil" : 100,
    "Bob" : 86
}
stud_res = {}

def CheckStud():
    for student in stud_score:
        score = stud_score[student]
        if score in range(90, 101):
            stud_res[student] = "Best"
        elif score in range(60, 90):
            stud_res[student] = "good"
        else:
            stud_res[student] = "Bad"
    print(stud_res)

# CheckStud()

Capitals_dict = {
    "USA": "Washingtone",
    "Finland": "Helsinki",
    "Spain" : "Madrid",
    "Japan" : "Tokio"
}

MyTravel_dict = {
    "USA" : {"New York" : 2, "Florida" : 1, "Cansas" : 3},
    "Finland" : {"Helsinki": 5, "Turku" : 4 },
    "Spain" : {"Barselona" : 12, "Sevila" : 21},
    "Japan" : {"Tokio" : 6, "Osaka" : 8}
}

def CapitalChecker():
    for country, capital in Capitals_dict.items():
        if country in MyTravel_dict:
            visited_city = MyTravel_dict[country]
            if capital in visited_city:
                visits = visited_city[capital]
                print(f"You are visited {country} ({capital}) {visits} times")
CapitalChecker()

        