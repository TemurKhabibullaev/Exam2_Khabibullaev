# Temur Khabibullaev 4/10/2020
import random
import Search_Methods
import time

while True:
    # Menu
    choice = int(input("Please choose to proceed:\n1. Bubble Sort.\n2. Selection Sort.\n3. Insertion Sort.\n"
                       "4. Merge Sort.\n5. Quick Sort.\n6. EXIT\n>>>"))
    # Button to exit
    if choice >= 6:
        break
    # Actual process
    else:
        # List will store numbers for sorting
        empty_list = []
        number = int(input("Please specify how many numbers:\n>>>"))
        # Inserting random numbers
        for i in range(number):
            empty_list.append(random.randint(1, 100000))
        print("Here's the list of your random numbers:\n",empty_list)
        time.sleep(7)
        # This choice is for Bubble Sort
        if choice == 1:
            bubble = Search_Methods.bubble_sort(empty_list)
            print("Here's your sorted numbers:\n",bubble)
            time.sleep(7)
        # This choice is for Selection Sort
        if choice == 2:
            selection = Search_Methods.selection_sort(empty_list)
            print("Here's your sorted numbers:\n",selection)
            time.sleep(7)
        # This choice is for Insertion Sort
        if choice == 3:
            insertion = Search_Methods.insertion_sort(empty_list)
            print("Here's your sorted numbers:\n",insertion)
            time.sleep(7)
        # This choice is for Merge Sort
        if choice == 4:
            merge = Search_Methods.merge_sort(empty_list)
            print("Here's your sorted numbers:\n",merge)
            time.sleep(7)
        # This choice is for Quick Sort
        if choice == 5:
            quick = Search_Methods.quick_sort(empty_list)
            print("Here's your sorted numbers:\n",quick)
            time.sleep(7)

