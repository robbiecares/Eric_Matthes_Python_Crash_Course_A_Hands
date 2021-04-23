def format_location(city,country):
    lowercase_words = ['of', 'the', 'an', 'and']
    lowercase_words = [word.title() for word in lowercase_words]
    lowercase_words = sorted(lowercase_words)
    fullname = f'{city}, {country}'
    fullname = fullname.title()

    for word in lowercase_words:
        parsedname = fullname.partition(word)
        while str(parsedname[1]) == word:
            fullname = (parsedname[0]) + str(parsedname[1]).lower() + str(parsedname[2])
            parsedname = fullname.partition(word)
            if parsedname[1] is None and parsedname[2] is None:
                continue
    fullname = str(parsedname[0])
    return fullname

def format_population(population):
    return population

def assemble_details(city,country,population=''):
    fullname = format_location(city,country)
    population = format_population(population)
    fulltext = f'{fullname} - population {population}'
    return fulltext
