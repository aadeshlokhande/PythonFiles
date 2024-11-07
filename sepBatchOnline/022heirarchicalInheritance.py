# heirarchical

class Parent:
    def ParentQuality(self):
        print("singing")
    
class Child1(Parent):
    def child1Quality(self):
        print("dancing")
    
class Child2(Parent):
    def child2Quality(self):
        print("guitar")

# chin1 = Child1()
# chin1.child1Quality()
# chin1.ParentQuality()

chin2 = Child2()
chin2.child2Quality()
chin2.ParentQuality()

