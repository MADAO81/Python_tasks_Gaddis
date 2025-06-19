# This program shows a simple bar chart
import matplotlib.pyplot as plt


def main():
    # Create lists with coords X of left side for each bar
    left_edges = [0, 10, 20, 30, 40]

    # Create list with heights of each bar
    heights = [100, 200, 300, 400, 500]

    # Create value for width of bar
    bar_width = 10

    # Build bar chart
    plt.bar(left_edges, heights, bar_width, color=('r', 'm', 'b', 'g', 'y'))

    # Add title
    plt.title("Sales by year")

    # Add descriptive marks to the axis
    plt.xlabel("Year")
    plt.ylabel("Sales volume")

    # Customize tick marks
    plt.xticks([5, 15, 25, 35, 45], ['2016', '2017', '2018', '2019', '2020'])

    plt.yticks([0, 100, 200, 300, 400, 500], ['$0m', '$1m', '$2m', '$3m', '$4m', '$5m'])

    # Show linear graph
    plt.show()


# Call main function
main()
