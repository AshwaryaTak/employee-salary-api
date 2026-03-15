def calculate_salary(country: str, gross: float):

    if country.lower() == "india":
        tds = gross * 0.10

    elif country.lower() == "united states":
        tds = gross * 0.12

    else:
        tds = 0

    net = gross - tds

    return {
        "gross_salary": gross,
        "tds": tds,
        "net_salary": net
    }