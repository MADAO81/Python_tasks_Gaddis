# This program shows simple pie chart
import matplotlib.pyplot as plt


def main():
    # Create values list
    values = [20, 60, 80, 40]

    # Create pie chart
    plt.pie(values)

    # Show pie chart
    plt.show()


# Call main function
main()
