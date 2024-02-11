import datetime


def get_current_time():
    current_time = datetime.datetime.now().time()
    return current_time


if __name__ == "__main__":
    current_time = get_current_time()
    print(f"Current time is: {current_time}")
