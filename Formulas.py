def sector_s_area(diameter, angle):
    if d_r.lower() == "d" and a_f.lower() == "a":
        ans = 3.14 * float(angle) * float(diameter) * float(diameter) / 1440
        print(str(ans))


while True:
    advt = input("Which formula do you want to run?(Option:Sector's area(SA)):")
    if advt.upper() == "SA":
        d_r = input("Do you want to use diameter or radius?(type d or r):")
        a_f = input("Do you want to use angle or fraction?(type a or f):")
        if d_r.lower() == "d" and a_f.lower() == "a":
            d = input("please give me the diameter:")
            a = input("please give me the angle:")
            sector_s_area(d, a)
    option = input("Do you want to run another formula? (type yes or no):")
    if option.lower() == "no":
        break
