class BrowserHistory:

    def __init__(self, homepage: str):
        self.head = HistoryNode(homepage)
        self.tail = self.head
        self.curr = self.head

    def visit(self, url: str) -> None:
        newPage = HistoryNode(url)
        self.curr.next = newPage
        newPage.previous = self.curr

        self.curr = newPage
        self.tail = self.curr

    def back(self, steps: int) -> str:
        count = 0

        while self.curr and count < steps:
            if self.curr == self.head:
                return self.head.value

            self.curr = self.curr.previous
            count += 1

        return self.curr.value

    def forward(self, steps: int) -> str:
        count = 0

        while self.curr and count < steps:
            if self.curr == self.tail:
                return self.tail.value

            self.curr = self.curr.next
            count += 1

        return self.curr.value


class HistoryNode:
    def __init__(self, url):
        self.value = url
        self.next = None
        self.previous = None

# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)