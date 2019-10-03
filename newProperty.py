#练习描述符
class MyProperty:
    def __init__(self,fget,fset,fdel):
        self.fget = fget
        self.fset = fset
        self.fdel = fdel

    def __get__(self, instance, owner):#该方法由‘.’触发
        #instance是MyProperty描述符拥有者的实例对象，即下面的的m，owner是MyProperty描述符拥有者本身，即man类
        return self.fget(instance)
    def __set__(self, instance, value):#该方法由‘=’触发
        #instance是MyProperty描述符拥有者的实例对象，value是要给拥有者的对应属性修改的值
        self.fset(instance,value)
    def __delete__(self, instance):#该方法由‘del’触发
        self.fdel(instance)

class Man:
    def __init__(self):
        self.__age = 0
    def getAge(self):
        return self.__age
    def setAge(self,age):
        self.__age = age
    def delAge(self):
        del self.__age
    x = MyProperty(getAge,setAge,delAge)



m = Man()
m.x = 3
print(m.x)
