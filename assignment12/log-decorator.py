# one time setup
import logging
logger = logging.getLogger(__name__ + "_parameter_log")
logger.setLevel(logging.INFO)
logger.addHandler(logging.FileHandler("./decorator.log", "a"))

# logger_decorator
def logger_decorator(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        logger.info(f"function: {func.__name__}")
        logger.info(f"positional parameters: {args if args else 'none'}")
        logger.info(f"keyword parameters: {kwargs if kwargs else 'none'}")
        logger.info(f"return: {result}")
        return result
    return wrapper

# Task 1.1: No parameters 
@logger_decorator
def greet():
    print("Hello, World!")

# Task 1.2: Positional arguments 
@logger_decorator
def check_all_true(*args):
    return all(args)

# Task 1.3: Keyword arguments
@logger_decorator
def accept_keywords(**kwargs):
    return logger_decorator 

# Main 
if __name__ == "__main__":
    greet()
    check_all_true(True, True, False)
    accept_keywords(city="Trumbull", state="Connecticut")
