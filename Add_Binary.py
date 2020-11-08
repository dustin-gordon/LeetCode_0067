import re

class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        # check input strings contain only 1 or 0:
        if (re.match('[^0-1]', a)) or (re.match('[^0-1]', b)):
            print('a = {0}'.format(a)) # debug
       	    print('b = {0}'.format(b)) # debug
            print('Input is not a valid binary string') # debug

        # check lengths of inputs meet constraint:
        elif (len(a) >= 1) and (len(b) <= 10000):
            print('a = {0}'.format(a)) # debug
            print('b = {0}'.format(b)) # debug
            print('Input is valid binary string') # debug

            # convert string a to number:
            a_num = 0
            for index in range(0, len(a)): 
                #print("index = {0}".format(index)) # debug
                if (a[-(index + 1)] == '1'):
                    a_num += 2**index
            print("a_num = {0}".format(a_num)) # debug

            # convert string b to number:
            b_num = 0
            for index in range(0, len(b)): 
                #print("index = {0}".format(index)) # debug
                if (b[-(index + 1)] == '1'):
                    b_num += 2**index
            print("b_num = {0}".format(b_num)) # debug

            # add numbers and convert to binary string:
            ab_sum = a_num + b_num
            sum_string = ""
            rem = 0
            print("sum = {0}".format(ab_sum)) # debug
            while(ab_sum != 0):
                rem = ab_sum % 2
                ab_sum = ab_sum // 2
                #print("temp. sum = {0}".format(ab_sum)) # debug
                #print("remainder = {0}".format(rem)) # debug
                sum_string = str(rem) + sum_string
            print("sum (binary) = {0}".format(sum_string)) # debug
            return sum_string

        
Soln = Solution()
Soln.addBinary("11","1")
Soln.addBinary("1010","1011")
#Soln.addBinary("abc","def")
