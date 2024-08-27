# Barracoders Meeting Calendar

A simple Python program to manage and organize meetings for the Barracoders coding club. This application allows users to add, view, and delete meetings, and saves the meetings to a file (`meetings.json`) for persistence across multiple sessions.

## Features

- **Add Meetings**: Schedule new meetings with a date, time, title, and description.
- **View Meetings**: Display all scheduled meetings in a user-friendly format.
- **Delete Meetings**: Remove meetings that are no longer needed.
- **Data Persistence**: All meetings are saved to a `meetings.json` file, ensuring they are available even after the program is closed and reopened.

## Requirements

- Python 3.x

## How to Run

1. **Clone the repository** (or download the `meeting_calendar.py` script):

    ```bash
    git clone https://github.com/your-username/barracoders-meeting-calendar.git
    cd barracoders-meeting-calendar
    ```

2. **Run the program**:

    ```bash
    python meeting_calendar.py
    ```

3. **Follow the on-screen instructions** to add, view, or delete meetings.

## Usage

When you run the program, you will be presented with a menu:


- **Add a Meeting**: Enter the date (YYYY-MM-DD), time (HH:MM), title, and description.
- **View Meetings**: Lists all scheduled meetings.
- **Delete a Meeting**: Enter the number corresponding to the meeting you wish to delete.
- **Exit**: Closes the application.

## Data Storage

All meetings are stored in a `meetings.json` file in the same directory as the script. The file is automatically updated whenever you add or delete a meeting.

If the `meetings.json` file is not found when the program starts, a new one will be created.

## Contributing

Contributions to the Barracoders Meeting Calendar project are currently restricted to club officers. If you are an officer and would like to propose changes, please follow these steps:
1. **Clone the repository** and create a new branch for your changes:

    ```bash
    git checkout -b your-branch-name
    ```

2. **Make your changes** to the codebase.

3. **Commit your changes** with a descriptive message:

    ```bash
    git commit -m "Describe your changes here"
    ```

4. **Push your changes** to the repository:

    ```bash
    git push origin your-branch-name
    ```

5. **Submit a pull request** on GitHub and await review from other officers.

If you are not an officer but have suggestions or feedback, please reach out to us or open an issue on GitHub. We value all input to help improve our project!

