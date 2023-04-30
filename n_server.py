import socket
from threading import Thread
import current_time
from datetime import datetime


class road_server(object):

    def __init__(self) -> None:
        self.buffersize = 1024
        self.all_cars = {}
        self.time_data = {}
        


    def build_socket(self):
        self.server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.server.bind(("localhost",6065))
        self.server.listen()
        print("waiting for the connection........")


    def multy_cars(self,car):
        while True:
            try:
                msg = car.recv(self.buffersize)
                for c in self.all_cars:
                    c.send(msg)
            except:
                for c in self.all_cars:
                    if c != car:
                        c.send(f'{self.all_cars[car]} has left the road'.encode())
                del self.all_cars[car]
                car.close()
                break
             

    def connections(self):

        while True:
            car, address = self.server.accept()
            print(f'{car} connected to the server')
            name = car.recv(self.buffersize).decode()
            time = current_time.print_time()
            self.all_cars[car] = name

            for c in self.all_cars:
                if c != car:
                    c.send(f'{name} has joined the road on {time}'.encode())
            
            thread = Thread(target = self.multy_cars, args = (car,))
            thread.start()


def main():
    server = road_server()
    server.build_socket()
    server.connections()

if __name__ == "__main__":
    main()


