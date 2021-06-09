# Python3.7+
import socket
import json

HOST, PORT = '', 1600

def parse_request(text):
    request_line = text.splitlines()[0]
    request_line = request_line.rstrip(b'\r\n')
    requests = request_line.split()
    params_dict = {} 
    if requests[0] == b'POST':
        request_body = text.splitlines()[-1]
        request_body = request_body.rstrip(b'\r\n')
        params_list = request_body.split(b'&')
        for pair in params_list:
            print(pair)
            (key, value)=pair.split(b'=')
            params_dict[key]=value
    # Break down the request line into components
    requests = requests + [params_dict]
    return requests

def handle_login(params_dict):
    with open("userdb.json", 'r') as result_f:
        creds=json.load(result_f)
        username=params_dict[b'Uname']
        userpasswd=params_dict[b'Pass']
        if creds[username.decode("utf-8")] == userpasswd.decode("utf-8"):
            return True
        else:
            return False

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

    requests = parse_request(request_data)
    print(requests)
    if requests[0] == b'GET':
        http_response = b"""\
HTTP/1.1 200 OK

<!DOCTYPE html>    
<html>    
<head>    
    <title>Login Form</title>    
    <link rel="icon" href="data:,">
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
    else:
        if handle_login(requests[3]):
         http_response = b"""\
HTTP/1.1 200 OK

     SUCCESS
"""
        else:
         http_response = b"""\
HTTP/1.1 200 OK

     FAILED TO LOG IN
"""

    client_connection.sendall(http_response)
    client_connection.close()
