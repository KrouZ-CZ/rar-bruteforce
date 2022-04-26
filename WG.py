class WordlistGenerator():
    def __init__(self, leght, words = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"):
        self.words = words
        self.leght = leght
        self.password = [0 for i in range(self.leght)]
        self.len_password = len(self.words) ** self.leght
        self.Programm = True
    def next(self):
        if self.Programm == False: return
        self.i = len(self.password) - 1
        while self.i > 0:
            if self.password[self.i] == len(self.words):
                self.password[self.i] = 0
                self.password[self.i - 1] += 1
            self.i -= 1
        if self.password[0] == len(self.words):
            self.Programm = False
        self.temp = [self.words[i] for i in self.password]
        self.password[-1] += 1
        return "".join(self.temp)