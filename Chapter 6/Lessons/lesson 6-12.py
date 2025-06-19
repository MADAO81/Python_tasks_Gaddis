# This program reads values from the video_times.txt file and calculates their sum.

def main():
    # Open file video_times.txt to read
    video_file = open("video_times.txt", "r")

    # Initialize storage with value 0.0
    total = 0.0

    # Initialize a variable to count video clips.
    count = 0

    print("Duration of all video clips:")

    # Get values from file and sum them.
    for line in video_file:
        # Convert a string to a floating point number.
        run_time = float(line)

        # Add 1 to variable "count"
        count += 1

        # Show duration
        print("Video № ", count, ": ", run_time, sep="")

        # Add duration to total
        total += run_time

    # Close the file
    video_file.close()

    # Show total duration
    print(f"Total duration is {total:.2f}  seconds")

# Call main function
main()

