import java.rmi.Remote;
import java.rmi.RemoteException;

public interface Serverremote extends Remote{
    void registerChatClient(Clientremote chatClient) throws RemoteException;
    void broadcastMessage(String message) throws RemoteException;
}