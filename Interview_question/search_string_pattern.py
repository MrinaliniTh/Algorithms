def search_string_pattern(input, pattern):
    res = []
    for data in input:
        if pattern in data:
            res.append(data)
    return res

print(search_string_pattern(['Amil Jaiswal', 'Bubli Jio', 'Ankit Jspiders','Jahanavi Tek', 'Amit Tij'], ''))
