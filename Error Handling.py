# Error Handling

while True:
    try:
        age = int(input("Input your age please "))
        10/age
        # raise the exception only when codes above work
        raise Exception("hey cut it out")
    except ValueError:  # run only when this error occurs
        print("Please enter a number")
        continue    # go back to the loop and run again
    except ZeroDivisionError:   # run only when this error occurs
        print("Please enter age higher than zero")
        break   # break the loop
    else:   # run only when no error occurs
        print("Thank you")
        break
    finally:    # run regardless whatever happens
        print("ok, i am finally done")
