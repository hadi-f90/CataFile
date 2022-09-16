class choice:

    def __init__(self, msg, choices):
        self.msg = msg
        self.choices = choices
        assert self.msg not in (None, "")
        assert isinstance(self.msg, str)
        assert self.choices not in (None, "", (), {}, [])
        assert isinstance(self.choices, (list, tuple))
        self.selection = None

    def get_user_input(self):
        print("msg")
        for _ in self.choices:
            print(self.choices.index(_), _)
        self.selection = int(input("Enter the number:"))
        if self.check_selection():
            return self.selection

    def check_selection(self):
        if self.selection in (None, ""):
            print("Empy Value is not allowed")
            self.get_user_input()

        elif not 0 < self.selection < len(self.choices) + 1:
            print("The number you've entered is out of selection range:")
            self.get_user_input()

        else:
            return True
