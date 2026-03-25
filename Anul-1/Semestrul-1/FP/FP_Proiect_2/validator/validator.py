from Domain.pachete import get_id, get_data_sosire, get_data_plecare, get_locatie, get_pret
import datetime


def validator(pachet, pachete):
    
    id = get_id(pachet)
    msg = ""
    for p in pachete:
        if get_id(p) == id:
            msg += "ID-ul exista deja \n"
    if get_data_sosire(pachet) > get_data_plecare(pachet):
        msg += "Data de plecare nu poate fi mai devreme de data de sosire!\n"
    if msg != "":
        raise Exception(msg)
    else:
        return True

def validare_date(calatorie,a=None):
    # Procesare locatie
    calatorie[3] = get_locatie(calatorie).lower()
    # Validare ID
    try:
        try:
            int(get_id(calatorie))
        except ValueError:
            raise ValueError("ID was not a valid number!")
        if a is not None:
            for i in a:
                if get_id(i) == get_id(calatorie):
                    raise ValueError("ID Already Exist!")

        # Validare Data
        df = '%d %m %Y'
        try:
            calatorie[1] = datetime.datetime.strptime(get_data_sosire(calatorie), df)
            calatorie[2] = datetime.datetime.strptime(get_data_plecare(calatorie), df)
        except ValueError:
            raise ValueError("Incorect data format, Must be DD-MM-YYYY")
        # Interval de timp pozitiv
        if get_data_sosire(calatorie) > get_data_plecare(calatorie):
            raise ValueError("Intervalul de timp introdus nu este valid!")
        # Validare Pret
        try:
            calatorie[4] = int(get_pret(calatorie))
        except ValueError:
            raise ValueError("Pretul trebuie sa fie un numar")
    except ValueError:
        return False
    else:
        return True