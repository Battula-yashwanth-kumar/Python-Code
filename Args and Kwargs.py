# *args is a short form used for arguments. It is used to unpack an argument. In the case of *args, the argument could be list or tuple.
# **kwargs is a short form used for keyword arguments. It passes the data to the argument in the form of a dictionary.

def funargs(normal, *argsrohan, **kwargsbala):
    print(normal)
    for item in argsrohan:
        print(item)
    for key, value in kwargsbala.items():
        print(f"{key} is a {value}")

# Example usage:
normal_arg = "I am a normal argument"
args_list = ["Rohan1", "Rohan2", "Rohan3"]
kwargs_dict = {"name": "Bala", "profession": "Engineer"}

funargs(normal_arg, *args_list, **kwargs_dict)
