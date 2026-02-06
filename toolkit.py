import socket

# -------- PORT SCANNER MODULE --------
def port_scanner():
    target = input("Enter target IP (example: 127.0.0.1): ")
    print("\nScanning common ports...\n")

    ports = [21, 22, 23, 80, 443]

    for port in ports:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(1)
            result = s.connect_ex((target, port))
            if result == 0:
                print(f"[OPEN] Port {port}")
            else:
                print(f"[CLOSED] Port {port}")
            s.close()
        except:
            print("Error scanning port")

# -------- BRUTE FORCE (DEMO) MODULE --------
def brute_force_demo():
    correct_password = "admin123"
    wordlist = ["12345", "password", "admin", "admin123"]

    print("\nStarting demo brute force...\n")

    for pwd in wordlist:
        print(f"Trying password: {pwd}")
        if pwd == correct_password:
            print(f"\n[SUCCESS] Password found: {pwd}")
            return

    print("\nPassword not found")

# -------- MAIN TOOLKIT MENU --------
def main():
    while True:
        print("\n--- Penetration Testing Toolkit ---")
        print("1. Port Scanner")
        print("2. Brute Force Demo")
        print("3. Exit")

        choice = input("Select option: ")

        if choice == "1":
            port_scanner()
        elif choice == "2":
            brute_force_demo()
        elif choice == "3":
            print("Exiting toolkit...")
            break
        else:
            print("Invalid choice")

main()
