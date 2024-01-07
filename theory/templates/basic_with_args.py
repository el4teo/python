import sys, getopt


if __name__ == '__main__':
    argv = sys.argv[1:]
    opts, args = getopt.getopt(argv,"ht",[])
    for opt, arg in opts:
      if opt == '-h':
        # Print help menu info ...
        print ('basic_with_args.py     // Call with no arguments for BlaBlaBla')
        print ('basic_with_args.py -t  // -t : BlaBlaBla')
        sys.exit()