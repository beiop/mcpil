def chechubben(server):
    import socket, struct, time, random
    timeout = 5
    try: #if len(sys.argv) != 2: print("Usage: mcpi_pinger.py [server url/IP]");exit()

        if ":" in server:
            targetServer = (server.split(":")[0], int(server.split(":")[1]) )
        else:
            targetServer = (server, 19132)

        print(f"\nPinging `{targetServer}` now:")

        magicCrap = b'\x00\xff\xff\x00\xfe\xfe\xfe\xfe\xfd\xfd\xfd\xfd\x124Vx'
        pingPacket = b'\x02' + struct.pack(">q", random.randint(5, 20) ) + magicCrap

        udp_socket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
        udp_socket.settimeout(timeout)
        udp_socket.sendto(pingPacket, targetServer)
        data = udp_socket.recvfrom(2048)[0]
        len_val = ord( data[34:34 + 1] )
        print(f"Server name: '{ data[35:35 + len_val].decode('utf-8').split(';')[2] }'")
    except socket.timeout:
        print("Address " + server + " did not respond in " + str(timeout) + " second(s)")
    except Exception as e:
        print(f"You done did messed up bruv. This error occured: {e}")
    finally:
        udp_socket.close()

if __name__ == "__main__":
    chechubben("mcpi.izor.in")
    chechubben("retrocraft.bounceme.net")  #eventually I'll replace this with some functionality : that when running this in the terminal, it will ask for some input, like the original did. I'm reallising now that I'm the reason why it no longer has this functionality and that I forgot to enable word wrap. but it may be better to not have word wrap.