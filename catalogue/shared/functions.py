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

def truncate(content, length=100, suffix=' ...'):
    if len(content) <= length:
        return content
    else:
        return ' '.join(content[:length+1].split(' ')[0:-1]) + suffix

def attachment_id_path(instance, filename):
    """Return the upload path of a File based on the class where it is used as an
    inline model. The assumes that the model contains the field `attached_to`,
    which hold the foreign key to the model that is going to have the
    attachment.

    """
    return '{0}/id_{1}/{2}'.format(
        instance.attached_to.__class__.__name__, instance.attached_to.id, filename
    )
