class Solution:
    def intToRoman(self, input_num: int) -> str:
        # romans = {1:'I', 5:'V', 10:'X', 50:'L', 100:'C', 500:'D', 1000:'M' }
        # print(romans.keys())
        finalRoman = ''
        
        def findRoman(num):
            if num>=1000:
                return 'M', 1000
            elif num>=500 and num<1000:
                if num>=900:
                    return 'CM', 900
                return 'D', 500
            elif num>=100 and num<500:
                if num>=400:
                    return 'CD', 400
                return 'C', 100
            elif num>=50 and num<100:
                if num>=90:
                    return 'XC', 90
                return 'L', 50
            elif num>=10 and num<50:
                if num>=40:
                    return  'XL', 40 
                return 'X', 10
            elif num>=5 and num<10:
                if num==9:
                    return 'IX', 9
                return 'V', 5, 
            elif num>=1 and num<5:
                if num==4:
                    return 'IV', 4
                return 'I', 1
            else:
                return 'I', 1
            
        val = input_num
        while val>0:
            romanResult, updateWith = findRoman(int(val))
            finalRoman+=romanResult
            val = val - updateWith

        return finalRoman   
                
        
                