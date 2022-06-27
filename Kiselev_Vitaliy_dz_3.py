
log_dict = {}


def type_logger(func):
  def wrapper(x):
    log_dict[x] = type(x), type(func)
    return print(log_dict)
    
  return wrapper


@type_logger
def calc_cube(x):
   return x ** 3

calc_cube(5)

calc_cube('5')