from CoverCost import CoverCost


def get_measurement(tile_object):
    """
    Requests conversion method to use  metric or imperial
    :param tile_object: object
    :return: none
    """
    while True:
        try:
            measure = input("Which type of measurement? (metric or imperial) ").lower()
            if measure == 'metric':
                tile_object.set_metric()
                break
            elif measure == 'imperial':
                tile_object.set_imperial()
                break
            else:
                print(f"{measure} does not match metric or imperial, please try again")
                continue

        except:
            print('Invalid Input: please only enter numbers for the work area! ')
            continue


def get_work_area(tile_object):
    """
    Requests work area dimension
    :param tile_object: object
    :return: none
    """
    while True:
        try:
            tile_object.clear_console()
            if tile_object.is_metric():
                tile_object.add_width_int(int(input("What is the work areas width in meters? ")))
                tile_object.add_width_fact(int(input("And now the remaining width in centimeters? ")))
                tile_object.add_height_int(int(input("What is the work areas height in meters? ")))
                tile_object.add_height_fact(int(input("And now the remaining height in centimeters? ")))
            else:
                tile_object.add_width_int(int(input("What is the work areas width in feet? ")))
                tile_object.add_width_fact(int(input("And now the remaining width in inches? ")))
                tile_object.add_height_int(int(input("What is the work areas height in feet? ")))
                tile_object.add_height_fact(int(input("And now the remaining height in inches? ")))
            break
        except ValueError:
            print('Invalid Input: please only enter whole numbers for the work area! ')
            continue


def get_tile_box_area(tile_object):
    """
    Requests tile size, tile count and price per box
    :param tile_object: object
    :return: none
    """
    while True:
        tile_object.clear_console()
        try:
            if tile_object.is_metric():
                tile_object.add_tile_width(int(input("What is the tile width in millimeters? ")))
                tile_object.add_tile_height(int(input("What is the tile height in millimeters? ")))
            else:

                while True:
                    try:
                        tile_wide = float(input(
                            "What is the tile width in inches? for fraction of an inch use .25 = quarter, .5 = half, .75 = 3 quarters "))

                        tile_wide_frac = tile_wide - int(tile_wide)

                        if tile_wide_frac in [0.0, 0.25, 0.5, 0.75]:
                            tile_object.add_tile_width(tile_wide)
                            break
                        else:
                            print("Invalid Fraction: use .25 = quarter, .5 = half, .75 = 3 quarters")
                            continue
                    except:
                        print("Something went wrong, please try again")
                        continue

                while True:

                    try:
                        tile_high = float(input(
                            "What is the tile height in inches? for fraction of an inch use .25 = quarter, .5 = half, .75 = 3 quarters "))

                        tile_high_frac = tile_high - int(tile_high)

                        if tile_high_frac in [0.0, 0.25, 0.5, 0.75]:
                            tile_object.add_tile_height(tile_high)
                            break
                        else:
                            print("Invalid Fraction: use .25 = quarter, .5 = half, .75 = 3 quarters")
                            continue
                    except:
                        print("Something went wrong, please try again")
                        continue

            tile_object.box_tile_count(int(input("How many Tiles are in the box?  ")))
            tile_object.price_per_box(float(input("How much does a box cost?  ")))
            break

        except ValueError:
            print('Invalid Input: please only enter numbers for the work area! ')
            continue


def show_result(tile_object):
    """
    Displays Calculation data
    :param tile_object: object
    :return: none
    """
    tile_object.clear_console()
    print("Tile Calculation\n")
    if tile_object.is_metric():
        print(
            f"Your work area is {tile_object.width_int}m {tile_object.width_fact}cm X {tile_object.height_int}m {tile_object.height_fact}cm")
        print(
            f"Tile size {tile_object.tile_width}mm X {tile_object.tile_height}mm with {tile_object.tile_count} tiles per box")
    else:
        print(
            f"Your work area is {tile_object.width_int}ft {tile_object.width_fact}in X {tile_object.height_int}ft {tile_object.height_fact}in")
        print(
            f"Tile size {tile_object.tile_width}in X {tile_object.tile_height}in with {tile_object.tile_count} tiles per box")
    print(f"You need {tile_object.boxes_needed()} boxes at a cost of {tile_object.box_price:.2f} per box\n")
    print(f"The Total : {tile_object.cal_total():.2f}\n\n")


def get_tile_price():
    """
    Tile Price Calculation program
    :return: none
    """
    tile_cost = CoverCost()

    get_measurement(tile_cost)

    get_work_area(tile_cost)

    get_tile_box_area(tile_cost)

    show_result(tile_cost)

    while True:
        replay = input("Do you want to get a new calculation? y/n").lower()

        if replay == 'y':
            get_tile_price()
            break
        elif replay == 'n':
            break
        else:
            print("Invalid Input: y for yes or n for no is desired  (y or n)")
            continue

    print("\n\n\tThank you for using our tile price calculator\n\n\tCall back soon")


# Runs Tile Price Calculator
get_tile_price()
