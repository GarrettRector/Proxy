import webbrowser


def main():
    url = input("Url to Access? > ")
    webbrowser.open(f"http://localhost:8000/?={url}")


if __name__ == "__main__":
    main()
