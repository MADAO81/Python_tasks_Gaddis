# This program shows a simple bar chart
import matplotlib.pyplot as plt

def main():
	# Create lists with coords X of left side for each bar
	left_edges = [0, 10, 20, 30, 40]
	
	# Create list with heights of each bar 
	heights = [100, 200, 300, 400, 500]
	
	# Create value for width of bar 
	bar_width = 5 
	
	# Build bar chart
	plt.bar(left_edges, heights, bar_width, color =('r','m','b','g','y'))

	# Show linear graph
	plt.show()

# Call main function
main()