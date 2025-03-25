# This program shows simple pie chart
import matplotlib.pyplot as plt


def main():
    # create sales list
    sales = [100, 400, 300, 600]

    # create list of marks
    slice_labels = ['1-st quarter', '2-nd quarter', '3-rd quarter', '4-th quarter']

    # create a pie chart
    plt.pie(sales, labels=slice_labels, colors=('r', 'g', 'b', 'y'))

    # add header
    plt.title("Sales by quarter")

    # show pie chart
    plt.show()


# Call main function
main()
