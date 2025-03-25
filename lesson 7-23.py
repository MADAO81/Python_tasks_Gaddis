# This program shows a simple linear graph
import matplotlib.pyplot as plt

def main():
	# Create lists to X,Y coordinates and for every data point.
	x_coords = [0, 1, 2, 3, 4]
	y_coords = [0, 3, 1, 5, 2]

	# Build the linear graph
	plt.plot(x_coords, y_coords, marker = "o")

	# Add title
	plt.title("Sales by year")

	# Add descriptive marks to the axises 
	plt.xlabel("Year")
	plt.ylabel("Sales")

	# Customize tick marks
    plt.xticks([0, 1, 2, 3, 4], ['2016', '2017', '2018', '2019', '2020'])
    plt.yticks([0, 1, 2, 3, 4, 5], ['$0m', '$1m', '$2m', '$3m', '$4m', '$5m'])
    
	# Add grid
	plt.grid(True)

	# Show linear graph
	plt.show()

# Call main function
main()