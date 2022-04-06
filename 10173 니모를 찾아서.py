while 1:
    a = input()
    if a == "EOI":
        break
    print("Found" if "nemo" in a.lower() else "Missing")