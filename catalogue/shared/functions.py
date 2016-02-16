def set_saeculo(self):
    d = str(self.date)
    s = ''

    # Set century
    century = int(d[:2])
    if century == 12:
        s = '13'
    elif century == 13:
        s = '14'
    elif century == 14:
        s = '15'
    elif century == 15:
        s = '16'

    # Set quarter
    quarter = int(d[2:4])
    if quarter < int(25):
        s += '.1'
    elif quarter < int(50):
        s += '.2'
    elif quarter < int(75):
        s += '.3'
    else:
        s += '.4'

    # Set certainty
    if d[4:5] == '?':
        s += '?'

    # Save the content
    return s