cert1 = {
    "name": "AZ-900",
    "provider": "Microsoft",
    "level": "Beginner",
    "cost": 165,
    "duration_weeks": 4
}
cert2 = {
    "name": "DP-100",
    "provider": "Microsoft", 
    "level": "Advanced",
    "cost": 330,
    "duration_weeks": 12
}
cert3 = {
    "name": "AWS-SAA",
    "provider": "Amazon",
    "level": "Intermediate",
    "cost": 300,
    "duration_weeks": 8
}

certifications = [cert1, cert2, cert3]

def show_certs(certs):
    for cert in certs:
        for key, value in cert.items():
            print(key + ": " + str(value))
        print("---")

def cheapest_cert(certs):
    lowest_cost = 999999
    low = None
    for cert in certs:
        if cert["cost"] < lowest_cost:
            lowest_cost = cert["cost"]
            low = cert
    print("Cheapest: " + low["name"] + " by " + low["provider"] + " — $" + str(lowest_cost))

def find_level(certs, level):
    for cert in certs:
        if cert["level"] == level:
            for key, value in cert.items():
                print(key + ": " + str(value))
            print("---")

show_certs(certifications)
cheapest_cert(certifications)
find_level(certifications, "Advanced")