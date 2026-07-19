import base64
import urllib.parse

def base64_encode(data):
    return base64.b64encode(data.encode('utf-8')).decode('utf-8')

def base64_decode(data):
    try:
        return base64.b64decode(data.encode('utf-8')).decode('utf-8')
    except Exception:
        return "[Error] Invalid Base64 data"

def hex_encode(data):
    return data.encode('utf-8').hex()

def hex_decode(data):
    try:
        return bytes.fromhex(data).decode('utf-8')
    except Exception:
        return "[Error] Invalid Hexadecimal data"

def url_encode(data):
    return urllib.parse.quote(data)

def url_decode(data):
    return urllib.parse.unquote(data)

def main():
    print("=" * 45)
    print("      API Traffic Encoder & Decoder CLI      ")
    print("=" * 45)
    print("1. Base64 Encode")
    print("2. Base64 Decode")
    print("3. Hex Encode")
    print("4. Hex Decode")
    print("5. URL Encode")
    print("6. URL Decode")
    print("7. Exit")
    print("=" * 45)
    
    while True:
        choice = input("\nSelect an option (1-7): ").strip()
        if choice == '7':
            print("Exiting tool. Security analysis complete.")
            break
        elif choice in ['1', '2', '3', '4', '5', '6']:
            payload = input("Enter the data string: ")
            if choice == '1': print("Result:", base64_encode(payload))
            elif choice == '2': print("Result:", base64_decode(payload))
            elif choice == '3': print("Result:", hex_encode(payload))
            elif choice == '4': print("Result:", hex_decode(payload))
            elif choice == '5': print("Result:", url_encode(payload))
            elif choice == '6': print("Result:", url_decode(payload))
        else:
            print("[!] Invalid selection. Please choose between 1 and 7.")

if __name__ == "__main__":
    main()
