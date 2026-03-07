class Solution:
    def strong_passwords(self, passwords):
        strong = []
       
        
        for pwd in passwords:
            if (len(pwd) >= 8 and
                any(c.isupper() for c in pwd) and
                any(c.isdigit() for c in pwd) and
                any(c in "@#$" for c in pwd)):
                
                strong.append(pwd)
       
        return strong


class Solution:
    def low_stock_products(self, inventory):
        result = []
        
        for product, quantity in inventory.items():
            if quantity < 10:
                result.append(product)
                
        return result


class Solution:
    def find_duplicate_words(self, sentence):
        words = sentence.lower().split()
        duplicates = []
        
        for i in range(len(words)-1):
            if words[i] == words[i+1]:
                duplicates.append(words[i])
                
        return duplicates


class Solution:
    def unique_products(self, products):
        result = []
        
        for p in products:
            if products.count(p) == 1:
                result.append(p)

        return result



