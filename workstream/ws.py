import fire

def hello(name):
    print("hello function")
    print("Hi " + name)

def _main():
    print("main function")
    fire.Fire()

if __name__ == '__main__':
    print("name main")
    _main()
