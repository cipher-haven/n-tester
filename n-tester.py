import speedtest
import time
from tqdm import tqdm
from colorama import Fore, Style, init
import sys

def print_design():
    init(autoreset=True)
    design = f"""
{Fore.CYAN}{Style.BRIGHT}
_____   __              ________           _____
___  | / /              ___  __/_____________  /_____________
__   |/ /  ________     __  /  _  _ \_  ___/  __/  _ \_  ___/
_  /|  /   _/_____/     _  /   /  __/(__  )/ /_ /  __/  /
/_/ |_/                 /_/    \___//____/ \__/ \___//_/
                       
                        >>Made by Cipher Haven<<
    """
    print(design)

def perform_speed_test():
    st = speedtest.Speedtest()
    st.get_best_server()

    print("Testing download speed...")
    with tqdm(total=100, desc="Download Speed", bar_format="{l_bar}{bar}| {n_fmt}/{total_fmt} Mbps") as pbar:
        download_speed = st.download() / 1_000_000  # Convert to Mbps
        pbar.update(100)

    print("Testing upload speed...")
    with tqdm(total=100, desc="Upload Speed", bar_format="{l_bar}{bar}| {n_fmt}/{total_fmt} Mbps") as pbar:
        upload_speed = st.upload() / 1_000_000  # Convert to Mbps
        pbar.update(100)

    ping = st.results.ping

    return download_speed, upload_speed, ping

def main():
    print_design()
    try:
        while True:
            download_speed, upload_speed, ping = perform_speed_test()
            print(f"\n{Fore.GREEN}Download Speed: {download_speed:.2f} Mbps")
            print(f"{Fore.GREEN}Upload Speed: {upload_speed:.2f} Mbps")
            print(f"{Fore.GREEN}Ping: {ping} ms")
            print("-" * 40)
            time.sleep(15)  # Wait for 15 seconds before the next test
    except KeyboardInterrupt:
        print("\nSpeed test interrupted. Exiting...")
        sys.exit()  # Exit cleanly without traceback

if __name__ == "__main__":
    main()
