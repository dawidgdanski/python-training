# 3.X only: nonlocal

def singleton3only(aClass):  # On @ decoration
    instance = None

    def onCall(*args, **kwargs):  # On instance creation
        nonlocal instance  # 3.X and later nonlocal
        if instance == None:
            instance = aClass(*args, **kwargs)  # One scope per class
        return instance

    return onCall
