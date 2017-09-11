import socketserver, threading, time
import sys

class UDPHandler(socketserver.BaseRequestHandler):  #Classe usada para receber a mensagem do usuário e no final envia-lá de volta

    def handle(self):
        data = self.request[0].strip()
        socket = self.request[1]
        current_thread = threading.current_thread()
        print("{}: client: {}, wrote: {}".format(current_thread.name, self.client_address, data.decode('utf-8')))
        socket.sendto(data[::-1], self.client_address)      #Na hora de enviar para o cliente, o servidor já inverte a string

if __name__ == "__main__":
    HOST = "0.0.0.0"
    PORT_str = " ".join(sys.argv[1:])
    PORT = int(PORT_str)

    print("Servidor começou em {} port {}".format(HOST, PORT))

    server = socketserver.UDPServer((HOST, PORT), UDPHandler)

    server_thread = threading.Thread(target=server.serve_forever)
    server_thread.daemon = True

    try:
        #Servidor tratando de threads concorrentes
        for i in range(5):
            server_thread = threading.Thread(target=server.serve_forever)
            server_thread.daemon = True
            server_thread.start()

        while True: time.sleep(100)     #Servidor fica funcionando até 100s
    except (KeyboardInterrupt, SystemExit):
        server.shutdown()
        server.server_close()
        exit()