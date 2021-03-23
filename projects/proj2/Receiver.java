package lab1.cs488.pace.edu;
import java.io.*;
import java.net.DatagramPacket;
import java.net.DatagramSocket;
import java.net.InetAddress;
import java.net.SocketTimeoutException;
import java.net.UnknownHostException;

public class Receiver {
	final static int ownPort = 8888;
	final static int targetPort = 7777;
	static InetAddress host = null;
	static{
		try {
			host = InetAddress.getByName("localhost");
		} catch (UnknownHostException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
	}

	public static void main(String[] args) throws IOException, InterruptedException {
	        File file = new File("./Resource/copy_1.jpg");
	        FileOutputStream fis = new FileOutputStream(file);
			
	        fis.close();
		}
}
