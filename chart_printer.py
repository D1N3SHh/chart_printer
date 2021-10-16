# program for printing charts for "chase problem"
# author: D1N3SHh
# https://github.com/D1N3SHh/chart_printer


import matplotlib.pyplot as plt


def test_set():
    global velocity_a, acceleration_a, velocity_b, acceleration_b, base_distance, time_range, time_interval
    velocity_a = 4
    acceleration_a = 9
    velocity_b = 40
    acceleration_b = 5
    base_distance = 6400
    time_range = 70
    time_interval = 5


def input_parameters():
    global velocity_a, acceleration_a, velocity_b, acceleration_b, time_range, time_interval, base_distance
    try:
        velocity_a = float(input("v\u2080A [m/s] = "))
        acceleration_a = float(input("aA [m/s\u00B2] = "))
        velocity_b = float(input("v\u2080B [m/s] = "))
        acceleration_b = float(input("aB [m/s\u00B2] = "))
        base_distance = float(input("Distance between bodies [m] = "))
        time_range = int(input("Time range [s] = "))
        time_interval = int(input("Time interval [s] = "))
    except ValueError:
        print("Illegal value. Try again.")
        input_parameters()


def range_of_time():
    global time_range, time_interval, time_scale
    time_scale = [0]
    for time in range(time_interval, time_range + 1, time_interval):
        time_scale.append(time)
        time += time_interval


def velocity_in_time():     # V = V0A + at
    global velocity_a, acceleration_a, velocity_b, acceleration_b, time_scale

    va_table = [velocity_a]
    vb_table = [velocity_b]
    for t in time_scale[1:]:
        va_table.append(float(velocity_a + acceleration_a * t))
        vb_table.append(float(velocity_b + acceleration_b * t))

    # print('\nt [s]', time_scale)
    # print('vA [m/s]', va_table)
    # print('vB [m/s]', vb_table)
    plt.title("velocity in time")
    plt.ylabel("v [m/s]")
    plt.xlabel("t [s]")
    plt.plot(time_scale, va_table, label = 'A')
    plt.plot(time_scale, vb_table, label = 'B')
    plt.ylim(ymin = 0)
    plt.xlim(xmin = 0)
    plt.grid()
    plt.legend()
    plt.show()


def way_of_bodies_in_time():    # S = V0t + (at^2)/2 
    global velocity_a, acceleration_a, velocity_b, acceleration_b, time_scale, base_distance, sa_table, sb_table

    sa_table = [0]
    sb_table = [base_distance]
    for t in time_scale[1:]:
        sa_table.append(float(velocity_a * t + (acceleration_a * t*t) / 2))
        sb_table.append(float(velocity_b * t + (acceleration_b * t*t) / 2 + base_distance))

    # print('\nt [s]', time_scale)
    # print('sA [m]', sa_table)
    # print('sB [m]', sb_table)
    plt.title("way of bodies in time")
    plt.ylabel("s [m]")
    plt.xlabel("t [s]")
    plt.plot(time_scale, sa_table, label = 'A')
    plt.plot(time_scale, sb_table, label = 'B')
    plt.ylim(ymin = 0)
    plt.xlim(xmin = 0)
    plt.grid()
    plt.legend()
    plt.show()


def distance_in_time():     # d = sB - sA
    global sa_table, sb_table, time_scale

    distance_table = []
    for i in range(0, len(time_scale)):
        distance_table.append(float(sb_table[i] - sa_table[i]))

    # print('\nt [s]', time_scale)
    # print('d [m]', distance_table)
    plt.title("distance in time")
    plt.ylabel("d [m]")
    plt.xlabel("t [s]")
    plt.plot(time_scale, distance_table, label = 'l')
    plt.ylim(ymin = 0)
    plt.xlim(xmin = 0)
    plt.grid()
    plt.legend()
    plt.show()


if __name__ == "__main__":
    input_parameters()
    # test_set()
    range_of_time()
    velocity_in_time()
    way_of_bodies_in_time()
    distance_in_time()