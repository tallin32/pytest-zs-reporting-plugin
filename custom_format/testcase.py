"""
Represents the "testCase" node in a test execution
"""
class TestCase:
    def __init__(self, key: str|None, name: str|None):
        self._key = key
        self._name = name

    def to_json(self) -> dict:
        ret = dict()
        if self._name: ret["name"] = self._name
        if self._key: ret["key"] = self._key
        return ret
    
__result_values = [ "pass", "fail", "skip" ]

"""
Represents a test execution
"""
class TestExecution:
    def __init__(result: str, source: str, testCase: TestCase|None):
        if result not in __result_values:
            raise ValueError("Invalid result")
        self._result = result
        self._source = source
        self._testCase = testCase or None

    def to_json(self) -> dct:
        ret = dict()
        if self._source: dict["source"] = self._source
        if self._result: dict["result"] = self._result
        if self._testCase: ret["testCase"] = self._testCase


"""
This class holds a list of test executions.
"""
class ExecutionContainer:
    def __init__(self, executions: list):
        self._executions = executions or list()
    
    def addExecution(self, execution: TestExecution):
        if not isinstance(execution, TestExecution):
            raise TypeError("Argument is not a TestExecution or descendant class")
        self._executions.append(execution)

    def fromSource(self, source: str) -> TestExecution:
        return list(filter(lambda x: x.source == source, self._executions))[0]
    
    def to_json(self):
        ret = dict()
        ret[executions] = self._executions
        return ret
