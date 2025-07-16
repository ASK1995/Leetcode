from collections import defaultdict

class Logger:
    def __init__(self):
        self.message_map = defaultdict(lambda:-10)

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        if(self.message_map[message] + 10) <= timestamp:
            self.message_map[message] = timestamp
            return True
        return False

# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)