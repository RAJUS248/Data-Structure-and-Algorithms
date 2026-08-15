# 07:05:45PM --> Output: 19:05:45

def timeConversion(Time):

    find_AMPM = Time[-2:]  # find AM PM

    remove_AMPM = Time[:-2] # remove AM PM

    hh, mm, ss = map(int , remove_AMPM.split(':'))

    if find_AMPM == 'AM':
        if hh == 12:
            hh = 0

    else:
        hh != 12
        hh = hh + 12
    return f"{hh:02}:{mm:02}:{ss:02}" 

Time = "07:05:45PM"
print(timeConversion(Time))
