import argparse

def calculate_salary(time, rate):
    return time * rate

#run:
# python 7.py -t 200 -r 1000
if __name__ == "__main__":
    ap = argparse.ArgumentParser()

    ap.add_argument("-t", "--time", help="Employee's work time in current month", required=True)
    ap.add_argument("-r", "--rate", help="Employee's rate per hour", required=True)

    args = vars(ap.parse_args())
    print(calculate_salary(int(args['time']),  int(args['rate'])))
