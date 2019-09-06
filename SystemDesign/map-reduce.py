"""
Input:
Product File: user.txt
 a very large (> 100 GB) file, each line of the file is in the following format: (product_id, user_id)
User File: product.txt
 a very large (> 100 GB) file, each line of the file is in the following format: (user_id, gender)

Output:
Filter the product by a given gender (male/female)
product_male.txt: a file containing all the product_ids of male users
or
product_female.txt:  a file containing all the products of female users
"""


class Mapper:
    def map(self, key, value):
        """
        :param key: file line number
        :param value: file line string
        Emit to reducers: a list of pairs ((user_id, 0), gender) or ((user_id, 1) , product_id)
        """
        tokens = tokenize(value)
        if tokens[1] == "male" or tokens[1] == "female":  # a line of (user_id, gender)
            emit(((tokens[0], 0), tokens[1]))  # emit ((user_id, 0), gender)
        else:  # a line of (product_id, user_id)
            emit(((tokens[0], 1), tokens[0]))  # emit ((user_id, 1), product_id)


class Reducer:
    def __init__(self):
        self.job = MapReduce.getInstance()
        self.gender_required = job.get("genderRequired")  # get the gender required from global

    def reduce(self, key, values):
        """
        :param key: user_id
        :param values: aggregated by the user_id, a list of [product_ids] or a gender
        Emit to output file: product_ids with
        """
        if key[1] == 0:
            # encounter ((user_id, 0), gender)
            self.gender_current_user = values[0]
        else:
            # encounter ((user_id, 1) , product_id)
            if self.gender_current_user != self.gender_required: return
            for product_id in values:
                emit(product_id)
            

class Partitioner:
    def get_partition(self, key, value, numReduceTasks):
        return hash(key[0]) % numReduceTasks  # partition by the user_id part of key


class Driver:
    # main program
    def __init__(self, gender):  # gender = "male" or "female"
        self.job = MapReduce.getInstance()
        self.job.setMapperClass(Mapper)
        self.job.setReducerClass(Reducer)
        self.job.set("genderRequired", gender)  # set the gender as global value
        self.job.setInputPaths(["user.txt", "product.txt"])
        self.job.setOutputPath("product_" + gender + ".txt")

    def run(self):
        self.job.waitForCompletion()
