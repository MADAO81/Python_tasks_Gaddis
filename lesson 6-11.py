# This program saves a sequence of video clip durations
# in a video_times.txt file.
from os import close


def main():
    # Get the number of video clips in the project.
    num_videos = int(input("How many videos do you have in project: "))

    # Open file to record video clip durations.
    video_file = open("video_times.txt", "w")

    # Get the duration of each video clip and write it to a file.
    print("Enter the duration of each video clip in seconds.")
    for count in range(1, num_videos + 1):
        run_time = float(input("Video №" + str(count) + ":"))
        video_file.write(str(run_time) + "\n")

    # Close the file
    video_file.close()
    print("Video saved to video_times.txt")

# Call main function
main()
