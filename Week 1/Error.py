def ErrorPrevention(Input,Type,message):
    try:
        test = Type(Input)
        return True
    except ValueError:
        print(message)
        print()
        return False
