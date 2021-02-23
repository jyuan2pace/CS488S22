# Python3.7+
import socket

HOST, PORT = '', 1234

listen_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
listen_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
listen_socket.bind((HOST, PORT))
listen_socket.listen(1)
print(f'Serving HTTP on port {PORT} ...')
while True:
    client_connection, client_address = listen_socket.accept()
    request_data = client_connection.recv(1024)
    # Print formatted request data a la 'curl -v'
    print(''.join(
        f'< {line}\n' for line in request_data.splitlines()
    ))
    http_response = b"""\
HTTP/1.1 200 OK

<!DOCTYPE html>    
<html>    
<head>    
    <title>Login Form</title>    
</head>    
<body>    
    <h2>Login Page</h2><br>    
    <div class="login">    
    <form id="login" method="post" action="?">    
        <label><b>User Name     
        </b>    
        </label>    
        <input type="text" name="Uname" id="Uname" placeholder="Username">    
        <br><br>    
        <label><b>Password     
        </b>    
        </label>    
        <input type="Password" name="Pass" id="Pass" placeholder="Password">    
        <br><br>    
        <button type="submit" name="log" id="log" value="submitted"> Submit </button>       
        <br><br>    
    </form>     
</div>    
</body>    
</html>     
"""
    client_connection.sendall(http_response)
    client_connection.close()
