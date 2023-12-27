import webbrowser
import subprocess

def search_stack_overflow(query):
    search_url = f"https://stackoverflow.com/search?q={query}"
    webbrowser.open(search_url)

def open_web_browser(url):
    webbrowser.open(url)

def list_python_modules():
    subprocess.run(["pip", "list"])

def developer_assistant():
    print("Developer Assistant:")
    print("1. Search on Stack Overflow")
    print("2. Open a web browser")
    print("3. List available Python modules")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        query = input("Enter your Stack Overflow search query: ")
        search_stack_overflow(query)
    elif choice == "2":
        url = input("Enter the URL you want to open: ")
        open_web_browser(url)
    elif choice == "3":
        list_python_modules()
    elif choice == "4":
        print("Exiting Developer Assistant.")
    else:
        print("Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    while True:
        developer_assistant()
        exit_choice = input("Do you want to exit? (yes/no): ").lower()
        if exit_choice == "yes":
            break
