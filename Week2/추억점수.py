def solution(name, yearning, photo):
    Name_year = dict(zip(name,yearning))
    return [sum(Name_year.get(ii,0) for ii in i) for i in photo]