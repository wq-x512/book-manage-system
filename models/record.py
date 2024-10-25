class Record:
    def __init__(self, uuid, bookname, userid, operation, time):
        self.uuid = uuid
        self.bookname = bookname
        self.userid = userid
        self.operation = operation
        self.time = time

    def assign(self, data):
        self.uuid = data['uuid']
        self.bookname = data['bookname']
        self.userid = data['userid']
        self.operation = data['operation']
        self.time = data['time']
