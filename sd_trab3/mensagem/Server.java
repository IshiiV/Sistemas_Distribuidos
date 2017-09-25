import java.rmi.*;
import java.util.ArrayList;
import java.rmi.registry.Registry;
import java.rmi.registry.LocateRegistry;
import java.rmi.server.UnicastRemoteObject;

public class Server implements Serverremote {

    private static final long serialVersionUID = 1L;
    private ArrayList<Clientremote> chatClients = new ArrayList<Clientremote>();
   
    public void registerChatClient(Clientremote chatClient) throws RemoteException {
        this.chatClients.add(chatClient);
    }
    public void broadcastMessage(String message) throws RemoteException {
        int i = 0;
        while (i < chatClients.size()) {
            chatClients.get(i++).retrieveMessage(message);
        }
    }

    public static void main(String[] args){
       
        try {
             Server obj = new Server();
        Serverremote stub = (Serverremote) UnicastRemoteObject.exportObject(obj, 0);

        Registry registry = LocateRegistry.getRegistry();
        registry.rebind("Serverremote", stub);

            System.err.println("Server ready");
        } catch (Exception e) {
            System.err.println("Server exception: " + e.toString());
            e.printStackTrace();
        }
    }
}