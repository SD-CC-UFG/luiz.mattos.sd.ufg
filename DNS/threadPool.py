import threading
import queue

MAX_THREADS = 100
THREAD_BLOCK = 10


class tPool:
    def __init__(self, function):
        self.work = function

        self.qtdThreads = 0
        self.freeThreadQueue = queue.Queue()

        self.noThreadsEvent()

    def createThreadBlock(self, function=None):
        if function is None:
            return [threading.Thread(target=self.work) for i in range(THREAD_BLOCK)]

        return [threading.Thread(target=function) for i in range(THREAD_BLOCK)]

    def setConnection(self, connection):
        self.connectionArgs = connection

    def start(self, teste):
        if self.freeThreadQueue.empty():
            if self.qtdThreads < MAX_THREADS:
                self.noThreadsEvent()
            else:
                while self.freeThreadQueue.empty():
                    pass

        print("QTD THREADS: ", self.qtdThreads)

        t = self.freeThreadQueue.get()

        t._args = [t, teste]

        t.start()
        print("threadStarted")

    def noThreadsEvent(self):
        print("Alocou")
        for i in self.createThreadBlock():
            self.freeThreadQueue.put(i)

        self.qtdThreads += THREAD_BLOCK

    def createThread(self, function=None):
        if function is None:
            return threading.Thread(target=self.work)

        return threading.Thread(target=function)

    def addQueue(self, thread):
        self.freeThreadQueue.put(thread)

    # TODO : Implementar um controle de concorrencia na fila de threads
