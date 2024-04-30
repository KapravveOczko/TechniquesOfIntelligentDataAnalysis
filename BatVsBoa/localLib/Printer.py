import matplotlib.pyplot as plt


def print_bat_vs_boa(bat_x, bat_y, boa_x, boa_y, boa_levy_x, boa_levy_y):
    plt.figure(figsize=(10, 6))

    plt.plot(bat_x, bat_y, label='BAT', color='blue')
    plt.plot(boa_x, boa_y, label='BOA', color='red')
    plt.plot(boa_levy_x, boa_levy_y, label='BOA levy', color='green')

    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('BAT and BOA comparison')
    plt.legend()
    plt.grid(True)
    plt.show()
