# :money_with_wings: Expense Splitter

## :rocket: Introduction
The **Expense Splitter** is a web-based application designed to help groups of people easily divide shared expenses. It allows users to input the amounts spent by each participant and then calculates how much each person owes or is owed, ensuring fairness and transparency in cost-sharing scenarios.

## :question: Problem Domain
Managing shared expenses can often be complicated, especially in group activities like trips, events, or joint purchases. Without a proper system, it becomes challenging to keep track of who owes what, leading to confusion or disputes. A reliable tool that helps split expenses fairly can save time and effort in such scenarios.

## :wrench: Solution Domain
The Expense Splitter provides a simple solution to the problem by:
- Allowing users to input each participant's spending.
- Calculating each participant's share of the total expenses.
- Displaying the amounts that each person owes or should receive.

## :computer: Technology
The application uses modern web technologies to ensure smooth functionality and responsiveness:
- **Frontend**: HTML, CSS, and JavaScript (with Vanilla JS for handling form submissions and calculations).
- **Backend**: None (this is a client-side application).
- **Data Storage**: In-memory JavaScript objects for tracking expenses (can be extended to integrate with a backend or database).

## :books: Data Structure Used
- **Objects (Data Structure)**: Used to store the expenses for each person.
- **Arrays (Data Structure)**: Utilized for managing the form entries and iterating over participants.
- **Mathematical Calculations (Algorithm)**: Calculating the individual share and adjusting the expenses accordingly.
- **Sorting (Algorithm)**: Sorting the results based on who owes or is owed money.

## :star: Key Features
### 1. :heavy_plus_sign: Add Expenses
- Allows users to input each person's name and the amount they have spent.
- Adds the amounts to the total expenses for the group.

### 2. :moneybag: Calculate Split
- Automatically calculates how much each person owes or should receive based on their share of the total expenses.
- Displays the results with clear labels showing the amounts owed and received.

### 3. :chart_with_upwards_trend: Display Results
- Dynamically displays a list of participants and the corresponding amounts they owe or are owed.

## :arrows_counterclockwise: Workflow
1. Users input the names and amounts for each person involved in the expense-sharing scenario.
2. The app calculates the total expenses and divides them equally among participants.
3. The results are displayed, showing who owes money and who should receive money.

## :clipboard: Installation
To run this project locally, follow these steps:

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/expense-splitter.git
    ```
2. Navigate to the project directory:
    ```bash
    cd expense-splitter
    ```
3. Open `index.html` in your preferred web browser to start using the application.

## :octocat: Contributing
If you wish to contribute to the project, feel free to fork this repository, make your changes, and create a pull request. Contributions are welcome!

## :page_facing_up: License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## :trophy: Conclusion
The Expense Splitter application provides a simple, intuitive, and efficient solution for managing and splitting group expenses. Whether you're planning a group trip, dinner, or event, this tool ensures everyone pays their fair share. The app is lightweight, easy to use, and can be customized further for more advanced features such as tracking recurring expenses or integrating with payment services.
