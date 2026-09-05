# MSCS532_Assignment1 by Weevern Gong

## Description
This program implements the insertion sort algorithm using Python. The program sorts a list of integers in monotonically decreasing order, from largest to smallest.

## Requirements
- Python 3.8 or higher
- Visual Studio Code or alternate IDE
- Python extension for Visual Studio Code
- Git (to clone repository)
- GitHub account (to fork repository to own GitHub account, etc.)
- Code Runner extension (optional requirement)

## Instructions
1. Go to the GitHub repository at https://github.com/wgongUC/MSCS532_Assignment1

2. Select either option 1 or option 2:

Option 1: Download ZIP File
- Click on the green button "Code" and select "Download ZIP".
- Extract the downloaded ZIP file, then open Visual Studio Code and select File > Open Folder.
- Select the folder containing Insertion_Sort_Decreasing_Order.py

Option 2: Clone with Git
- Click on the green button "Code", and select the HTTPS tab. Click "Copy URL to clipboard" on the right to copy the url https://github.com/wgongUC/MSCS532_Assignment1.git. 
- In Windows, open a terminal window and run this command:
    git clone https://github.com/wgongUC/MSCS532_Assignment1.git
- A new project folder will be created in the current terminal location. 
- In Visual Studio Code, select File > Open Folder and select the project folder that was created.

3. To run the program in Visual Studio Code, select Terminal > New Terminal and run the following command:
   python Insertion_Sort_Decreasing_Order.py
The terminal will display the input list for the program, and the output of the program which is the sorted list.

4. To test the program with custom inputs, edit the numbers in the numbers_arr array in Insertion_Sort_Decreasing_Order.py, then save the program file, and run it.

## Example Input
[5, 2, 20, 9, 1, 5, 6, 3, 71, 8, 4, 56, 12]

## Example Output
[71, 56, 20, 12, 9, 8, 6, 5, 5, 4, 3, 2, 1]

## Time Complexity
The best-case time complexity is Θ(n). The average-case and worst-case time complexities are Θ(n²).

## Reference
Cormen, T. H., Leiserson, C. E., Rivest, R. L., & Stein, C. (2022). Introduction to Algorithms (4th ed.). Random House Publishing Services. https://reader2.yuzu.com/books/9780262367509