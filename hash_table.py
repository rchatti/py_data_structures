"""

Methods: Insert, Search, Delete
"""

class hash_table():
    def __init__(self):
        self.rc_ht = [[] for _ in range(10)]

    def insert(self, ins_key, ins_val):
        ht_key = hash(ins_key) % len(self.rc_ht)
        self.rc_ht[ht_key].append((ins_key, ins_val))


    def search(self, search_key):
        hash_key = hash(search_key) % len(self.rc_ht)

        if not self.rc_ht[hash_key]:
            print("Value not found!!")
        else:
            for k,v in self.rc_ht[hash_key]:
                if k == search_key:
                    return v
        
        print("Error searching... ")

dollars = hash_table()
dollars.insert(10,'Ravi')
dollars.insert(11,'Srimai')
dollars.insert(20,'Avanthi')

print(dollars.rc_ht)

print(dollars.search(20))