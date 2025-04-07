import networkx as nx
import matplotlib.pyplot as plt
from colorama import Fore, Style
from colorama import init
from tkinter import *
import random
import logging
init()

# Config for logging

logging.basicConfig(
    level=logging.DEBUG,
    format = "%(asctime)s - %(levelname)s - %(message)s",
    filename='debug.log',
    filemode='w',
    encoding='UTF-8'
)

# Main Class

class Number:
    def __init__(self, first_number, second_number):
        self.first_number = None
        self.second_number = None

    # Main menu of program

    def chooser(self):
        print("Basic: ")
        print(' ')
        print(Fore.BLUE + '1. Limited Calculating' + Style.RESET_ALL)
        print(Fore.BLUE + '2. Random Calculating' + Style.RESET_ALL)
        print(Fore.BLUE + '3. Uncorrect Calculating' + Style.RESET_ALL)
        print(' ')
        print("Functional: ")
        print(' ')
        print(Fore.GREEN + '4. Functional Calculating' + Style.RESET_ALL)
        print(Fore.GREEN + '5. Alternative Calculating' + Style.RESET_ALL)
        print(Fore.GREEN + '6. Grap Calculating' + Style.RESET_ALL)
        print(' ')
        choose = int(input("Choose calculating style "))

        if choose == 1:
            self.limited_calculating()

        elif choose == 2:
            self.random_calculating()

        elif choose == 3:
            self.uncorrect_calculating()
        
        elif choose == 4:
            self.functional_calculating()

        elif choose == 5:
            self.alternative_calculating()

        elif choose == 6:
            self.graph_calculating()

    # limited calculating logic

    def limited_calculating(self):
        self.first_number = int(input())
        self.second_number = int(input())
        try:
            if self.first_number > 9:
                result = self.first_number - self.second_number
                print(result)
            elif self.first_number < 9:
                print(Fore.LIGHTRED_EX + 'Cannot find function' + Style.RESET_ALL)
            if self.second_number > 0:
                result = self.second_number - self.first_number
                print(result)
            elif self.second_number < 0:
                result = self.second_number + self.first_number
                print(result)
            logging.info('Limited calculating has been ended corrected')
            logging.info(f'User entres {self.first_number} + {self.second_number}. Answer: {result}')

        except ValueError:
            logging.error('Value error has been happened')

    # random calculating logic

    def random_calculating(self):
        try:
            self.first_number = random.randrange(-99999999, 99999999)
            self.second_number = random.randrange(-99999999, 99999999)
            result = self.first_number + self.second_number
            print(f"Random has choosed {self.first_number} As first number")
            print(f"Random has choosed {self.second_number} As second number")
            print(result)
            logging.info('Random calculating has been ended corrected')
            logging.info(f'Randomizer enters {self.first_number} + {self.second_number}. Answer: {result}')
        
        except ValueError:
            logging.error('Value error has been happened')

    # alternative calculating logic

    def alternative_calculating(self):
        try: 
            self.first_number = int(input())
            self.second_number = int(input())
            if self.first_number == self.second_number:
                result = self.second_number - self.first_number
                if result == 0:
                    result += self.first_number
                    result -= random.randrange(1, 9999) - 42
                    print(result)
                else:
                    print(result)
            logging.info('Alternative calculating has been ended corrected')
            logging.info(f'User entres {self.first_number} + {self.second_number}. Answer: {result}')

        except ValueError:
            logging.error('Value error has been happened')         

    # functional calculating logic   

    def functional_calculating(self):
        self.first_number = int(input())
        self.second_number = int(input())
        result = self.first_number + self.second_number
        try:
            if result == 0:
                root = Tk()
                root.title("FCMD")
                root.minsize(100, 200)
                root.geometry("210x210+50+50")
                text = Label(root, text="You created window")
                text.pack()
                root.mainloop()
                logging.info('Functional calculating has been ended corrected')
                logging.info(f'User entres {self.first_number} + {self.second_number}. Answer: {result}')

            elif result == 1:
                from platform import platform, machine, processor, version
                print(platform(0,1))
                print(machine())
                print(processor())
                print(version())
                logging.info('Functional calculating has been ended corrected')
                logging.info(f'User entres {self.first_number} + {self.second_number}. Answer: {result}')

        except ValueError:
            logging.error('Value error has been happened')

    def graph_calculating(self):
        try:
            self.first_number = int(input())
            self.second_number = int(input())
            result = self.first_number + self.second_number

            result_advance = result
            result_advance -= random.randrange(0,99)

            G = nx.DiGraph()

            G.add_edge("A", "B", weight=self.first_number)
            G.add_edge("C", "D", weight=self.second_number)
            G.add_edge("D", "B", weight=result)
            G.add_edge("A", "D", weight=result_advance)

            for u, v, data in G.edges(data=True):
                print(f"Edge: {u} -> {v} has weight {data['weight']}")

            pos = nx.spring_layout(G)

            nx.draw(G, pos, with_labels=True, node_color="grey", edge_color="blue")

            edge_labels = nx.get_edge_attributes(G, "weight")

            nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

            plt.show()
            logging.info('Graph calculating has been ended corrected')
            logging.info(f'User entres {self.first_number} + {self.second_number}. Answer: {result}, Extra answer: {result_advance}')
        except ValueError:
            logging.error('Value error has been happened')

    # uncorrect calculating logic

    def uncorrect_calculating(self):
        try:
            self.first_number = int(input())
            self.second_number = int(input())
            self.first_number += random.randrange(1, 5)
            self.second_number -= random.randrange(1, 7)
            result = self.first_number + self.second_number
            print(result)
            logging.info('Uncorrect calculating has been ended corrected')
            logging.info(f'User entres {self.first_number} + {self.second_number}. Answer: {result}')
        except ValueError:
            logging.error('Value error has been happened')

    # closing program

    def close(self):
        pass

# User code

nums = Number(None, None)

nums.chooser()
input()