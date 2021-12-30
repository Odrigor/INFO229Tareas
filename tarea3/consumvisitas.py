#!/usr/bin/env python
import pika, sys, os
import time
import re
import pageviewapi.period

def wikipediaViews(wword):
    pageviewapi.period.sum_last('es.wikipedia', wword, last=30,
                            access='all-access', agent='all-agents')

    views = pageviewapi.period.avg_last('es.wikipedia', wword, last=30)
    print(" %r visitas en los últimos 30 días." % views)

def main():
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
    channel = connection.channel()

    channel.queue_declare(queue='hello')

    def callback(ch, method, properties, body):
        print(" [x] Received %r" % body.decode())
        word = body.decode()
        wword = re.search('\(([^)]+)', word).group(1)
        wikipediaViews(wword)
        print(" [x] Done")

    channel.basic_consume(queue='hello', on_message_callback=callback, auto_ack=True)

    print(' [*] Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()
    
if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Interrupted')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)
