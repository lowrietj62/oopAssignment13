class Customer:

    def __init__(self, first_name: str, last_name: str, phone: str, email: str):
        self._first_name = first_name
        self._last_name = last_name
        self._phone = phone
        self._email = email

    # ------------------------------------------------------------------
    # Getters
    # ------------------------------------------------------------------

    def get_first_name(self):
        return self._first_name

    def get_last_name(self):
        return self._last_name

    def get_full_name(self):
        return f"{self._first_name} {self._last_name}"

    def get_phone(self):
        return self._phone

    def get_email(self):
        return self._email

    # ------------------------------------------------------------------
    # Setters
    # ------------------------------------------------------------------

    def set_first_name(self, first_name: str):
        self._first_name = first_name

    def set_last_name(self, last_name: str):
        self._last_name = last_name

    def set_phone(self, phone: str):
        self._phone = phone

    def set_email(self, email: str):
        self._email = email

    # ------------------------------------------------------------------
    # Display
    # ------------------------------------------------------------------

    def display_info(self):
        print(f"  Name  : {self.get_full_name()}")
        print(f"  Phone : {self._phone}")
        print(f"  Email : {self._email}")

    def __repr__(self):
        return f"Customer({self.get_full_name()!r}, {self._phone!r}, {self._email!r})"