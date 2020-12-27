def verify_sort(a):
    """
    Verifies an array is sorted properly.

    Args:
        a (string[]|integer[]): array of strings or integers to validate as sorted

    Returns:
        boolean: whether or not the supplied array is sorted properly
    """

    i = 0
    out = "Values have been sorted properly!"
    num_err = 0
    while i < len(a) - 1:
        if a[i] > a[i + 1]:
            out = "[ERROR] Values have not been sorted properly!"
            num_err += 1
        i += 1
    print(out + " [" + str(num_err) + "]")
    return num_err == 0
