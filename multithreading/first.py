import threading
import requests
import time


def print_cube(num):
    "function to print cube of given number"
    print("cube : {0} calculation with thread name: {1}".format((num * num * num), threading.current_thread().name))


def print_square(num):
    "function to print square of given number"
    print("square : {} calculation with thread name: {}".format((num * num), threading.current_thread().name ))


def api_response(url):
    r = requests.get(url)
    r.json()


if __name__ == "__main__":

    # print name of main thread
    print("Main thread name: {}".format(threading.main_thread().name))

    t1 = threading.Thread(target=print_cube, name='t1', args=(10,))
    t2 = threading.Thread(target=print_square, name='t2', args=(10,))

    t1.start()
    t2.start()

    # wait until all threads finish
    t1.join()
    t2.join()

    url = "https://www.blinkhealth.com/api/medications/formulations?c_platform=web&c_app=rx&slug=promethazine"
    start_time = time.time()
    t3 = threading.Thread(target=api_response, name='t3', args=(url, ))
    t4 = threading.Thread(target=api_response, name='t4', args=(url, ))

    t3.start()
    t4.start()

    # wait until all threads finish
    t3.join()
    t4.join()
    print(1, time.time() - start_time)

    start_time = time.time()

    api_response(url)
    api_response(url)

    print(2, time.time() - start_time)
    print("Done !")
