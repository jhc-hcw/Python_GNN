class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age



    # def __init__(self, name):
    #     self.name = name
    #     self.age = 0

    def shout(self):
        print("我的名字{}，我的年龄{}".format(self.name, self.age))


an = Animal('jhc', 88);
an.shout()
an.shout()
an.age = 0
an.shout()
