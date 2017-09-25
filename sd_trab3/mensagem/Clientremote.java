import java.rmi.Remote;
import java.rmi.RemoteException;

public interface Clientremote extends Remote{
    void retrieveMessage(String message) throws RemoteException;
}