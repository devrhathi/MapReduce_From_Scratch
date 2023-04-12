import socketserver
import os
from master_handler import handler
import subprocess


class Master:
    PORT = 3000
    NUM_OF_WORKERS=1
    WORKER_BASE_PORT_NUMBER=8000

    def __init__(self):
        curr_dir = os.path.dirname(__file__)
        parent_dir = os.path.dirname(curr_dir)

        with open(os.path.join(curr_dir, 'config.txt')) as f:
            self.NUM_OF_WORKERS = int(f.readline().strip().split("=")[1])
            self.WORKER_BASE_PORT_NUMBER = int(f.readline().strip().split("=")[1])

        for i in range(self.WORKER_BASE_PORT_NUMBER, self.WORKER_BASE_PORT_NUMBER+self.NUM_OF_WORKERS):
            print(i)
            list_of_workers.append(subprocess.Popen(["python", f"{os.path.join(parent_dir, 'Worker', 'worker.py')}", f"{i}"], shell=True))

        metadata_path = os.path.join(parent_dir, 'metadata')
        if(not os.path.exists(metadata_path)):
            os.mkdir(os.path.join(parent_dir,'metadata'))

        with socketserver.TCPServer(("", self.PORT), handler) as httpd:
            print("serving master server at port", self.PORT)
            httpd.serve_forever()
        

list_of_workers = []
instance_master = Master()
