import datetime
import random


class Cache:

    def __init__(self):
        # Constructor
        self.cache = {}
        self.MaxSize = 5

    def empty(self):
        return self.cache == {}

    def size(self):
        return len(self.cache)

    def __contains__(self, key):
        return key in self.cache

    def view(self):
        return self.cache

    # Update cache and remove oldest item, when size reaches maximum
    def update(self, value):
        if (len(self.cache) == self.MaxSize):
            freed_key = self.delete()  # remove element with LRU
            # add once freed up some space
            self.cache[freed_key] = {'time added': datetime.datetime.now().isoformat(), 'value': value}
        else:  # adds while there is free space
            self.cache[self.size()] = {'time added': datetime.datetime.now().isoformat(), 'value': value}

    def delete(self):
        # Find and Remove oldest item from cache based on "time added" parameter
        old_entry = None
        for key in self.cache:
            if old_entry is None:
                old_entry = key
            elif self.cache[key]['time added'] < self.cache[old_entry]['time added']:
                old_entry = key

        print('Removed Element:\t' + str(self.cache[old_entry]))
        self.cache.pop(old_entry)
        return old_entry

    def start_cache(self):

        # Test the cache
        Keys = [i for i in range(5)]  # Total Space in cache
        sites = ['str1 ', 'str2', 'str3', 'str4', 'str5', 'str6', 'str7', 'str8', 'str9', 'str10']

        # Cache object
        cache = Cache()

        # Updating Cache with entries
        for i in range(20):
            print("Iteration: {0}".format(i + 1))
            value = ''.join([random.choice(sites)])  # randomly add a new value to the cache
            print('Added Element:\t' + value)
            cache.update(value)

            print("# Cached Entries: {0}\n".format(cache.size()))

        # Cache List
        print('\n\n\t\t', '*' * 10, ' CACHE LIST ', '*' * 10)
        for k, v in cache.view().items():
            print("Index {0} : {1}".format(k, v))


LRU_cache = Cache
Cache.start_cache(LRU_cache)
