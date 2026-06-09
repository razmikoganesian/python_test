from multiprocessing import Process, Queue, Value


def prepare_tea(queue):
    queue.put("Masala tea is ready!")


counter = Value("i", 0)

if __name__ == "__main__":
    queue = Queue()
    p = Process(target=prepare_tea, args=(queue,))
    p.start()
    p.join()
    print(queue.get())
