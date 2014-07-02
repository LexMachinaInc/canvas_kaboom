from celery import Celery
from celery.canvas import chord
import sys

celery = Celery()

@celery.task
def produce_n(n):
    print 'Producing', n
    return n


@celery.task
def collect_total(ns):
    print 'Collecting', ns
    return sum(ns)


@celery.task
def print_result(total):
    print 'Resulted', total
    return total


def fails():
    return (
        chord([
            produce_n.s(n + 1) for n in range(10)
        ])(
            collect_total.s() |\
            print_result.s()
        )
    )


def works():
    return (
        chord([
            produce_n.s(n + 1) for n in range(10)
        ])(
            collect_total.s()
        )
    )


def main():
    celery.start()

if __name__ == '__main__':
    main()
