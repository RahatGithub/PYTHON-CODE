name = "Facebook"  # declaring a global variable 'name'


def main():
    name = "FB"  # declaring a local variable 'name' inside main()
    def rename():
        global name  # notifying that, from now on, we're going to use the global variable 'name'
        name = "Meta"  # reassigning the global variable

    print(name, "before rename()")  # it will print "FB before rename()"
    rename()  # calling rename() will reassign the global variable
    print(name, "after rename()")  # it will print "FB after rename()"
    # actually, the value of the global variable 'name' has been changed to "Meta" but the value of local variable 'name' is still "FB"


print(name, "before calling main()")  # it will print "Facebook before calling main()"
main()  # calling main() will trigger rename() which reassigns the global variable 'name'
print(name, "after calling main()")  # it will print "Meta after calling main()"