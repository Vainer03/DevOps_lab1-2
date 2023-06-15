
def calc(a, b, operator):
  match operator:
    case "+":
        result = a + b
    case "-":
        result = a - b
    case "*":
        result = a * b
    case "/":
        if b == 0:
          result = "ERROR:1"
        else:
          result = a/b
    case _:
        result = "ERROR:2"
  return result
      
a = int(input())
b = int(input())
operator = input()
result = calc(a, b, operator)
match result:
  case "ERROR:1":
    print("Division by zero is not allowed in here")
  case "ERROR:2":
    print("Unknown query")
  case _:
    print(result)
