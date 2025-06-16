# This program demonstrates 
# the functional version of the range_sum function
def pipe(data, *fseq):
    for fn in fseq:
        data = fn(data)
    return data

def main():
    # Algorithm 
    def range_sum(data):  
        seq, params = data
        fn = lambda start, end: 0 if start > end \
                                  else seq[start] + fn(start + 1, end)
        return fn(*params)  
        
    # data input
    def indata():
        seq = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        params = (2,5) # params are the start and end parameters.
        return seq, params 
        
    # data output 
    def outdata():
        def f(data):
            msg = "The sum of the values from position 2 to position 5 is "
            print(msg, format(data), sep = "")
        return f 

    # Pipeline (functional core)
    pipe(indata(), range_sum, outdata())
    
# call main function
main()
    