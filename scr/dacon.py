import scr.li_handler as li_handler

class Out:
    class list:
        def __init__(self):
            pass
        def csv(self):
            ul_csv = li_handler.Ul.file('.csv')
            li = ul_csv.li()
            return li

class In:
    pass
    