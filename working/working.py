import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    start_minutes = 00
    end_minutes = 00
    #check AM to PM
    if time_12 := re.match(r"(\d?\d):?(\d?\d)? AM to (\d?\d):?(\d?\d)? PM",s):

        # checking hours
        if 0 < int(time_12.group(1)) <= 12:
            if 0 < int(time_12.group(3)) <= 12:
                start_hours = 0 if int(time_12.group(1)) == 12 else int(time_12.group(1))
                end_hours = 12 if int(time_12.group(3)) == 12 else int(time_12.group(3)) + 12
            else:
                raise ValueError

        else:
            raise ValueError


    #check PM to AM
    elif time_12 := re.match(r"(\d?\d):?(\d?\d)? PM to (\d?\d):?(\d?\d)? AM",s):
        if 0 < int(time_12.group(1)) <= 12:
            if 0 < int(time_12.group(3)) <= 12:
                start_hours = 12 if int(time_12.group(1)) == 12 else int(time_12.group(1))+12
                end_hours = int(time_12.group(3))
                if end_hours == 12:
                    end_hours = 0
            else:
                raise ValueError
        else:
            raise ValueError
    else:
        raise ValueError


    # checking minutes
    if time_12.group(2):
        if 0 <= int(time_12.group(2)) < 60:
            start_minutes = int(time_12.group(2))
        else:
            raise ValueError
    else:
        pass
    if time_12.group(4):
        if 0 <= int(time_12.group(4)) < 60:
            end_minutes = int(time_12.group(4))
        else:
            raise ValueError
    else:
        pass
    #return time
    time_24 = f"{start_hours:02}:{start_minutes:02} to {end_hours:02}:{end_minutes:02}"
    return time_24


if __name__ == "__main__":
    main()
