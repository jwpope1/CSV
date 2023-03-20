
while True:
    try:
        answer = float(input("How many hours did you work? "))
        payrate = float(input("What is your payrate? "))
        #paycheck = answer * payrate
        print(f"Thank you. The total you made for the week was ${answer*payrate:,.2f}.")
        break
    except ValueError as err:
        #pass
        print(f"There was an error. The error is {err}")
        
print("I am done!")

#NOT COMPLETE
