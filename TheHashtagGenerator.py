def generate_hashtag(s):

    # First of all we check if the string has 140 characters or more.
    if len(s) >= 140 or s == "":

        return False

    # Let's convert every character in the string lowercase to work better.
    s = s.lower()

    # We generate a new list and add the '#' character.
    newp = list()

    newp.append('#')

    # We start the loop that go to each character.
    for i in range(len(s)):

        # We generate another loop to check how many non-aplhabetic characters we are keeping in the list.
        count = 0
        for character in newp:
            if character.isalpha():
                count += 1

        # We begin with the conditonals.

        # First of all of them we check if the first character is an alphabetic character.
        # If it is, we add uppercase to the list.
        if i == 0 and s[i].isalpha():

            newp.append(s[i].upper())

        # Next if the previous character was a space and the actual is an alphabetic character
        # we add uppercase to the list.
        elif s[i-1] == ' ' and s[i].isalpha():

            newp.append(s[i].upper())

        # If the character is a space continue the loop.
        elif s[i] == ' ':

            continue
        # If it is not an alphabetic character we do the same
        elif not s[i].isalpha():

            continue

        # If the character is an alphabetic character and our non.alphabetic character counter is 0
        # we add the uppercase new character because before that we had non-alphabetical characters in
        # our list.

        elif s[i].isalpha() and count == 0:

            nepw.append(s[i].upper())

        # We add the rest.
        else:

            newp.append(s[i])

    # Join everything and enjoy the result.
    result = "".join(newp)

    return result
