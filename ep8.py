class Friend:

    def __init__(self,name,age,gender):
        self.name = name
        self.age = age
        self.gender = gender
        
    
    def sayhello(self):
        print(f'{self.name}ว่าไงเพื่อน!')

    
    def letfootball(self):
        if self.gender == 'ชาย':
            tail = 'วะ'
            callme = 'กู'
        else:
            tail = 'จ้า'
            callme = 'เรา'
        print(f'ไง{tail}{self.name}ไปเตะบอลกับ{callme}ป่าว?')


class BestFriend(Friend):
    def __init__(self, name, age, gender, relation):
        super().__init__(name, age, gender)
        self.relation = relation

    def sayhello(self):
        print(f'หวัดดี ชื่อ {self.name}')

if __name__ == '__main__':
    friend1 = Friend('โทน',34,'ชาย')
    friend2 = Friend('เบ้า',34,'ชาย')
    friend3 = BestFriend('น้ำ',30,'หญิง','ซี้')
    friend4 = BestFriend('เอ็ม',34,'ชาย','ซี้')
    friend5 = BestFriend('ด้วง',34,'ชาย','ไม่ซี้')

    print('---------สนามบอล---------')
    friend1.sayhello()
    friend2.sayhello()
    friend3.sayhello()
    friend4.sayhello()
    friend5.sayhello()

    friend1.letfootball()
    friend2.letfootball()
    friend3.letfootball()
    friend4.letfootball()
    friend5.letfootball()