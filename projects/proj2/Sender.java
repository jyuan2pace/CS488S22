package lab1.cs488.pace.edu;

import java.io.*;
import java.net.DatagramPacket;
import java.net.DatagramSocket;
import java.net.InetAddress;
import java.net.Socket;
import java.net.UnknownHostException;
public class Sender {
	final static int ownPort = 7777;
	final static int targetPort = 8888;
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
	        File file = new File("./Resource/1.jpg");
	        FileInputStream fis = new FileInputStream(file);
			
	        byte[] data = new byte[1024];
	        //Socket socket = new Socket(host.getHostAddress(),targetPort);
	        DatagramSocket datagramSocket = new DatagramSocket(ownPort);
	        System.out.println("Sender: connection built. about to transfer.");
	        while(fis.read(data) != -1) 
	        {
	        	//socket.getOutputStream().write(data);
	        	DatagramPacket packet = new DatagramPacket(data, data.length, host, targetPort);
	        	datagramSocket.send(packet);
	        }
	        System.out.println("Sender: finished.");
	        datagramSocket.close();
	        
	        
	        fis.close();
	}
		
	}

