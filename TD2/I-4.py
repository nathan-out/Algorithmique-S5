def sequence():
    """Prend en entré n entiers positifs, -1 étant le marqueur de fin"""

    tot = 0
    tot_number = 0
    min_value, max_value = None, None
    finish = False
    while not finish:
        input_value = int(input("Enter positive int or -1 to stop: "))
        # condition de fin
        if input_value == -1:
            finish = True
        else:
            # Premier tour de boucle
            if min_value == None:
                min_value, max_value = input_value, input_value
            # Si l'input est le nouveau min
            elif input_value < min_value:
                min_value = input_value
            # Si l'input est le nouveau max
            elif input_value > max_value:
                max_value = input_value

            tot += input_value
            tot_number += 1

    return f"average : {tot / tot_number}\nmin : {min_value}\nmax : {max_value}"


if __name__ == "__main__":
    print(sequence())
