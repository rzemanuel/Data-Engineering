from Permutations.data_gen import init_data, permute_data
from Permutations.database_gen import sql_create

unpermuted_data = init_data()
permuted_data = permute_data(unpermuted_data)
sql_create(permuted_data)
