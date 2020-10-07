class signup:

    def reg(self, name, username, password):
        file=open('regi.txt','a')
        data=name+','+username+','+password+'\n'
        file.write(data)
        file.close()

    def display(self):
        reginfo=[]
        file=open('regi.txt','r')
        data=file.readlines()
        file.close()

        for i in data:
            replacedata=i.replace('\n','')
            medata=replacedata.split(',')
            reginfo.append(medata)

        for i in range(len(reginfo)):
            print('\nname:',reginfo[i][0])
            print('username:',reginfo[i][1])
            print('password:',reginfo[i][2])


a = signup()
a.reg('ryuuzin','t102','teasdpass')
a.display()
"""

"""