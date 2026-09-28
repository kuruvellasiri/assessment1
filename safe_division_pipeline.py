def safe_divide(pairs, errors):
    
    for a, b in pairs:
        try:
            result = a / b
            yield result
        except ZeroDivisionError:
            errors.append(((a, b), "ZeroDivisionError"))
        except TypeError:
            errors.append(((a, b), "TypeError"))


def main():

    pairs = [(10, 2), (5, 0), (9, 3), ("a", 2), (8, 4)]
    errors=[]
    # Consume the generator
    results = list(safe_divide(pairs, errors))

    # Generator expression
    total = sum(x for x in results)

    # Dictionary comprehension
    result_dict=dict(errors)
    

    print("Results:", results)
    print("Sum:", total)
    print("Errors:", errors)
    print("result in dictionary:",result_dict)

if __name__ == "__main__":
    main()