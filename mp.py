import multiprocessing
import os

def whoami(what):
    print("Process %s says: %s" % (os.getpid(), what))

print('Name: ', __name__)
def main():
    whoami("I'm the main program")
    for n in range(1):
        p = multiprocessing.Process(target=whoami, name="Subprocess "+str(n), args=("I'm function %s" % n,))
        p.start()

if __name__ == "__main__":
    print('Inside IF; Name: ', __name__)
    main()