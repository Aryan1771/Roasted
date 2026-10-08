"""Bounded arithmetic for chatbot input, without executing Python code."""

import ast
import math
import operator

OPERATIONS = {
    ast.Add: operator.add, ast.Sub: operator.sub, ast.Mult: operator.mul,
    ast.Div: operator.truediv, ast.FloorDiv: operator.floordiv,
    ast.Mod: operator.mod, ast.Pow: operator.pow,
}


def calculate(expression):
    if len(expression) > 256:
        raise ValueError("Expression is too long")
    try:
        tree = ast.parse(expression, mode="eval")
        if sum(1 for _ in ast.walk(tree)) > 64:
            raise ValueError("Expression is too complex")

        def visit(node):
            if isinstance(node, ast.Constant) and type(node.value) in (int, float):
                result = node.value
            elif isinstance(node, ast.UnaryOp) and isinstance(node.op, (ast.UAdd, ast.USub)):
                result = visit(node.operand) * (-1 if isinstance(node.op, ast.USub) else 1)
            elif isinstance(node, ast.BinOp) and type(node.op) in OPERATIONS:
                left, right = visit(node.left), visit(node.right)
                if isinstance(node.op, ast.Pow) and abs(right) > 100:
                    raise ValueError("Exponent is too large")
                result = OPERATIONS[type(node.op)](left, right)
            else:
                raise ValueError("Only numbers and arithmetic operators are supported")
            if type(result) not in (int, float) or not math.isfinite(result) or abs(result) > 1e100:
                raise ValueError("Result is outside the supported range")
            return result

        return visit(tree.body)
    except (SyntaxError, ArithmeticError, RecursionError) as error:
        raise ValueError("Invalid arithmetic expression") from error
