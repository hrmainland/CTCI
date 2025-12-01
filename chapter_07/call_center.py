from dataclasses import dataclass
from random import random

from enum import Enum


class WorkerType(Enum):
    RESPONDANT = 1
    MANAGER = 2
    DIRECTOR = 3


class WorkerFactory:
    @staticmethod
    def createWorker(worker_type: WorkerType):
        if worker_type == WorkerType.DIRECTOR:
            return Director()
        if worker_type == WorkerType.MANAGER:
            return Manager()
        if worker_type == WorkerType.RESPONDANT:
            return Respondant()


class Worker:
    def answer_call(self):
        print("How can I help you?")

    def is_available(self):
        if random() < 0.4:
            return True
        return False


class Respondant(Worker):
    def answer_call(self):
        print("This is a respondant speaking")
        super().answer_call()


class Manager(Worker):
    def answer_call(self):
        print("This is a manager speaking")
        super().answer_call()


class Director(Worker):
    def answer_call(self):

        print("This is a director speaking")
        super().answer_call()


class CallCenter:
    def __init__(self, num_respondants, num_managers, num_directors):
        self.respondants = [
            WorkerFactory.createWorker(WorkerType.RESPONDANT)
            for _ in range(num_respondants)
        ]
        self.managers = [
            WorkerFactory.createWorker(WorkerType.MANAGER) for _ in range(num_managers)
        ]
        self.directors = [
            WorkerFactory.createWorker(WorkerType.DIRECTOR)
            for _ in range(num_directors)
        ]
        self.call_queue = []

    def take_call(self):
        for worker in self.respondants + self.managers + self.directors:
            if worker.is_available():
                worker.answer_call()
                return
        self.call_queue.append("call")


cc = CallCenter(2, 3, 4)
cc.take_call()
