import datetime
import json
import os

class MeetingCalendar:
    def __init__(self, filename="meetings.json"):
        self.filename = filename
        self.meetings = []
        self.load_meetings()

    def load_meetings(self):
        """Load meetings from a file."""
        if os.path.exists(self.filename):
            try:
                with open(self.filename, "r") as file:
                    self.meetings = json.load(file)
                    print("Meetings loaded from file.")
            except json.JSONDecodeError:
                print("Error: File is corrupted or contains invalid JSON. Starting with an empty meeting list.")
                self.meetings = []
            except Exception as e:
                print(f"Error loading meetings: {e}")
                self.meetings = []
        else:
            print("No saved meetings found. Starting fresh.")

    def save_meetings(self):
        """Save meetings to a file."""
        try:
            with open(self.filename, "w") as file:
                json.dump(self.meetings, file, indent=4)
                print("Meetings saved to file.")
        except Exception as e:
            print(f"Error saving meetings: {e}")

    def add_meeting(self, date, time, title, description):
        meeting = {
            "date": date,
            "time": time,
            "title": title,
            "description": description
        }
        self.meetings.append(meeting)
        print(f"Meeting '{title}' added successfully!")
        self.save_meetings()

    def view_meetings(self):
        if not self.meetings:
            print("No meetings scheduled.")
            return

        print("\nScheduled Meetings:")
        for idx, meeting in enumerate(self.meetings, start=1):
            print(f"{idx}. {meeting['date']} at {meeting['time']} - {meeting['title']}: {meeting['description']}")

    def delete_meeting(self, index):
        if 0 <= index < len(self.meetings):
            removed_meeting = self.meetings.pop(index)
            print(f"Meeting '{removed_meeting['title']}' deleted successfully!")
            self.save_meetings()
        else:
            print("Invalid meeting number. Please try again.")

    def show_menu(self):
        print("\n--- Barracoders Meeting Calendar ---")
        print("1. Add a Meeting")
        print("2. View Meetings")
        print("3. Delete a Meeting")
        print("4. Exit")

def main():
    calendar = MeetingCalendar()

    while True:
        calendar.show_menu()
        choice = input("Enter your choice: ")

        if choice == "1":
            date = input("Enter the meeting date (YYYY-MM-DD): ")
            time = input("Enter the meeting time (HH:MM): ")
            title = input("Enter the meeting title: ")
            description = input("Enter the meeting description: ")
            try:
                datetime.datetime.strptime(date, "%Y-%m-%d")
                datetime.datetime.strptime(time, "%H:%M")
                calendar.add_meeting(date, time, title, description)
            except ValueError:
                print("Invalid date or time format. Please use YYYY-MM-DD for date and HH:MM for time.")
                
        elif choice == "2":
            calendar.view_meetings()

        elif choice == "3":
            calendar.view_meetings()
            try:
                index = int(input("Enter the meeting number to delete: ")) - 1
                calendar.delete_meeting(index)
            except ValueError:
                print("Invalid input. Please enter a number.")
                
        elif choice == "4":
            print("Exiting the Meeting Calendar. Goodbye!")
            break

        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
