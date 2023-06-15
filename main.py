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
          raise ZeroDivisionError
        else:
          result = a/b
    case _:
        raise ValueError
  return result

def main():
  try:
    a = float(input())
    b = float(input())
  except:
    print("both a and b are supposed to be numbers")
    return 1
  
  operator = input()
  try:
    print(calc(a, b, operator))
  except ZeroDivisionError:
    print("Division by zero is not allowed in here")
    return 2
  except ValueError:
      print("Unknown query")
      return 3
  return 0

main()
