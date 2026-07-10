def print_logo(thickness):
    c = 'H'

    # Top Cone
    for i in range(thickness):
        print((c * (2 * i + 1)).center(thickness * 2 - 1))

    # Top Pillars
    for i in range(thickness + 1):
        print((c * thickness).center(thickness * 2) +
              (c * thickness).center(thickness * 6))

    # Middle Belt
    for i in range((thickness + 1) // 2):
        print((c * thickness * 5).center(thickness * 6))

    # Bottom Pillars
    for i in range(thickness + 1):
        print((c * thickness).center(thickness * 2) +
              (c * thickness).center(thickness * 6))

    # Bottom Cone
    for i in range(thickness):
        print(((c * ((thickness - i) * 2 - 1)).center(thickness * 2)).rjust(thickness * 6))