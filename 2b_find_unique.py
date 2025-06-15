def find_unique_element(arr):

    # ist input eine liste?
    if not isinstance(arr, list):
        raise TypeError("input muss eine liste sein")
    # ist array listenlänge ungerade? 
    if len(arr) % 2 == 0:
        raise ValueError("array muss eine ungerade länge haben")

    #ergebnis mit 0 initialisieren 
    result = 0

    for num in arr:
        #ist jedes element ein int? 
        if not isinstance(num, int):
            raise ValueError("alle elemente müssen integer sein")
        #kürzt doppelte zahlen raus (mit xor)
        result ^= num
    # einzelnes ergebnis bleit über
    return result
