def DNA_strand(dna):
    output = []
    for i in dna:
        if i == "A":
            output.append("T")
        elif i == "T":
            output.append("A")
        elif i == "C":
            output.append("G")
        elif i == "G":
            output.append("C")
        else:
            print("Alien DNA Detected")
    return "".join(output)
