def run():
    my_list = [1, 'hola', True, 4.5]
    my_dict = {"first_name":"jose", "last_name":"polanco"}

    super_list = [
        {"first_name":"jose", "last_name":"polanco"},
        {"first_name":"isidora", "last_name":"paillao"},
        {"first_name":"aquiles", "last_name":"polanco"},
        {"first_name":"sixta", "last_name":"ceron"}    
    ]

    super_dict = {
        "natural_num": [1,2,3,4,5],
        "integer_num": [-1,-2, 0, 3],
        "floating_num": [1.2,1.3,1.4,1.5,1.6,1.7]
    }
    

    for key, value in super_dict.items():
        print(key, "_", value)
        
if __name__ == '__main__':
    run()

