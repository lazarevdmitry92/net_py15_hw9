max_rating = None
max_grade = None

with open('ratings.txt') as f:
    for line in f:
        grade = line.strip()
        score = f.readline().strip().split()
        scorelist = []
        for i in score:
            scorelist.append(int(i))
        avg_rating = sum(scorelist)/len(scorelist)
        if max_rating is None or avg_rating > max_rating:
            max_rating = avg_rating
            max_grade = grade
        f.readline()
print("Лучшая оценка {} у {} класса".format(max_rating, max_grade))
