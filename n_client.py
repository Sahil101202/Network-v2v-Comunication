import socket
from threading import Thread
from datetime import datetime
import current_time


class car(object):

    def __init__(self) -> None:
        self.buffersize = 1024
        self.name = input("write your name : ")
        self.time = []
        self.iterations = 0
        self.time_diff = []
        
    

    def build_car_socket(self):
        self.car = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.car.connect(("0.0.0.0",6065))
        self.car.send(self.name.encode())
        
        

    def send_message(self):
        while True:
            data = f'{self.name} : {input("")}'
            time = current_time.print_time()[11:24]
            self.time.append(time)
            self.car.send(data.encode())
            


    def receive(self):
        while True:
            try:
                data = self.car.recv(self.buffersize).decode()
                print(data)
                if self.time:
                    time2 = current_time.print_time()[11:24]
                    self.time.append(time2)
                    sec = current_time.time_differece(self.time)
                    self.time_diff.append(float(sec))
                    self.iterations += 1
                    print(self.iterations)
                    print(self.time_diff)
                    self.time.clear()
                    
            except:
                self.car.close()
                break


    def run_forever(self):
        send_thread = Thread(target = self.send_message)
        receive_thread = Thread(target = self.receive)
        send_thread.start()
        receive_thread.start()


    


def main():
   peer = car()
   peer.build_car_socket()
   peer.run_forever()

if __name__ == "__main__":
    main() 




