def main():
    # Pass a character value to the function show_mamal_info 
    show_mammal_info('I am a sequence of characters')
    
# The show_mammal info function accepts an object 
# as an argument, it calls its own methods
# show_species and make_sound methods.
def show_mammal_info(creature):
    creature.show_species()
    creature.make_sound()
    
# Call main function
main()