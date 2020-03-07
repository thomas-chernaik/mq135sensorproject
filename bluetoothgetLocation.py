import bluetooth
def getLocation():

    server_sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
    sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
    server_sock.bind(("", bluetooth.PORT_ANY))

    server_sock.listen(10)

    port = server_sock.getsockname()[1]

    uuid = "94f39d29-7d6d-437d-973b-fba39e49d4ee"

    bluetooth.advertise_service(server_sock, "SampleServer", service_id=uuid,
                                service_classes=[uuid, bluetooth.SERIAL_PORT_CLASS],
                                profiles=[bluetooth.SERIAL_PORT_PROFILE],
                                # protocols=[bluetooth.OBEX_UUID]
                                )

    print("Waiting for connection on RFCOMM channel", port)

    client_sock, client_info = server_sock.accept()
    #sock.connect(client_info)

    print("Accepted connection from", client_info)

    try:
        while True:
            data = client_sock.recv(1024)
            if data:
                break
        txtdata = data.decode("utf-8")
        txtbits = txtdata.split(" ")
        if txtbits[0] == "LOC":
            print("Received", txtdata)

    except OSError:
        pass

    print("Disconnected.")

    client_sock.close()
    server_sock.close()
    print("All done.")
    return txtbits[1].replace("\r","").replace("\n","")

file = "location.txt"

with open(file, "w+") as myfile:
    myfile.write("Barnet")

while True:
    location = getLocation()
    with open(file, "w+") as myfile:
        myfile.write(location)