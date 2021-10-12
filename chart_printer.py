# program for printing charts of "the problem of the pursuit of bodies"
# author: D1N3SHh
# https://github.com/D1N3SHh/chart_printer


import matplotlib.pyplot as plt


def test_set():
    global velocity_a, acceleration_a, velocity_b, acceleration_b, time_interval, base_distance
    velocity_a = 4
    acceleration_a = 9
    velocity_b = 40
    acceleration_b = 5
    time_interval = 10
    base_distance = 6400


def input_parameters():
    global velocity_a, acceleration_a, velocity_b, acceleration_b, time_interval, base_distance
    try:
        velocity_a = float(input("v\u2080A [m/s] = "))
        acceleration_a = float(input("aA [m/s\u00B2] = "))
        velocity_b = float(input("v\u2080B [m/s] = "))
        acceleration_b = float(input("aB [m/s\u00B2] = "))
        time_interval = int(input("Time interval [s] = "))
        base_distance = float(input("Distance between bodies = "))
    except ValueError:
        print("Illegal value. Try again.")
        input_parameters()


def range_of_time():
    global time_interval, time_range
    time_range = [0]
    time = time_interval
    while len(time_range) < 10:
        time_range.append(time)
        time += time_interval


def velocity_in_time():     # V = V0A + at
    global velocity_a, acceleration_a, velocity_b, acceleration_b, time_range

    va_table = [velocity_a]
    vb_table = [velocity_b]
    for t in time_range[1:]:
        va_table.append(float(velocity_a + acceleration_a * t))
        vb_table.append(float(velocity_b + acceleration_b * t))

    print('\nt [s]', time_range)
    print('vA [m/s]', va_table)
    print('vB [m/s]', vb_table)
    plt.ylabel("v [m/s]")
    plt.xlabel("t [s]")
    plt.plot(time_range, va_table, label = 'A')
    plt.plot(time_range, vb_table, label = 'B')
    plt.legend()
    plt.show()


def way_of_bodies_in_time():    # S = V0t + (at^2)/2 
    global velocity_a, acceleration_a, velocity_b, acceleration_b, time_range, base_distance, sa_table, sb_table

    sa_table = [0]
    sb_table = [base_distance]
    for t in time_range[1:]:
        sa_table.append(float(velocity_a * t + (acceleration_a * t*t) / 2))
        sb_table.append(float(velocity_b * t + (acceleration_b * t*t) / 2 + base_distance))

    print('\nt [s]', time_range)
    print('sA [m]', sa_table)
    print('sB [m]', sb_table)
    plt.ylabel("s [m]")
    plt.xlabel("t [s]")
    plt.plot(time_range, sa_table, label = 'A')
    plt.plot(time_range, sb_table, label = 'B')
    plt.legend()
    plt.show()


def distance_in_time():     # l = sB - sA
    global sa_table, sb_table, time_range

    distance_table = []
    for i in range(0, 10):
        distance_table.append(float(sb_table[i] - sa_table[i]))

    print('\nt [s]', time_range)
    print('l [m]', distance_table)
    plt.ylabel("l [m]")
    plt.xlabel("t [s]")
    plt.plot(time_range, distance_table, label = 'l')
    plt.legend()
    plt.show()


if __name__ == "__main__":
    input_parameters()
    # test_set()
    range_of_time()
    velocity_in_time()
    way_of_bodies_in_time()
    distance_in_time()