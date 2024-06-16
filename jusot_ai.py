import os
import time
import random
import pygame
import re
from colorama import Fore, Style
from nltk.chat.util import Chat, reflections
import socket

class LinuxAI:
    def __init__(self):
        self.DIRECTORIES = {'SOUND_DIR': os.path.realpath(os.path.join(os.getcwd(), 'sounds'))}
        self.name = "Jusot"
        self.owner = "Elimane"
        self.pairs = [
            [
                r"hi|hello|hey|yo",
                ["Hi there!", "Hello!", "Hey!"]
            ],
            [
                r"how are you ?",
                ["I'm doing well, thank you!", "I'm great, thanks for asking!"]
            ],
            [
                r"what is your name ?",
                [f"You can call me {self.name}.", f"I'm {self.name}, your virtual assistant."]
            ],
            [
                r"who is your owner ?",
                [f"My owner is {self.owner}.", f"{self.owner} is my creator."]
            ],
            [
                r"(.*) your name ?",
                [f"You can call me {self.name}.", f"I'm {self.name}, your virtual assistant."]
            ],
            [
                r"what can you do ?|what are your capabilities ?",
                ["I can assist you with Linux-related tasks or answer your questions."]
            ],
            [
                r"help|help\(\)",
                self.display_help
            ],
            [
                r"scan ports on (\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})",
                self.scan_ports
            ],
            [
                r"thanks|thank you",
                ["You're welcome!", "My pleasure!", "No problem!"]
            ],
            [
                r"sorry|apologize",
                ["No worries!", "It's okay!", "No problem!"]
            ],
            [
                r"quit|exit|goodbye|bye",
                ["Goodbye! Have a great day!",
                 "See you next time! Until then, take care.",
                 "Hasta la vista! Until we meet again."]
            ],
            [
                r"(.*)",
                ["Sorry, I didn't understand that. Can you please ask me something else?"]
            ]
        ]
        self.context = {"prev_input": "", "prev_response": ""}

    def play_sound(self, sound_filename):
        pygame.mixer.init()
        sound_file_path = os.path.join(self.DIRECTORIES["SOUND_DIR"], sound_filename)
        sound = pygame.mixer.Sound(sound_file_path)
        sound.set_volume(0.5)
        sound.play()

    def get_response(self, query):
        self.context["prev_input"] = query
        for pattern, responses in self.pairs:
            if callable(responses):
                match = re.match(pattern, query, re.IGNORECASE)
                if match:
                    return responses(*match.groups())
            else:
                if re.match(pattern, query, re.IGNORECASE):
                    response = random.choice(responses)
                    self.context["prev_response"] = response
                    return response
        self.context["prev_response"] = None
        return None

    def display_help(self):
        print(Fore.CYAN + "Here are some things you can ask me:" + Style.RESET_ALL)
        for pattern, _ in self.pairs:
            command = re.findall(r"[\w\s]+", pattern)
            if command:
                print(f"- {Fore.MAGENTA}{command[0].strip()}{Style.RESET_ALL}")
            else:
                print(f"- {Fore.RED}No specific command found.{Style.RESET_ALL}")
        print(Fore.CYAN + "You can also ask general questions or seek assistance with Linux-related tasks." + Style.RESET_ALL)

    def scan_ports(self, target):
        self.play_sound('thinking.mp3')
        open_ports = []
        try:
            for port in range(1, 65536):
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                sock.settimeout(1)
                result = sock.connect_ex((target, port))
                if result == 0:
                    open_ports.append(port)
                sock.close()
        except socket.error:
            print("Error occurred while scanning ports.")

        response = f"[+] Open ports on {target}: {', '.join(map(str, open_ports))}" if open_ports else f"No open ports found on {target}."
        return response

def main():
    assistant = LinuxAI()
    assistant.play_sound('wake.mp3')
    print(Fore.YELLOW + f"Welcome to the {assistant.name} Assistant by {assistant.owner}!" + Style.RESET_ALL)

    chat_pairs = [(x, y) for (x, y) in assistant.pairs]
    chatbot = Chat(chat_pairs, reflections)

    while True:
        user_input = input(Fore.BLUE + f"{assistant.owner}: " + Style.RESET_ALL)
        user_input = user_input.strip().capitalize()

        if user_input.lower() in ["help", "help()"]:
            assistant.display_help()
        elif user_input.lower() in ["exit", "quit", "goodbye", "bye"]:
            print(Fore.YELLOW + "Shutting down..." + Style.RESET_ALL)
            assistant.play_sound('shutdown.mp3')
            time.sleep(5)
            print(Fore.GREEN + f"{assistant.name}: {random.choice(assistant.pairs[-2][1])}" + Style.RESET_ALL)
            break
        else:
            response = assistant.get_response(user_input)
            if response is not None:
                if callable(response):
                    print(Fore.GREEN + f"{assistant.name}: {response()}" + Style.RESET_ALL)
                else:
                    assistant.play_sound('data_writing.mp3')
                    time.sleep(2)
                    print(Fore.GREEN + f"{assistant.name}: {response}" + Style.RESET_ALL)
            else:
                if assistant.context["prev_response"]:
                    print(Fore.GREEN + f"{assistant.name}: {assistant.context['prev_response']}" + Style.RESET_ALL)
                else:
                    print(Fore.RED + f"{assistant.name}: I'm not sure how to respond to that." + Style.RESET_ALL)

if __name__ == "__main__":
    main()
