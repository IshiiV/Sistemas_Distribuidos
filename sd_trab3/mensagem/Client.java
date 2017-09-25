import java.rmi.*;
import java.rmi.server.UnicastRemoteObject;
import java.rmi.NotBoundException;
import java.rmi.RemoteException;
import java.net.MalformedURLException;
import java.util.Scanner;

public class Client extends UnicastRemoteObject implements Clientremote, Runnable{


    private static final long serialVersionUID = 1L;
    private Serverremote chatServer;
    private String name = null;
    protected Client(String name, Serverremote chatServer) throws RemoteException {
        this.name = name;
        this.chatServer = chatServer;
        chatServer.registerChatClient(this);
    }
    public void retrieveMessage(String message) throws RemoteException{
        System.out.println(message);
    }
    public void run() {
        Scanner scanner = new Scanner(System.in);
        String message;
        while(true){
            message = scanner.nextLine();
            try {
                chatServer.broadcastMessage(name + " : "+message);
            } catch (RemoteException e){
                e.printStackTrace();
            }
        }
    }

    public static void main(String[] args) throws MalformedURLException, RemoteException, NotBoundException{
        String chatServerURL = "rmi://localhost/Serverremote";
        Serverremote chatServer = (Serverremote) Naming.lookup(chatServerURL);
        new Thread(new Client(args[0], chatServer)).start();
    }
}