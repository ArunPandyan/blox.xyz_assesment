import unittest

def addNumbers(val_a,val_b):
    try:
        a=int(val_a)
        b=int(val_b)
        sum1=a+b 
        return str(sum1)
    except:
        return "enter Valid Inputs"

val1,val2=input().split()
print(addNumbers(val1,val2))

'''  ----- Performing Text Cases for the code-------'''

class Testaddstring(unittest.TestCase):
    def test_postivenumbers(self):
        ans=addNumbers("45","40")
        self.assertEqual(ans,'85')
    
    def test_negativenumbers(self):
        ans=addNumbers("-45","-40")
        self.assertEqual(ans,'-85')

    def test_postinegative(self):
        ans=addNumbers("-45","40")
        self.assertEqual(ans,'-5')

    def test_boundarycase1(self):
        ans=addNumbers("0","0")
        self.assertEqual(ans,'0')
    
    def test_bondarycase2(self):
        ans=addNumbers("1000000000000000","2000000000000000")
        self.assertEqual(ans,'3000000000000000')
    
    def test_boundarycase3(self):
        ans=addNumbers("-4000000000000","1")
        self.assertEqual(ans,'-3999999999999')

if __name__ == '__main__':
    unittest.main()
