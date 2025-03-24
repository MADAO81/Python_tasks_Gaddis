# This program shows a simple linear graph
import matplotlib.pyplot as plt

def main():
	# Create lists to X,Y coordinates and for every data point.
	x_coords = [0, 1, 2, 3, 4]
	y_coords = [0, 3, 1, 5, 2]

	# Build the linear graph
	plt.plot(x_coords, y_coords)

	# Add title
	plt.title("Data sample")

	# Add descriptive marks to the axises 
	plt.xlabel("This is X-axis")
	plt.ylabel("This is Y-axis")

	# Set limits to the axises
	plt.xlim(xmin = -1, xmax = 10)
	plt.ylim(ymin = -1, ymax = 6)

	# Add grid
	plt.grid(True)

	# Show linear graph
	plt.show()

# Call main function
main()