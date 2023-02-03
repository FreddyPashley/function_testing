import time

class Test:
    version = "1.0.1"
    class TestResult:
        def __init__(self, result, function, args, time_taken, expected_type, expected_value, expected_chars, expected_length, errors=None):
            self.value = result
            self.type = type(result)
            self.function = Test().function_name(function)
            self.args = args
            self.time_taken_secs = time_taken if time_taken != 0 else "tr"
            self.expected_type = str(expected_type).split()[-1].replace("'","").replace(">","") if expected_type != 0 else "N/A"
            self.expected_value = expected_value
            self.expected_chars = expected_chars if expected_chars is not None else "N/A"
            self.expected_length = expected_length if expected_length is not None else "N/A"
            self.matching_types = expected_type == type(result) if expected_type != 0 else "N/A"
            self.matching_values = (expected_value == result) if expected_value != None else "N/A"
            self.matching_chars = (expected_chars == len(result) if type(result) == str else None) if expected_chars is not None else "N/A"
            self.matching_length = (expected_length == len(result) if type(result) in [list, dict] else None) if expected_length is not None else "N/A"
            self.errors = errors
            self.valid = True if True in [getattr(self, i) for i in dir(self) if "__" not in i and i.startswith("matching_")] else False

            

        def all(self):
            """
            Dumps all info from test to the terminal
            """
            attrs = [i for i in dir(self) if "__" not in i and i != "type"]
            
            attrs_ = [[i, str(getattr(self, i))] for i in attrs if not hasattr(getattr(self, i), "__call__")]

            attrs_.insert(0, ["Attribute", "Value"])
            
            longest_1 = 0
            longest_2 = 0
            for i in range(len(attrs_)):
                item = attrs_[i]
                if len(item[0]) > longest_1:
                    longest_1 = len(item[0])
                if len(item[1]) > longest_2:
                    longest_2 = len(item[1])

            attrs_.insert(1, ["-"*longest_1, "-"*longest_2])
            
            for i in range(len(attrs_)):
                item1, item2 = attrs_[i]
                if item2 != "N/A":
                    print(item1+(" "*(longest_1-len(item1)+4))+item2)
            
            
    def __init__(self):
        pass

    def testing(self, string, environ):
        assert eval(string, environ)

    def test(self, function, locals_, args=[], expected_type=0, expected_value=None, expected_chars=None, expected_length=None):
        args_str = ", ".join([str(i) for i in args])
        func_name = self.function_name(function)
        to_exec = f"{func_name}({args_str})"

        self.t1 = time.time()
        try:
            result = eval(to_exec, locals_)
        except Exception as err:
            result = None
            error = err
        else:
            error = None

        self.t2 = time.time()

        self.time_taken = self.t2 - self.t1
            
        return self.TestResult(result, function, args, self.time_taken, expected_type, expected_value, expected_chars, expected_length, errors=error)

    
    def function_name(self, function):
        """
        Gets name of function from the object
        Example: <function func1 at 0x7fb328773e20>
                           ^^^^^
        """
        return str(function).split()[1]
