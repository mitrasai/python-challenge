def compute_pay(hours, rate):
    if hours > 40:
        overtime = hours - 40
        regular_hours = 40
        regular_pay = regular_hours * rate
        overtime_pay = overtime * rate * 1.5
        pay = round(overtime_pay + regular_pay, 2)
    else:
        pay = round(hours * rate, 2)
    return pay


def check(input):
    try:
        result = float(input)
        return result
    except:
        print("Error, please enter numeric input")
        quit()


hour = input("Enter Hours: ")
hr = check(hour)
rate = input("Enter Rate: ")
r = check(rate)

pay = compute_pay(hr, r)
print(f"Pay: {pay}")
