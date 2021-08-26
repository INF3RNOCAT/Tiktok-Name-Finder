import requests, colorama, threading, time, random
from colorama import Fore, Style

# Initialize
colorama.init()

# Config Variables

INTERVAL = 0
NAME_LENGTH = 4

# Main Code

class TikTokUserFinder:
    def __init__(self, interval, name_length):
        self.interval = interval
        self.name_length = name_length
        self.username = ""
        self.headers = {"user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36"}
        self.random = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "_", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
        threading.Thread(target=self.run).start()

    def generate_name(self, length):
        string = ""
        for i in range(length):
            string += random.choice(self.random)

        self.username = string

    def parse_response(self, status_code):
        if status_code == 404:
            print(Fore.GREEN + Style.BRIGHT + f"{self.username} is not taken!" + Style.RESET_ALL)
        elif status_code == 200:
            print(Fore.RED + Style.BRIGHT + f"{self.username} is taken!" + Style.RESET_ALL)
        else:
            print(Fore.YELLOW + Style.BRIGHT + f"Information about {self.username} is unknown." + Style.RESET_ALL)

    def run(self):
        while True:
            self.generate_name(self.name_length)
            try:
                response = requests.get(f"https://www.tiktok.com/@{self.username}/", headers=self.headers)
                self.parse_response(response.status_code)
            except Exception as e:
                print(Fore.BLUE + Style.BRIGHT + f"Exception Occurred: {str(e)}", + Style.RESET_ALL)

            time.sleep(self.interval)


Runner = TikTokUserFinder(INTERVAL, NAME_LENGTH)
