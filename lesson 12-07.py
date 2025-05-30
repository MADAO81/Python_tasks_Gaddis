# This program simulates the Hanoi Towers puzzle.

def main():
    # Set some initial values.
    num_discs = 3 
    from_peg = 1 
    to_peg = 3 
    temp_peg = 2 
    
    # Solve the puzzle.
    move_discs(num_discs, from_peg, to_peg, temp_peg)
    print("All the discs have been moved.")
    
# The moveDiscs function shows the process of moving the rings in the Hanoi Towers puzzle.
# Function Parameters:
# num: the number of rings to move.
# from_peg: the rod from which to take the ring.
# to_peg: the rod to put the ring on.
# temp_peg: temporary rod 
def move_discs(num, from_peg, to_peg, temp_peg):
    if num > 0:
        move_discs(num-1, from_peg, temp_peg, to_peg)
        print("Rearrange the disc from", from_peg, " to the ", to_peg)
        move_discs(num-1, temp_peg, to_peg, from_peg)
        
# call main function
main()