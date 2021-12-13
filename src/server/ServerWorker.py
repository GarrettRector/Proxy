import requests
import bs4 as bs4


class serverWorker:
    def __init__(self, url: str, serverURL: str):
        self.url = url if url.startswith("https") | url.startswith("http") else f"https://{url}"
        self.serverURL = serverURL

    def getUrl(self):
        content = requests.get(self.url, stream=True)
        soup = bs4.BeautifulSoup(content.content, "html.parser")
        for link in soup.find_all("a"):
            link_ = str(link).split('"')
            try:
                if link_[3].startswith("/"):
                    print(self.url)
                    link_[3] = f"{self.url}{link_[2]}"
                string = f'{link_[0]}"{link_[1]}"{link_[2]}"http://{self.serverURL}/?={link_[3]}"{"".join(link_[4:])}'
            except IndexError:
                string = f'{link_[0]}"{link_[1]}"{link_[2]}"{"".join(link_[3:])}"'
            link.replace_with(bs4.BeautifulSoup(string, "html.parser"))
        return soup.prettify()
