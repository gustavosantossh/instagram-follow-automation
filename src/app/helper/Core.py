import random
import string

class Core:

    @staticmethod
    def randomToken() -> str:
        chars = string.ascii_letters + string.digits
        prefix = [random.choice(chars) for _ in range(18)]
        return "".join(prefix)
   