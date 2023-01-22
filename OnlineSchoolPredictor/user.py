from canstants import ALREADY_EXIST, SENT_ACCOUNT

class Users:
    def __init__(self,bot):
        self.db = bot.database
        self.debug = bot.debug

    def is_active(self, user_id):
        try:
            self.db.cur.execute("SELECT * from users WHERE id = ?", [str(user_id)])
            placeholder = self.db.cur.fetchone()
            if placeholder is not None:
                return True
            return False

        except Exception as e:
            print(e)

    def is_admin(self, user_id):
        self.db.cur.execute("SELECT * from users WHERE id = ?", [str(user_id)])
        placeholder = self.db.cur.fetchone()
        if placeholder[2] == "admin":
            return True

        return False

    def is_data_open(self):
        return self.db.is_open

    def register(self, message):
        ac = 0
        self.db.open_database()

        self.db.cur.execute("SELECT * FROM users")
        s = self.db.cur.fetchall()
        for i in s:
            if i[0] == str(message.user.user_id):
                ac += 1
                return ALREADY_EXIST

        if ac == 0:
            self.db.cur.execute("INSERT INTO users VALUES (?,?,?, ?)", (message.user.user_id, message.user.first_name, "member", ""))
            self.debug.user_registered(message.user.username)
            self.db.commit()
            return SENT_ACCOUNT



