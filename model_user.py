class UserProfile:
    def __init__(self, user_id):
        self.user_id= 0
        self.U_GADGET = 0
        self.ONNET_MIN = 0
        self.ONNET_MAX = 0
        self.OFFNET_MIN = 0
        self.OFFNET_MAX = 0
        self.DATA_MIN = 0
        self.DATA_MAX = 0
        self.ROAMING = 0
        self.INTNET = 0
        self.FAMILY = 0
        self.SMS = 0
        self.SOCIAL = 0
        self.EDUCATIONAL = 0
        self.TV = 0
        self.LIFEBOX = 0
        self.NUMBER_TYPE = 0
        self.PRICE_MIN = 0
        self.PRICE_MAX = 0


user_profiles = {}  # Словник для збереження профілів користувачів
