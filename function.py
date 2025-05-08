
def exam_result(*args,**kwargs):
    
    name = kwargs.get("name")
    course = kwargs.get("course")

    if not name:
        name = "Student"

    if not args:
            print(f"Hello {name}, we don't have your results for {course}")
            
    else:
        sum = 0
        for num in args:
                        sum+=num
                        avg = sum/len(args)

        print(f"Hello {name}, your average score for {course} is {avg}")