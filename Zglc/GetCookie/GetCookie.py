
class GetCookie():
	def __init__(self):
		pass
    def GetCookie(self,str):
        str = str.split(';')
        str1 = str[3]
        ck=str1.split(',')[-1]
        return ck
if __name__ == '__main__':
    str = 'acw_tc=76b20f7215416840900418635e705a534fed30fb4ca86aadbcb244419e04d5;path=/;HttpOnly;Max-Age=2678401, sid=JyAVM73MUC7nTdlhURHILEARLoqGa4JalLIAw6SK; expires=Thu, 08-Nov-2018 15:34:50 GMT; Max-Age=7200; path=/; secure; HttpOnly, SERVERID=bdeffaa4bcbb95a824cda8088ef618ad|1541684090|1541684090;Path=/'
    G = getCookie()
    print(G.getCookie(str))